# WorkBuddy Design System Styles

This directory contains the core CSS files for the WorkBuddy Design System. These files define the design tokens and utility classes used throughout the application.

## Core Files

### 1. [design_tokens.css](./design_tokens.css)
The **Source of Truth** for all design variables. It contains:
- **Global Primitives**: Colors, base spacing, radii, and widths.
- **Typography Primitives**: Font families, weights, sizes, and line heights.
- **Semantic Colors**: Color mappings for text, borders, and backgrounds that adapt based on the theme.

#### Theme & Mode Support
- **Color Themes**: Supports `light` (default) and `dark` modes via the `data-theme` attribute on the root or container element.
- **Typography Modes**: Supports `md` (default) and `lg` text scaling via the `data-typography` attribute.

---

### 2. [typography_utilities.css](./typography_utilities.css)
A set of high-level utility classes for consistent text styling. Instead of manually applying multiple primitive tokens, use these "composite" classes.

**Naming Convention**: `.typography-[category]-[size]`  
Available categories: `body`, `label`, `display`.

**Example Usage**:
```html
<h1 class="typography-display-lg">Welcome</h1>
<p class="typography-body-md">This is a paragraph.</p>
```

---

### 3. [shadow_utilities.css](./shadow_utilities.css)
Utility classes for drop shadows and interactive states.

**Shadows**:
- Range from `.shadow-xs` to `.shadow-3xl`.
- Uses multi-layered box-shadows as defined in the design specs.

**Focus Rings**:
- `.focus-ring`: Standard brand focus state.
- `.focus-ring-error`: Focus state for error or invalid inputs.

**Example Usage**:
```html
<div class="shadow-md">Elevated Card</div>
<button class="focus-ring">Click Me</button>
```

## How to Use
1. Import `design_tokens.css` first to initialize all variables.
2. Import the utility files (`typography_utilities.css`, `shadow_utilities.css`) to gain access to the helper classes.
3. Apply classes directly to your HTML elements.
