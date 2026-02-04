import json
import os
import re
import sys

TOKEN_DIR = os.path.dirname(os.path.abspath(__file__))
# The folders are directly inside the TOKEN_DIR
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

def resolve_value(value):
    if not isinstance(value, str):
        return value
    
    # Regex to find {Reference}
    def replacer(match):
        ref_name = match.group(1)
        # Apply the same de-duplication logic during resolution
        parts = []
        for p in ref_name.split('.'):
            sanitized = sanitize_name(p)
            if not parts:
                parts.append(sanitized)
            else:
                last = parts[-1]
                # Check for redundancy or synonyms
                if sanitized == last:
                    continue
                if (last == 'background' and sanitized == 'bg') or (last == 'bg' and sanitized == 'background'):
                    continue
                if (last == 'foreground' and sanitized == 'fg') or (last == 'fg' and sanitized == 'foreground'):
                    continue
                if (last == 'color' and sanitized == 'colors') or (last == 'colors' and sanitized == 'color'):
                    continue
                # Handle cases where sanitized starts with last- (e.g., text and text-primary)
                if sanitized.startswith(last + '-'):
                    parts[-1] = sanitized # Replace with more specific version
                else:
                    parts.append(sanitized)
        
        var_name = '-'.join(parts)
        # Final pass for common redundancies
        var_name = var_name.replace('text-text-', 'text-')
        var_name = var_name.replace('border-border-', 'border-')
        var_name = var_name.replace('background-bg-', 'background-')
        var_name = var_name.replace('foreground-fg-', 'foreground-')
        
        return f"var(--{var_name})"
    
    return re.sub(r'\{([^}]+)\}', replacer, value)

def flatten_tokens(obj, prefix='', tokens=None):
    if tokens is None:
        tokens = {}
        
    for key, value in obj.items():
        if key.startswith('$'):
            continue
            
        sanitized_key = sanitize_name(key)
        
        if not prefix:
            new_prefix = sanitized_key
        else:
            prefix_parts = prefix.split('-')
            last_part = prefix_parts[-1]
            
            # Check for redundancy or synonyms
            is_redundant = False
            if sanitized_key == last_part:
                is_redundant = True
            elif (last_part == 'background' and sanitized_key == 'bg') or (last_part == 'bg' and sanitized_key == 'background'):
                is_redundant = True
            elif (last_part == 'foreground' and sanitized_key == 'fg') or (last_part == 'fg' and sanitized_key == 'foreground'):
                is_redundant = True
            elif (last_part == 'color' and sanitized_key == 'colors') or (last_part == 'colors' and sanitized_key == 'color'):
                is_redundant = True
            
            if is_redundant:
                new_prefix = prefix # Don't add anything
            elif sanitized_key.startswith(last_part + '-'):
                # Key already contains the prefix part (e.g., prefix='text', key='text-primary')
                new_prefix = prefix[:-len(last_part)] + sanitized_key
            else:
                new_prefix = f"{prefix}-{sanitized_key}"
            
        # Global cleanup for common start repetitions (e.g., color-colors)
        new_prefix = re.sub(r'^(color|colors)-(color|colors)-', r'\1-', new_prefix)
        # Fix specific cases mentioned by user
        new_prefix = new_prefix.replace('text-text-', 'text-')
        new_prefix = new_prefix.replace('border-border-', 'border-')
        new_prefix = new_prefix.replace('background-bg-', 'background-')
        new_prefix = new_prefix.replace('foreground-fg-', 'foreground-')

        if isinstance(value, dict) and '$value' in value:
            if value.get('$type') in ['typography']:
                continue
            else:
                tokens[new_prefix] = resolve_value(value['$value'])
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
    ':root': [], # Primitives, Spacing (Default), Global resets
    '[data-theme="light"], :root': [], # Light mode (default)
    '[data-theme="dark"]': [],         # Dark mode
    ':root, [data-typography="md"]': [], # Typography MD (default)
    '[data-typography="lg"]': []       # Typography LG
}

# 1. Primitives (Global)
primitives_file = os.path.join(SOURCE_DIR, '_Primitives', 'Core Value.json')
tokens = process_file(primitives_file)
for key, val in tokens.items():
    css_groups[':root'].append(f"  --{key}: {val};")

# 2. Semantic Colors - Light Mode (Default)
light_mode_file = os.path.join(SOURCE_DIR, '1. Color modes', 'Light Mode.json')
tokens = process_file(light_mode_file)
for key, val in tokens.items():
    css_groups['[data-theme="light"], :root'].append(f"  --{key}: {val};")

# 3. Semantic Colors - Dark Mode
dark_mode_file = os.path.join(SOURCE_DIR, '1. Color modes', 'Dark Mode.json')
tokens = process_file(dark_mode_file)
for key, val in tokens.items():
    css_groups['[data-theme="dark"]'].append(f"  --{key}: {val};")

# 4. Spacing (Global)
spacing_file = os.path.join(SOURCE_DIR, '4. Spacing', 'Spacing Default.json')
tokens = process_file(spacing_file)
for key, val in tokens.items():
    clean_val = val
    if isinstance(val, (int, float)):
        clean_val = f"{val}px"
    css_groups[':root'].append(f"  --{key}: {clean_val};")

# 5. Radius & Widths (Global)
for folder in ['3. Radius', '5. Widths']:
    full_path = os.path.join(SOURCE_DIR, folder)
    if os.path.exists(full_path):
        for file in os.listdir(full_path):
            if file.endswith('.json'):
                tokens = process_file(os.path.join(full_path, file))
                for key, val in tokens.items():
                    clean_val = val
                    if isinstance(val, (int, float)):
                        clean_val = f"{val}px"
                    css_groups[':root'].append(f"  --{key}: {clean_val};")

# 6. Typography
# MD Mode (Default)
typo_md_file = os.path.join(SOURCE_DIR, '2. Typography', 'Breakpoint md.json')
tokens = process_file(typo_md_file)
for key, val in tokens.items():
    clean_val = val
    if isinstance(val, (int, float)):
        # Apply px to dimensions but not weights
        if any(x in key for x in ['size', 'height', 'spacing', 'indent']) and 'weight' not in key:
            clean_val = f"{val}px"
    css_groups[':root, [data-typography="md"]'].append(f"  --{key}: {clean_val};")

# LG Mode
typo_lg_file = os.path.join(SOURCE_DIR, '2. Typography', 'Breakpoint lg.json')
tokens = process_file(typo_lg_file)
for key, val in tokens.items():
    clean_val = val
    if isinstance(val, (int, float)):
        if any(x in key for x in ['size', 'height', 'spacing', 'indent']) and 'weight' not in key:
            clean_val = f"{val}px"
    css_groups['[data-typography="lg"]'].append(f"  --{key}: {clean_val};")

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
