import json
import os
import re
import sys

TOKEN_DIR = os.path.dirname(os.path.abspath(__file__))
SOURCE_DIR = os.path.join(TOKEN_DIR, 'originial-tokens')
OUTPUT_FILE = os.path.join(TOKEN_DIR, '..', 'wb-design-system', 'design_tokens.css')

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
        var_name = sanitize_name(ref_name)
        return f"var(--{var_name})"
    
    return re.sub(r'\{([^}]+)\}', replacer, value)

def flatten_tokens(obj, prefix='', tokens=None):
    if tokens is None:
        tokens = {}
        
    for key, value in obj.items():
        if key.startswith('$'):
            continue
            
        new_prefix = f"{prefix}-{sanitize_name(key)}" if prefix else sanitize_name(key)
        
        if isinstance(value, dict) and '$value' in value:
            if value.get('$type') == 'typography':
                # Handle composite typography token
                typography_obj = value['$value']
                for prop, prop_val in typography_obj.items():
                    # camelCase to kebab-case
                    prop_name = sanitize_name(re.sub(r'(?<!^)(?=[A-Z])', '-', prop))
                    resolved_val = resolve_value(prop_val)
                    tokens[f"{new_prefix}-{prop_name}"] = resolved_val
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

# 4. Spacing (Global for now, unless spacing mode requested)
spacing_file = os.path.join(SOURCE_DIR, '4. Spacing', 'Spacing Default.json')
tokens = process_file(spacing_file)
for key, val in tokens.items():
    clean_val = val
    if isinstance(val, (int, float)):
        clean_val = f"{val}px"
    css_groups[':root'].append(f"  --{key}: {clean_val};")

# 5. Radius & Widths (Global)
for folder, subdir_path in [('3. Radius', '3. Radius'), ('5. Widths', '5. Widths')]:
    full_path = os.path.join(SOURCE_DIR, subdir_path)
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

# Encode CSS
with open(OUTPUT_FILE, 'w') as f:
    f.write("/* Generated CSS Variables - Multi-Theme Support */\n\n")
    
    # Order: Primitives First
    f.write("/* 1. Global Primitives */\n")
    f.write(":root {\n")
    f.write("\n".join(css_groups[':root']))
    f.write("\n}\n\n")
    
    # Typography Defaults
    f.write("/* 2. Typography - MD (Default) */\n")
    f.write(":root, [data-typography=\"md\"] {\n")
    f.write("\n".join(css_groups[':root, [data-typography="md"]']))
    f.write("\n}\n\n")
    
    # Typography LG
    f.write("/* 3. Typography - LG */\n")
    f.write("[data-typography=\"lg\"] {\n")
    f.write("\n".join(css_groups['[data-typography="lg"]']))
    f.write("\n}\n\n")

    # Colors Light
    f.write("/* 4. Colors - Light Mode (Default) */\n")
    f.write("[data-theme=\"light\"], :root {\n")
    f.write("\n".join(css_groups['[data-theme="light"], :root']))
    f.write("\n}\n\n")
    
    # Colors Dark
    f.write("/* 5. Colors - Dark Mode */\n")
    f.write("[data-theme=\"dark\"] {\n")
    f.write("\n".join(css_groups['[data-theme="dark"]']))
    f.write("\n}\n")

print(f"Successfully generated {OUTPUT_FILE}")
