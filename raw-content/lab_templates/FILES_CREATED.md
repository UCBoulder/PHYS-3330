# Files Created for Lab Guide Conversion Project

This document lists all files created to help you convert lab guides from Jekyll/Pandoc to Wagtail format.

## Created: 2025-11-03

### Core Tool
1. **convert_to_wagtail.py** (503 lines)
   - Main Python conversion script
   - Converts markdown structure to Wagtail blocks
   - Handles images, equations, tables, code blocks
   - Auto-copies and renames image files

### Documentation Files
2. **README_CONVERSION.md** - Navigation hub and start page
3. **QUICK_START.md** - Fast track reference guide
4. **CONVERSION_GUIDE.md** - Comprehensive conversion documentation
5. **CONVERSION_README.md** - Project overview and features
6. **WORKFLOW_DIAGRAM.md** - Visual workflow diagrams
7. **SUMMARY.md** - What was created and why
8. **FILES_CREATED.md** - This file

### Helper Scripts
9. **convert_all_labs.bat** - Windows batch script for one-click conversion
10. **convert_all_labs.sh** - Unix/Mac bash script for one-click conversion

## Test Results

Successfully tested on:
- **lab1-raw.md** (711 lines)
  - Converted to structured Wagtail format
  - 24 images identified and copied
  - Output: raw-content/wagtail_output/lab1-wagtail.md

## How to Use

### Quick Start
```bash
# Windows
convert_all_labs.bat

# Mac/Linux
./convert_all_labs.sh
```

### Manual
```bash
python convert_to_wagtail.py raw-content/lab*-raw.md --create-image-dir
```

## Documentation Reading Order

**For First-Time Users:**
1. README_CONVERSION.md (start here)
2. QUICK_START.md (fast reference)
3. Run conversion on one lab
4. CONVERSION_GUIDE.md (detailed reference)

**For Quick Reference:**
1. QUICK_START.md only
2. Run conversion
3. Refer to CONVERSION_GUIDE.md as needed

## File Sizes

| File | Lines | Purpose |
|------|-------|---------|
| convert_to_wagtail.py | 503 | Main conversion script |
| CONVERSION_GUIDE.md | 850+ | Comprehensive documentation |
| QUICK_START.md | 200+ | Fast track guide |
| WORKFLOW_DIAGRAM.md | 400+ | Visual diagrams |
| SUMMARY.md | 400+ | Project summary |
| README_CONVERSION.md | 300+ | Navigation hub |
| CONVERSION_README.md | 300+ | Overview |

## Output Structure

After running conversion:
```
raw-content/wagtail_output/
├── lab1-wagtail.md
├── lab2-wagtail.md
├── ...
└── images/
    ├── banana.jpg
    ├── scope-guide.png
    └── ... (100+ images)
```

## Next Steps

1. Read README_CONVERSION.md or QUICK_START.md
2. Run conversion: `python convert_to_wagtail.py raw-content/lab*-raw.md --create-image-dir`
3. Review output in raw-content/wagtail_output/
4. Enhance converted content manually
5. Import to Wagtail

## Support

- Script issues: See error messages and CONVERSION_GUIDE.md troubleshooting
- Wagtail format: See raw-content/lab_templates/README.md
- Import errors: Use Wagtail's "Validate Markdown" feature

---

**Ready to convert?** Start with README_CONVERSION.md!
