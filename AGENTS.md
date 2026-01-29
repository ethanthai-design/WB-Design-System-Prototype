# AGENTS.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Repository overview (big picture)
This repo contains two sibling workstreams:

- `wb-design-system/`: an Angular workspace (Angular CLI) containing:
  - `projects/wb-design-system` — the publishable **component library** (built with `ng-packagr`).
  - `projects/showcase` — an **Angular application** used as a local playground to render/validate the library.
  - Storybook configured for the library.
- `wb-design-tokens/`: source **design token JSON** (organized by category/mode). The design system consumes tokens via a generated CSS variables file.

The token CSS variables live at `wb-design-system/projects/wb-design-system/src/lib/styles/design_tokens.css` and are consumed by:
- Storybook (via `wb-design-system/angular.json` storybook `styles`)
- the Showcase app (via `wb-design-system/projects/showcase/src/styles.scss`)

## Common commands
Most work happens inside `wb-design-system/`.

### Install dependencies
```bash
cd wb-design-system
npm ci
```
(Use `npm install` if you need to update the lockfile.)

### Run the local “showcase” app
`package.json` has `"start": "ng serve"`, but the workspace does not set a `defaultProject`, so prefer an explicit project name:

```bash
cd wb-design-system
npx ng serve showcase
```

### Build
Build the library (outputs to `wb-design-system/dist/wb-design-system/` per `projects/wb-design-system/ng-package.json`):

```bash
cd wb-design-system
npx ng build wb-design-system
```

Build the showcase app:

```bash
cd wb-design-system
npx ng build showcase
```

Watch mode (library):
```bash
cd wb-design-system
npx ng build wb-design-system --watch --configuration development
```

### Storybook
Run Storybook (port `6006` configured in `wb-design-system/angular.json`):

```bash
cd wb-design-system
npm run storybook
```

Build static Storybook:
```bash
cd wb-design-system
npm run build-storybook
```

Note: Storybook is wired to Compodoc (`compodoc: true`) and `projects/wb-design-system/.storybook/preview.ts` imports `projects/wb-design-system/documentation.json`.

### Tests
Run unit tests for the library:
```bash
cd wb-design-system
npx ng test wb-design-system
```

Run unit tests for the showcase app:
```bash
cd wb-design-system
npx ng test showcase
```

Run a single spec file (Karma builder supports `--include`):
```bash
cd wb-design-system
npx ng test wb-design-system --watch=false --include="projects/wb-design-system/src/lib/**/some-file.spec.ts"
```

### Linting
No `lint` script/target is configured in this repo’s Angular workspace (`angular.json` does not define a `lint` architect target).

## Code structure notes
### Angular library (`projects/wb-design-system`)
- Public entrypoint: `projects/wb-design-system/src/public-api.ts` — export any components/services you want consumers to import.
- Implementation lives under `projects/wb-design-system/src/lib/`.
- Packaging config: `projects/wb-design-system/ng-package.json` (ng-packagr).

### Storybook in this repo
- Storybook config: `projects/wb-design-system/.storybook/`.
- Stories live alongside the library source at `projects/wb-design-system/src/**` (commonly under `src/stories/`).

### Design tokens
- Token sources: `wb-design-tokens/` (JSON grouped by mode/category).
- Generated output consumed by Angular/Storybook: `wb-design-system/projects/wb-design-system/src/lib/styles/design_tokens.css`.
  - The CSS is structured to support themes/variants via attributes such as `data-theme` (e.g. `data-theme="dark"`) and `data-typography`.

There is also a Python script at `wb-design-tokens/convert_tokens.py` intended to generate CSS variables, but it currently references an input directory (`originial-tokens/`) and an output path that do not exist in this repo. If you plan to regenerate tokens from the JSON folders in `wb-design-tokens/`, verify/update the script paths first.