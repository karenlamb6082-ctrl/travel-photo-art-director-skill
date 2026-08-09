---
name: travel-photo-art-director
description: Curate, pre-edit, art-direct, generate, and quality-check cohesive art series from travel photo folders or selected travel images. Use when Codex needs to review many travel photos, build contact sheets, select representative landscapes, improve crops and color before design, create a 3:5 or source-responsive editorial series, combine preserved photography with zine collage and experimental materials, produce source-comparison variants, or deliver a verified multi-image collection rather than a single generic filter.
---

# Travel Photo Art Director

Turn a travel photo folder into a deliberately curated art series. Preserve photographic evidence when it strengthens the work, remove it when conceptual distillation is stronger, and judge the collection as a sequence rather than nine unrelated images.

## Core principles

- Curate before generating. Do not force every supplied photo into the series.
- Improve the source before styling. Crop, rotate, straighten, balance tone, and remove distractions when useful.
- Derive design decisions from the source geometry, weather, color, and emotional residue.
- Preserve truthful uncertainty. Never invent a location, date, landmark, or event that is not supported by metadata or the user.
- Make each image distinct while maintaining a shared material and color vocabulary.
- Keep final images project-local; do not leave deliverables only in a generation cache.
- Verify the series visually and as files before claiming completion.

## Default contract

When the user asks for a series without specifying details, use these defaults:

- nine final images;
- vertical 3:5 output unless source orientation or the user requires otherwise;
- landscape emphasis;
- no page numbers;
- optional short English text, never long model-generated copy;
- one overview contact sheet;
- non-destructive source handling;
- local delivery first; upload externally only when requested or already established in the task.

Ask only when a missing choice would materially change the result. Otherwise inspect the sources and proceed.

## Workflow

### 1. Ground the source set

Identify:

- source folder or supplied images;
- requested image count and aspect ratio;
- subject preference such as landscape, people, architecture, or food;
- whether original photo pixels should remain visible;
- whether text, comparison variants, or external delivery are wanted.

Inventory the files with fast filesystem search. Group bursts and near-duplicates before judging individual frames.

For a large folder, run `scripts/build_contact_sheet.py` by day or subfolder. Inspect every resulting sheet before selecting. Do not infer the whole collection from a small sample.

### 2. Curate representative sources

Build a shortlist that covers different visual roles, not merely different timestamps:

- atmospheric opener;
- scale or geological structure;
- water or movement;
- path, road, bridge, or directional line;
- botanical detail;
- broad field, lake, or quiet plane;
- weather or sky event;
- color event;
- closing image with visual release.

Prefer frames with a clear gesture, strong figure-ground relationship, useful negative space, or unusual material detail. Exclude accidental clutter, weak duplicates, and subjects outside the user's emphasis.

Do not reuse one source in more than two final images unless repetition is a deliberate series device.

### 3. Choose the art mode

Read `references/modes.md` before selecting a mode. Choose per image, not automatically for the whole folder:

- **Original-Led** when the photograph is already strong and should remain dominant.
- **Distilled** when the source idea is stronger than its literal pixels.
- **Hybrid Mixed-Media** when preserved photography should collide with zine structure and tactile material transformation.

For a varied nine-image set, avoid putting all nine in the same mode. Use Hybrid Mixed-Media as the default only when the user explicitly favors preserved photography plus artistic transformation.

### 4. Pre-edit non-destructively

Inspect each selected source at useful resolution. Create a derived master rather than modifying the original.

Apply only source-serving edits:

- crop to the strongest gesture;
- rotate slightly when a diagonal becomes more intentional;
- straighten accidental horizons;
- recover highlight and shadow structure;
- reduce color casts while preserving meaningful weather;
- remove vehicles, signs, food, people, or foreground clutter only when they conflict with the brief;
- retain texture and believable photographic detail.

Do not over-sharpen, erase atmosphere, or replace the whole scene before deciding the art mode.

### 5. Build an art-direction recipe

Read `references/art-direction.md` for selection, typography, color, and material guidance.

Define for every output:

1. source role and preserved anchors;
2. dominant composition family;
3. photographic share, if any;
4. one primary material process;
5. at most two supporting processes;
6. one color event or restrained palette;
7. text role, exact wording, or an explicit no-text decision;
8. hard exclusions.

Do not treat a material name as a complete concept. Wax, resin, cyanotype, paper, fiber, radiograph, foil, ceramic, graphite, and pigment must perform a source-derived function.

### 6. Generate deliberately

Use the available image-generation or image-editing capability. Issue one generation call per distinct image rather than asking for unrelated outputs from one generic prompt.

Label references explicitly:

- edit target or photographic subject;
- style or prior-series reference;
- supporting compositing or material reference.

For Hybrid mode, require a recognizably photographic region and specify where material transformation begins. For Distilled mode, explicitly prohibit retained photographic pixels. For Original-Led mode, protect source geometry and limit intervention.

Keep in-image text short and exact. Prefer zero to four words. If accurate text is not essential, omit it rather than accepting corrupted lettering.

### 7. Judge the collection

Save every candidate into the workspace and run `scripts/build_series_overview.py` after nine images exist.

Inspect the overview for:

- repeated compositions or motifs;
- one source dominating the series;
- excessive use of the same color or material;
- weak photographic anchors;
- accidental people, food, vehicles, signs, UI, logos, watermarks, dates, or page numbers;
- misspelled or unnecessary text;
- a flat sequence with no opening, contrast, pause, or ending.

Regenerate weak members instead of keeping them merely because they were already produced. Read `references/quality-gates.md` before final delivery.

### 8. Build requested variants

When the user requests a source-comparison version:

- crop the exact source regions used by the artwork;
- lightly correct and rotate them when beneficial;
- combine multiple source crops into one coherent source board;
- place the source board consistently on the requested side;
- preserve the final output ratio;
- keep the artwork itself unchanged unless revision is requested.

Do not label comparisons with page numbers unless explicitly requested.

### 9. Deliver and verify

Deliver:

- numbered final images;
- one overview image;
- comparison variants when requested;
- concise notes on the selected art modes and any verified limitations.

Verify file count, names, dimensions, and readability. If uploading to Drive or another service, wait for completion and list the destination folder to confirm every file exists.

## Bundled resources

- `scripts/build_contact_sheet.py`: build labeled sheets for broad source inspection.
- `scripts/build_series_overview.py`: build a clean grid for collection-level QA.
- `references/modes.md`: select and constrain the three art modes.
- `references/art-direction.md`: curate, pre-edit, compose, color, texture, and write prompts.
- `references/quality-gates.md`: validate individual works, the series, comparisons, and delivery.

