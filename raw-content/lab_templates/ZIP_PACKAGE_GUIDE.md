# ZIP Package Creation for Wagtail Import

The conversion script now supports automatic creation of Wagtail-ready ZIP packages that can be directly uploaded to your Django/Wagtail platform.

## Quick Start

### Create ZIP for Single Lab

```bash
python convert_to_wagtail.py raw-content/lab1-raw.md --create-zip
```

### Create ZIPs for All Labs

```bash
# Windows
convert_all_labs.bat

# Mac/Linux
./convert_all_labs.sh

# Or manually
python convert_to_wagtail.py raw-content/lab*-raw.md --create-zip
```

## What Gets Created

When you use `--create-zip`, the script creates:

```
raw-content/wagtail_output/
├── lab1-wagtail.md              # Converted markdown
├── lab2-wagtail.md
├── ...
├── images/                      # All images (shared)
│   ├── banana.jpg
│   ├── scope-guide.png
│   └── ...
└── zip/                         # ZIP packages for import
    ├── lab1.zip                 # Ready for Wagtail
    ├── lab2.zip
    └── ...
```

### Inside Each ZIP File

Each ZIP package has the correct structure for Wagtail import:

```
lab1.zip
└── lab1/
    ├── guide.md                 # Converted lab guide
    └── images/                  # Only images used in this lab
        ├── banana.jpg
        ├── scope-guide.png
        └── ...
```

## ZIP Package Features

✅ **Correct Structure** - Matches Wagtail's expected format exactly
✅ **Smart Image Selection** - Only includes images actually referenced in the lab
✅ **Proper Naming** - Uses lab name as folder and ZIP name
✅ **Ready to Upload** - No manual organization needed

## Importing to Wagtail

### Method 1: Direct ZIP Upload (Recommended)

1. Go to Wagtail admin
2. Navigate to the lab guide section
3. Click "Import Markdown"
4. **Click "Validate Markdown"** (optional but recommended)
5. Upload the ZIP file (e.g., `lab1.zip`)
6. Review imported content
7. Save and publish

### Method 2: Extract and Upload Separately

If you prefer manual control:

1. Extract the ZIP file
2. Upload `guide.md`
3. Upload the `images/` folder
4. Review and publish

## Examples

### Convert Single Lab with ZIP

```bash
python convert_to_wagtail.py raw-content/lab1-raw.md --create-zip
```

**Output:**
- `raw-content/wagtail_output/lab1-wagtail.md`
- `raw-content/wagtail_output/images/` (all images)
- `raw-content/wagtail_output/zip/lab1.zip` ← **Upload this to Wagtail**

### Convert All Labs with ZIPs

```bash
python convert_to_wagtail.py raw-content/lab*-raw.md --create-zip
```

**Output:**
- `raw-content/wagtail_output/zip/lab1.zip`
- `raw-content/wagtail_output/zip/lab2.zip`
- `raw-content/wagtail_output/zip/lab3.zip`
- ... (one ZIP per lab)

## Workflow Comparison

### Old Workflow (Manual)

```
1. Convert: python convert_to_wagtail.py lab1.md --create-image-dir
2. Create directory: mkdir lab1
3. Copy guide: cp lab1-wagtail.md lab1/guide.md
4. Create images dir: mkdir lab1/images
5. Manually copy relevant images to lab1/images/
6. Create ZIP: zip -r lab1.zip lab1/
7. Upload to Wagtail
```

### New Workflow (Automatic)

```
1. Convert: python convert_to_wagtail.py lab1.md --create-zip
2. Upload raw-content/wagtail_output/zip/lab1.zip to Wagtail
```

**Time saved:** ~5 minutes per lab guide!

## Command Options

| Command | What It Does |
|---------|-------------|
| `--create-image-dir` | Creates `images/` directory and copies all referenced images |
| `--create-zip` | Creates ZIP package (automatically enables `--create-image-dir`) |

**Note:** `--create-zip` automatically enables `--create-image-dir`, so you don't need both flags.

## File Locations

After running conversion with `--create-zip`:

```
raw-content/wagtail_output/
│
├── lab1-wagtail.md          ← For reference/editing
├── lab2-wagtail.md
├── ...
│
├── images/                  ← All images (shared pool)
│   ├── banana.jpg
│   ├── scope-guide.png
│   └── ...
│
└── zip/                     ← UPLOAD THESE TO WAGTAIL
    ├── lab1.zip            ← Contains lab1/guide.md + lab1/images/
    ├── lab2.zip            ← Contains lab2/guide.md + lab2/images/
    └── ...
```

## ZIP Package Contents

### What's Included

✅ `guide.md` - The converted lab guide in Wagtail format
✅ `images/` - Only images referenced in this specific lab guide
✅ Proper directory structure: `labN/guide.md` and `labN/images/`

### What's NOT Included

❌ Images not referenced in the lab guide
❌ Temporary files
❌ Original raw markdown

## Benefits of ZIP Packages

1. **One-Click Upload** - Just upload the ZIP, no manual organization
2. **Correct Structure** - Guaranteed to match Wagtail's expectations
3. **Optimized** - Only includes images actually used in each lab
4. **Consistent** - Same structure for every lab guide
5. **Fast** - Automates 5+ minutes of manual work per lab

## Troubleshooting

### Issue: ZIP file is too large

**Solution:** This is normal for labs with many images. Wagtail should handle files up to several MB. If you have issues, contact your Wagtail admin about upload limits.

### Issue: Missing images in ZIP

**Problem:** Some images aren't included in the ZIP package.

**Solution:** Check that the images are:
1. Referenced in the markdown with correct `image_path:` format
2. Present in the `resources/` directory
3. Successfully copied to the shared `images/` directory

### Issue: Wrong directory structure in ZIP

**Problem:** ZIP doesn't match expected format.

**Solution:** The script automatically creates the correct structure. If you're seeing issues, try:
1. Delete `raw-content/wagtail_output/`
2. Re-run the conversion
3. Check the console output for errors

## Manual Review Still Required

Even with automatic ZIP creation, you should still:

1. ✏️ **Review the converted markdown** in `lab1-wagtail.md`
2. ✏️ **Improve accessibility** (equation spoken versions, alt text)
3. ✏️ **Enhance captions** (figures, tables)
4. ✏️ **Add bibliography** (BIBENTRY blocks)
5. ✏️ **Test in Wagtail** (validate before final upload)

The ZIP creation is just the final packaging step - quality review is still essential!

## Advanced: Batch Processing

### Convert All Labs to ZIPs

```bash
# Windows
convert_all_labs.bat

# Mac/Linux
./convert_all_labs.sh
```

This creates ZIP packages for all lab guides at once.

### Upload All ZIPs

You can then upload all ZIP files in sequence:

1. `lab1.zip` → Import → Review → Publish
2. `lab2.zip` → Import → Review → Publish
3. `lab3.zip` → Import → Review → Publish
4. ... continue for all labs

## Summary

The `--create-zip` flag automates the final packaging step, saving you 5+ minutes per lab guide and ensuring the correct structure for Wagtail import.

**Quick command:**
```bash
python convert_to_wagtail.py raw-content/lab*-raw.md --create-zip
```

**Output:** Ready-to-upload ZIP files in `raw-content/wagtail_output/zip/`

**Next step:** Upload ZIPs to Wagtail and publish! 🚀

---

For more details, see:
- [QUICK_START.md](QUICK_START.md) - Fast track guide
- [CONVERSION_GUIDE.md](CONVERSION_GUIDE.md) - Comprehensive documentation
- [README_CONVERSION.md](README_CONVERSION.md) - Main navigation
