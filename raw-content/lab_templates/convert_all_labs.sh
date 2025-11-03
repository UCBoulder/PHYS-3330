#!/bin/bash
# Bash script to convert all lab guides to Wagtail format
# Usage: ./convert_all_labs.sh

echo "========================================"
echo "Converting Lab Guides to Wagtail Format"
echo "========================================"
echo ""

# Convert all lab*-raw.md files with ZIP package creation
python3 convert_to_wagtail.py raw-content/lab*-raw.md --create-zip

echo ""
echo "========================================"
echo "Conversion Complete!"
echo "========================================"
echo ""
echo "Output location: raw-content/wagtail_output/"
echo "ZIP packages: raw-content/wagtail_output/zip/"
echo ""
echo "Next steps:"
echo "1. Review converted files manually"
echo "2. Improve equation spoken versions"
echo "3. Enhance figure alt text"
echo "4. Add bibliography entries"
echo "5. Upload ZIP files to Wagtail (or organize manually)"
echo ""
echo "See CONVERSION_GUIDE.md for detailed instructions"
echo ""
