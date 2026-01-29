# WB-Design System Prototype

Welcome to the **WB-Design System Prototype** repository. This project is a foundational design system built for WorkBuddy, focusing on scalability, multi-theme support, and seamless developer-designer handoff.

## 📂 Repository Structure

This repository is organized into two main parts:

1.  **[`Design-Tokens`](./Design-Tokens)**: The source of truth for design tokens. It contains JSON token definitions and a conversion pipeline to generate CSS variables.
2.  **[`Development-Source`](./Development-Source)**: The main development workspace containing:
    - **`Library-Core`**: The Angular-based component library.
    - **`Preview-App`**: A showcase/preview application for testing components.

## 🚀 Quick Start

To get started with the design system, follow these steps:

### 1. Generate Design Tokens
If you've updated tokens in the `Design-Tokens` directory, you'll need to regenerate the CSS:
```bash
cd Design-Tokens
python3 convert_tokens.py
```

### 2. Run the Library Preview
To run the preview application:
```bash
cd Development-Source
npm install
npm start
```

### 3. Run Storybook
To see and interact with components in Storybook:
```bash
cd Development-Source
npm run storybook
```

## 🛠 Tech Stack

- **Framework**: [Angular 19](https://angular.dev/)
- **Documentation/Workbench**: [Storybook](https://storybook.js.org/)
- **Styling**: Vanilla CSS with Design Tokens
- **Design Tokens**: JSON-based tokens converted via Python

## 📜 Documentation

- [Design Tokens Guide](./Design-Tokens/README.md) - Learn how tokens are structured and updated.
- [Development Workspace Guide](./Development-Source/README.md) - Learn how to build and use components.
