# Complete Field Reference for All Block Types

## HEADING Block
**Required:**
- `level` - Heading level: `h2`, `h3`, `h4`, `h5`, `h6` (auto-extracted from `##` count)

**Optional:**
- `reference_id` - Unique ID for cross-referencing (extracted from `{#id}` syntax)

**Content:** Heading text

**🎨 New Typora-Compatible Format (Recommended):**
```markdown
## Introduction {#introduction}

### Subsection {#theory-derivation}
```

**Traditional Format (Still Supported):**
```markdown
<!-- HEADING -->
reference_id: introduction
level: h2
---
Introduction
<!-- /HEADING -->
```

**Smart Extraction:**
- Level extracted from `##` symbols (2-6 supported)
- Reference ID extracted from `{#id}` attribute
- Both formats work on import

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
- `alt_text` - Accessibility description (minimum 10 characters, extracted from `![alt](path)`)
- `image_id` OR `image_path` - Image reference (extracted from `![alt](path)`)

**Optional:**
- `reference_id` - Unique ID for cross-referencing
- `display_width` - Width: `full`, `half`, or `third` (default: full)
- `auto_number` - Include in numbering: `true` or `false` (default: true)
- `credit` - Attribution/source credit

**Content:** Standard markdown image `![alt](path)` followed by caption as italic text

**🎨 New Typora-Compatible Format (Recommended):**
```markdown
<!-- FIGURE -->
reference_id: fig-apparatus
display_width: full
auto_number: true
---

![Photo of 2-meter inclined plane with cart and sensors](images/apparatus.jpg)

*Experimental apparatus showing inclined plane and photogate sensors.*
<!-- /FIGURE -->
```

**Traditional Format (Still Supported):**
```markdown
<!-- FIGURE -->
reference_id: fig-apparatus
image_path: images/apparatus.jpg
alt_text: Photo of 2-meter inclined plane with cart and sensors
display_width: full
auto_number: true
---
Experimental apparatus showing inclined plane and photogate sensors.
<!-- /FIGURE -->
```

**Smart Extraction:**
- Alt text extracted from `![alt](path)` syntax
- Image path extracted from `![alt](path)` syntax
- Caption extracted from italic text
- Both formats work on import

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
- `language` - Programming language for syntax highlighting (auto-extracted from ` ```language`)

**Optional:**
- `reference_id` - Unique ID for cross-referencing (extracted from `{#id}`)
- `caption` - Code description/purpose (italic text above code block)
- `show_line_numbers` - Display line numbers: `true` or `false` (default: false)

**Content:** Standard fenced code block

**🎨 New Typora-Compatible Format (Recommended):**
```markdown
*Python script to calculate average velocity* {#code-data-analysis}

```python
import numpy as np
distances = np.array([1.5, 1.5, 1.5])
times = np.array([2.34, 1.67, 1.35])
velocities = distances / times
print(f"Average: {np.mean(velocities):.2f} m/s")
```
```

**Simple Code Without Caption:**
```markdown
```python
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [1, 4, 9])
plt.show()
```
```

**Traditional Format (Still Supported):**
```markdown
<!-- CODE -->
reference_id: code-data-analysis
language: python
caption: Python script to calculate average velocity
show_line_numbers: true
---
```python
import numpy as np
velocities = distances / times
```
<!-- /CODE -->
```

**Smart Extraction:**
- Language extracted from fence info string (` ```python`)
- Caption extracted from italic text above code block
- Reference ID extracted from `{#id}` attribute
- Both formats work on import

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

## MARKDOWN Block
**Required:**
- None

**Optional:**
- None

**Content:** Regular markdown text with formatting

**🎨 New Format (Plain Markdown - Recommended):**
```markdown
This is regular markdown content with **bold**, *italic*, and `code` formatting.

You can use:
- Unordered lists
- Multiple paragraphs
- [Links](https://example.com)
- Inline math: $E = mc^2$

All without any HTML comment wrappers!
```

**Traditional Format (Still Supported):**
```markdown
<!-- MARKDOWN -->
---
This is markdown content wrapped in HTML comments.
<!-- /MARKDOWN -->
```

**How It Works:**
- On **export**: Generates plain markdown without wrappers
- On **import**: Both wrapped and unwrapped markdown work
- **Backward compatible**: Old HTML comment format still supported
- **Note**: Most lab guide content doesn't need explicit MARKDOWN blocks
