# Lab Guide Conversion Workflow

## Current vs New System

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         CURRENT SYSTEM (Jekyll)                          │
└─────────────────────────────────────────────────────────────────────────┘

    raw-content/lab1-raw.md              resources/lab1fig/*.jpg
            ↓                                      ↓
    [Manually edit markdown]              [Manually manage images]
            ↓                                      ↓
    raw-content/mdtohtml.sh              [Images in resources/]
            ↓                                      ↓
        [pandoc]  ──────────────────────→  _includes/lab1.html
            ↓
    [Jekyll build]
            ↓
    ┌─────────────────┐
    │  Static Website │
    └─────────────────┘

    Limitations:
    ❌ Hard to collaborate (HTML output)
    ❌ No version control friendly format for final output
    ❌ Difficult to update content
    ❌ No structured content for reuse
    ❌ Limited search/organization


┌─────────────────────────────────────────────────────────────────────────┐
│                      NEW SYSTEM (Django/Wagtail)                         │
└─────────────────────────────────────────────────────────────────────────┘

    raw-content/lab1-raw.md              resources/lab1fig/*.jpg
            ↓                                      ↓
    [convert_to_wagtail.py]  ←───────────  [Auto-copy images]
            ↓                                      ↓
    wagtail_output/lab1-wagtail.md        wagtail_output/images/
            ↓                                      ↓
    [Manual review & enhancement]         [Organize per lab]
            ↓                                      ↓
    lab1/guide.md                         lab1/images/*.jpg
            ↓                                      ↓
         ┌──────────────────────────────────────┐
         │  Wagtail CMS Import (Validate first) │
         └──────────────────────────────────────┘
                        ↓
         ┌──────────────────────────────┐
         │  Structured Content in CMS   │
         │  - HEADING blocks            │
         │  - FIGURE blocks             │
         │  - EQUATION blocks           │
         │  - TABLE blocks              │
         │  - CODE blocks               │
         └──────────────────────────────┘
                        ↓
         ┌──────────────────────────────┐
         │    Web Portal (Django)       │
         └──────────────────────────────┘

    Benefits:
    ✅ Version control friendly (markdown)
    ✅ Easy collaboration
    ✅ Structured, reusable content
    ✅ Modern CMS features
    ✅ Better search & organization
    ✅ Mobile-friendly
    ✅ Accessibility features
```

## Detailed Conversion Process

```
┌───────────────────────────────────────────────────────────────────────┐
│                        STEP 1: AUTOMATED CONVERSION                    │
└───────────────────────────────────────────────────────────────────────┘

INPUT: lab1-raw.md
─────────────────────────────────────────────────────────────────────────
---
title: "Lab 1 - Electronic Measurements"
author: [Department of Physics]
---

# Goals
Today you will learn...

![Banana cables](../resources/lab1fig/banana.jpg){#fig:banana width="8cm"}

$$V = IR$$

| Data | Value |
|------|-------|
| V    | 5V    |
─────────────────────────────────────────────────────────────────────────

                    ↓  [convert_to_wagtail.py]

OUTPUT: lab1-wagtail.md
─────────────────────────────────────────────────────────────────────────
---
lab_number: 1
lab_title: "Lab 1 - Electronic Measurements"
duration_hours: 3.0
difficulty: intermediate
enable_section_numbering: true
keywords: "lab, electronic, measurements"
---

## Learning Objectives

Students will:

Today you will learn...

<!-- HEADING -->
reference_id: goals
level: h1
---
Goals
<!-- /HEADING -->

<!-- FIGURE -->
reference_id: fig:banana
image_path: images/banana.jpg
alt_text: Banana cables
display_width: half
auto_number: true
---
Banana cables
<!-- /FIGURE -->

<!-- EQUATION -->
reference_id: eq-1
display_type: display
auto_number: true
spoken_version: V equals I R
---
V = IR
<!-- /EQUATION -->

<!-- TABLE -->
reference_id: table-1
caption: Data table 1
auto_number: true
---
| Data | Value |
|------|-------|
| V    | 5V    |
<!-- /TABLE -->
─────────────────────────────────────────────────────────────────────────


┌───────────────────────────────────────────────────────────────────────┐
│                      STEP 2: MANUAL ENHANCEMENT                        │
└───────────────────────────────────────────────────────────────────────┘

Review and improve:

1. Learning Objectives
   ✏️ Make student-focused
   ✏️ Use action verbs

2. Equation Spoken Versions
   BEFORE: "V equals I R"
   AFTER:  "Voltage equals current times resistance"

3. Figure Alt Text
   BEFORE: "Banana cables"
   AFTER:  "Photo of red and black banana cables with metal connector
            tips for power supply and multimeter connections"

4. Table Captions
   BEFORE: "Data table 1"
   AFTER:  "Voltage measurements across test resistor for five trials"

5. Bibliography
   Add BIBENTRY blocks for any citations


┌───────────────────────────────────────────────────────────────────────┐
│                    STEP 3: ORGANIZE FOR IMPORT                         │
└───────────────────────────────────────────────────────────────────────┘

Create directory structure:

lab1/
├── guide.md              ← Copy from wagtail_output/lab1-wagtail.md
└── images/
    ├── banana.jpg        ← Copy relevant images
    ├── scope-guide.png
    └── coax.png


┌───────────────────────────────────────────────────────────────────────┐
│                      STEP 4: IMPORT TO WAGTAIL                         │
└───────────────────────────────────────────────────────────────────────┘

In Wagtail Admin:

1. Click "Import Markdown"
2. Click "Validate Markdown" (fix any errors)
3. Upload guide.md
4. Upload images/ folder (or ZIP together)
5. Review imported content
6. Adjust formatting if needed
7. Save and publish

Result: ✅ Lab guide live on new platform!
```

## Image Handling Flow

```
OLD IMAGE PATHS:
../resources/lab1fig/banana.jpg
../resources/lab1fig/scope-guide.png
../resources/lab2fig/circuit.jpg

        ↓  [Script processes]

CONVERSION:
- Extracts filename: banana.jpg, scope-guide.png
- Updates path: images/banana.jpg
- Copies file: resources/lab1fig/banana.jpg → wagtail_output/images/banana.jpg

NEW IMAGE PATHS:
images/banana.jpg
images/scope-guide.png
images/circuit.jpg

        ↓  [Manual organization for import]

IMPORT STRUCTURE:
lab1/images/banana.jpg
lab1/images/scope-guide.png
lab2/images/circuit.jpg
```

## Block Type Transformation Map

```
┌─────────────────────┬──────────────────────────────────────────────┐
│   MARKDOWN ELEMENT  │         WAGTAIL BLOCK TYPE                   │
├─────────────────────┼──────────────────────────────────────────────┤
│ # Heading           │ <!-- HEADING -->                             │
│                     │ reference_id: id                             │
│                     │ level: h1                                    │
│                     │ ---                                          │
│                     │ Heading                                      │
│                     │ <!-- /HEADING -->                            │
├─────────────────────┼──────────────────────────────────────────────┤
│ ![cap](img){#id}    │ <!-- FIGURE -->                              │
│                     │ reference_id: id                             │
│                     │ image_path: images/img.jpg                   │
│                     │ alt_text: description                        │
│                     │ ---                                          │
│                     │ Caption                                      │
│                     │ <!-- /FIGURE -->                             │
├─────────────────────┼──────────────────────────────────────────────┤
│ $$equation$$        │ <!-- EQUATION -->                            │
│                     │ reference_id: eq-1                           │
│                     │ display_type: display                        │
│                     │ spoken_version: description                  │
│                     │ ---                                          │
│                     │ equation                                     │
│                     │ <!-- /EQUATION -->                           │
├─────────────────────┼──────────────────────────────────────────────┤
│ | table |           │ <!-- TABLE -->                               │
│                     │ caption: description                         │
│                     │ ---                                          │
│                     │ | table |                                    │
│                     │ <!-- /TABLE -->                              │
├─────────────────────┼──────────────────────────────────────────────┤
│ ```python           │ <!-- CODE -->                                │
│ code                │ language: python                             │
│ ```                 │ ---                                          │
│                     │ ```python                                    │
│                     │ code                                         │
│                     │ ```                                          │
│                     │ <!-- /CODE -->                               │
└─────────────────────┴──────────────────────────────────────────────┘
```

## Timeline Estimate

```
┌─────────────────────────────────────────────────────────────────┐
│                   FIRST LAB (Learning)                          │
└─────────────────────────────────────────────────────────────────┘

⏱️ Run conversion script           [  5 min ]
⏱️ Review converted file           [ 30 min ]
⏱️ Enhance accessibility features  [ 30 min ]
⏱️ Add bibliography                [ 15 min ]
⏱️ Organize for import             [ 10 min ]
⏱️ Import to Wagtail              [ 15 min ]
⏱️ Review and adjust               [ 15 min ]
                                   ─────────
                         TOTAL:    [120 min / 2 hours]


┌─────────────────────────────────────────────────────────────────┐
│              SUBSEQUENT LABS (Optimized)                        │
└─────────────────────────────────────────────────────────────────┘

⏱️ Run conversion (batch)          [  1 min for all ]
⏱️ Review one lab                  [ 20 min ]
⏱️ Enhance features                [ 20 min ]
⏱️ Organize for import             [  5 min ]
⏱️ Import to Wagtail              [ 10 min ]
                                   ─────────
                   PER LAB:        [ 55 min ]

FOR ALL 10 LABS:  ~10 hours total (1-2 work days)
```

## File Organization Progression

```
BEFORE CONVERSION:
PHYS-3330/
├── raw-content/
│   ├── lab1-raw.md
│   ├── lab2-raw.md
│   └── mdtohtml.sh
└── resources/
    ├── lab1fig/
    │   ├── banana.jpg
    │   └── scope.png
    └── lab2fig/
        └── circuit.jpg

        ↓  [Run conversion script]

AFTER CONVERSION:
PHYS-3330/
├── raw-content/
│   ├── lab1-raw.md              (preserved)
│   └── wagtail_output/
│       ├── lab1-wagtail.md      (generated)
│       ├── lab2-wagtail.md
│       └── images/
│           ├── banana.jpg       (copied)
│           ├── scope.png
│           └── circuit.jpg
└── resources/                   (preserved)

        ↓  [Manual organization]

READY FOR IMPORT:
import-ready/
├── lab1/
│   ├── guide.md
│   └── images/
│       ├── banana.jpg
│       └── scope.png
└── lab2/
    ├── guide.md
    └── images/
        └── circuit.jpg

        ↓  [Import to Wagtail]

IN WAGTAIL CMS:
✅ Lab 1 - Electronic Measurements
✅ Lab 2 - ...
✅ Lab 3 - ...
```

## Getting Started Checklist

```
□ 1. Review CONVERSION_README.md for overview
□ 2. Check Python version: python --version (need 3.7+)
□ 3. Read QUICK_START.md for fast track
□ 4. Run conversion on one lab first
      python convert_to_wagtail.py raw-content/lab1-raw.md --create-image-dir
□ 5. Review output: raw-content/wagtail_output/lab1-wagtail.md
□ 6. Manually enhance the converted content
□ 7. Test import in Wagtail with lab1
□ 8. Refine workflow based on experience
□ 9. Convert all labs: ./convert_all_labs.sh
□ 10. Process remaining labs systematically
```

---

For detailed instructions, see:
- **Quick start:** [QUICK_START.md](QUICK_START.md)
- **Comprehensive guide:** [CONVERSION_GUIDE.md](CONVERSION_GUIDE.md)
- **Summary:** [SUMMARY.md](SUMMARY.md)
