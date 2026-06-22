# Styling, Customization & Theming Reference

shadcn/ui uses semantic CSS variables mapped to Tailwind utility classes. This provides a highly flexible configuration model: updating a single CSS variable dynamically styles all components referencing that token in both light and dark modes.

---

## 1. Core Color System

All core components follow the `name` / `name-foreground` token pair pattern.
- The base variable controls the background color of the surface.
- The `-foreground` variable controls typography and icon colors inside that surface.

### Semantic Token Map

| Token | Scoping / Purpose |
| :--- | :--- |
| `--background` / `--foreground` | Main viewport background and default text |
| `--card` / `--card-foreground` | Card widgets, dialog boxes, and surface panels |
| `--popover` / `--popover-foreground` | Floating popovers, tooltips, and flyout selectors |
| `--primary` / `--primary-foreground` | Primary buttons, active elements, and CTA highlights |
| `--secondary` / `--secondary-foreground` | Secondary/alternative action layers |
| `--muted` / `--muted-foreground` | Muted headers, secondary labels, and disabled states |
| `--accent` / `--accent-foreground` | Hover targets and subtle selection highlights |
| `--destructive` / `--destructive-foreground` | Error states, dangerous actions, and warning cards |
| `--border` | Dividers and global element boundaries |
| `--input` | Text inputs and selector borders |
| `--ring` | Focus state outlines and accessibility rings |

---

## 2. Color Spaces: OKLCH Format

Modern presets in shadcn/ui leverage the **OKLCH** color format (`oklch(L C H)`), which offers uniform perceptual brightness across all hues:
- **Lightness (L)**: Represents brightness (from `0` for absolute black to `1` for pure white).
- **Chroma (C)**: Represents color saturation (from `0` for complete monochrome/gray to high values for vibrant colors).
- **Hue (H)**: Represents the color angle on the wheel (from `0` to `360`).

*Example CSS variable:*
```css
--primary: oklch(0.205 0 0); /* A perceptual gray-black hue */
```

---

## 3. Registering Custom Colors

To add new custom theme properties, always edit the global stylesheet specified by `tailwindCssFile` in `components.json` (usually `globals.css`).

### Step 1: Declare variables in the CSS entry file
```css
:root {
  --warning: oklch(0.84 0.16 84);
  --warning-foreground: oklch(0.28 0.07 46);
}

.dark {
  --warning: oklch(0.41 0.11 46);
  --warning-foreground: oklch(0.99 0.02 95);
}
```

### Step 2: Register variables with Tailwind

#### For Tailwind CSS v4 (`@theme inline`)
Add the theme properties directly within your CSS entry point:
```css
@theme inline {
  --color-warning: var(--warning);
  --color-warning-foreground: var(--warning-foreground);
}
```

#### For Tailwind CSS v3 (`tailwind.config.js`)
Extend the theme colors mapping inside the configuration script:
```javascript
module.exports = {
  theme: {
    extend: {
      colors: {
        warning: "oklch(var(--warning) / <alpha-value>)",
        "warning-foreground": "oklch(var(--warning-foreground) / <alpha-value>)",
      },
    },
  },
}
```

---

## 4. Dark Mode Setup

The default dark mode uses class-based toggle controls via a `.dark` selector on the root document element (`<html>`).

### Integrating inside React (Next.js Example)
Use `next-themes` to manage states:
```tsx
import { ThemeProvider } from "next-themes"

export function AppProviders({ children }: { children: React.ReactNode }) {
  return (
    <ThemeProvider attribute="class" defaultTheme="system" enableSystem>
      {children}
    </ThemeProvider>
  )
}
```

---

## 5. Border Radius Configuration

A single global variable controls component rounding metrics:
```css
--radius: 0.5rem;
```
Component structures automatically calculate nested rounding radii using dynamic offsets to maintain visual hierarchy:
- Outer element (e.g. `Card` wrapper): `rounded-lg` $\rightarrow$ `var(--radius)`
- Inner element (e.g. `Input` inside card): `rounded-md` $\rightarrow$ `calc(var(--radius) - 2px)`

---

## 6. Customizing Component Styles

Follow these four patterns in sequential preference to customize components:

### Pattern 1: Built-in Variants
Leverage existing variants built with `class-variance-authority`:
```tsx
<Button variant="outline" size="sm">Action</Button>
```

### Pattern 2: Component Layout overrides
Override spacing, width, and alignments using `className`:
```tsx
<Card className="max-w-md mx-auto mt-8">...</Card>
```

### Pattern 3: Adding custom variants
Add a variant entry directly to the component definition file (e.g., `components/ui/button.tsx`):
```tsx
// inside button.tsx cva() options:
variants: {
  variant: {
    warning: "bg-warning text-warning-foreground hover:bg-warning/90",
  }
}
```

### Pattern 4: Wrapping Primitives
Combine multiple shadcn/ui components into high-level reuse layouts:
```tsx
export function ConfirmModal({ title, onConfirm, children }: ConfirmProps) {
  return (
    <AlertDialog>
      <AlertDialogTrigger asChild>{children}</AlertDialogTrigger>
      <AlertDialogContent>
        <AlertDialogHeader>
          <AlertDialogTitle>{title}</AlertDialogTitle>
        </AlertDialogHeader>
        <AlertDialogFooter>
          <AlertDialogCancel>Cancel</AlertDialogCancel>
          <AlertDialogAction onClick={onConfirm}>Proceed</AlertDialogAction>
        </AlertDialogFooter>
      </AlertDialogContent>
    </AlertDialog>
  )
}
```
