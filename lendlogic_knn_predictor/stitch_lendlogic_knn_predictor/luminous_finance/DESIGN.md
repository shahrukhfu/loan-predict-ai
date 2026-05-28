---
name: Luminous Finance
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#c7c4d7'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#908fa0'
  outline-variant: '#464554'
  surface-tint: '#c0c1ff'
  primary: '#c0c1ff'
  on-primary: '#1000a9'
  primary-container: '#8083ff'
  on-primary-container: '#0d0096'
  inverse-primary: '#494bd6'
  secondary: '#4edea3'
  on-secondary: '#003824'
  secondary-container: '#00a572'
  on-secondary-container: '#00311f'
  tertiary: '#ffb2b7'
  on-tertiary: '#67001b'
  tertiary-container: '#ff516a'
  on-tertiary-container: '#5b0017'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e1e0ff'
  primary-fixed-dim: '#c0c1ff'
  on-primary-fixed: '#07006c'
  on-primary-fixed-variant: '#2f2ebe'
  secondary-fixed: '#6ffbbe'
  secondary-fixed-dim: '#4edea3'
  on-secondary-fixed: '#002113'
  on-secondary-fixed-variant: '#005236'
  tertiary-fixed: '#ffdadb'
  tertiary-fixed-dim: '#ffb2b7'
  on-tertiary-fixed: '#40000d'
  on-tertiary-fixed-variant: '#92002a'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  display-lg:
    fontFamily: Geist
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Geist
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Geist
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  headline-md:
    fontFamily: Geist
    fontSize: 24px
    fontWeight: '500'
    lineHeight: 32px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-md:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.02em
  label-sm:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 4px
  container-padding-desktop: 40px
  container-padding-mobile: 20px
  gutter: 24px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style

The design system is engineered for a high-stakes, high-trust financial environment focused on loan prediction. The brand personality is precise, sophisticated, and technologically advanced. It aims to evoke a sense of "digital craftsmanship" and "predictive clarity."

The aesthetic is a refined **Glassmorphism** integrated with **Corporate Modern** structures. It utilizes deep layering, translucent surfaces, and subtle "glowing" indicators to represent data flow and decision-making processes. The UI must feel like a premium command center—authoritative yet accessible.

**Key Visual Principles:**
- **Optical Depth:** Use of blurred background fills to create a sense of Z-axis space.
- **Luminance over Color:** Using light and glow to draw attention rather than heavy fills.
- **Precision:** Perfect alignment and thin strokes to mirror the accuracy of financial algorithms.

## Colors

The palette is anchored in a deep obsidian environment to reduce eye strain and emphasize critical data points.

- **Primary (Electric Indigo):** Used for interactive elements, primary actions, and "calculating" states.
- **Success (Emerald):** Reserved exclusively for loan approvals and positive financial indicators.
- **Error/Rejection (Crimson):** Used for loan rejections, warnings, and high-risk alerts.
- **Neutral/Surface:** The background is `#0a0a0a`. Surface containers use `#171717` with varying degrees of transparency to allow for glassmorphism effects.
- **Accents:** Use low-opacity indigo glows behind primary containers to suggest activity and depth.

## Typography

This design system utilizes a trio of typefaces to achieve a "Technical Premium" look.

- **Geist** is used for headlines to provide a sharp, geometric, and modern tech feel.
- **Inter** handles the body copy, ensuring maximum readability for complex financial terms.
- **JetBrains Mono** is employed for labels, data points, and "calculated" values to evoke a sense of algorithmic precision.

**Contrast Strategy:** Use high weight contrast between `headline-lg` (Bold) and `body-md` (Regular). Numeric data should always be set in the label font to differentiate "data" from "instruction."

## Layout & Spacing

The layout follows a **Fluid Grid** model with strict 4px increments.

- **Desktop:** 12-column grid, 24px gutters, max-width 1440px.
- **Tablet:** 8-column grid, 16px gutters.
- **Mobile:** 4-column grid, 16px gutters.

**Spacing Philosophy:** Use generous whitespace (`stack-lg`) between major sections to prevent information density fatigue. Elements within a card (e.g., a label and a value) should use `stack-sm` to maintain proximity.

## Elevation & Depth

Elevation is achieved through **Glassmorphism and Tonal Layering** rather than traditional drop shadows.

1.  **Level 0 (Base):** `#0a0a0a` flat background.
2.  **Level 1 (Cards/Containers):** `#171717` at 70% opacity with a `16px` backdrop-blur. A `1px` solid border using `#262626` is mandatory to define edges.
3.  **Level 2 (Modals/Popovers):** `#1e1e1e` at 80% opacity, `32px` backdrop-blur, and a subtle outer glow of `primary_color` (10% opacity) to suggest it is floating.

**Strokes:** Use "inner-glow" strokes on buttons—a 1px top-border that is slightly lighter than the button color to simulate a physical edge catching a light source.

## Shapes

The design system uses a **Rounded** shape language to soften the "industrial" feel of the dark theme.

- **Base Radius:** 0.5rem (8px) for input fields, buttons, and small widgets.
- **Large Radius:** 1rem (16px) for primary container cards and modals.
- **Interactive Elements:** Buttons should maintain a consistent 8px radius; avoid pill shapes to keep the look structured and professional.

## Components

### Buttons
- **Primary:** Electric Indigo background, white text. Add a 10px indigo shadow with 40% opacity only on hover to simulate "ignition."
- **Ghost:** Transparent background, 1px border (`#262626`), transition to white border on hover.

### Input Fields
- Dark backgrounds (`#0a0a0a`), 1px borders.
- **Focus State:** Border changes to Electric Indigo with a 2px outer glow. Labels should shift to the `label-sm` style above the field.

### Loan Status Chips
- **Approved:** Emerald green text with a 10% emerald background tint and emerald border.
- **Denied:** Crimson text with a 10% crimson background tint and crimson border.

### Data Cards
- Glassmorphic finish (Backdrop blur).
- Include a 1px border. 
- Header within the card should use `label-sm` for the category and `headline-md` for the primary value.

### Progress Indicators (The "Prediction" Engine)
- Use thin, animated lines. The "Calculating" state should use a sweeping indigo gradient movement across a track.