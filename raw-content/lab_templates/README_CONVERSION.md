# Lab Guide Conversion Toolkit - Start Here

Welcome! This toolkit converts your Jekyll/Pandoc lab guides to the new Django/Wagtail platform format.

## 🚀 Quick Links

**Just want to get started?** → [QUICK_START.md](QUICK_START.md)

**Need comprehensive details?** → [CONVERSION_GUIDE.md](CONVERSION_GUIDE.md)

**Want visual workflow?** → [WORKFLOW_DIAGRAM.md](WORKFLOW_DIAGRAM.md)

**Looking for summary?** → [SUMMARY.md](SUMMARY.md)

## 📋 What's Included

### Core Tool
- **[convert_to_wagtail.py](convert_to_wagtail.py)** - Python script that does all the conversion work

### Documentation
1. **[CONVERSION_README.md](CONVERSION_README.md)** - Project overview and features
2. **[QUICK_START.md](QUICK_START.md)** - Fast track guide (5 minutes)
3. **[ZIP_PACKAGE_GUIDE.md](ZIP_PACKAGE_GUIDE.md)** - ZIP package creation for easy import
4. **[CONVERSION_GUIDE.md](CONVERSION_GUIDE.md)** - Complete documentation (30 minutes read)
5. **[WORKFLOW_DIAGRAM.md](WORKFLOW_DIAGRAM.md)** - Visual workflow diagrams
6. **[SUMMARY.md](SUMMARY.md)** - What was created and why

### Helper Scripts
- **convert_all_labs.bat** - One-click conversion for Windows
- **convert_all_labs.sh** - One-click conversion for Mac/Linux

### Wagtail Format Reference
- **raw-content/lab_templates/README.md** - Wagtail format documentation
- **raw-content/lab_templates/FIELD_REFERENCE.md** - All field options
- **raw-content/lab_templates/comprehensive-template.md** - Full example

## 🎯 Choose Your Path

### Path 1: "I Want to Start Right Now" (5 min)

```bash
# Convert all labs with ready-to-upload ZIP packages
python convert_to_wagtail.py raw-content/lab*-raw.md --create-zip

# Review output
ls raw-content/wagtail_output/zip/
```

Then upload ZIP files to Wagtail! See [ZIP_PACKAGE_GUIDE.md](ZIP_PACKAGE_GUIDE.md) for details.

### Path 2: "I Want to Understand First" (30 min)

1. Read [CONVERSION_README.md](CONVERSION_README.md) for overview
2. Review [WORKFLOW_DIAGRAM.md](WORKFLOW_DIAGRAM.md) for visual understanding
3. Read [CONVERSION_GUIDE.md](CONVERSION_GUIDE.md) for comprehensive details
4. Run conversion on one lab to test

### Path 3: "I Want a Quick Reference" (2 min)

Read [QUICK_START.md](QUICK_START.md) - it has everything you need in condensed form.

## 🔍 Find What You Need

| I want to... | Read this |
|--------------|-----------|
| **Start converting immediately** | [QUICK_START.md](QUICK_START.md) |
| **Understand the whole process** | [CONVERSION_GUIDE.md](CONVERSION_GUIDE.md) |
| **See visual workflow** | [WORKFLOW_DIAGRAM.md](WORKFLOW_DIAGRAM.md) |
| **Know what was created** | [SUMMARY.md](SUMMARY.md) |
| **Learn Wagtail format** | [raw-content/lab_templates/README.md](raw-content/lab_templates/README.md) |
| **Troubleshoot errors** | [CONVERSION_GUIDE.md](CONVERSION_GUIDE.md#troubleshooting) |
| **Customize the script** | [CONVERSION_GUIDE.md](CONVERSION_GUIDE.md#advanced-customizing-the-conversion) |

## ⚡ Most Common Commands

```bash
# Convert single lab with ZIP package (recommended)
python convert_to_wagtail.py raw-content/lab1-raw.md --create-zip

# Convert all labs with ZIP packages
python convert_to_wagtail.py raw-content/lab*-raw.md --create-zip

# Windows: One-click conversion with ZIPs
convert_all_labs.bat

# Mac/Linux: One-click conversion with ZIPs
./convert_all_labs.sh
```

## 📊 What Gets Converted

| From (Jekyll/Pandoc) | To (Wagtail) |
|---------------------|--------------|
| `# Heading` | `HEADING` block with reference ID |
| `![caption](img){#id}` | `FIGURE` block with metadata |
| `$$equation$$` | `EQUATION` block with accessibility |
| Markdown tables | `TABLE` blocks with captions |
| Code blocks | `CODE` blocks with syntax highlighting |
| `../resources/img.jpg` | `images/img.jpg` (auto-copied) |

## ✏️ What Needs Manual Review

After automated conversion, you should enhance:

1. **Equation spoken versions** - For screen reader accessibility
2. **Figure alt text** - Detailed descriptions
3. **Table captions** - Make them informative
4. **Learning objectives** - Student-focused wording
5. **Bibliography** - Create BIBENTRY blocks

See [CONVERSION_GUIDE.md](CONVERSION_GUIDE.md#manual-review-required) for details.

## 🎓 Example: Before & After

**Before (Jekyll/Pandoc):**
```markdown
![Banana cables](../resources/lab1fig/banana.jpg){#fig:banana}
```

**After (Wagtail):**
```markdown
<!-- FIGURE -->
reference_id: fig:banana
image_path: images/banana.jpg
alt_text: Photo of red and black banana cables with metal connector tips
display_width: half
auto_number: true
---
Banana cables used for connecting to power supply and multimeter.
<!-- /FIGURE -->
```

## 📁 Project Structure

```
PHYS-3330/
│
├── convert_to_wagtail.py          ← Main conversion script
│
├── Documentation/
│   ├── README_CONVERSION.md       ← This file (start here)
│   ├── QUICK_START.md             ← Fast track guide
│   ├── CONVERSION_GUIDE.md        ← Comprehensive guide
│   ├── CONVERSION_README.md       ← Project overview
│   ├── WORKFLOW_DIAGRAM.md        ← Visual diagrams
│   └── SUMMARY.md                 ← What was created
│
├── Helper Scripts/
│   ├── convert_all_labs.bat       ← Windows batch file
│   └── convert_all_labs.sh        ← Unix/Mac bash script
│
└── raw-content/
    ├── lab_templates/             ← Wagtail format reference
    │   ├── README.md
    │   ├── FIELD_REFERENCE.md
    │   └── comprehensive-template.md
    │
    ├── lab1-raw.md                ← Your existing labs
    ├── lab2-raw.md
    └── wagtail_output/            ← Generated by script
        ├── lab1-wagtail.md
        └── images/
```

## ⚙️ Requirements

- **Python:** 3.7 or higher (`python --version`)
- **Operating System:** Windows, Mac, or Linux
- **Dependencies:** None (uses Python standard library only)

## 🆘 Getting Help

### Script Issues
1. Check the error message
2. See [CONVERSION_GUIDE.md - Troubleshooting](CONVERSION_GUIDE.md#troubleshooting)
3. Verify Python version is 3.7+

### Wagtail Format Questions
1. See [raw-content/lab_templates/README.md](raw-content/lab_templates/README.md)
2. Check [FIELD_REFERENCE.md](raw-content/lab_templates/FIELD_REFERENCE.md)
3. Review [comprehensive-template.md](raw-content/lab_templates/comprehensive-template.md)

### Import Errors
1. Use Wagtail's "Validate Markdown" button
2. Check all image paths are correct
3. Verify EQUATION blocks have valid LaTeX
4. Ensure reference IDs are unique

## 🎯 Success Path

```
1. Read QUICK_START.md             [5 min]
   ↓
2. Run conversion on all labs      [1 min]
   ↓
3. Review one lab thoroughly       [30 min]
   ↓
4. Test import in Wagtail         [15 min]
   ↓
5. Process remaining labs          [~10 hours total]
   ↓
6. 🎉 All labs on new platform!
```

## 💡 Pro Tips

1. **Start with one lab** - Test the full workflow before converting all
2. **Use git** - Commit converted files to track changes
3. **Validate in Wagtail** - Use the "Validate Markdown" feature before importing
4. **Review systematically** - Create a checklist for each lab
5. **Improve as you go** - Learn from each lab to refine the process

## 📝 Quick Checklist

Before you start:
- [ ] Python 3.7+ installed
- [ ] Have access to Wagtail admin
- [ ] Read QUICK_START.md
- [ ] Understand Wagtail format basics

First lab:
- [ ] Convert lab1 with script
- [ ] Review and enhance output
- [ ] Organize files for import
- [ ] Test import in Wagtail
- [ ] Document any issues/improvements

Scale up:
- [ ] Convert all remaining labs
- [ ] Apply enhancements systematically
- [ ] Import to Wagtail one by one
- [ ] Verify all content displays correctly

## 🚀 Ready to Start?

1. **Absolute beginner?** → [QUICK_START.md](QUICK_START.md)
2. **Want full details?** → [CONVERSION_GUIDE.md](CONVERSION_GUIDE.md)
3. **Visual learner?** → [WORKFLOW_DIAGRAM.md](WORKFLOW_DIAGRAM.md)
4. **Just do it!** → Run `python convert_to_wagtail.py raw-content/lab*-raw.md --create-image-dir`

---

**Questions?** Check the documentation files above or review error messages from the script.

**Happy converting!** 🎓✨
