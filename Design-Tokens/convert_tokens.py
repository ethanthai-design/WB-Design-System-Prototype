import json
import os
import re
import sys

TOKEN_DIR = os.path.dirname(os.path.abspath(__file__))
SOURCE_DIR = TOKEN_DIR
OUTPUT_FILE = os.path.join(TOKEN_DIR, '..', 'Development-Source', 'projects', 'Library-Core', 'src', 'lib', 'styles', 'design_tokens.css')

def sanitize_name(key):
    # Replace dots and parens with -
    temp = re.sub(r'[().]', '-', key)
    # Replace spaces with -
    temp = re.sub(r'\s+', '-', temp)
    # Remove other special chars
    temp = re.sub(r'[^a-zA-Z0-9-]', '-', temp)
    # Collapse multiple dashes
    temp = re.sub(r'-+', '-', temp)
    # Trim dashes
    temp = temp.strip('-')
    return temp.lower()

def merge_paths(prefix, key):
    if not prefix:
        return key
    
    prefix_parts = prefix.split('-')
    key_parts = key.split('-')
    
    # Handle synonyms and direct matches at the boundary
    synonyms = {
        'bg': 'background',
        'background': 'bg',
        'fg': 'foreground',
        'foreground': 'fg',
        'colors': 'color',
        'color': 'colors',
        'shadow': 'shadows',
        'shadows': 'shadow',
        'focus-ring': 'focus-rings',
        'focus-rings': 'focus-ring'
    }
    
    # Try to find the longest overlap
    for i in range(min(len(prefix_parts), len(key_parts)), 0, -1):
        overlap_p = prefix_parts[-i:]
        overlap_k = key_parts[:i]
        
        # Check if they match exactly or are synonyms part-by-part
        match = True
        for p, k in zip(overlap_p, overlap_k):
            if p != k and synonyms.get(p) != k:
                match = False
                break
        
        if match:
            # Merge and normalize to preferred terms
            merged = prefix_parts[:-i] + key_parts
            normalized = []
            for part in merged:
                if part == 'bg': normalized.append('background')
                elif part == 'fg': normalized.append('foreground')
                else: normalized.append(part)
            return '-'.join(normalized)
            
    # Normalize even if no merge happened
    merged = prefix_parts + key_parts
    normalized = []
    for part in merged:
        if part == 'bg': normalized.append('background')
        elif part == 'fg': normalized.append('foreground')
        else: normalized.append(part)
    return '-'.join(normalized)

def resolve_value(value):
    if not isinstance(value, str):
        return value
    
    def replacer(match):
        ref_name = match.group(1)
        # Apply the same merge_paths logic during resolution
        parts = ref_name.split('.')
        current_path = ""
        for p in parts:
            sanitized = sanitize_name(p)
            current_path = merge_paths(current_path, sanitized)
        
        # Global cleanup for specific leftovers
        current_path = re.sub(r'-+', '-', current_path).strip('-')
        return f"var(--{current_path})"
    
    return re.sub(r'\{([^}]+)\}', replacer, value)

def flatten_tokens(obj, prefix='', tokens=None):
    if tokens is None:
        tokens = {}
        
    for key, value in obj.items():
        if key.startswith('$'):
            continue
            
        sanitized_key = sanitize_name(key)
        new_prefix = merge_paths(prefix, sanitized_key)
        
        # Global cleanup for repetitive prefixes (e.g., color-colors)
        new_prefix = re.sub(r'^(color|colors)-(color|colors)-', r'color-', new_prefix)
        # Clean up double mentions if they escaped merge_paths
        new_prefix = re.sub(r'-+', '-', new_prefix).strip('-')

        if isinstance(value, dict) and '$value' in value:
            # Skip composite tokens
            if value.get('$type') in ['typography']:
                continue
            
            val = resolve_value(value['$value'])
            
            # Systematically append px to numeric values for dimensions
            if isinstance(val, (int, float)):
                types_needing_px = ['number', 'fontSizes', 'lineHeights', 'letterSpacing', 'paragraphSpacing', 'paragraphIndent', 'dimension', 'borderRadius']
                # Check $type or key context
                if value.get('$type') in types_needing_px:
                    val = f"{val}px"
                elif any(x in new_prefix for x in ['spacing', 'radius', 'width', 'size', 'height', 'indent']):
                    # Ensure we don't add px to font-weight or other non-dimensions
                    if 'weight' not in new_prefix and 'case' not in new_prefix and 'decoration' not in new_prefix:
                        val = f"{val}px"
            
            # Font-weight mapping
            if value.get('$type') == 'fontWeights' or 'font-weight' in new_prefix:
                weight_map = {
                    'regular': '400',
                    'medium': '500',
                    'semibold': '600',
                    'bold': '700'
                }
                if isinstance(val, str):
                    lower_val = val.lower()
                    # Check for keywords and map to numeric values
                    for name, weight in weight_map.items():
                        if name in lower_val:
                            val = weight
                            break
            
            tokens[new_prefix] = val
        elif isinstance(value, dict):
            flatten_tokens(value, new_prefix, tokens)
            
    return tokens

def process_file(file_path):
    try:
        if not os.path.exists(file_path):
            print(f"Warning: File not found: {file_path}")
            return {}
        with open(file_path, 'r') as f:
            content = json.load(f)
        return flatten_tokens(content)
    except Exception as e:
        print(f"Error parsing {file_path}: {e}")
        return {}

# Define CSS Groups
css_groups = {
    ':root': [],
    '[data-theme="light"], :root': [],
    '[data-theme="dark"]': [],
    ':root, [data-typography="md"]': [],
    '[data-typography="lg"]': []
}

# 1. Primitives
primitives_file = os.path.join(SOURCE_DIR, '_Primitives', 'Core Value.json')
tokens = process_file(primitives_file)
for key, val in tokens.items():
    css_groups[':root'].append(f"  --{key}: {val};")

# 2. Semantic Colors - Light Mode
light_mode_file = os.path.join(SOURCE_DIR, '1. Color modes', 'Light Mode.json')
tokens = process_file(light_mode_file)
for key, val in tokens.items():
    css_groups['[data-theme="light"], :root'].append(f"  --{key}: {val};")

# 3. Semantic Colors - Dark Mode
dark_mode_file = os.path.join(SOURCE_DIR, '1. Color modes', 'Dark Mode.json')
tokens = process_file(dark_mode_file)
for key, val in tokens.items():
    css_groups['[data-theme="dark"]'].append(f"  --{key}: {val};")

# 4. Spacing
spacing_file = os.path.join(SOURCE_DIR, '4. Spacing', 'Spacing Default.json')
tokens = process_file(spacing_file)
for key, val in tokens.items():
    css_groups[':root'].append(f"  --{key}: {val};")

# 5. Radius & Widths
for folder in ['3. Radius', '5. Widths']:
    full_path = os.path.join(SOURCE_DIR, folder)
    if os.path.exists(full_path):
        for file in os.listdir(full_path):
            if file.endswith('.json'):
                tokens = process_file(os.path.join(full_path, file))
                for key, val in tokens.items():
                    css_groups[':root'].append(f"  --{key}: {val};")

# 6. Typography
# MD Mode
typo_md_file = os.path.join(SOURCE_DIR, '2. Typography', 'Breakpoint md.json')
tokens = process_file(typo_md_file)
for key, val in tokens.items():
    css_groups[':root, [data-typography="md"]'].append(f"  --{key}: {val};")

# LG Mode
typo_lg_file = os.path.join(SOURCE_DIR, '2. Typography', 'Breakpoint lg.json')
tokens = process_file(typo_lg_file)
for key, val in tokens.items():
    css_groups['[data-typography="lg"]'].append(f"  --{key}: {val};")

# Output CSS
os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
with open(OUTPUT_FILE, 'w') as f:
    f.write("/* Generated CSS Variables - Multi-Theme Support */\n\n")
    
    f.write("/* 1. Global Primitives */\n")
    f.write(":root {\n")
    f.write("\n".join(css_groups[':root']))
    f.write("\n}\n\n")
    
    f.write("/* 2. Typography - MD (Default) */\n")
    f.write(":root, [data-typography=\"md\"] {\n")
    f.write("\n".join(css_groups[':root, [data-typography="md"]']))
    f.write("\n}\n\n")
    
    f.write("/* 3. Typography - LG */\n")
    f.write("[data-typography=\"lg\"] {\n")
    f.write("\n".join(css_groups['[data-typography="lg"]']))
    f.write("\n}\n\n")

    f.write("/* 4. Colors - Light Mode (Default) */\n")
    f.write("[data-theme=\"light\"], :root {\n")
    f.write("\n".join(css_groups['[data-theme="light"], :root']))
    f.write("\n}\n\n")
    
    f.write("/* 5. Colors - Dark Mode */\n")
    f.write("[data-theme=\"dark\"] {\n")
    f.write("\n".join(css_groups['[data-theme="dark"]']))
    f.write("\n}\n")

print(f"Successfully generated {OUTPUT_FILE}")
