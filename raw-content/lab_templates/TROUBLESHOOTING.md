# Troubleshooting Guide - Lab Guide Conversion

## Common Validation Errors in Wagtail

### Error: "Invalid level 'h1'. Must be one of: h2, h3, h4, h5, h6"

**Problem:** Wagtail only accepts heading levels h2 through h6 (not h1).

**Solution:** The script has been updated to automatically convert:
- `#` (h1) → `h2`
- `##` (h2) → `h3`
- `###` (h3) → `h4`
- etc.

**If you still see this error:**
1. Check for any manually created HEADING blocks with `level: h1`
2. Change `level: h1` to `level: h2`
3. Re-upload

**Fixed in version:** Script updated 2025-11-03

---

### Error: "'bool' object has no attribute 'lower'"

**Problem:** This error occurs when the Wagtail parser encounters an improperly formatted field.

**Possible Causes:**

1. **Missing required fields** - Check that all required fields are present:
   - HEADING: `level`
   - EQUATION: `display_type`, `spoken_version`, `auto_number`
   - FIGURE: `image_path` or `image_id`, `alt_text`
   - TABLE: `caption`
   - CODE: `language`

2. **Empty or invalid field values** - Check for:
   - Empty strings: `caption: ""`
   - Missing colons: `auto_number true` (should be `auto_number: true`)
   - Invalid boolean values: Use `true`/`false` (lowercase, unquoted)

3. **Malformed block structure** - Verify:
   - Opening tag: `<!-- BLOCKTYPE -->`
   - Metadata fields (key: value)
   - Separator: `---` (for blocks with content)
   - Content section
   - Closing tag: `<!-- /BLOCKTYPE -->`

**How to Debug:**

1. **Use Wagtail's "Validate Markdown" button** - It will show which block/line has the error

2. **Check the specific block mentioned in the error:**
   ```markdown
   <!-- FIGURE -->
   reference_id: fig-test
   image_path: images/test.jpg
   alt_text: Test image
   display_width: full
   auto_number: true    ← Check this is lowercase true/false
   ---
   Caption text here
   <!-- /FIGURE -->
   ```

3. **Common fixes:**
   - Ensure `auto_number: true` (not `auto_number: True` or `auto_number: yes`)
   - Ensure `show_line_numbers: false` (not `show_line_numbers: False`)
   - Check for missing `---` separator between metadata and content
   - Verify all required fields are present

4. **Search for the problem:**
   ```bash
   # Find blocks with boolean fields
   grep -n "auto_number\|show_line_numbers\|dismissible" your-file.md

   # Check for missing separators
   grep -B5 "<!-- /" your-file.md | grep -v "^---$"
   ```

---

### Error: "Missing required field 'X'"

**Problem:** A required field is not present in a block.

**Solution:** Add the missing field. Required fields by block type:

#### HEADING
- `level` (h2, h3, h4, h5, or h6)

#### EQUATION
- `display_type` (display or inline)
- `spoken_version` (minimum 5 characters)
- `auto_number` (true or false)

#### FIGURE
- `image_path` (for import) or `image_id` (for export)
- `alt_text` (minimum 10 characters)

#### TABLE
- `caption` (minimum 5 characters)

#### CODE
- `language` (e.g., python, matlab, bash)

#### SAFETY_WARNING
- `severity` (danger, warning, caution, or info)
- `title` (minimum 3 characters)

---

### Error: "Image not found" or "Invalid image_path"

**Problem:** Referenced image doesn't exist or path is incorrect.

**Solutions:**

1. **Check the image exists:**
   ```bash
   ls raw-content/wagtail_output/zip/lab1/images/
   ```

2. **Verify image_path format:**
   ```markdown
   <!-- FIGURE -->
   image_path: images/banana.jpg    ← Correct (relative path)
   <!-- /FIGURE -->
   ```

   NOT:
   - `image_path: ../resources/banana.jpg`
   - `image_path: /images/banana.jpg`
   - `image_path: C:\Users\...\banana.jpg`

3. **Check filename matches exactly:**
   - Case-sensitive: `Banana.jpg` ≠ `banana.jpg`
   - Spaces: Use exact name: `bnc banana adapter.png`

4. **Re-run conversion with `--create-zip`:**
   ```bash
   python convert_to_wagtail.py raw-content/lab1-raw.md --create-zip
   ```

---

### Error: "Invalid cross-reference"

**Problem:** A `\ref{}` or `\cite{}` points to a non-existent ID.

**Solutions:**

1. **Check reference_id exists:**
   ```bash
   # Find all reference IDs
   grep "reference_id:" lab1-wagtail.md

   # Find all references to a specific ID
   grep "\\ref{fig-banana}" lab1-wagtail.md
   ```

2. **Ensure reference_id matches exactly:**
   - Case-sensitive
   - Hyphens vs underscores
   - Common mistake: `\ref{fig:banana}` but `reference_id: fig-banana`

3. **For bibliography:**
   ```markdown
   # Must have matching BIBENTRY
   \cite{young2020}  ← Citation in text

   <!-- BIBENTRY -->
   reference_key: young2020  ← Must match
   authors: Young, H. D.
   ...
   <!-- /BIBENTRY -->
   ```

---

### Error: "Ensure this value has at most 50 characters"

**Problem:** Reference IDs exceeding 50-character limit.

**Cause:** Long section titles generate long reference IDs. Wagtail has a 50-character limit.

**Solution:** The script (v1.1+) now automatically truncates reference IDs to 50 characters.

**If you still see this error:**
1. Verify you're using the latest script (v1.1)
2. Check for any manually created reference IDs that are too long
3. Shorten them:
   ```markdown
   <!-- HEADING -->
   reference_id: appendix-b-changing-output-termination  ← 42 chars (OK)
   level: h2
   ---
   Appendix B: Changing the Output Termination
   <!-- /HEADING -->
   ```

**Auto-generated IDs:** Script now handles this automatically. Re-run conversion if you have old output.

---

### Error: "LaTeX syntax error" in equations

**Problem:** Invalid LaTeX in EQUATION block.

**Solutions:**

1. **Check for unmatched braces:**
   ```latex
   \frac{a}{b}    ✓ Correct
   \frac{a{b}     ✗ Missing }
   ```

2. **Escape special characters:**
   ```latex
   \{  \}  \_  \&  \%  \#
   ```

3. **Use correct LaTeX commands:**
   ```latex
   \Delta V = IR              ✓
   ΔV = IR                    ✗ Use LaTeX commands
   ```

4. **Test in a LaTeX editor first** if unsure

---

## Conversion Script Issues

### Issue: "No images copied"

**Problem:** Script reports 0 images found or copied.

**Solutions:**

1. **Check image paths in original markdown:**
   ```bash
   grep "!\[" raw-content/lab1-raw.md
   ```

2. **Verify resources directory exists:**
   ```bash
   ls resources/lab1fig/
   ```

3. **Check image path format in original:**
   - Should be: `../resources/lab1fig/image.jpg`
   - Script looks for pattern: `../resources/`

### Issue: "UnicodeEncodeError" on Windows

**Problem:** Console can't display certain characters.

**Solution:** Already fixed in current version. Script uses ASCII-safe output:
- `[OK]` instead of `✓`
- `-` instead of Unicode tree characters

### Issue: "ZIP file is empty" or "Missing guide.md"

**Problem:** ZIP package creation failed.

**Solutions:**

1. **Check conversion succeeded:**
   ```bash
   ls raw-content/wagtail_output/lab1-wagtail.md
   ```

2. **Verify ZIP was created:**
   ```bash
   ls raw-content/wagtail_output/zip/
   ```

3. **Check ZIP contents:**
   ```bash
   unzip -l raw-content/wagtail_output/zip/lab1.zip
   ```

4. **Re-run with `--create-zip`:**
   ```bash
   rm -rf raw-content/wagtail_output
   python convert_to_wagtail.py raw-content/lab1-raw.md --create-zip
   ```

---

## Wagtail Import Issues

### Issue: "Upload failed"

**Possible causes:**
1. File too large (check Wagtail upload limits)
2. Invalid ZIP structure
3. Network timeout

**Solutions:**
1. Check file size: `ls -lh lab1.zip`
2. Verify ZIP structure (should have `lab1/guide.md` and `lab1/images/`)
3. Try uploading individual files instead of ZIP
4. Contact Wagtail administrator about upload limits

### Issue: "Content not displaying correctly"

**Solutions:**
1. Check browser console for JavaScript errors
2. Verify all images loaded correctly
3. Review equations render properly (may need page refresh)
4. Check for CSS conflicts

---

## Getting More Help

### Quick Diagnostics

Run these commands to check your setup:

```bash
# Check Python version (need 3.7+)
python --version

# Check script exists
ls convert_to_wagtail.py

# Check a conversion
python convert_to_wagtail.py raw-content/lab1-raw.md --create-zip

# Check output
ls raw-content/wagtail_output/
ls raw-content/wagtail_output/zip/

# Verify ZIP contents
unzip -l raw-content/wagtail_output/zip/lab1.zip
```

### Validation Checklist

Before uploading to Wagtail:

- [ ] All HEADING blocks use h2-h6 (not h1)
- [ ] All boolean fields use lowercase: `true`/`false`
- [ ] All required fields present for each block type
- [ ] All image_path values use relative `images/` paths
- [ ] All cross-references (`\ref{}`) point to existing IDs
- [ ] All citations (`\cite{}`) have matching BIBENTRY blocks
- [ ] LaTeX equations have valid syntax
- [ ] Alt text is descriptive (minimum 10 characters)
- [ ] Spoken versions are natural language (minimum 5 characters)
- [ ] ZIP contains `labN/guide.md` and `labN/images/`

### Resources

- **Script help:** `python convert_to_wagtail.py --help`
- **Wagtail format:** [raw-content/lab_templates/README.md](raw-content/lab_templates/README.md)
- **Field reference:** [raw-content/lab_templates/FIELD_REFERENCE.md](raw-content/lab_templates/FIELD_REFERENCE.md)
- **Examples:** [raw-content/lab_templates/comprehensive-template.md](raw-content/lab_templates/comprehensive-template.md)

---

## Report Issues

If you encounter a bug in the conversion script:

1. Note the exact command you ran
2. Capture the complete error message
3. Check if error persists with a fresh conversion:
   ```bash
   rm -rf raw-content/wagtail_output
   python convert_to_wagtail.py <your-command>
   ```
4. Review this troubleshooting guide
5. Check the generated markdown file for issues

**Most issues are quickly resolved by:**
- Re-running the conversion
- Checking the validation output in Wagtail
- Reviewing the specific block mentioned in the error
- Ensuring all required fields are present

Happy troubleshooting! 🔧
