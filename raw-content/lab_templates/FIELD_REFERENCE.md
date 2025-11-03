# Complete Field Reference for All Block Types

## HEADING Block
**Required:**
- `level` - Heading level: `h2`, `h3`, `h4`, `h5`, `h6`

**Optional:**
- `reference_id` - Unique ID for cross-referencing

**Content:** Heading text (plain text, not markdown heading format)

**Format:**
```markdown
<!-- HEADING -->
reference_id: introduction
level: h2
---
Introduction
<!-- /HEADING -->
```

**Note:** The heading text goes in the content section (after `---`), NOT in the metadata. This keeps HEADING consistent with all other block types.

## EQUATION Block
**Required:**
- `display_type` - Display mode: `display` or `inline`
- `spoken_version` - Accessibility description (minimum 5 characters)
- `auto_number` - Include in numbering: `true` or `false`

**Optional:**
- `reference_id` - Unique ID for cross-referencing
- `caption` - Optional caption below equation

## SAFETY_WARNING Block
**Required:**
- `severity` - Level: `danger`, `warning`, `caution`, or `info`
- `title` - Warning title/heading

**Optional:**
- `icon` - Icon name: `exclamation-triangle`, `exclamation-circle`, `bolt`, `fire`, `radiation`, `biohazard`, `skull`, `hand`, `eye`, `info-circle`
- `dismissible` - User can dismiss: `true` or `false` (default: false)

**Content:** Warning message (supports markdown)

## FIGURE Block
**Required:**
- `alt_text` - Accessibility description (minimum 10 characters)
- `image_id` OR `image_path` - Image reference

**Optional:**
- `reference_id` - Unique ID for cross-referencing
- `display_width` - Width: `full`, `half`, or `third` (default: full)
- `auto_number` - Include in numbering: `true` or `false` (default: true)
- `credit` - Attribution/source credit

**Content:** Caption (supports markdown/LaTeX)

## TABLE Block
**Required:**
- `caption` - Table caption (minimum 5 characters)

**Optional:**
- `reference_id` - Unique ID for cross-referencing
- `auto_number` - Include in numbering: `true` or `false` (default: true)
- `show_row_numbers` - Display row numbers: `true` or `false` (default: false)
- `summary` - Accessibility summary of table contents

**Content:** Markdown table

## CODE Block
**Required:**
- `language` - Programming language for syntax highlighting

**Optional:**
- `reference_id` - Unique ID for cross-referencing
- `caption` - Code description/purpose
- `show_line_numbers` - Display line numbers: `true` or `false` (default: false)

**Content:** Code

## BIBENTRY Block
**Required:**
- `reference_key` - Unique citation key
- `authors` - Author name(s) (use "and" to separate multiple authors)
- `title` - Title of work
- `year` - Publication year

**Optional:**
- `publication` - Journal, book, or conference name (e.g., "Physical Review, 42(3)" or "Pearson, 15th Edition")
- `pages` - Page range (e.g., "234-256" or "pp. 15-20")
- `url` - Web address for online sources
- `doi` - Digital Object Identifier (e.g., "10.1103/PhysRev.47.777")
- `access_date` - Date accessed for online sources (YYYY-MM-DD format)
- `notes` - Additional notes about the reference

**Format:**
```markdown
<!-- BIBENTRY -->
reference_key: young2020
authors: Young, H. D. and Freedman, R. A.
title: University Physics with Modern Physics
publication: Pearson, 15th Edition
year: 2020
<!-- /BIBENTRY -->
```

**Note:** BIBENTRY blocks are metadata-only (no `---` separator, no content section).
