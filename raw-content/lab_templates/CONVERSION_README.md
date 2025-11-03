# Lab Guide Content Conversion Toolkit

This toolkit converts your existing Jekyll/Pandoc lab guide content to the new Django/Wagtail platform format.

## 📁 What's Included

| File | Purpose |
|------|---------|
| [convert_to_wagtail.py](convert_to_wagtail.py) | Main conversion script (Python 3.7+) |
| [CONVERSION_GUIDE.md](CONVERSION_GUIDE.md) | Comprehensive conversion documentation |
| [QUICK_START.md](QUICK_START.md) | Quick reference guide |
| `convert_all_labs.bat` | Windows batch script to convert all labs |
| `convert_all_labs.sh` | Unix/Mac bash script to convert all labs |

## 🚀 Quick Start

### For Windows Users

Double-click `convert_all_labs.bat` or run:
```cmd
convert_all_labs.bat
```

### For Mac/Linux Users

```bash
./convert_all_labs.sh
```

### Manual Conversion

```bash
# Single lab
python convert_to_wagtail.py raw-content/lab1-raw.md --create-image-dir

# All labs
python convert_to_wagtail.py raw-content/lab*-raw.md --create-image-dir
```

## 📖 Documentation

- **First time?** → Start with [QUICK_START.md](QUICK_START.md)
- **Need details?** → See [CONVERSION_GUIDE.md](CONVERSION_GUIDE.md)
- **Wagtail format reference?** → See [raw-content/lab_templates/README.md](raw-content/lab_templates/README.md)

## 🔄 Workflow Overview

```
Current System                    Conversion Script               New Wagtail System
─────────────                    ─────────────────               ──────────────────
lab1-raw.md                           ▼                          lab1-wagtail.md
  ↓                            [convert_to_wagtail.py]                ↓
mdtohtml.sh + pandoc                  ▼                          Wagtail import
  ↓                            Auto-converts:                         ↓
_includes/lab1.html              - Headings → HEADING blocks      Rich structured
  ↓                              - Figures → FIGURE blocks         content in CMS
Jekyll site                      - Equations → EQUATION blocks         ↓
                                 - Tables → TABLE blocks          Easy versioning
                                 - Code → CODE blocks              & collaboration
                                   ▼
                               Manual review & enhancement
                                   ▼
                               Import to Wagtail
```

## ✨ Key Features

### Automated Conversions
- ✅ YAML frontmatter transformation
- ✅ Pandoc-style figures to FIGURE blocks
- ✅ Markdown headings to HEADING blocks
- ✅ LaTeX equations to EQUATION blocks
- ✅ Markdown tables to TABLE blocks
- ✅ Code blocks to CODE blocks
- ✅ Image path updates
- ✅ Automatic image file copying

### Manual Enhancement Required
- ✏️ Equation spoken versions (accessibility)
- ✏️ Figure alt text descriptions
- ✏️ Table captions
- ✏️ Bibliography entries
- ✏️ Learning objectives refinement

## 📂 Output Structure

After running the conversion:

```
raw-content/
└── wagtail_output/
    ├── lab1-wagtail.md
    ├── lab2-wagtail.md
    ├── ...
    └── images/
        ├── banana.jpg
        ├── scope-guide.png
        └── ...
```

## 🎯 Next Steps After Conversion

1. **Review** converted files in `raw-content/wagtail_output/`
2. **Enhance** accessibility features:
   - Equation spoken versions
   - Figure alt text
   - Table summaries
3. **Add** bibliography entries (BIBENTRY blocks)
4. **Organize** each lab with its images:
   ```
   lab1/
   ├── guide.md
   └── images/
   ```
5. **Import** to Wagtail:
   - Validate markdown first
   - Upload guide.md + images folder
   - Review and publish

## 🔧 System Requirements

- **Python:** 3.7 or higher
- **Operating System:** Windows, Mac, or Linux
- **Dependencies:** None (uses Python standard library only)

## 📋 Example Conversion

**Input** ([lab1-raw.md](raw-content/lab1-raw.md)):
```markdown
---
title: "Lab 1 - Electronic Measurements"
---

# Goals
Today you will learn to use equipment...

![Banana cables](../resources/lab1fig/banana.jpg){#fig:banana width="8cm"}
```

**Output** (lab1-wagtail.md):
```markdown
---
lab_number: 1
lab_title: "Lab 1 - Electronic Measurements"
duration_hours: 3.0
difficulty: intermediate
enable_section_numbering: true
---

## Learning Objectives

Students will:

Today you will learn to use equipment...

<!-- FIGURE -->
reference_id: fig:banana
image_path: images/banana.jpg
alt_text: Banana cables
display_width: half
auto_number: true
---
Banana cables
<!-- /FIGURE -->
```

## 🆘 Troubleshooting

### Images Not Found
- Check that images exist in `resources/` directory
- Verify original markdown has correct image paths
- Manually copy if needed

### Script Errors
- Ensure Python 3.7+ is installed: `python --version`
- Check file paths are correct
- See error messages for specific issues

### Wagtail Import Errors
- Use "Validate Markdown" button in Wagtail admin
- Check all FIGURE blocks have valid image paths
- Verify EQUATION blocks have proper LaTeX syntax
- Ensure reference IDs are unique

## 📚 Additional Resources

- **Wagtail Template Documentation:** [raw-content/lab_templates/README.md](raw-content/lab_templates/README.md)
- **Field Reference:** [raw-content/lab_templates/FIELD_REFERENCE.md](raw-content/lab_templates/FIELD_REFERENCE.md)
- **Example Template:** [raw-content/lab_templates/comprehensive-template.md](raw-content/lab_templates/comprehensive-template.md)

## 🤝 Getting Help

1. Check the error messages and console output
2. Review [CONVERSION_GUIDE.md](CONVERSION_GUIDE.md) troubleshooting section
3. Use Wagtail's "Validate Markdown" feature before importing
4. Consult the template documentation in `raw-content/lab_templates/`

## 📝 Notes

- **Original files are preserved** - The script only creates new files
- **Git-friendly** - Converted files work well with version control
- **Extensible** - Script can be customized for your needs
- **Human review essential** - Automated conversion handles structure, you add quality

## 🎓 Philosophy

This toolkit automates the **mechanical** transformation while preserving your need for **human expertise** in:
- Pedagogical decisions (learning objectives)
- Accessibility improvements (alt text, spoken versions)
- Content quality (captions, descriptions)
- Academic rigor (bibliography, citations)

The script does the tedious work. You focus on making great lab guides! 🚀

---

**Ready to convert?** See [QUICK_START.md](QUICK_START.md) to begin!
