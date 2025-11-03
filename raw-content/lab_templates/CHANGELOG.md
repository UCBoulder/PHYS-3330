# Changelog - Lab Guide Conversion Script

## Version 1.1 - 2025-11-03

### 🔧 Critical Fixes

#### Image Path Fix
**Problem:** Script was generating `image_path: images/banana.jpg`, causing Wagtail validation errors because the importer automatically adds the `images/` prefix, resulting in `images/images/banana.jpg`.

**Solution:** Script now outputs just the filename: `image_path: banana.jpg`

**Files Changed:**
- `convert_to_wagtail.py` line 406: Changed `return f"images/{filename}"` to `return filename`
- Updated ZIP package creation regex to match new format (line 497)

**Impact:** This fixes the validation errors users were encountering during Wagtail import.

---

### 🎯 Heading Level Fix
**Problem:** Wagtail only accepts heading levels h2-h6, but script was generating h1.

**Solution:** Script now automatically shifts all heading levels:
- `#` (h1) → `h2`
- `##` (h2) → `h3`
- `###` (h3) → `h4`
- etc.

**Files Changed:**
- `convert_to_wagtail.py` lines 191-194: Added level shifting logic

---

### 📏 Reference ID Length Fix
**Problem:** Wagtail has a 50-character limit on reference IDs. Long heading titles created IDs exceeding this limit, causing validation errors: "Ensure this value has at most 50 characters".

**Solution:** Script now truncates reference IDs to 50 characters maximum.

**Example:**
- Before: `appendix-b-changing-the-output-termination-on-the-function-generator-keysight-edu33212a` (88 chars)
- After: `appendix-b-changing-the-output-termination-on-the` (50 chars)

**Files Changed:**
- `convert_to_wagtail.py` lines 399-401: Added length check and truncation logic

**Impact:** Prevents validation errors for long section titles.

---

### ✨ New Features

#### ZIP Package Creation
Added `--create-zip` flag to automatically create Wagtail-ready ZIP packages.

**Usage:**
```bash
python convert_to_wagtail.py raw-content/lab1-raw.md --create-zip
```

**Output:**
- `raw-content/wagtail_output/zip/lab1.zip`
- Proper structure: `lab1/guide.md` + `lab1/images/`
- Only includes images actually referenced in the lab

**Benefits:**
- One-click upload to Wagtail
- Correct directory structure guaranteed
- Smart image selection (only used images)
- Saves 5+ minutes of manual work per lab

**Files Changed:**
- Added `_create_zip_package()` method (lines 463-529)
- Added `--create-zip` argument to parser (line 557)
- Updated helper scripts to use `--create-zip` by default

---

### 📚 Documentation Updates

#### New Documents
1. **ZIP_PACKAGE_GUIDE.md** - Complete guide to ZIP package feature
2. **TROUBLESHOOTING.md** - Comprehensive troubleshooting guide for common issues
3. **CHANGELOG.md** - This file

#### Updated Documents
1. **README_CONVERSION.md** - Added ZIP package guide to documentation list, updated commands
2. **convert_all_labs.bat** - Now uses `--create-zip` by default
3. **convert_all_labs.sh** - Now uses `--create-zip` by default

---

## Version 1.0 - 2025-11-03 (Initial Release)

### ✨ Features

#### Automated Conversions
- YAML frontmatter transformation (Jekyll → Wagtail)
- Pandoc-style figures → FIGURE blocks
- Markdown headings → HEADING blocks
- LaTeX equations → EQUATION blocks
- Markdown tables → TABLE blocks
- Fenced code blocks → CODE blocks
- Automatic image copying from `resources/` to `images/`

#### Command-Line Options
- `--create-image-dir` - Create images directory and copy files
- `-o OUTPUT` - Specify custom output path

#### Helper Scripts
- `convert_all_labs.bat` (Windows)
- `convert_all_labs.sh` (Unix/Mac)

#### Documentation
- CONVERSION_README.md - Project overview
- QUICK_START.md - Fast track guide
- CONVERSION_GUIDE.md - Comprehensive documentation
- WORKFLOW_DIAGRAM.md - Visual workflows
- SUMMARY.md - Complete project summary

---

## Migration Guide: 1.0 → 1.1

If you converted files with version 1.0, you need to re-convert them to fix the image path issue.

### Quick Migration

```bash
# Delete old output
rm -rf raw-content/wagtail_output

# Re-run conversion with latest script
python convert_to_wagtail.py raw-content/lab*-raw.md --create-zip

# Upload new ZIP files to Wagtail
```

### What Changed in Your Files

**Before (v1.0):**
```markdown
<!-- FIGURE -->
reference_id: fig-banana
image_path: images/banana.jpg    ← Had images/ prefix
alt_text: Banana cables
---
Caption
<!-- /FIGURE -->
```

**After (v1.1):**
```markdown
<!-- FIGURE -->
reference_id: fig-banana
image_path: banana.jpg            ← Just filename now
alt_text: Banana cables
---
Caption
<!-- /FIGURE -->
```

This change is **required** for successful Wagtail import.

---

## Known Issues

### Non-Issues (By Design)

1. **Generic captions for auto-detected tables** - Tables get generic captions like "Data table 1". This is intentional and should be manually improved during review.

2. **Basic equation spoken versions** - Auto-generated spoken versions are basic. Manual review is required for accessibility.

3. **No automatic bibliography** - Script creates placeholder. BIBENTRY blocks must be added manually.

### Limitations

1. **Heading level capped at h6** - Any headings beyond h6 level are capped at h6 (Wagtail limitation)

2. **No safety warning detection** - Script doesn't automatically detect and create SAFETY_WARNING blocks. These must be added manually.

3. **Inline equations preserved as-is** - Only display equations (`$$...$$`) are converted to EQUATION blocks. Inline math (`$...$`) remains inline.

---

## Upgrade Instructions

### For Git Users

```bash
# Pull latest version
git pull origin main

# Or if you have local changes
git stash
git pull origin main
git stash pop
```

### For Manual Downloads

1. Download latest `convert_to_wagtail.py`
2. Replace your existing file
3. Re-run conversions

### Verify Version

Check the script version:
```bash
python convert_to_wagtail.py --help
```

Look for updated examples showing `--create-zip` flag.

---

## Future Enhancements (Planned)

### Short Term
- [ ] Add `--validate-only` flag for dry-run validation
- [ ] Better equation spoken version generation
- [ ] Extract table captions from preceding paragraphs
- [ ] Add `--strict` mode to fail on missing images

### Medium Term
- [ ] Interactive mode for reviewing conversions
- [ ] Support for custom frontmatter fields
- [ ] Batch processing with progress bar
- [ ] Export conversion statistics/report

### Long Term
- [ ] Automatic safety warning detection
- [ ] Bibliography extraction from references section
- [ ] Support for custom block types
- [ ] Integration tests with Wagtail API

---

## Bug Reports

Found a bug? Please:

1. Check this CHANGELOG to see if it's already fixed
2. Re-run conversion with latest version
3. Check TROUBLESHOOTING.md for solutions
4. Verify your input markdown is valid

---

## Version History Summary

| Version | Date | Key Changes |
|---------|------|-------------|
| 1.1 | 2025-11-03 | Fixed image paths, added ZIP creation, fixed heading levels |
| 1.0 | 2025-11-03 | Initial release with core conversion features |

---

**Current Version: 1.1**
**Last Updated: 2025-11-03**
