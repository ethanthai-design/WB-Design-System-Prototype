# WB-Design System Prototype

Welcome to the **WB-Design System Prototype** repository. This project is a foundational design system built for WorkBuddy, focusing on scalability, multi-theme support, and seamless developer-designer handoff.

## 📂 Repository Structure

This repository is organized into two main parts:

1.  **[`wb-design-tokens`](./wb-design-tokens)**: The source of truth for design tokens. It contains JSON token definitions and a conversion pipeline to generate CSS variables.
2.  **[`wb-design-system`](./wb-design-system)**: The Angular-based component library. It consumes the generated design tokens and provides a library of reusable UI components.

## 🚀 Quick Start

To get started with the design system, follow these steps:

### 1. Generate Design Tokens
If you've updated tokens in the `wb-design-tokens` directory, you'll need to regenerate the CSS:
```bash
cd wb-design-tokens
python3 convert_tokens.py
```

### 2. Run Storybook
To see and interact with the components in Storybook:
```bash
cd wb-design-system
npm install
npm run storybook
```

## 🛠 Tech Stack

- **Framework**: [Angular 19](https://angular.dev/)
- **Documentation/Workbench**: [Storybook](https://storybook.js.org/)
- **Styling**: Vanilla CSS with Design Tokens
- **Design Tokens**: JSON-based tokens converted via Python

## 📜 Documentation

- [Design Tokens Guide](./wb-design-tokens/README.md) - Learn how tokens are structured and updated.
- [Component Library Guide](./wb-design-system/README.md) - Learn how to build and use components.
