# Conversion Script: Typora Compatibility Update

## Overview

The `convert_to_wagtail.py` script has been updated to generate **Typora-compatible markdown** that aligns with the new import/export format improvements made to the Wagtail system.

## Changes Made

### 1. Headings - Now use Kramdown/Pandoc `{#id}` syntax

**Before:**
```markdown
<!-- HEADING -->
reference_id: introduction
level: h2
---
Introduction
<!-- /HEADING -->
```

**After:**
```markdown
## Introduction {#introduction}
```

**Benefits:**
- ✅ Renders perfectly in Typora
- ✅ Works with Typora's automatic TOC generation
- ✅ Standard Kramdown/Pandoc syntax
- ✅ Clean, readable format

---

### 2. Figures - Now use standard markdown image syntax

**Before:**
```markdown
<!-- FIGURE -->
reference_id: fig-apparatus
image_path: images/setup.jpg
alt_text: Photo of apparatus
display_width: full
auto_number: true
---
Caption text
<!-- /FIGURE -->
```

**After:**
```markdown
<!-- FIGURE -->
reference_id: fig-apparatus
display_width: full
auto_number: true
---

![Photo of apparatus with detailed description](images/setup.jpg)

*Caption text here*
<!-- /FIGURE -->
```

**Benefits:**
- ✅ Images render directly in Typora
- ✅ Alt text and image path in standard `![alt](path)` format
- ✅ Caption as italic text (visible in preview)
- ✅ Metadata preserved in compact HTML comment
- ✅ No duplication between alt_text and caption

---

### 3. Code Blocks - Now use caption above code

**Before:**
```markdown
<!-- CODE -->
language: python
caption: Code example
show_line_numbers: false
---
```python
code here
```
<!-- /CODE -->
```

**After:**
```markdown
*Python code example* {#code-python-1234}

```python
code here
```
```

**Benefits:**
- ✅ Syntax highlighting in Typora
- ✅ Caption as italic text (visible in preview)
- ✅ Standard fenced code block format
- ✅ Optional reference ID with `{#id}` syntax

---

### 4. Learning Objectives - Already using standard format

No changes needed - already outputs standard markdown:
```markdown
## Learning Objectives

- Students will...
```

---

## Technical Details

### Modified Methods

1. **`_convert_headings()`** (Lines 209-237)
   - Generates `## Title {#ref-id}` format
   - Uses `#` count for heading level
   - Auto-generates reference ID from title

2. **`_convert_figures()`** (Lines 239-304)
   - Generates standard `![alt](path)` syntax
   - Adds italic caption below image
   - Improves alt text for accessibility
   - Preserves Wagtail metadata in HTML comment

3. **`_convert_code_blocks()`** (Lines 369-395)
   - Generates caption as italic text: `*Caption* {#id}`
   - Keeps standard fenced code blocks
   - Auto-generates reference ID from content hash

### Unchanged Methods

- `_convert_equations()` - Already uses traditional format (LaTeX in HTML comment)
- `_convert_tables()` - Already uses markdown tables in content
- `_convert_learning_objectives()` - Already uses standard markdown headings

---

## Testing

Tested with `lab1-raw.md`:
```bash
cd raw-content/lab_templates
python convert_to_wagtail.py ../lab1-raw.md --create-zip
```

**Results:**
- ✅ All headings converted to `{#id}` format
- ✅ All figures use standard markdown image syntax
- ✅ All code blocks have italic captions
- ✅ ZIP package created successfully
- ✅ Output compatible with Wagtail importer

---

## Compatibility

### Forward Compatibility
- Output uses new Typora-compatible format
- Works with updated Wagtail import logic (commits a7b90cb, 29ad8aa, 6d4b1bb)

### Backward Compatibility
- Wagtail importer supports both old and new formats
- Users can still manually edit with traditional format if needed
- Smart extraction handles both syntaxes on import

---

## Benefits for Users

1. **Better Typora Experience**
   - Images render in preview
   - Headings work with TOC
   - Code has syntax highlighting
   - Cleaner, more readable files

2. **Easier Editing**
   - Standard markdown throughout
   - No HTML comment clutter in content
   - Visual feedback in Typora

3. **Improved Accessibility**
   - Better alt text for images
   - Expanded descriptions for screen readers

4. **Version Control Friendly**
   - Cleaner diffs in Git
   - More readable in plain text

---

## Examples from Lab1 Output

### Heading Example:
```markdown
# Lab Notebook Guidelines {#lab-notebook-guidelines}
```

### Figure Example:
```markdown
<!-- FIGURE -->
reference_id: fig:banana
display_width: half
auto_number: true
---

![**Banana cables** - wires with banana connectors at the end. The power supply and DMM have banana sockets to make connections to.](images/banana.jpg)

***Banana cables** - wires with banana connectors at the end. The power supply and DMM have banana sockets to make connections to.*
<!-- /FIGURE -->
```

**Note:** Images now include the `images/` directory prefix so they render properly in Typora when the markdown file is in the same directory as the `images/` folder.

### Code Example:
```markdown
*Text code example* {#code-text-4867}

```text
def parallel_resistance(resistors: list) -> float:
    conductance = 0.0
    for resistance in resistors:
        conductance += 1.0 / resistance
    return 1.0 / conductance
```
```

---

## Version History

- **v1.3** (2025-11-04): Updated to generate Typora-compatible format
- **v1.2** (2025-11-04): Added automatic path detection
- **v1.1**: Added ZIP package creation
- **v1.0**: Initial conversion script

---

## Next Steps

1. ✅ Update conversion script (DONE)
2. ✅ Test with lab1-raw.md (DONE)
3. 🔄 Convert all remaining labs with updated script
4. 🔄 Review and improve auto-generated captions/alt-text
5. 🔄 Test import into Wagtail system

---

## Related Documentation

- [SCRIPT_UPDATES.md](SCRIPT_UPDATES.md) - Automatic path detection (v1.2)
- [README.md](README.md) - Template documentation with Typora format
- [QUICK_START.md](QUICK_START.md) - Quick start guide
- [comprehensive-template.md](comprehensive-template.md) - Full example template
