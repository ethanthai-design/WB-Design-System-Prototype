# WB Design System - Development Source

This is the main development workspace for the WorkBuddy Design System, built with Angular 19 and Storybook.

## 🚀 Getting Started

### Installation
From the `Development-Source` directory, run:
```bash
npm install
```

### Preview App
To run the showcase/preview application:
```bash
npm start
```
This will start the preview app at `http://localhost:4200`.

### Storybook
To see components in isolation and interact with them in Storybook:
```bash
npm run storybook
```
This will start the Storybook server at `http://localhost:6006`.

## 🏗 Project Structure

- **`projects/Library-Core/`**: The core component library source code.
  - `src/lib/components/`: Reusable UI components.
  - `src/lib/styles/`: Global styles and base styling logic.
- **`projects/Preview-App/`**: A showcase application used to test and demonstrate components during development.
- **`design_tokens.css`**: The generated CSS variables consumed by the library.

## 🎨 Styling & Tokens

We use **CSS Variables** for all styling. These variables are generated from the [`Design-Tokens`](../Design-Tokens) package.

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
    ng generate component lib/components/my-component --project Library-Core
    ```
2.  **Create Story**: Add a `my-component.stories.ts` file in the component directory to document it in Storybook.
3.  **Export**: Ensure the component is exported from `public-api.ts`.

## 📦 Building for Production

To build the library for distribution:
```bash
npm run build
```
The output will be in the `_Build_Output/` directory.
