# WorkBuddy Design System Prototype

Welcome! This project has been restructured to be easier to navigate.

## 📂 Project Structure

- **`Design-Tokens/`**: This is where the design "DNA" lives (colors, fonts, spacing).
  - Use `python3 convert_tokens.py` here to update the styles used by the developers.
- **`Development-Source/`**: This contains all the actual code for the design system.
  - **`projects/Library-Core/`**: The core components of the design system (Buttons, Inputs, etc.).
  - **`projects/Preview-App/`**: A "showcase" application where you can see the components in action.
- **`_Build_Output/`**: This is where the "finished products" go after the code is built (automatically hidden).

## ✨ Clean Workspace View
I have set up a "Clean View" for this project to hide technical "noise" (like `node_modules`, `tsconfig.json`, etc.).

- **To see everything**: In VS Code, go to **Settings** > Search for **"Exclude"** > and toggle off the rules.
- **Why hide them?**: This keeps your sidebar focused on the design and source code while keeping the "engine" running in the background.

## 🚀 Common Commands

If you are working inside the **`Development-Source`** folder:
- **`npm run storybook`**: Start the visual component explorer.
- **`npm run build`**: Build the library and the preview app.
- **`npm start`**: Run the preview application.
