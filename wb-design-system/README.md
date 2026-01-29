# WB Design System - Component Library

This is the primary component library for WorkBuddy, built with Angular 19 and Storybook.

## 🚀 Getting Started

### Installation
From the `wb-design-system` directory, run:
```bash
npm install
```

### Development Server
To see components in isolation and interact with them:
```bash
npm run storybook
```
This will start the Storybook server at `http://localhost:6006`.

## 🏗 Project Structure

- `projects/wb-design-system/`: The library source code.
  - `src/lib/components/`: UI components (Button, Input, etc.).
  - `src/lib/styles/`: Global styles and generated `design_tokens.css`.
- `.storybook/`: Storybook configuration, including global styles and theme setup.

## 🎨 Styling & Tokens

We use **CSS Variables** for all styling. These variables are generated from the [`wb-design-tokens`](../wb-design-tokens) package.

### Using Tokens in Components
To use a token in a component's `.scss` or `.css` file:
```scss
.my-component {
  background-color: var(--color-background-bg-primary);
  border-radius: var(--radius-md);
  padding: var(--spacing-md);
}
```

## 🛠 Adding a New Component

1.  **Generate**: Use the Angular CLI to generate a component inside the library:
    ```bash
    ng generate component lib/components/my-component --project wb-design-system
    ```
2.  **Create Story**: Add a `my-component.stories.ts` file in the component directory to document it in Storybook.
3.  **Export**: Ensure the component is exported from `public-api.ts`.

## 📦 Building for Production

To build the library for distribution:
```bash
npm run build
```
The output will be in the `dist/wb-design-system` directory.
