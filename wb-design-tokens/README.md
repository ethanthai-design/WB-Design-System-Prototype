# WB Design Tokens

This package contains the raw design tokens and the scripts to convert them into usable CSS variables for the WB Design System.

## 🏗 Structure

- `originial-tokens/`: (Hidden/Internal) Contains the raw JSON token files exported from design tools (like Figma).
- `1. Color modes/`: Theme-specific color overrides (Light/Dark).
- `2. Typography/`: Desktop and Mobile typography scales.
- `3. Radius/`: Border radius tokens.
- `4. Spacing/`: Layout and component spacing tokens.
- `5. Widths/`: Max-width and container width tokens.
- `_Primitives/`: Core color palettes and foundational values.
- `convert_tokens.py`: A Python script that parses the JSON files and generates a `design_tokens.css` file in the component library.

## 🔄 How to Update Tokens

1.  **Modify JSON**: Edit or add tokens in the respective JSON files within the subdirectories.
2.  **Run Conversion**: Run the Python script to update the CSS variables in the Angular project:
    ```bash
    python3 convert_tokens.py
    ```
3.  **Verify**: Check `../wb-design-system/projects/wb-design-system/src/lib/styles/design_tokens.css` to see the changes.

## 🎨 Theme Support

The generated CSS supports multi-theming via data attributes:
- **Default (Light)**: Applied globally or via `[data-theme="light"]`.
- **Dark Mode**: Activated via `[data-theme="dark"]`.
- **Typography Sizing**: Supports `[data-typography="md"]` (default) and `[data-typography="lg"]`.

## 💻 Usage in CSS

Tokens are converted to kebab-case CSS variables. For example:
- JSON: `Colors.Brand.500` -> CSS: `--colors-brand-500`
- Usage: `color: var(--colors-brand-500);`
