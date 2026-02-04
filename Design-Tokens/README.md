# WB Design Tokens

This package contains the raw design tokens and the automated pipeline to convert them into production-ready CSS variables.

## 🏗 Structure

- `_Primitives/`: Core foundational values (palettes, base spacing).
- `1. Color modes/`: Theme-level overrides (Light/Dark).
- `2. Typography/`: Multi-breakpoint typography scales.
- `3. Radius/`, `4. Spacing/`, `5. Widths/`: Atomic dimension tokens.
- `convert_tokens.py`: The "brain" of the conversion pipeline.

## 🔄 Conversion Script Logic

The `convert_tokens.py` script does more than just flatting JSON; it applies several critical transformation rules to ensure the CSS output is clean and developer-friendly:

### 1. Intelligent De-duplication
The script detects and merges redundant path segments. 
- **Example**: `Font family` > `font-family-display` becomes `--font-family-display` instead of `--font-family-font-family-display`.

### 2. Standardization & Synonyms
Common shorthands are normalized to their full versions to maintain a premium API.
- **Example**: `bg` -> `background`, `fg` -> `foreground`.

### 3. Unit Injection
Numeric values in dimension-related categories are automatically padded with units.
- **Example**: `spacing-xs: 4` -> `--spacing-xs: 4px`.
- **Categories**: spacing, radius, width, font-size, line-height.

### 4. Font-Weight Numeric Mapping
Design-friendly labels are mapped to CSS-standard numeric weights.
- **Example**: `Regular` -> `400`, `Medium` -> `500`, `Bold` -> `700`.

## � How to Update

1.  **Modify JSON**: Edit tokens in the respective JSON files.
2.  **Run Conversion**: 
    ```bash
    python3 convert_tokens.py
    ```
3.  **Verify**: Changes are automatically written to `Development-Source/projects/Library-Core/src/lib/styles/design_tokens.css`.

## 💻 Usage

Tokens are converted to kebab-case. 
- **JSON**: `Colors.Brand.500` -> **CSS**: `--colors-brand-500`
- **Resolution**: Internal references (e.g., `{Colors.Gray.900}`) are resolved and de-duplicated during conversion.
