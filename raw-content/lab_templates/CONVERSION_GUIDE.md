# Lab Guide Conversion Guide: Jekyll/Pandoc to Wagtail

This guide explains how to convert your existing lab guide content from the current Jekyll/Pandoc format to the new Django/Wagtail platform format.

## Overview

The conversion script (`convert_to_wagtail.py`) automates the transformation of your markdown lab guides from the current system to a format compatible with your new Wagtail CMS platform.

### What Gets Converted

**Current Format (Jekyll/Pandoc):**
- Raw markdown files (e.g., `lab1-raw.md`)
- Pandoc-style figure syntax: `![caption](path){#fig:id}`
- Standard markdown headings: `# Title`, `## Section`
- LaTeX equations: `$$...$$`
- Images in `resources/` directory
- HTML generation via `mdtohtml.sh` script

**Target Format (Wagtail):**
- Structured markdown with block markers
- HEADING blocks for sections
- FIGURE blocks with metadata
- EQUATION blocks with accessibility features
- TABLE blocks with captions
- CODE blocks with syntax highlighting
- Images in `images/` subdirectory

## Installation & Requirements

### Prerequisites
- Python 3.7 or higher
- Your existing PHYS-3330 repository

### No Additional Dependencies Required
The conversion script uses only Python standard library modules.

## Quick Start

### Convert a Single Lab Guide

```bash
# Basic conversion
python convert_to_wagtail.py raw-content/lab1-raw.md

# Convert with automatic image copying
python convert_to_wagtail.py raw-content/lab1-raw.md --create-image-dir

# Convert with custom output location
python convert_to_wagtail.py raw-content/lab1-raw.md -o my-labs/lab1.md
```

### Convert All Lab Guides

```bash
# Convert all lab files at once
python convert_to_wagtail.py raw-content/lab*-raw.md --create-image-dir
```

## Output Structure

When you run the conversion, it creates:

```
raw-content/
└── wagtail_output/
    ├── lab1-wagtail.md       # Converted markdown file
    ├── lab2-wagtail.md
    ├── ...
    └── images/               # Shared image directory (if --create-image-dir used)
        ├── apparatus-setup.jpg
        ├── force-diagram.png
        └── ...
```

For importing to Wagtail, organize each lab guide with its own images:

```
lab-guides-for-import/
├── lab1/
│   ├── guide.md
│   └── images/
│       ├── banana.jpg
│       ├── coax.png
│       └── ...
├── lab2/
│   ├── guide.md
│   └── images/
│       └── ...
```

## Conversion Details

### 1. Frontmatter Conversion

**Before (Jekyll/Pandoc):**
```yaml
---
title: "Lab 1 - Electronic Measurements"
author: [Department of Physics | University of Colorado Boulder]
---
```

**After (Wagtail):**
```yaml
---
lab_number: 1
lab_title: "Lab 1 - Electronic Measurements"
duration_hours: 3.0
difficulty: intermediate
enable_section_numbering: true
keywords: "lab, 1, electronic, measurements"
---
```

### 2. Headings

**Before:**
```markdown
# Lab Notebook Guidelines
```

**After:**
```markdown
<!-- HEADING -->
reference_id: lab-notebook-guidelines
level: h1
---
Lab Notebook Guidelines
<!-- /HEADING -->
```

### 3. Figures

**Before (Pandoc syntax):**
```markdown
![**Banana cables** - wires with banana connectors](../resources/lab1fig/banana.jpg){#fig:banana width="8cm"}
```

**After (Wagtail FIGURE block):**
```markdown
<!-- FIGURE -->
reference_id: fig:banana
image_path: images/banana.jpg
alt_text: Banana cables - wires with banana connectors at the end. The power supply and DMM have banana sockets to make connections to.
display_width: half
auto_number: true
---
**Banana cables** - wires with banana connectors at the end. The power supply and DMM have banana sockets to make connections to.
<!-- /FIGURE -->
```

### 4. Equations

**Before:**
```markdown
$$\Delta V = IR$$
```

**After:**
```markdown
<!-- EQUATION -->
reference_id: eq-1
display_type: display
auto_number: true
spoken_version: Delta V equals I R
---
\Delta V = IR
<!-- /EQUATION -->
```

### 5. Code Blocks

**Before:**
```markdown
```python
import numpy as np
print("Hello")
```
```

**After:**
```markdown
<!-- CODE -->
language: python
caption: Code example
show_line_numbers: false
---
```python
import numpy as np
print("Hello")
```
<!-- /CODE -->
```

### 6. Tables

**Before:**
```markdown
| Column 1 | Column 2 |
|----------|----------|
| Data 1   | Data 2   |
```

**After:**
```markdown
<!-- TABLE -->
reference_id: table-1
caption: Data table 1
auto_number: true
show_row_numbers: false
summary: Table showing experimental data and results
---
| Column 1 | Column 2 |
|----------|----------|
| Data 1   | Data 2   |
<!-- /TABLE -->
```

## Manual Review Required

While the script automates most of the conversion, you should **manually review and improve** the following:

### 1. Learning Objectives
The script extracts "Goals" sections, but you may want to refine the wording:

```markdown
## Learning Objectives

Students will:

- Learn to use equipment for building and testing circuits
- Understand voltage and current measurement techniques
- Develop familiarity with oscilloscopes and function generators
```

### 2. Equation Spoken Versions
The automatically generated spoken versions are basic. Improve them for accessibility:

**Auto-generated (review needed):**
```
spoken_version: Delta V equals I R
```

**Better:**
```
spoken_version: The voltage drop equals current times resistance
```

### 3. Figure Alt Text
Review and enhance alt text for better accessibility:

**Auto-generated:**
```
alt_text: Banana cables - wires with banana connectors at the end.
```

**Better:**
```
alt_text: Photo showing red and black banana cables with metal connector tips that plug into banana jack sockets on measurement equipment
```

### 4. Table Captions
The script generates generic captions. Make them descriptive:

**Auto-generated:**
```
caption: Data table 1
```

**Better:**
```
caption: Voltage and current measurements for five trials at different resistor values
```

### 5. Reference IDs
The script generates reference IDs automatically, but you may want to standardize them:

```markdown
<!-- HEADING -->
reference_id: power-supply-setup    <!-- Review: is this the best ID? -->
level: h2
---
Set up the DC voltage bias
<!-- /HEADING -->
```

### 6. Bibliography
The script creates a placeholder bibliography section. You'll need to manually create BIBENTRY blocks:

```markdown
# Bibliography

<!-- BIBENTRY -->
reference_key: young2020
authors: Young, H. D. and Freedman, R. A.
title: University Physics with Modern Physics
publication: Pearson, 15th Edition
year: 2020
<!-- /BIBENTRY -->

<!-- BIBENTRY -->
reference_key: steck2020
authors: Steck, D. A.
title: Analog and Digital Electronics
url: https://atomoptics-nas.uoregon.edu/~dsteck/teaching/electronics/electronics-notes.pdf
year: 2020
<!-- /BIBENTRY -->
```

## Image Handling

### Automatic Image Copying

When you use `--create-image-dir`, the script:
1. Creates an `images/` directory
2. Scans your markdown for image references
3. Copies images from `resources/` to `images/`
4. Reports any missing images

### Manual Image Organization

For Wagtail import, organize each lab with its images:

```bash
# Create directory structure
mkdir -p lab-guides-for-import/lab1/images

# Copy converted markdown
cp raw-content/wagtail_output/lab1-wagtail.md lab-guides-for-import/lab1/guide.md

# Copy relevant images
cp raw-content/wagtail_output/images/banana.jpg lab-guides-for-import/lab1/images/
cp raw-content/wagtail_output/images/coax.png lab-guides-for-import/lab1/images/
# ... etc
```

### Image Path Updates

The script automatically converts:
- `../resources/lab1fig/banana.jpg` → `images/banana.jpg`
- `../resources/lab1fig/scope-guide.png` → `images/scope-guide.png`

## Validation Before Import

Before importing to Wagtail:

1. **Open the converted file** and review the structure
2. **Check all FIGURE blocks** have valid image paths
3. **Review EQUATION blocks** for proper LaTeX and spoken versions
4. **Verify reference IDs** are unique and descriptive
5. **Test cross-references** (like `\ref{fig:banana}`) point to valid IDs
6. **Enhance captions and alt text** for accessibility
7. **Create BIBENTRY blocks** for any citations

### Using Wagtail's Validator

Once in Wagtail:
1. Navigate to the lab page in admin
2. Click "Import Markdown"
3. Click "Validate Markdown" button
4. Fix any errors reported
5. Upload the markdown file and images

## Command Reference

### Basic Usage

```bash
python convert_to_wagtail.py INPUT_FILE [OPTIONS]
```

### Options

| Option | Description |
|--------|-------------|
| `INPUT_FILE` | Path to markdown file(s) to convert (supports wildcards) |
| `-o OUTPUT`, `--output OUTPUT` | Custom output path (single file only) |
| `--create-image-dir` | Create images directory and copy referenced images |
| `-h`, `--help` | Show help message |

### Examples

```bash
# Convert single file to default location
python convert_to_wagtail.py raw-content/lab1-raw.md

# Convert with images
python convert_to_wagtail.py raw-content/lab1-raw.md --create-image-dir

# Convert to specific location
python convert_to_wagtail.py raw-content/lab1-raw.md -o ~/Desktop/lab1.md

# Convert all labs
python convert_to_wagtail.py raw-content/lab*-raw.md --create-image-dir

# Convert specific labs
python convert_to_wagtail.py raw-content/lab1-raw.md raw-content/lab2-raw.md --create-image-dir
```

## Workflow: Complete Conversion Process

Here's the recommended end-to-end workflow:

### Step 1: Convert All Lab Guides

```bash
# From PHYS-3330 repository root
python convert_to_wagtail.py raw-content/lab*-raw.md --create-image-dir
```

### Step 2: Review First Lab Guide

```bash
# Open in your editor
code raw-content/wagtail_output/lab1-wagtail.md
```

Review and improve:
- [ ] Learning objectives wording
- [ ] Equation spoken versions
- [ ] Figure alt text descriptions
- [ ] Table captions
- [ ] Reference IDs
- [ ] Bibliography entries

### Step 3: Organize for Wagtail Import

```bash
# Create organized structure
mkdir -p lab-guides-for-import/lab1/images

# Copy files
cp raw-content/wagtail_output/lab1-wagtail.md lab-guides-for-import/lab1/guide.md

# Copy images (select only those used in lab1)
# You can identify them by opening lab1-wagtail.md and checking image_path fields
```

### Step 4: Import to Wagtail

1. Log into Wagtail admin
2. Navigate to the appropriate section
3. Click "Import Markdown"
4. Validate the markdown first
5. Upload `guide.md` and `images/` folder
6. Review imported content
7. Make any final adjustments in Wagtail editor
8. Save and publish

### Step 5: Repeat for Other Labs

Repeat steps 2-4 for each lab guide.

## Troubleshooting

### Issue: "MISSING images"

**Problem:** Script reports `[MISSING] Not found: path/to/image.jpg`

**Solution:**
- Check if the image exists in the `resources/` directory
- Verify the path in the original markdown file
- Manually copy the image if needed

### Issue: Invalid LaTeX in equations

**Problem:** Equations don't render properly in Wagtail

**Solution:**
- Review the EQUATION blocks in the converted file
- Check for unescaped special characters
- Verify LaTeX syntax is correct
- Test in a LaTeX editor if needed

### Issue: Broken cross-references

**Problem:** References like `\ref{fig:banana}` don't work

**Solution:**
- Ensure the reference_id matches exactly (case-sensitive)
- Check that the referenced block exists
- Use the correct prefix (fig:, eq:, table:)

### Issue: Unicode/encoding errors on Windows

**Problem:** Script crashes with encoding errors

**Solution:**
- The script now uses `[OK]` instead of Unicode checkmarks
- If you still have issues, ensure your terminal supports UTF-8
- Try running from PowerShell instead of CMD

## Advanced: Customizing the Conversion

The script is designed to be extensible. Common customizations:

### Adjust Image Width Mapping

Edit `_convert_figures()` method to change width thresholds:

```python
# In convert_to_wagtail.py, around line 263
if width_cm < 8:
    width = 'third'
elif width_cm < 12:
    width = 'half'
else:
    width = 'full'
```

### Improve Equation Spoken Versions

Edit `_equation_to_spoken()` method to add more sophisticated conversions:

```python
# In convert_to_wagtail.py, around line 411
replacements = {
    r'\\frac\{([^}]+)\}\{([^}]+)\}': r'\1 over \2',
    r'\\Delta': 'delta',
    r'\\omega': 'omega',
    # Add more...
}
```

### Add Safety Warning Detection

You could extend the script to detect certain keywords and create SAFETY_WARNING blocks:

```python
def _detect_safety_warnings(self, body: str) -> str:
    """Detect safety-related text and convert to SAFETY_WARNING blocks."""
    # Look for patterns like "CAUTION:", "WARNING:", etc.
    # Convert to appropriate SAFETY_WARNING blocks
    pass
```

## Getting Help

- **Script issues:** Check the error message and traceback
- **Wagtail import errors:** Use the "Validate Markdown" feature
- **Format questions:** See `raw-content/lab_templates/README.md`
- **Field reference:** See `raw-content/lab_templates/FIELD_REFERENCE.md`
- **Template example:** See `raw-content/lab_templates/comprehensive-template.md`

## Version Control Recommendation

It's a good idea to commit your converted files to git:

```bash
git add raw-content/wagtail_output/
git commit -m "Add Wagtail-formatted lab guides"
```

This preserves both your original files and converted versions, allowing you to:
- Track changes over time
- Revert if needed
- Compare before/after versions
- Collaborate with others

## Summary

The conversion script handles the mechanical transformation of your lab guides, but **human review is essential** for quality. Focus your manual effort on:

1. ✅ Improving accessibility (alt text, spoken versions)
2. ✅ Enhancing descriptive text (captions, titles)
3. ✅ Organizing bibliography entries
4. ✅ Validating cross-references
5. ✅ Fine-tuning formatting

Once converted and reviewed, your lab guides will be ready for the modern Wagtail platform with structured content that's easier to maintain, version control, and collaborate on.

Happy converting! 🚀
