# Library Core - WB Design System

This is the core Angular library containing the reusable components of the WB Design System.

## 🛠 Development

### Core Components
Components are located in `src/lib/components/`. Each component should include:
- `*.component.ts`: Logic and metadata.
- `*.component.html`: Template.
- `*.component.scss`: Styles (using design tokens).
- `*.stories.ts`: Storybook documentation.

### Exporting Components
All components intended for public use must be exported from `src/public-api.ts`.

## 📦 Building

To build the library:
```bash
ng build Library-Core
```
The compiled library will be stored in `../../_Build_Output/library-core`.

## 🎨 Consuming Styles
The library consumes `design_tokens.css` located in the root of the workspace. Ensure this file is generated before building the library.
