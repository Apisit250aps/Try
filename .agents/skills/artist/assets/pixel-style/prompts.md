# Pixel Style — Generation Prompts

Built-in image generation; two initial separate new-image calls, no input images,
opaque backgrounds. These prompts describe intent, not verified grid metadata.

## character-example.png

```text
Use case: stylized-concept. Asset type: a pixel-art style reference image for the Artist skill in the Wayu Arts project. Create one original friendly adventurer character, full body, short dark hair, teal jacket, cream scarf, brown boots, small coral backpack. Clear readable silhouette and expressive simple eyes. Medium: authentic low-resolution 2D pixel art, deliberate square pixel clusters and crisp stair-step contours, consistent visibly coarse pixel size throughout the character. Target a 128 by 128 logical pixel canvas displayed with an integer nearest-neighbor enlargement to a square 1024 by 1024 reference image. Limited cohesive 16-color palette, near-black outline one logical pixel thick, selective two-tone shading, warm pastel teal/coral/cream accents. Centered full body with generous padding, a flat plain warm-cream opaque background. No smooth illustration, no vector curves, no antialiasing, no blur, no gradients, no 3D, no photographic texture, no text, no logos, no watermark, no interface or frame. This is a visual style example, not a sheet of multiple poses.
```

## environment-example.png

```text
Use case: illustration-story. Asset type: a pixel-art environment style reference image for the Artist skill in the Wayu Arts project. One original compact cozy train platform at dusk with a small teal-and-cream wooden shelter, a coral bench, one warm amber lamp, a short stretch of rails in the foreground, a leafy tree and a blue evening sky. No people, no train, no signs or writing. Small complete side-on environment vignette with clear silhouette hierarchy and readable architecture, comfortable margins. Medium: authentic low-resolution 2D pixel art, deliberate square pixel clusters, crisp stair-step contours, consistent coarse pixel scale across all objects. Target a 128 by 128 logical pixel canvas displayed with integer nearest-neighbor enlargement to a square 1024 by 1024 reference image. Limited cohesive palette of teal, cream, coral, muted blue and dark charcoal; use flat solid color clusters and two or three discrete shade steps per material. Entire background opaque. Avoid smooth/vector illustration, antialiasing, blur, smooth gradients, glow effects, 3D, photographic texture, excessive tiny noisy pixels, text, logos, watermarks and frames. Match a warm friendly original pixel-art collection; do not imitate an existing game.
```

## Detailed examples — 2026-11-25

Three additional new-image calls using the built-in tool, no input images,
opaque backgrounds. Logical dimensions are design targets until verified.

### character-detailed-example.png

```text
Use case: stylized-concept. Create one high-detail 2D pixel-art character illustration to demonstrate the Artist skill's DETAILED pixel preset. Subject: original friendly female botanical explorer, short auburn bob, sage-teal field jacket, cream shirt, plum trousers, tan boots, coral satchel and a small botanical field notebook held in one hand. Entire figure visible, expressive readable face, convincing hands and layered costume construction, clear silhouette with comfortable margin on every side. Native design intent: 256x256 logical pixels for this single character, high-detail pixel art rather than coarse tiny 32x32 sprite art, display as an enlarged square reference PNG. One consistent fine square pixel scale; clean stair-step contours; deliberate connected pixel clusters, restrained one- or two-logical-pixel outlines, solid hard-edged color clusters. Palette about 24-32 harmonized colors, 3 discrete shade levels per material, warm directional daylight. Plain solid warm-cream opaque background. Avoid smooth vector outlines, soft brushes, antialiasing, dithering noise, blurry shading, continuous gradients, textures, 3D, extra characters, text, logos, frames and watermark. Do not imitate any existing game, character or artist. It must read as richly detailed pixel illustration at a 256-pixel design resolution, not as a smooth painting with a pixel filter.
```

### expression-sheet-example.png

```text
Use case: stylized-concept. Make ONE pixel-art facial expression reference sheet with exactly FOUR equal square cells in a neat 2 by 2 arrangement, on a plain warm cream opaque background. Each cell shows the same original friendly young adult character: short dark-brown bob with a clear side part, brown eyes, one small coral hair clip on the character's anatomical left, teal jacket collar and cream scarf. Same face construction, head size, hair silhouette, clip side, head angle and palette in all four cells. Expressions in reading order: relaxed neutral, happy smile, focused concentration, mild surprise. Keep them distinct through brows, eyes and mouth without changing identity. Head and shoulders framing; each face is large and comfortably padded within its cell. Native design intent: EACH CELL at least 128x128 logical pixels, total sheet 256x256 logical pixels; do not allocate only 128 pixels to the entire sheet. Fine consistent square pixel clusters and clean stepped silhouettes; rich readable facial detail, 24-32-color cohesive palette, 3 solid shade bands, crisp hard edges, no antialiasing or smooth gradients. Present an enlarged square reference PNG. No labels, writing, speech bubbles, frames, dividers, interface, logos or watermark; separate cells using generous negative space. No painterly texture, blur, glossy 3D or tiny coarse 32x32 sprites. This is a visual reference sheet, not an animation.
```

### environment-wide-example.png

```text
Use case: illustration-story. Create a richly detailed original pixel-art environment illustration of a peaceful small-town canal-side bookshop at late afternoon, warm light in the windows, teal-green timber storefront, coral awning, cream plaster, tiled roof, books visible through the window, a bicycle parked outside, broad stone walkway, canal and small bridge receding in the background, trees framing the street. No people and no legible shop signage or text. Wide cinematic 16:9 composition with clear foreground/middle/background separation, focal point on the bookshop, controlled detail hierarchy and coherent perspective. Native design intent: 512x288 logical pixels (both dimensions exceed 128), high-detail pixel illustration with fine consistent square pixel scale and carefully built clusters; show clean stepped contours at larger viewing scale. Ask for an enlarged 16:9 reference PNG. Use a restrained 32-48-color scene palette, discrete 3 or 4 shade levels per material, hard-edged shapes; warm afternoon sunlight and cooler architectural shadows represented by solid pixel clusters. Full opaque environment background. No smooth gradients, glow, blur, painterly or photographic texture, anti-aliased vector curves, tiny coarse 32x32 appearance, text, labels, UI, frames, logos or watermark. No imitation of any existing game or artist. Make architecture and material detail intentional and legible rather than scattered noisy pixels.
```
