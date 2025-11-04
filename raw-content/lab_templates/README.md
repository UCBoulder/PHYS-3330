# Lab Guide Markdown Templates

This directory contains markdown templates for creating lab guides that can be imported into the Wagtail CMS.

## Quick Start

1. **Copy the template**: `cp comprehensive-template.md my-lab-01.md`
2. **Create images folder**: `mkdir my-lab-01-images`
3. **Edit the template**: Replace example content with your lab content
4. **Add images**: Place all images in the images folder
5. **Validate**: Use Wagtail's "Validate Markdown" button before importing
6. **Import**: Upload via Wagtail admin → Navigate to lab page → "Import Markdown"

---

## Understanding the Template Structure

### 1. YAML Frontmatter (Required)

Every lab guide must start with YAML frontmatter containing metadata:

```yaml
---
lab_number: 1
lab_title: "Your Lab Title Here"
duration_hours: 3.0
difficulty: introductory  # Options: introductory, intermediate, advanced
enable_section_numbering: true
keywords: "physics, mechanics, newton"  # Optional
---
```

**Required Fields:**
- `lab_number` - Integer (e.g., 1, 2, 3)
- `lab_title` - String in quotes
- `duration_hours` - Decimal number (e.g., 2.0, 3.5)
- `difficulty` - One of: `introductory`, `intermediate`, `advanced`
- `enable_section_numbering` - Boolean: `true` or `false`

**Optional Fields:**
- `keywords` - Comma-separated string for searchability

### 2. Learning Objectives Section

Immediately after frontmatter, add a Learning Objectives section:

```markdown
## Learning Objectives

- Students will learn to...
- Students will understand...
- Students will be able to...
```

This section supports **basic markdown only** (bold, italic, lists). No block markers needed here.

### 3. Content Blocks

The rest of your lab guide uses **block markers** for structured content. Each block has:
- Opening marker: `<!-- BLOCKTYPE -->`
- Metadata fields (key: value pairs)
- Closing marker: `<!-- /BLOCKTYPE -->`
- Content (appears after closing marker for most blocks)

### 4. Bibliography Section (Optional)

If your lab guide has citations (using `\cite{reference_key}`), add a **separate** Bibliography section at the very end:

```markdown
# Bibliography

<!-- BIBENTRY -->
reference_key: young2020
authors: Young, H. D. and Freedman, R. A.
title: University Physics with Modern Physics
publication: Pearson, 15th Edition
year: 2020
<!-- /BIBENTRY -->
```

**Important:** This `# Bibliography` section is stored separately from your main content in the Wagtail admin.

---

## Block Type Reference

### HEADING Block

Use for major sections to enable cross-referencing and auto-numbering.

**🎨 New Typora-Compatible Format (Recommended):**
```markdown
## Introduction {#introduction}

### Subsection {#theory-derivation}
```

**Key Benefits:**
- ✅ Renders beautifully in Typora with automatic TOC generation
- ✅ Standard Kramdown/Pandoc-style `{#id}` attributes for cross-references
- ✅ No HTML comments needed for simple cases
- ✅ Heading level extracted automatically from `##` symbols
- ✅ Clean, readable markdown

**Traditional Format (Still Supported):**
```markdown
<!-- HEADING -->
reference_id: introduction
level: h2
---
Introduction
<!-- /HEADING -->
```

**How It Works:**
- On **export**: Generates standard markdown headings (e.g., `## Title {#id}`)
- On **import**: Smart extraction parses heading syntax automatically
- **Backward compatible**: Old HTML comment format still works

**Required Fields:**
- `level` - Heading level: `h2`, `h3`, `h4`, `h5`, or `h6` (auto-extracted from `##` count)

**Optional Fields:**
- `reference_id` - Unique ID for cross-references (extracted from `{#id}` syntax)

**When to use:**
- Major sections you want to reference elsewhere
- Sections that should appear in auto-generated table of contents
- Top-level headings (Introduction, Theory, etc.)
- **Any heading you want auto-numbered** (if `enable_section_numbering: true`)

**When NOT to use:**
- Minor subsections that don't need cross-referencing AND don't need numbering
- Use regular markdown headings (###) ONLY if you want unnumbered subsections
- **Note:** Regular markdown headings will NOT be auto-numbered, even if section numbering is enabled

**Section Numbering Behavior:**
- `enable_section_numbering: true` in frontmatter → HEADING blocks get numbered
- Regular markdown headings (without HEADING blocks) are NEVER numbered
- For consistent appearance, use HEADING blocks for ALL major sections when numbering is enabled

**Examples:**

**Simple Heading (Typora-compatible):**
```markdown
## Introduction {#introduction}

This is the introduction text...
```

**Heading Without Reference ID:**
```markdown
## Background

This section doesn't need to be referenced elsewhere...
```

**Subsection Example:**
```markdown
## Theory {#theory}

### Derivation {#theory-derivation}

Detailed derivation here...
```

**Traditional Format Example:**
```markdown
<!-- HEADING -->
reference_id: introduction
level: h2
---
Introduction
<!-- /HEADING -->

This is the introduction text...
```

**Referencing:**
```markdown
As described in \ref{introduction}, we investigate Newton's laws.
```

**Important Notes:**
- Use standard markdown heading syntax (`##`) for best Typora compatibility
- Reference IDs are optional - only add `{#id}` if you need to reference the section
- Heading level is determined by number of `#` symbols (2-6 supported)
- Smart extraction works both ways: import and export

---

### EQUATION Block

Use for mathematical equations you want to reference.

**Format:**
```markdown
<!-- EQUATION -->
reference_id: eq-unique-name
display_type: display
auto_number: true
spoken_version: Force equals mass times acceleration
caption: Newton's Second Law
<!-- /EQUATION -->
---
F = ma
```

**Required Fields:**
- `display_type` - Display mode: `display` (block equation, centered) or `inline` (within text)
- `spoken_version` - Accessibility description for screen readers (minimum 5 characters)
- `auto_number` - Include in equation numbering: `true` or `false`

**Optional Fields:**
- `reference_id` - Unique ID for cross-references (required if you want to use `\ref{}`)
- `caption` - Optional caption displayed below the equation

**Display Types:**
- `display` - Block equation (centered, on own line) - **Most common for lab guides**
- `inline` - Inline equation (within paragraph text) - Rarely used in markdown format

**Auto-Numbering:**
- `auto_number: true` - Equation gets numbered (e.g., "Equation 1", "Equation 2")
- `auto_number: false` - Equation is not numbered (useful for intermediate steps)

**Spoken Version Guidelines:**
Read the equation naturally as you would speak it aloud:
- "Force equals mass times acceleration" for $F = ma$
- "One half m v squared" for $\frac{1}{2}mv^2$
- "Partial squared u over partial t squared equals c squared partial squared u over partial x squared"

**LaTeX Support:**
- Full LaTeX math syntax supported (fractions, Greek letters, matrices, etc.)
- Use `---` separator between metadata and LaTeX code
- Supports multi-line equations with `\begin{aligned}` environment

**Examples:**

**Basic Equation:**
```markdown
<!-- EQUATION -->
reference_id: eq-newton-2nd
display_type: display
auto_number: true
spoken_version: Force equals mass times acceleration
<!-- /EQUATION -->
---
\vec{F} = m\vec{a}
```

**Multi-line Equation with Caption:**
```markdown
<!-- EQUATION -->
reference_id: eq-kinetic-energy
display_type: display
auto_number: true
spoken_version: Kinetic energy equals one half m v squared, which equals p squared over two m
caption: Kinetic energy in terms of velocity and momentum
<!-- /EQUATION -->
---
\begin{aligned}
KE &= \frac{1}{2}mv^2 \\
   &= \frac{p^2}{2m}
\end{aligned}
```

**Unnumbered Intermediate Step:**
```markdown
<!-- EQUATION -->
display_type: display
auto_number: false
spoken_version: x equals negative b plus or minus square root of b squared minus four a c, all over two a
<!-- /EQUATION -->
---
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
```
Note: No `reference_id` needed if you're not cross-referencing it.

**Referencing:**
```markdown
According to Newton's Second Law (\ref{eq-newton-2nd}), force equals...

The kinetic energy (\ref{eq-kinetic-energy}) can be expressed as...
```

---

### FIGURE Block

Use for images, diagrams, photos, and illustrations.

**🎨 New Typora-Compatible Format (Recommended):**
```markdown
<!-- FIGURE -->
reference_id: fig-apparatus
display_width: full
auto_number: true
---

![Photo of 2-meter inclined plane with cart and two photogate sensors](images/apparatus-setup.jpg)

*Experimental apparatus showing inclined plane and photogate sensors.*
<!-- /FIGURE -->
```

**Key Benefits:**
- ✅ Images render directly in Typora preview with standard `![alt](path)` syntax
- ✅ Alt text and image path extracted from markdown automatically (no duplication!)
- ✅ Caption displays as italic text (visible in Typora)
- ✅ Wagtail-specific metadata (display_width, etc.) stored in compact HTML comment
- ✅ Clean, readable format

**Traditional Format (Still Supported):**
```markdown
<!-- FIGURE -->
reference_id: fig-unique-name
image_path: images/filename.jpg
alt_text: Descriptive text for screen readers
display_width: full
auto_number: true
---
Brief description of the figure (caption text).
<!-- /FIGURE -->
```

**How It Works:**
- On **export**: Generates standard `![alt](path)` syntax with caption as italic text
- On **import**: Smart extraction parses image syntax to extract alt_text and image_path
- **Backward compatible**: Old format with metadata still works
- **Image ID tracking**: System stores `image_id` in metadata for reliable re-export

**Required Fields:**
- `image_path` OR `image_id` - Image reference (extracted from `![alt](path)` or specified in metadata)
- `alt_text` - Accessibility description (extracted from `![alt](path)` or specified in metadata, minimum 10 characters)

**Optional Fields:**
- `reference_id` - Unique ID for cross-referencing (required if you want to use `\ref{}`)
- `display_width` - Width: `full`, `half`, or `third` (default: `full`)
- `auto_number` - Include in numbering: `true` or `false` (default: `true`)
- `credit` - Attribution/source credit

**Content:** Standard markdown image `![alt](path)` followed by caption as italic text

**Image Format Support:**
- JPG/JPEG - Photos
- PNG - Diagrams with transparency
- SVG - Vector graphics (recommended for diagrams)
- GIF - Simple animations (use sparingly)

**Image Organization:**
```
lab-01-newton/
├── guide.md
└── images/
    ├── apparatus-setup.jpg
    ├── force-diagram.png
    └── results-graph.svg
```

**Examples:**

**Simple Figure (Typora-compatible):**
```markdown
<!-- FIGURE -->
reference_id: fig-apparatus
display_width: full
auto_number: true
---

![Photo of 2-meter inclined plane with cart and two photogate sensors mounted on stands](images/apparatus-setup.jpg)

*Experimental apparatus showing inclined plane and photogate sensors.*
<!-- /FIGURE -->

The setup (\ref{fig-apparatus}) includes two photogate sensors...
```

**Figure with Credit (Typora-compatible):**
```markdown
<!-- FIGURE -->
reference_id: fig-force-diagram
display_width: half
auto_number: true
credit: Adapted from Serway & Jewett, Physics for Scientists and Engineers
---

![Free body diagram with weight vector, normal force, and friction vector](images/force-diagram.png)

*Free body diagram showing all forces acting on the cart.*
<!-- /FIGURE -->
```

**Traditional Format Example:**
```markdown
<!-- FIGURE -->
reference_id: fig-apparatus
image_path: images/apparatus-setup.jpg
alt_text: Photo of 2-meter inclined plane with cart and two photogate sensors mounted on stands
display_width: full
auto_number: true
---
Experimental apparatus showing inclined plane and photogate sensors.
<!-- /FIGURE -->
```

**Display Width Options:**
- `full` - Full page width (default)
- `half` - Half page width (good for side-by-side figures)
- `third` - One-third page width (for multiple small figures)

**Alt Text Best Practices:**
- Describe what's IN the image, not what it represents
- Be concise but complete
- Include relevant details (colors, positions, labels)
- Don't start with "Image of" or "Picture of"
- Minimum 10 characters required for accessibility

---

### TABLE Block

Use for data tables, results, specifications.

**Format:**
```markdown
<!-- TABLE -->
reference_id: table-unique-name
caption: Description of table contents
auto_number: true
show_row_numbers: false
summary: Accessibility summary describing table contents
<!-- /TABLE -->
---
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Data 1   | Data 2   | Data 3   |
| Data 4   | Data 5   | Data 6   |
```

**Required Fields:**
- `caption` - Table caption (minimum 5 characters for accessibility)

**Optional Fields:**
- `reference_id` - Unique ID for cross-referencing (required if you want to use `\ref{}`)
- `auto_number` - Include in numbering: `true` or `false` (default: `true`)
- `show_row_numbers` - Display row numbers in first column: `true` or `false` (default: `false`)
- `summary` - Accessibility summary describing table contents

**Content:** Markdown table

**Table Syntax:**
- Use standard markdown table format
- First row is header (automatically bolded)
- Second row is separator (`|---|---|---|`)
- Data rows follow

**Alignment:**
```markdown
| Left aligned | Center aligned | Right aligned |
|:-------------|:--------------:|--------------:|
| Text         | Text           | 123           |
```
- `:---` = left align
- `:---:` = center align
- `---:` = right align

**Example:**
```markdown
<!-- TABLE -->
reference_id: table-measurements
caption: Distance and time measurements for five trials
auto_number: true
show_row_numbers: false
summary: Five trials showing incline angle, time of descent, and calculated velocity for a dynamics cart
<!-- /TABLE -->
---
| Trial | Distance (m) | Time (s) | Velocity (m/s) |
|------:|-------------:|---------:|---------------:|
| 1     | 1.50         | 2.34     | 0.64           |
| 2     | 1.50         | 1.67     | 0.90           |
| 3     | 1.50         | 1.35     | 1.11           |

The results (\ref{table-measurements}) show a clear trend...
```

**Example with Row Numbers:**
```markdown
<!-- TABLE -->
reference_id: table-calculations
caption: Calculated accelerations and uncertainties
auto_number: true
show_row_numbers: true
summary: Comparison of measured versus theoretical acceleration values at five different angles
<!-- /TABLE -->
---
| Angle (°) | Measured (m/s²) | Theoretical (m/s²) | Error (%) |
|----------:|----------------:|-------------------:|----------:|
| 5.0       | 0.84            | 0.85               | 1.2       |
| 10.0      | 1.68            | 1.70               | 1.4       |
| 15.0      | 2.49            | 2.53               | 1.6       |
```

---

### CODE Block

Use for programming code, scripts, or command-line examples.

**🎨 New Typora-Compatible Format (Recommended):**
```markdown
*Python script to calculate average velocity from photogate data* {#code-data-analysis}

```python
import numpy as np

# Load data
distances = np.array([1.5, 1.5, 1.5])  # meters
times = np.array([2.34, 1.67, 1.35])  # seconds

# Calculate velocities
velocities = distances / times
print(f"Average: {np.mean(velocities):.2f} m/s")
```
```

**Key Benefits:**
- ✅ Code renders with syntax highlighting in Typora
- ✅ Caption displays as italic text above code (visible in preview)
- ✅ Language auto-extracted from fence info string (` ```python`)
- ✅ Standard fenced code block format
- ✅ Optional Kramdown-style `{#id}` for cross-references
- ✅ No HTML comments needed for simple cases

**Traditional Format (Still Supported):**
```markdown
<!-- CODE -->
reference_id: code-unique-name
language: python
caption: Description of what the code does
show_line_numbers: true
---
```python
# Your code here
import numpy as np
print("Hello, physics!")
```
<!-- /CODE -->
```

**How It Works:**
- On **export**: Generates standard fenced code blocks with caption as italic text above
- On **import**: Smart extraction parses fence info string to extract language
- **Backward compatible**: Old HTML comment format still works
- **Wagtail-specific metadata**: `show_line_numbers` stored in compact HTML comment when needed

**Required Fields:**
- `language` - Programming language for syntax highlighting (auto-extracted from ` ```language` or specified in metadata)

**Optional Fields:**
- `reference_id` - Unique ID for cross-referencing (extracted from `{#id}` or specified in metadata)
- `caption` - Brief description of code purpose (italic text above code block)
- `show_line_numbers` - Display line numbers: `true` or `false` (default: `false`)

**Content:** Standard fenced code block with language specifier

**Supported Languages:**
- `python` - Python
- `matlab` - MATLAB/Octave
- `r` - R statistical language
- `cpp` - C++
- `java` - Java
- `javascript` - JavaScript
- `bash` - Shell scripts
- `sql` - SQL queries
- Many more...

**Examples:**

**Simple Code Block (Typora-compatible):**
```markdown
*Python script to calculate average velocity from photogate data* {#code-data-analysis}

```python
import numpy as np

# Load data
distances = np.array([1.5, 1.5, 1.5])  # meters
times = np.array([2.34, 1.67, 1.35])  # seconds

# Calculate velocities
velocities = distances / times
avg_velocity = np.mean(velocities)
print(f"Average velocity: {avg_velocity:.2f} m/s")
```

The analysis script (\ref{code-data-analysis}) processes the photogate data...
```

**Code Without Caption or Reference:**
```markdown
```python
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [1, 4, 9])
plt.show()
```
```

**Traditional Format Example:**
```markdown
<!-- CODE -->
reference_id: code-data-analysis
language: python
caption: Python script to calculate average velocity from photogate data.
show_line_numbers: true
---
```python
import numpy as np
distances = np.array([1.5, 1.5, 1.5])
times = np.array([2.34, 1.67, 1.35])
velocities = distances / times
print(f"Average: {np.mean(velocities):.2f} m/s")
```
<!-- /CODE -->
```

**Referencing:**
```markdown
The analysis script (\ref{code-data-analysis}) processes the photogate data...
```

---

### SAFETY_WARNING Block

Use for safety warnings, cautions, and hazards.

**Format:**
```markdown
<!-- SAFETY_WARNING -->
severity: warning
title: Laser Hazard
icon: exclamation-triangle
dismissible: false
<!-- /SAFETY_WARNING -->
---
The laser used in this experiment can cause permanent eye damage. Never look directly into the beam or reflections.
```

**Required Fields:**
- `severity` - Level: `info`, `caution`, `warning`, or `danger`
- `title` - Warning title/heading (minimum 3 characters)

**Optional Fields:**
- `icon` - Icon name: `exclamation-triangle`, `exclamation-circle`, `bolt`, `fire`, `radiation`, `biohazard`, `skull`, `hand`, `eye`, `info-circle`
- `dismissible` - User can dismiss: `true` or `false` (default: `false`)

**Content:** Warning message (supports markdown)

**Severity Levels:**
- `info` - Blue, for general information
- `caution` - Yellow, for minor hazards (wear safety glasses)
- `warning` - Orange, for moderate hazards (laser, chemicals)
- `danger` - Red, for serious hazards (high voltage, extreme temperatures)

**Examples:**

**Caution Level:**
```markdown
<!-- SAFETY_WARNING -->
severity: caution
title: Eye Protection Required
icon: eye
dismissible: false
<!-- /SAFETY_WARNING -->
---
Wear safety goggles at all times during this experiment.
```

**Warning Level:**
```markdown
<!-- SAFETY_WARNING -->
severity: warning
title: Laser Hazard
icon: exclamation-triangle
dismissible: false
<!-- /SAFETY_WARNING -->
---
The laser can cause permanent eye damage. Never look directly into the beam or reflections.
```

**Danger Level:**
```markdown
<!-- SAFETY_WARNING -->
severity: danger
title: High Voltage
icon: bolt
dismissible: false
<!-- /SAFETY_WARNING -->
---
High voltage (120V AC)! Do not touch exposed wires while the power supply is on. Ensure all connections are made with power OFF.
```

**Info Level (Dismissible):**
```markdown
<!-- SAFETY_WARNING -->
severity: info
title: General Lab Safety
icon: info-circle
dismissible: true
<!-- /SAFETY_WARNING -->
---
Follow all laboratory safety procedures. Know the location of safety equipment including fire extinguishers, eyewash stations, and emergency exits.
```

**Best Practices:**
- Place safety warnings BEFORE the relevant procedure step
- Be specific about the hazard
- Include mitigation steps
- Use appropriate severity level
- Always include a descriptive title
- Set dismissible to `false` for critical safety warnings

---

### BIBENTRY Block (Bibliography)

Use for citing references, textbooks, articles, and resources.

**IMPORTANT LOCATION:** BIBENTRY blocks must be placed in a separate `# Bibliography` section at the END of your markdown file (after all content). This section maps to a separate `bibliography` field in the Wagtail admin, NOT the main content field.

**Format:**
```markdown
<!-- BIBENTRY -->
reference_key: unique-cite-key
authors: Last, First and Other, Author
title: Title of Work
publication: Journal/Book/Conference Name
year: 2020
<!-- /BIBENTRY -->
```

**Required Fields:**
- `reference_key` - Unique citation key (e.g., `young2020`, `taylor1997`)
- `authors` - Author names (use "and" to separate multiple authors)
- `title` - Title of work
- `year` - Publication year

**Optional Fields:**
- `publication` - Journal, book, or conference name (e.g., "Physical Review, 42(3)" or "Pearson, 15th Edition")
- `pages` - Page range (e.g., "234-256" or "pp. 15-20")
- `url` - Web address for online sources
- `doi` - Digital Object Identifier (e.g., "10.1103/PhysRev.47.777")
- `access_date` - Date accessed for online sources (YYYY-MM-DD format)
- `notes` - Additional notes about the reference

**Important Notes:**
- BIBENTRY blocks are metadata-only (no content section, no `---` separator)
- Use the `publication` field for journal names, book publishers, or any publication venue
- For books, include edition in the `publication` field (e.g., "Pearson, 15th Edition")
- For articles, include journal and volume in `publication` (e.g., "Physical Review, 42(3)")

**Example Book:**
```markdown
<!-- BIBENTRY -->
reference_key: young2020
authors: Young, H. D. and Freedman, R. A.
title: University Physics with Modern Physics
publication: Pearson, 15th Edition
year: 2020
<!-- /BIBENTRY -->
```

**Example Article:**
```markdown
<!-- BIBENTRY -->
reference_key: einstein1905
authors: Einstein, A.
title: On the Electrodynamics of Moving Bodies
publication: Annalen der Physik, 17
year: 1905
pages: 891-921
doi: 10.1002/andp.19053221004
<!-- /BIBENTRY -->
```

**Example Website:**
```markdown
<!-- BIBENTRY -->
reference_key: nist2023
authors: National Institute of Standards and Technology
title: Fundamental Physical Constants
year: 2023
url: https://physics.nist.gov/cuu/Constants/
access_date: 2023-09-15
<!-- /BIBENTRY -->
```

**Citing in Text:**
```markdown
According to Young and Freedman \cite{young2020}, Newton's laws...

This phenomenon is well documented \cite{einstein1905, feynman1963}.
```

---

## Cross-Referencing Guide

### Using `\ref{}`

Reference equations, figures, tables, and sections:

```markdown
<!-- Create a referenceable item -->
<!-- EQUATION -->
reference_id: eq-force
<!-- /EQUATION -->
$$F = ma$$

<!-- Reference it elsewhere -->
Newton's Second Law (\ref{eq-force}) states that force equals...
```

**What Gets Auto-Numbered:**
- Equations: `\ref{eq-force}` → "Equation 1"
- Figures: `\ref{fig-diagram}` → "Figure 2"
- Tables: `\ref{table-data}` → "Table 1"
- Sections: `\ref{introduction}` → "Section 1.1"

### Using `\cite{}`

Reference bibliography entries:

```markdown
<!-- Create a bibliography entry -->
<!-- BIBENTRY -->
reference_key: taylor1997
entry_type: book
author: Taylor, J. R.
title: An Introduction to Error Analysis
publisher: University Science Books
year: 1997
<!-- /BIBENTRY -->

<!-- Cite it in text -->
Error propagation \cite{taylor1997} is essential for...

<!-- Multiple citations -->
This is well-established \cite{taylor1997, young2020, serway2018}.
```

**Citation Format:**
- Single: `\cite{key}` → "[1]"
- Multiple: `\cite{key1, key2}` → "[1, 2]"

### Naming Conventions

**Use descriptive, unique IDs:**

✅ **Good:**
- `eq-newton-second-law`
- `fig-apparatus-setup`
- `table-measurement-results`
- `code-python-analysis`

❌ **Bad:**
- `eq1`, `eq2` (not descriptive)
- `figure`, `table` (not unique)
- `my equation` (spaces not allowed)

**Format:**
- Use lowercase
- Use hyphens (not underscores or spaces)
- Include type prefix (`eq-`, `fig-`, `table-`, `code-`)
- Be descriptive but concise

---

## Markdown Content (Outside Blocks)

Between block markers, you can use standard markdown.

### MARKDOWN Block (Rich Text Areas)

For rich text content (paragraphs, lists, formatting), use MARKDOWN blocks:

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

**Key Benefits:**
- ✅ Exports as plain markdown (no HTML comment wrappers)
- ✅ Renders perfectly in Typora
- ✅ Cleaner, more readable format
- ✅ Standard markdown throughout

**Traditional Format (Still Supported):**
```markdown
<!-- MARKDOWN -->
---
This is markdown content wrapped in HTML comments.
<!-- /MARKDOWN -->
```

**How It Works:**
- On **export**: Generates plain markdown directly without wrappers
- On **import**: Both wrapped and unwrapped markdown work
- **Backward compatible**: Old HTML comment format still supported
- **Note**: Most lab guide content doesn't need explicit MARKDOWN blocks - just write regular markdown!

### Text Formatting
```markdown
**Bold text**
*Italic text*
***Bold and italic***
`Inline code`
```

### Lists
```markdown
Unordered:
- Item 1
- Item 2
  - Nested item

Ordered:
1. First step
2. Second step
3. Third step
```

### Links
```markdown
[Link text](https://example.com)
[Internal page](/path/to/page)
```

### Inline Math
```markdown
The velocity is $v = \frac{d}{t}$ where $d$ is distance.
```

### Blockquotes
```markdown
> This is a quote or note.
> It can span multiple lines.
```

---

## Complete Workflow Example

### Step 1: Plan Your Lab

1. Decide on lab number and title
2. List major sections (Introduction, Theory, Procedure, etc.)
3. Identify what needs cross-referencing (equations, figures)
4. Gather images and save to `images/` folder

### Step 2: Set Up Files

```bash
# Create lab directory
mkdir lab-03-conservation-energy
cd lab-03-conservation-energy

# Copy template
cp ../comprehensive-template.md guide.md

# Create images folder
mkdir images

# Add your images
# (Copy your image files to the images/ folder)
```

### Step 3: Edit Frontmatter

```yaml
---
lab_number: 3
lab_title: "Conservation of Energy"
duration_hours: 3.0
difficulty: intermediate
enable_section_numbering: true
keywords: "energy, conservation, pendulum, physics"
---
```

### Step 4: Add Learning Objectives

```markdown
## Learning Objectives

- Students will demonstrate conservation of energy in pendulum motion
- Students will calculate potential and kinetic energy at different positions
- Students will analyze energy losses due to friction and air resistance
```

### Step 5: Build Content Sections

**Introduction:**
```markdown
<!-- HEADING -->
reference_id: introduction
level: 2
<!-- /HEADING -->
## Introduction

In this lab, we investigate conservation of energy using a simple pendulum.
We'll measure the pendulum's height and velocity to calculate energy at
different points in its swing.
```

**Key Equations:**
```markdown
<!-- HEADING -->
reference_id: theory
level: 2
<!-- /HEADING -->
## Theory

The total mechanical energy is:

<!-- EQUATION -->
reference_id: eq-total-energy
<!-- /EQUATION -->
$$
E_{total} = PE + KE = mgh + \frac{1}{2}mv^2
$$

For a conservative system, \ref{eq-total-energy} remains constant.
```

**Figures:**
```markdown
<!-- FIGURE -->
reference_id: fig-pendulum-setup
caption: Pendulum apparatus with photogate at lowest point.
image_path: images/pendulum-setup.jpg
alt_text: Pendulum suspended from stand with photogate sensor positioned at bottom of swing arc
<!-- /FIGURE -->
```

**Data Table:**
```markdown
<!-- TABLE -->
reference_id: table-energy-measurements
caption: Height, velocity, and energy measurements at five positions.
<!-- /TABLE -->

| Position | Height (m) | Velocity (m/s) | PE (J) | KE (J) | Total (J) |
|---------:|-----------:|---------------:|-------:|-------:|----------:|
| 1        | 0.50       | 0.00           | 4.90   | 0.00   | 4.90      |
| 2        | 0.25       | 3.13           | 2.45   | 2.45   | 4.90      |
```

### Step 6: Add Safety Warnings

```markdown
<!-- SAFETY_WARNING -->
severity: caution
<!-- /SAFETY_WARNING -->
**Caution:** Stand clear of the pendulum's swing path to avoid being struck.
```

### Step 7: Add Bibliography

```markdown
<!-- HEADING -->
reference_id: references
level: 2
<!-- /HEADING -->
## References

<!-- BIBENTRY -->
reference_key: serway2018
entry_type: book
author: Serway, R. A. and Jewett, J. W.
title: Physics for Scientists and Engineers
publisher: Cengage Learning
year: 2018
<!-- /BIBENTRY -->
```

### Step 8: Validate and Import

1. Save your `guide.md` file
2. In Wagtail admin, navigate to the lab page
3. Click "Import Markdown"
4. Click "Validate Markdown" button first (recommended)
5. If validation passes, upload your markdown file
6. Upload your images folder (or ZIP both together)
7. Review imported content
8. Save and publish

---

## Common Issues and Solutions

### Issue: "Missing required frontmatter field"
**Solution:** Ensure all required fields are present: `lab_number`, `lab_title`, `duration_hours`, `difficulty`, `enable_section_numbering`

### Issue: "Block not closed"
**Solution:** Every `<!-- BLOCKTYPE -->` must have a matching `<!-- /BLOCKTYPE -->`

### Issue: "Invalid reference ID"
**Solution:** Reference IDs cannot contain spaces. Use hyphens: `my-equation` not `my equation`

### Issue: "Cross-reference not found"
**Solution:** Make sure the referenced ID exists and matches exactly (case-sensitive)

### Issue: "Image not found"
**Solution:**
- Check that image is in `images/` folder
- Verify `image_path` uses relative path: `images/filename.jpg`
- Check filename spelling and extension

### Issue: "Citation key undefined"
**Solution:** Every `\cite{key}` must have a corresponding `<!-- BIBENTRY -->` with matching `reference_key`

### Issue: "Equation not rendering"
**Solution:**
- Use `$$` for display math (on its own lines)
- Escape special characters: `\{`, `\}`, `\_`
- Check for unmatched braces in LaTeX

---

## Best Practices Summary

### DO:
✅ Use descriptive, unique reference IDs
✅ Add alt text to all images (accessibility)
✅ Validate markdown before importing
✅ Keep images in `images/` subdirectory
✅ Use appropriate severity for safety warnings
✅ Test cross-references point to valid IDs
✅ Add captions to figures and tables
✅ Use consistent naming conventions

### DON'T:
❌ Use spaces in reference IDs
❌ Forget closing block markers
❌ Skip required frontmatter fields
❌ Use absolute paths for images
❌ Hardcode "Figure 1" - use `\ref{}`
❌ Cite sources without BIBENTRY blocks
❌ Skip levels in heading hierarchy (h2 → h4)

---

## Version Control with Git

The markdown format works excellently with Git:

```bash
# Initialize Git repository
git init
git add guide.md images/
git commit -m "Initial lab 3 content"

# Create branch for major revision
git checkout -b update-procedure
# Make changes...
git add guide.md
git commit -m "Revise procedure section for clarity"

# Merge changes
git checkout main
git merge update-procedure

# View history
git log --oneline
git diff HEAD~1  # Compare with previous version
```

**Benefits:**
- Track every change with detailed history
- Collaborate via pull requests
- Review changes before merging
- Rollback to any previous version
- Branch for experimental rewrites

---

## Getting Help

- **Template Examples**: See `comprehensive-template.md` for complete working examples
- **Validation Errors**: Use Wagtail's "Validate Markdown" button before importing
- **Parser Documentation**: See `docs/MARKDOWN_IMPORT_EXPORT_EXTENSIBILITY.md` in the project root
- **Block Syntax Questions**: Check the examples in `comprehensive-template.md`
- **Import Issues**: Check Wagtail admin error messages for specific line numbers

---

## Advanced Tips

### Multiple Images in One Figure
Create separate FIGURE blocks:

```markdown
<!-- FIGURE -->
reference_id: fig-setup-1
caption: View from front
image_path: images/setup-front.jpg
alt_text: Front view of apparatus
<!-- /FIGURE -->

<!-- FIGURE -->
reference_id: fig-setup-2
caption: View from side
image_path: images/setup-side.jpg
alt_text: Side view showing angle measurement
<!-- /FIGURE -->
```

### Complex Equations with Alignment
```markdown
<!-- EQUATION -->
reference_id: eq-derivation
<!-- /EQUATION -->
$$
\begin{aligned}
E &= PE + KE \\
  &= mgh + \frac{1}{2}mv^2 \\
  &= m(gh + \frac{1}{2}v^2)
\end{aligned}
$$
```

### Code with Line Numbers
Some syntax highlighters support line numbers automatically. Just specify the language:

```markdown
<!-- CODE -->
reference_id: code-example
language: python
caption: Example with automatic line numbering
<!-- /CODE -->
```python
def calculate_energy(mass, height, velocity):
    pe = mass * 9.81 * height
    ke = 0.5 * mass * velocity**2
    return pe + ke
```
```

---

## Template Checklist

Before importing, verify:

- [ ] YAML frontmatter has all required fields
- [ ] All block markers are properly closed
- [ ] All `\ref{}` point to existing reference IDs
- [ ] All `\cite{}` have corresponding BIBENTRY blocks
- [ ] All images exist in `images/` folder
- [ ] All image blocks have alt text
- [ ] All figures and tables have captions
- [ ] No spaces in reference IDs
- [ ] Heading hierarchy doesn't skip levels
- [ ] Safety warnings use appropriate severity
- [ ] Ran "Validate Markdown" in Wagtail (no errors)

Once validated, your lab guide is ready to import! 🎉
