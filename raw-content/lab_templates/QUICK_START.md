# Quick Start: Convert Lab Guides to Wagtail Format

## TL;DR - Fast Track

```bash
# 1. Convert all labs with automatic image handling
python convert_to_wagtail.py raw-content/lab*-raw.md --create-image-dir

# 2. Review output
ls raw-content/wagtail_output/

# 3. Manually improve the converted files
#    - Fix equation spoken versions
#    - Enhance figure alt text
#    - Add bibliography entries
#    - Review captions

# 4. Organize for Wagtail import (per lab)
mkdir -p import-ready/lab1/images
cp raw-content/wagtail_output/lab1-wagtail.md import-ready/lab1/guide.md
# Copy relevant images from wagtail_output/images/ to import-ready/lab1/images/

# 5. Import to Wagtail
#    - Upload guide.md and images folder
#    - Validate, review, publish
```

## What This Script Does

**Converts this:**
```markdown
# Lab 1 - Electronic Measurements

![Banana cables](../resources/lab1fig/banana.jpg){#fig:banana width="8cm"}

$$V = IR$$
```

**Into this:**
```markdown
---
lab_number: 1
lab_title: "Lab 1 - Electronic Measurements"
duration_hours: 3.0
difficulty: intermediate
enable_section_numbering: true
---

<!-- HEADING -->
reference_id: lab-1-electronic-measurements
level: h1
---
Lab 1 - Electronic Measurements
<!-- /HEADING -->

<!-- FIGURE -->
reference_id: fig:banana
image_path: images/banana.jpg
alt_text: Banana cables
display_width: half
auto_number: true
---
Banana cables
<!-- /FIGURE -->

<!-- EQUATION -->
reference_id: eq-1
display_type: display
auto_number: true
spoken_version: V equals I R
---
V = IR
<!-- /EQUATION -->
```

## Three-Step Process

### 1. Run Conversion (5 minutes)

```bash
python convert_to_wagtail.py raw-content/lab*-raw.md --create-image-dir
```

**Output:** `raw-content/wagtail_output/` with all converted files

### 2. Manual Review (15-30 minutes per lab)

Open each converted file and improve:

- ✏️ **Learning objectives** - Make student-focused
- ✏️ **Equation spoken versions** - Improve accessibility
- ✏️ **Figure alt text** - Add detailed descriptions
- ✏️ **Table captions** - Make descriptive
- ✏️ **Bibliography** - Add BIBENTRY blocks

### 3. Import to Wagtail (10 minutes per lab)

1. Organize files:
   ```
   lab1/
   ├── guide.md
   └── images/
       ├── image1.jpg
       └── image2.png
   ```

2. In Wagtail admin:
   - Click "Import Markdown"
   - Validate first
   - Upload files
   - Review and publish

## Most Important Manual Edits

### Equation Spoken Versions

**Auto-generated (❌ Needs work):**
```yaml
spoken_version: Delta V equals I R
```

**Improved (✅ Better):**
```yaml
spoken_version: Voltage drop equals current times resistance
```

### Figure Alt Text

**Auto-generated (❌ Too brief):**
```yaml
alt_text: Banana cables
```

**Improved (✅ Descriptive):**
```yaml
alt_text: Photo of red and black banana cables with metal tips for connecting to power supply and multimeter
```

### Bibliography

**Add these manually:**
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

## Common Issues

| Problem | Solution |
|---------|----------|
| Missing images | Copy manually from `resources/` |
| Broken LaTeX | Review EQUATION blocks for syntax errors |
| Bad reference IDs | Make them descriptive: `power-supply-setup` not `section-1` |
| Generic captions | Rewrite to be specific and informative |

## Need More Detail?

See [CONVERSION_GUIDE.md](CONVERSION_GUIDE.md) for comprehensive documentation.

## Template References

Check these for Wagtail format examples:
- `raw-content/lab_templates/README.md` - Complete documentation
- `raw-content/lab_templates/comprehensive-template.md` - Full example
- `raw-content/lab_templates/FIELD_REFERENCE.md` - All field options

## Support

Questions about:
- **Script functionality** → See error messages and [CONVERSION_GUIDE.md](CONVERSION_GUIDE.md)
- **Wagtail format** → See `lab_templates/` documentation
- **Import errors** → Use Wagtail's "Validate Markdown" feature
