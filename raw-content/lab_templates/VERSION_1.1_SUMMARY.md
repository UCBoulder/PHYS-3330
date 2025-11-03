# Version 1.1 - Critical Update Summary

## 🎯 What Was Fixed

### Critical Bug: Image Path Issue (RESOLVED ✅)

**The Problem:**
The script was generating:
```markdown
image_path: images/banana.jpg
```

But Wagtail's importer automatically adds `images/` prefix, resulting in:
```
images/images/banana.jpg  ← Double path error!
```

This caused validation failures during import.

**The Fix:**
Script now generates just the filename:
```markdown
image_path: banana.jpg
```

Wagtail adds the `images/` prefix automatically, resulting in correct path:
```
images/banana.jpg  ← Correct!
```

---

## 🚀 How to Use the Fixed Version

### Quick Start

```bash
# Delete old output (if you have any from v1.0)
rm -rf raw-content/wagtail_output

# Run conversion with v1.1
python convert_to_wagtail.py raw-content/lab1-raw.md --create-zip

# Upload the ZIP to Wagtail
# File: raw-content/wagtail_output/zip/lab1.zip
```

### Verify the Fix

Check that image paths are correct:
```bash
grep "image_path:" raw-content/wagtail_output/lab1-wagtail.md
```

**Should see:**
```
image_path: banana.jpg
image_path: scope-guide.png
```

**Should NOT see:**
```
image_path: images/banana.jpg  ← Old/wrong format
```

---

## ✨ What Else Changed

### 1. Heading Levels Fixed
- Changed h1 → h2, h2 → h3, etc.
- Wagtail only accepts h2-h6
- Now fully compliant

### 2. ZIP Package Creation
- New `--create-zip` flag
- Creates ready-to-upload Wagtail packages
- Proper structure: `lab1/guide.md` + `lab1/images/`
- Smart image selection (only used images)

### 3. Better Documentation
- Added TROUBLESHOOTING.md
- Added ZIP_PACKAGE_GUIDE.md
- Added CHANGELOG.md
- Updated all existing docs

---

## 📊 Impact on Your Workflow

### Before v1.1 (Broken)
```bash
python convert_to_wagtail.py lab1-raw.md --create-zip
# Upload ZIP to Wagtail
# ❌ FAILS with validation error
# ❌ Image paths broken (images/images/)
```

### After v1.1 (Working)
```bash
python convert_to_wagtail.py lab1-raw.md --create-zip
# Upload ZIP to Wagtail
# ✅ WORKS! Validation passes
# ✅ Image paths correct
```

---

## 🔄 If You Already Converted Files

**You need to re-convert!**

The old v1.0 output has broken image paths. Here's how to update:

```bash
# Step 1: Clean up
rm -rf raw-content/wagtail_output

# Step 2: Re-convert with v1.1
python convert_to_wagtail.py raw-content/lab*-raw.md --create-zip

# Step 3: Upload new ZIPs to Wagtail
# Files are in: raw-content/wagtail_output/zip/
```

**Why re-convert?**
- Fixes image paths (images/file.jpg → file.jpg)
- Fixes heading levels (h1 → h2)
- Uses improved ZIP packaging

---

## 🎉 Success Indicators

After uploading the new v1.1 files to Wagtail, you should see:

✅ **No validation errors**
✅ **All images display correctly**
✅ **Headings formatted properly**
✅ **Cross-references work**
✅ **Equations render**

If you still see errors, check [TROUBLESHOOTING.md](TROUBLESHOOTING.md).

---

## 📝 Complete Workflow

### 1. Convert All Labs
```bash
# Windows
convert_all_labs.bat

# Mac/Linux
./convert_all_labs.sh

# Or manually
python convert_to_wagtail.py raw-content/lab*-raw.md --create-zip
```

### 2. Review Output
```bash
# Check generated files
ls raw-content/wagtail_output/zip/

# Verify one file (optional)
grep "image_path:" raw-content/wagtail_output/lab1-wagtail.md
```

### 3. Upload to Wagtail
For each lab:
1. Go to Wagtail admin → Import Markdown
2. Upload `labN.zip` from `raw-content/wagtail_output/zip/`
3. Review imported content
4. Save and publish

### 4. Manual Enhancements (Optional but Recommended)
- Improve equation spoken versions
- Enhance figure alt text
- Add descriptive table captions
- Create bibliography entries

---

## 🆘 Troubleshooting

### Issue: Still seeing validation errors

**Solution:**
1. Verify you're using v1.1: Check image paths in output
2. Delete old output: `rm -rf raw-content/wagtail_output`
3. Re-run conversion
4. Upload fresh ZIPs

### Issue: Images not displaying

**Check:**
```bash
# Verify images in ZIP
unzip -l raw-content/wagtail_output/zip/lab1.zip

# Should show:
# lab1/guide.md
# lab1/images/banana.jpg
# lab1/images/scope-guide.png
# etc.
```

### Issue: Wrong image paths in output

**If you see:**
```markdown
image_path: images/banana.jpg  ← WRONG (v1.0)
```

**You need:**
```markdown
image_path: banana.jpg  ← CORRECT (v1.1)
```

**Fix:** Re-download/update the script and re-run conversion.

---

## 📚 Documentation

- **Quick Start:** [QUICK_START.md](QUICK_START.md)
- **ZIP Guide:** [ZIP_PACKAGE_GUIDE.md](ZIP_PACKAGE_GUIDE.md)
- **Troubleshooting:** [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
- **Full Details:** [CONVERSION_GUIDE.md](CONVERSION_GUIDE.md)
- **Changelog:** [CHANGELOG.md](CHANGELOG.md)

---

## 🎯 What's Next?

With v1.1, you can now:

1. ✅ Convert all your lab guides successfully
2. ✅ Upload ZIP packages directly to Wagtail
3. ✅ Have all images display correctly
4. ✅ Pass Wagtail validation

**Recommended next steps:**
1. Convert all labs using the batch script
2. Upload ZIPs to Wagtail one by one
3. Review and enhance content as needed
4. Publish your lab guides!

---

## 💡 Key Takeaway

**The v1.1 update fixes the critical image path bug that was preventing successful Wagtail imports.**

Simply re-run your conversions with the updated script and your imports should work perfectly! 🚀

---

**Version:** 1.1
**Date:** 2025-11-03
**Status:** ✅ Production Ready
