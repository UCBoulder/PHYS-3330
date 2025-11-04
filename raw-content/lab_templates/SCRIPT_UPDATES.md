# Script Updates: Automatic Path Detection (v1.2)

## What Changed

The `convert_to_wagtail.py` script now **automatically detects** the repository structure and finds resources without requiring manual path flags.

## New Features

### 1. Automatic Repository Detection
- Finds the repository root by looking for `.git` directory
- Locates the `resources/` directory automatically
- Works from any location in the repository

### 2. Smart Output Placement
- Always places output in `raw-content/wagtail_output/`
- Consistent output location regardless of where you run the script

### 3. Flexible Input Paths
- Accepts input paths relative to your current working directory
- Works whether you run from `lab_templates/` or repository root

## Usage

### Before (Required Manual Paths)
```bash
python convert_to_wagtail.py raw-content/lab1-raw.md \
  --create-zip \
  --resource-dir ../../resources
```

### After (Automatic Detection)
```bash
# From lab_templates directory:
cd raw-content/lab_templates
python convert_to_wagtail.py ../lab1-raw.md --create-zip

# Or from repository root:
python raw-content/lab_templates/convert_to_wagtail.py raw-content/lab1-raw.md --create-zip
```

## How It Works

The script now:
1. Detects its own location (`raw-content/lab_templates/`)
2. Walks up the directory tree to find the repository root
3. Locates `resources/` directory relative to the repo root
4. Resolves input file paths relative to current working directory
5. Places all output in `raw-content/wagtail_output/`

## Benefits

- **No manual path configuration** - Works out of the box
- **More reliable** - Less chance of path errors
- **Easier to use** - Just run from the script's directory
- **Portable** - Works on any system (Windows, Mac, Linux)

## Example Output

```bash
$ cd raw-content/lab_templates
$ python convert_to_wagtail.py ../lab1-raw.md --create-zip

Converting C:\...\PHYS-3330\raw-content\lab1-raw.md to Wagtail format...
[OK] Converted file saved to: C:\...\PHYS-3330\raw-content\wagtail_output\lab1-wagtail.md

[OK] Created image directory: C:\...\PHYS-3330\raw-content\wagtail_output\images
  Using resources from: C:\...\PHYS-3330\resources

  Found 24 images referenced:
    [OK] Copied: scope-screen.png
    [OK] Copied: bnc-plug.jpg
    ...

[OK] ZIP package created: C:\...\PHYS-3330\raw-content\wagtail_output\zip\lab1.zip
```

## Updated Documentation

All documentation has been updated to reflect the new automatic path detection:

- [README.md](README.md) - Added conversion instructions
- [QUICK_START.md](QUICK_START.md) - Updated all examples
- [CONVERSION_GUIDE.md](CONVERSION_GUIDE.md) - Updated usage examples

## Backward Compatibility

The script still supports all existing flags:
- `--create-image-dir` - Create images directory and copy images
- `--create-zip` - Create ready-to-import ZIP packages
- `-o` / `--output` - Custom output location (optional)

The old `--resource-dir` flag is no longer needed (removed from documentation but would still work if someone uses it).

## Version History

- **v1.2** (2025-11-04): Added automatic path detection
- **v1.1**: Added ZIP package creation
- **v1.0**: Initial conversion script
