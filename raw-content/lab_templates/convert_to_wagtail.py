#!/usr/bin/env python3
"""
Convert existing Jekyll/Pandoc lab guides to Wagtail-compatible markdown format.

This script converts lab guide markdown files from the current format
(designed for pandoc + Jekyll) to the new Wagtail CMS format with structured blocks.

Usage:
    python convert_to_wagtail.py raw-content/lab1-raw.md -o output/lab1-wagtail.md
    python convert_to_wagtail.py raw-content/lab1-raw.md --create-image-dir
"""

import re
import argparse
import os
import shutil
import zipfile
from pathlib import Path
from typing import Dict, List, Tuple, Optional


class WagtailMarkdownConverter:
    """Convert Jekyll-style markdown to Wagtail block format."""

    def __init__(self, input_file: Path, output_file: Optional[Path] = None,
                 create_image_dir: bool = False, create_zip: bool = False):
        self.input_file = Path(input_file)
        self.output_file = output_file or self._default_output_path()
        self.create_image_dir = create_image_dir
        self.create_zip = create_zip
        self.image_dir = None
        self.zip_path = None
        self.bibliography = []
        self.equation_counter = 0
        self.figure_counter = 0
        self.table_counter = 0

    def _default_output_path(self) -> Path:
        """Generate default output filename."""
        stem = self.input_file.stem.replace('-raw', '')
        return self.input_file.parent / 'wagtail_output' / f"{stem}-wagtail.md"

    def convert(self) -> str:
        """Main conversion method."""
        print(f"Converting {self.input_file} to Wagtail format...")

        # Read input file
        with open(self.input_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract YAML frontmatter
        frontmatter, body = self._extract_frontmatter(content)

        # Convert frontmatter
        wagtail_frontmatter = self._convert_frontmatter(frontmatter)

        # Convert body content
        converted_body = self._convert_body(body)

        # Combine everything
        output = wagtail_frontmatter + "\n\n" + converted_body

        # Write output
        self.output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.output_file, 'w', encoding='utf-8') as f:
            f.write(output)

        print(f"[OK] Converted file saved to: {self.output_file}")

        # Handle images
        if self.create_image_dir:
            self._setup_image_directory()

        # Create ZIP package if requested
        if self.create_zip:
            self._create_zip_package()

        return output

    def _extract_frontmatter(self, content: str) -> Tuple[Dict, str]:
        """Extract YAML frontmatter from markdown."""
        match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', content, re.DOTALL)
        if match:
            yaml_content = match.group(1)
            body = match.group(2)

            # Parse YAML (simple key: value parsing)
            frontmatter = {}
            for line in yaml_content.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    frontmatter[key.strip()] = value.strip().strip('"').strip("'")

            return frontmatter, body
        return {}, content

    def _convert_frontmatter(self, frontmatter: Dict) -> str:
        """Convert Jekyll frontmatter to Wagtail frontmatter."""
        # Extract lab number from filename if not in frontmatter
        lab_number = frontmatter.get('lab_number', '')
        if not lab_number:
            # Try to extract from filename like "lab1-raw.md"
            match = re.search(r'lab(\d+)', self.input_file.stem)
            if match:
                lab_number = match.group(1)

        title = frontmatter.get('title', 'Untitled Lab')

        # Generate keywords from title
        keywords = frontmatter.get('keywords', '')
        if not keywords:
            # Extract simple keywords from title
            keywords = ', '.join(title.lower().split()[:5])

        wagtail_front = f"""---
lab_number: {lab_number}
lab_title: "{title}"
duration_hours: 3.0
difficulty: intermediate
enable_section_numbering: true
keywords: "{keywords}"
---"""

        return wagtail_front

    def _convert_body(self, body: str) -> str:
        """Convert body content to Wagtail block format."""
        # First, extract learning objectives if present as a section
        body = self._convert_learning_objectives(body)

        # Convert headings to HEADING blocks
        body = self._convert_headings(body)

        # Convert pandoc-style figures to FIGURE blocks
        body = self._convert_figures(body)

        # Convert inline LaTeX equations to EQUATION blocks
        body = self._convert_equations(body)

        # Convert tables to TABLE blocks (if any markdown tables exist)
        body = self._convert_tables(body)

        # Convert code blocks to CODE blocks
        body = self._convert_code_blocks(body)

        # Extract bibliography/references
        body = self._extract_bibliography(body)

        # Clean up HTML comments that aren't needed
        body = self._clean_html_comments(body)

        return body

    def _convert_learning_objectives(self, body: str) -> str:
        """Extract and format learning objectives section."""
        # Look for common patterns like "# Goals" or "# Today you will"
        goals_pattern = r'^#\s+(Goals|Objectives|Today you will.*?)\s*\n(.*?)(?=\n#\s+|\Z)'

        match = re.search(goals_pattern, body, re.MULTILINE | re.DOTALL)
        if match:
            goals_content = match.group(2).strip()

            # Create Learning Objectives section
            learning_obj = "## Learning Objectives\n\n"
            learning_obj += "Students will:\n\n"
            learning_obj += goals_content + "\n\n"

            # Remove original goals section and prepend learning objectives
            body = re.sub(goals_pattern, '', body, flags=re.MULTILINE | re.DOTALL)
            body = learning_obj + body

        return body

    def _convert_headings(self, body: str) -> str:
        """Convert markdown headings to HEADING blocks."""

        def heading_replacer(match):
            level = len(match.group(1))  # Number of # characters
            title = match.group(2).strip()

            # Skip Learning Objectives (already handled)
            if title == "Learning Objectives":
                return match.group(0)

            # Generate reference ID from title
            ref_id = self._generate_ref_id(title)

            # Map # count to h2, h3, etc.
            # Wagtail only allows h2-h6, so shift everything down by 1
            # # becomes h2, ## becomes h3, etc.
            wagtail_level = level + 1
            if wagtail_level > 6:
                wagtail_level = 6  # Cap at h6
            heading_level = f"h{wagtail_level}"

            block = f"""<!-- HEADING -->
reference_id: {ref_id}
level: {heading_level}
---
{title}
<!-- /HEADING -->"""

            return block

        # Match markdown headings: ## Title or ### Title
        pattern = r'^(#{1,6})\s+(.+?)(?:\s*\{[^}]*\})?\s*$'
        body = re.sub(pattern, heading_replacer, body, flags=re.MULTILINE)

        return body

    def _convert_figures(self, body: str) -> str:
        """Convert pandoc-style figures to FIGURE blocks."""

        # Pandoc figure format: ![caption](path){#fig:id width="..."}
        # Also handles: ![caption](<path with spaces>){#fig:id width="..."}
        pattern = r'!\[(.*?)\]\(<?(.*?)>?\)(?:\{([^}]+)\})?'

        def figure_replacer(match):
            caption = match.group(1).strip()
            image_path = match.group(2).strip()
            attributes = match.group(3) or ''

            # Extract reference ID from attributes like {#fig:banana width="8cm"}
            ref_id = ''
            width = 'full'

            if attributes:
                ref_match = re.search(r'#(fig:[^\s}]+)', attributes)
                if ref_match:
                    ref_id = ref_match.group(1)

                width_match = re.search(r'width="(\d+)cm"', attributes)
                if width_match:
                    width_cm = int(width_match.group(1))
                    # Map cm to display width
                    if width_cm < 8:
                        width = 'third'
                    elif width_cm < 12:
                        width = 'half'
                    else:
                        width = 'full'

            # If no ref_id, generate one
            if not ref_id:
                self.figure_counter += 1
                ref_id = f"fig-{self.figure_counter}"

            # Convert image path from ../resources/... to images/...
            new_image_path = self._convert_image_path(image_path)

            # Generate alt text from caption (simplified)
            alt_text = self._caption_to_alt_text(caption)

            block = f"""<!-- FIGURE -->
reference_id: {ref_id}
image_path: {new_image_path}
alt_text: {alt_text}
display_width: {width}
auto_number: true
---
{caption}
<!-- /FIGURE -->"""

            return block

        body = re.sub(pattern, figure_replacer, body)
        return body

    def _convert_equations(self, body: str) -> str:
        """Convert LaTeX equations to EQUATION blocks."""

        # Display equations: $$ ... $$
        def display_eq_replacer(match):
            equation = match.group(1).strip()

            # Generate reference ID (simplified)
            self.equation_counter += 1
            ref_id = f"eq-{self.equation_counter}"

            # Generate spoken version (simplified - user should review)
            spoken = self._equation_to_spoken(equation)

            block = f"""<!-- EQUATION -->
reference_id: {ref_id}
display_type: display
auto_number: true
spoken_version: {spoken}
---
{equation}
<!-- /EQUATION -->"""

            return block

        # Match display equations ($$...$$)
        body = re.sub(r'\$\$(.*?)\$\$', display_eq_replacer, body, flags=re.DOTALL)

        # Note: We keep inline equations as $...$ (they're supported in markdown content)

        return body

    def _convert_tables(self, body: str) -> str:
        """Convert markdown tables to TABLE blocks."""

        # Match markdown tables
        table_pattern = r'(\|.+\|(?:\n\|.+\|)+)'

        def table_replacer(match):
            table_content = match.group(1)

            # Generate reference ID
            self.table_counter += 1
            ref_id = f"table-{self.table_counter}"

            # Try to extract caption from preceding text (if any)
            caption = f"Data table {self.table_counter}"

            block = f"""<!-- TABLE -->
reference_id: {ref_id}
caption: {caption}
auto_number: true
show_row_numbers: false
summary: Table showing experimental data and results
---
{table_content}
<!-- /TABLE -->"""

            return block

        body = re.sub(table_pattern, table_replacer, body, flags=re.MULTILINE)
        return body

    def _convert_code_blocks(self, body: str) -> str:
        """Convert code blocks to CODE blocks."""

        # Match fenced code blocks: ```language\n code \n```
        pattern = r'```(\w+)?\n(.*?)\n```'

        def code_replacer(match):
            language = match.group(1) or 'text'
            code_content = match.group(2)

            block = f"""<!-- CODE -->
language: {language}
caption: Code example
show_line_numbers: false
---
```{language}
{code_content}
```
<!-- /CODE -->"""

            return block

        body = re.sub(pattern, code_replacer, body, flags=re.DOTALL)
        return body

    def _extract_bibliography(self, body: str) -> str:
        """Extract bibliography and append to end."""
        # This is simplified - you may want to add specific bibliography extraction
        # based on your current format

        # Look for "# References" or similar sections
        ref_pattern = r'#\s+(References|Bibliography|Text Books)\s*\n(.*?)(?=\n#\s+|\Z)'

        match = re.search(ref_pattern, body, re.MULTILINE | re.DOTALL)
        if match:
            ref_content = match.group(2)

            # TODO: Parse references and convert to BIBENTRY blocks
            # For now, we'll add a placeholder
            bibliography = "\n\n# Bibliography\n\n"
            bibliography += "<!-- Add BIBENTRY blocks here for your references -->\n"

            # Remove from body and append at end
            body = re.sub(ref_pattern, '', body, flags=re.MULTILINE | re.DOTALL)
            body = body.rstrip() + "\n" + bibliography

        return body

    def _clean_html_comments(self, body: str) -> str:
        """Remove HTML comments that aren't block markers."""
        # Keep our block markers, remove others
        pattern = r'<!--(?!\s*(?:HEADING|EQUATION|FIGURE|TABLE|CODE|SAFETY_WARNING|BIBENTRY|/)).*?-->'
        body = re.sub(pattern, '', body, flags=re.DOTALL)
        return body

    def _generate_ref_id(self, text: str) -> str:
        """Generate a reference ID from text.

        Wagtail has a 50-character limit on reference IDs, so we truncate if needed.
        """
        # Convert to lowercase, replace spaces with hyphens
        ref_id = text.lower()
        ref_id = re.sub(r'[^\w\s-]', '', ref_id)  # Remove special chars
        ref_id = re.sub(r'\s+', '-', ref_id)       # Spaces to hyphens
        ref_id = re.sub(r'-+', '-', ref_id)        # Multiple hyphens to one
        ref_id = ref_id.strip('-')

        # Truncate to 50 characters (Wagtail limit)
        if len(ref_id) > 50:
            ref_id = ref_id[:50].rstrip('-')  # Remove trailing hyphen if truncation creates one

        return ref_id

    def _convert_image_path(self, old_path: str) -> str:
        """Convert image path from ../resources/lab1fig/image.jpg to just the filename.

        The Wagtail importer will handle adding the images/ directory prefix,
        so we only need to provide the bare filename here.
        """
        # Clean up any trailing characters like >
        old_path = old_path.rstrip('>')
        # Extract just the filename (no directory prefix)
        filename = os.path.basename(old_path)
        return filename

    def _caption_to_alt_text(self, caption: str) -> str:
        """Generate alt text from caption (simplified)."""
        # Remove markdown formatting
        alt = re.sub(r'\*\*?(.+?)\*\*?', r'\1', caption)
        alt = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', alt)
        # Truncate if too long
        if len(alt) > 200:
            alt = alt[:197] + "..."
        return alt

    def _equation_to_spoken(self, equation: str) -> str:
        """Generate spoken version of equation (simplified - needs review)."""
        # This is a very basic conversion - users should review and improve
        spoken = equation

        # Simple substitutions
        replacements = {
            r'\\frac\{([^}]+)\}\{([^}]+)\}': r'\1 over \2',
            r'\\times': 'times',
            r'\\cdot': 'times',
            r'\\Delta': 'Delta',
            r'\\sum': 'sum of',
            r'\^2': 'squared',
            r'\^3': 'cubed',
        }

        for pattern, replacement in replacements.items():
            spoken = re.sub(pattern, replacement, spoken)

        # Remove LaTeX commands
        spoken = re.sub(r'\\[a-zA-Z]+', '', spoken)
        spoken = re.sub(r'[{}]', '', spoken)

        return spoken.strip()

    def _setup_image_directory(self):
        """Create images directory and copy image files."""
        # Create images directory next to output file
        self.image_dir = self.output_file.parent / "images"
        self.image_dir.mkdir(exist_ok=True)

        print(f"\n[OK] Created image directory: {self.image_dir}")
        print("  Copy your image files from 'resources/' to this directory")

        # Try to identify source images directory
        # Look for ../resources/lab*fig/ pattern in input file
        with open(self.input_file, 'r', encoding='utf-8') as f:
            content = f.read()

        image_paths = re.findall(r'\.\./resources/([^)]+)', content)

        if image_paths:
            print(f"\n  Found {len(image_paths)} images referenced:")
            for img_path in set(image_paths):
                # Clean up any angle brackets from the path
                clean_path = img_path.strip('<>')
                source = self.input_file.parent.parent / 'resources' / clean_path
                if source.exists():
                    dest = self.image_dir / os.path.basename(clean_path)
                    shutil.copy2(source, dest)
                    print(f"    [OK] Copied: {os.path.basename(clean_path)}")
                else:
                    print(f"    [MISSING] Not found: {clean_path}")

    def _create_zip_package(self):
        """Create Wagtail-ready ZIP package with proper structure."""
        # Determine lab name from output file
        lab_stem = self.output_file.stem.replace('-wagtail', '')

        # Create zip directory structure in wagtail_output/zip/
        zip_dir = self.output_file.parent / 'zip' / lab_stem
        zip_dir.mkdir(parents=True, exist_ok=True)

        # Copy guide.md
        guide_dest = zip_dir / 'guide.md'
        shutil.copy2(self.output_file, guide_dest)

        # Copy images if they exist
        if self.image_dir and self.image_dir.exists():
            # Create images directory in zip structure
            images_dest_dir = zip_dir / 'images'
            images_dest_dir.mkdir(exist_ok=True)

            # Read the converted markdown to find which images are actually used
            with open(self.output_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Find all image_path references in the markdown
            # Note: image_path now contains just the filename (no images/ prefix)
            used_images = re.findall(r'image_path:\s*([^\n]+)', content)

            if used_images:
                print(f"\n[OK] Copying {len(set(used_images))} images to ZIP package:")
                for img_name in set(used_images):
                    source_img = self.image_dir / img_name
                    if source_img.exists():
                        dest_img = images_dest_dir / img_name
                        shutil.copy2(source_img, dest_img)
                        print(f"    - {img_name}")
                    else:
                        print(f"    [MISSING] {img_name}")

        # Create ZIP file
        zip_parent = self.output_file.parent / 'zip'
        self.zip_path = zip_parent / f"{lab_stem}.zip"

        print(f"\n[OK] Creating ZIP package: {self.zip_path}")

        with zipfile.ZipFile(self.zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Add guide.md
            zipf.write(guide_dest, f"{lab_stem}/guide.md")

            # Add images if they exist
            images_dir = zip_dir / 'images'
            if images_dir.exists():
                for img_file in images_dir.iterdir():
                    if img_file.is_file():
                        zipf.write(img_file, f"{lab_stem}/images/{img_file.name}")

        print(f"[OK] ZIP package created: {self.zip_path}")
        print(f"\nPackage structure:")
        print(f"  {lab_stem}.zip")
        print(f"    {lab_stem}/")
        print(f"      - guide.md")
        if images_dir.exists() and any(images_dir.iterdir()):
            print(f"      - images/")
            for img_file in sorted(images_dir.iterdir()):
                if img_file.is_file():
                    print(f"          - {img_file.name}")

        # Clean up temporary directory structure
        shutil.rmtree(zip_dir)


def main():
    parser = argparse.ArgumentParser(
        description='Convert Jekyll/Pandoc lab guides to Wagtail format',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Convert single file
  python convert_to_wagtail.py raw-content/lab1-raw.md

  # Convert with custom output location
  python convert_to_wagtail.py raw-content/lab1-raw.md -o output/lab1.md

  # Convert and create image directory
  python convert_to_wagtail.py raw-content/lab1-raw.md --create-image-dir

  # Convert and create Wagtail-ready ZIP package
  python convert_to_wagtail.py raw-content/lab1-raw.md --create-zip

  # Convert all lab files with ZIP packages
  python convert_to_wagtail.py raw-content/lab*.md --create-zip
        """
    )

    parser.add_argument('input_files', nargs='+', help='Input markdown file(s)')
    parser.add_argument('-o', '--output', help='Output file path (for single file only)')
    parser.add_argument('--create-image-dir', action='store_true',
                       help='Create images directory and copy referenced images')
    parser.add_argument('--create-zip', action='store_true',
                       help='Create Wagtail-ready ZIP package for import (requires --create-image-dir)')

    args = parser.parse_args()

    # Validate arguments
    if args.create_zip and not args.create_image_dir:
        print("Warning: --create-zip requires --create-image-dir, enabling it automatically")
        args.create_image_dir = True

    # Handle multiple files
    if len(args.input_files) > 1 and args.output:
        print("Error: Cannot specify output path when converting multiple files")
        return 1

    for input_file in args.input_files:
        try:
            converter = WagtailMarkdownConverter(
                input_file=input_file,
                output_file=args.output,
                create_image_dir=args.create_image_dir,
                create_zip=args.create_zip
            )
            converter.convert()
            print()
        except Exception as e:
            print(f"Error converting {input_file}: {e}")
            import traceback
            traceback.print_exc()
            return 1

    print("[OK] Conversion complete!")
    return 0


if __name__ == '__main__':
    exit(main())
