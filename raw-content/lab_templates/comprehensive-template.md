---
# YAML Frontmatter - Required metadata for the lab guide
# All fields below are required unless marked optional

lab_number: 1
lab_title: "Template: Comprehensive Lab Guide Example"
duration_hours: 3.0
difficulty: introductory  # Options: introductory, intermediate, advanced
enable_section_numbering: true
keywords: "template, example, reference"  # Optional: comma-separated keywords
---

## Learning Objectives

Write your learning objectives here as a bulleted list. This section supports basic markdown formatting like **bold** and *italics*.

- Students will learn to measure physical quantities with appropriate precision
- Students will understand the concept of **measurement uncertainty**
- Students will be able to analyze data using statistical methods

<!-- HEADING -->
reference_id: introduction
level: h2
---
Introduction
<!-- /HEADING -->

This is a **markdown block** (the default content type). You can use standard markdown formatting:

- Bulleted lists
- **Bold text** and *italic text*
- Links: [Wagtail CMS](https://wagtail.org)

In this lab, we'll explore Newton's Second Law (see \ref{eq-newton-2nd}) and collect data (see \ref{table-measurements}). Our experimental setup is shown in \ref{fig-apparatus}. Inclined plane experiments have a rich history in the study of classical mechanics \cite{atwood1784} and remain fundamental to physics education \cite{young2020}.

**Note:** Use `\ref{reference_id}` to create cross-references to equations, figures, tables, and sections.

<!-- HEADING -->
reference_id: theory
level: h2
---
Theory
<!-- /HEADING -->

<!-- HEADING -->
reference_id: basic-equations
level: h3
---
Example: Basic Equation Block
<!-- /HEADING -->

Here's how to add an equation with a reference ID:

<!-- EQUATION -->
reference_id: eq-newton-2nd
display_type: display
auto_number: true
spoken_version: Force equals mass times acceleration
---
\vec{F} = m\vec{a}
<!-- /EQUATION -->

You can reference this equation in text like this: "According to \ref{eq-newton-2nd}, force equals mass times acceleration."

**Required fields:**
- `display_type` - Use `display` for block equations (centered), `inline` for inline math
- `spoken_version` - Screen reader description (accessibility requirement, min 5 chars)
- `auto_number` - Set to `true` to include in equation numbering, `false` to exclude

**Optional fields:**
- `reference_id` - Unique ID for cross-referencing (required if you want to use `\ref{}`)
- `caption` - Optional caption displayed below equation

<!-- HEADING -->
reference_id: multi-line-equations
level: h3
---
Example: Multi-line Equation
<!-- /HEADING -->

<!-- EQUATION -->
reference_id: eq-kinetic-energy
display_type: display
auto_number: true
spoken_version: Kinetic energy equals one half m v squared, which equals p squared over two m
caption: Kinetic energy in terms of mass and velocity, or momentum
---
\begin{aligned}
KE &= \frac{1}{2}mv^2 \\
   &= \frac{p^2}{2m}
\end{aligned}
<!-- /EQUATION -->

The kinetic energy (\ref{eq-kinetic-energy}) can be expressed in terms of momentum.

<!-- HEADING -->
reference_id: complex-equations
level: h3
---
Example: Complex Equation with Greek Letters
<!-- /HEADING -->

<!-- EQUATION -->
reference_id: eq-wave-function
display_type: display
auto_number: true
spoken_version: Wave function psi of x and t equals A times e to the i times k x minus omega t
---
\Psi(x,t) = A e^{i(kx - \omega t)}
<!-- /EQUATION -->

<!-- HEADING -->
reference_id: safety
level: h2
---
Safety Considerations
<!-- /HEADING -->

Use safety warning blocks to highlight important safety information. There are four severity levels: `info`, `caution`, `warning`, and `danger`.

**Required fields:**
- `severity` - Level: `info`, `caution`, `warning`, or `danger`
- `title` - Warning title/heading

**Optional fields:**
- `icon` - Icon name (e.g., `exclamation-triangle`, `bolt`, `fire`)
- `dismissible` - User can dismiss: `true` or `false` (default: false)

<!-- SAFETY_WARNING -->
severity: caution
title: Eye Protection Required
icon: eye
dismissible: false
---
Wear safety goggles at all times during this experiment.
<!-- /SAFETY_WARNING -->

<!-- SAFETY_WARNING -->
severity: warning
title: Laser Hazard
icon: exclamation-triangle
dismissible: false
---
The laser used in this experiment can cause permanent eye damage. Never look directly into the beam or reflections.
<!-- /SAFETY_WARNING -->

<!-- SAFETY_WARNING -->
severity: danger
title: High Voltage
icon: bolt
dismissible: false
---
High voltage (120V AC)! Do not touch exposed wires while the power supply is on. Ensure all connections are made with power OFF.
<!-- /SAFETY_WARNING -->

<!-- SAFETY_WARNING -->
severity: info
title: General Lab Safety
icon: info-circle
dismissible: true
---
Follow all laboratory safety procedures. Know the location of safety equipment including fire extinguishers, eyewash stations, and emergency exits.
<!-- /SAFETY_WARNING -->

<!-- HEADING -->
reference_id: apparatus
level: h2
---
Experimental Apparatus
<!-- /HEADING -->

<!-- HEADING -->
reference_id: figure-basics
level: h3
---
Example: Figure with Caption
<!-- /HEADING -->

<!-- FIGURE -->
reference_id: fig-apparatus
image_path: images/apparatus-setup.jpg
alt_text: Photo of 2-meter inclined plane with dynamics cart and two photogate sensors mounted on stands
display_width: full
auto_number: true
---
Experimental setup showing the inclined plane, cart, and photogate sensors.
<!-- /FIGURE -->

**Required fields:**
- `image_path` - Relative path to image (use when importing, e.g., `images/filename.jpg`)
- `image_id` - Wagtail image ID (automatically added during export)
- `alt_text` - Accessibility description for screen readers (minimum 10 chars)

**Optional fields:**
- `reference_id` - Unique ID for cross-referencing
- `display_width` - Width: `full`, `half`, or `third` (default: `full`)
- `auto_number` - Include in numbering: `true` or `false` (default: `true`)
- `credit` - Attribution/source credit

**Note:**
- Place your images in the `images/` directory alongside this markdown file
- Use `image_path: images/filename.jpg` (relative path)
- Always include descriptive `alt_text` for accessibility
- The `image_id` field is added automatically during export from Wagtail

As shown in \ref{fig-apparatus}, the cart is positioned at the top of the incline.

<!-- HEADING -->
reference_id: multiple-figures
level: h3
---
Example: Multiple Figures
<!-- /HEADING -->

<!-- FIGURE -->
reference_id: fig-force-diagram
image_path: images/force-diagram.png
alt_text: Free body diagram with weight vector pointing down, normal force perpendicular to incline, and friction vector opposing motion
display_width: half
auto_number: true
credit: Adapted from Serway & Jewett, Physics for Scientists and Engineers
---
Free body diagram showing all forces acting on the cart.
<!-- /FIGURE -->

<!-- FIGURE -->
reference_id: fig-photogate
image_path: images/photogate-detail.jpg
alt_text: Photogate sensor mounted on aluminum track with infrared beam crossing the track
display_width: half
auto_number: true
---
Close-up view of the photogate sensor setup.
<!-- /FIGURE -->

Refer to \ref{fig-force-diagram} for the force analysis and \ref{fig-photogate} for sensor placement details.

<!-- HEADING -->
reference_id: procedure
level: h2
---
Procedure
<!-- /HEADING -->

<!-- HEADING -->
reference_id: ordered-lists
level: h3
---
Example: Ordered Lists
<!-- /HEADING -->

1. Set up the apparatus as shown in \ref{fig-apparatus}
2. Calibrate the photogate sensors according to manufacturer instructions
3. Measure the mass of the cart using the digital balance
4. Record the angle of the incline using the protractor
5. Release the cart from rest and record the time intervals
6. Repeat for 5 different incline angles

<!-- HEADING -->
reference_id: nested-lists
level: h3
---
Example: Nested Lists
<!-- /HEADING -->

1. **Part A: Preliminary Measurements**
   - Measure cart mass (±0.1 g)
   - Measure track length (±0.1 cm)
   - Record room temperature

2. **Part B: Data Collection**
   - Set incline angle to 5°
   - Perform 5 trial runs
   - Record all photogate times in \ref{table-measurements}

3. **Part C: Analysis**
   - Calculate average velocities
   - Compute acceleration using \ref{eq-newton-2nd}
   - Compare with theoretical prediction

<!-- HEADING -->
reference_id: data-collection
level: h2
---
Data Collection
<!-- /HEADING -->

<!-- HEADING -->
reference_id: simple-table
level: h3
---
Example: Simple Data Table
<!-- /HEADING -->

<!-- TABLE -->
reference_id: table-measurements
caption: Time measurements for cart motion at different angles
auto_number: true
show_row_numbers: false
summary: Five trials showing incline angle, time of descent, and calculated velocity for a dynamics cart
---
| Trial | Angle (°) | Time (s) | Velocity (m/s) |
|-------|-----------|----------|----------------|
| 1     | 5.0       | 2.34     | 0.64           |
| 2     | 10.0      | 1.67     | 0.90           |
| 3     | 15.0      | 1.35     | 1.11           |
| 4     | 20.0      | 1.18     | 1.27           |
| 5     | 25.0      | 1.05     | 1.43           |
<!-- /TABLE -->

**Required fields:**
- `caption` - Table caption (minimum 5 characters)

**Optional fields:**
- `reference_id` - Unique ID for cross-referencing
- `auto_number` - Include in numbering: `true` or `false` (default: `true`)
- `show_row_numbers` - Display row numbers: `true` or `false` (default: `false`)
- `summary` - Accessibility summary describing table contents

**Note:** Table syntax uses standard markdown table format. Always include:
- `caption` to describe the table contents
- Header row with column names
- Separator row with dashes
- Data rows with consistent formatting

The data in \ref{table-measurements} shows the relationship between angle and velocity.

<!-- HEADING -->
reference_id: complex-table
level: h3
---
Example: Complex Table with Calculations
<!-- /HEADING -->

<!-- TABLE -->
reference_id: table-calculations
caption: Calculated accelerations and uncertainties for each trial
auto_number: true
show_row_numbers: true
summary: Comparison of measured versus theoretical acceleration values at five different incline angles, including percent error calculations
---
| Angle θ (°) | Measured a (m/s²) | Theoretical a (m/s²) | Percent Error (%) |
|-------------|-------------------|----------------------|-------------------|
| 5.0 ± 0.5   | 0.84 ± 0.05      | 0.85                 | 1.2               |
| 10.0 ± 0.5  | 1.68 ± 0.08      | 1.70                 | 1.4               |
| 15.0 ± 0.5  | 2.49 ± 0.11      | 2.53                 | 1.6               |
| 20.0 ± 0.5  | 3.28 ± 0.15      | 3.35                 | 2.1               |
| 25.0 ± 0.5  | 4.02 ± 0.18      | 4.14                 | 2.9               |
<!-- /TABLE -->

<!-- HEADING -->
reference_id: analysis
level: h2
---
Data Analysis
<!-- /HEADING -->

<!-- HEADING -->
reference_id: python-code
level: h3
---
Example: Python Code Block
<!-- /HEADING -->

<!-- CODE -->
reference_id: code-analysis
language: python
caption: Python script for calculating acceleration from photogate data
show_line_numbers: true
---
import numpy as np
import matplotlib.pyplot as plt

# Data from Table 1
angles = np.array([5, 10, 15, 20, 25])  # degrees
times = np.array([2.34, 1.67, 1.35, 1.18, 1.05])  # seconds
distance = 1.5  # meters

# Calculate velocities
velocities = distance / times

# Calculate accelerations
angles_rad = np.radians(angles)
g = 9.81  # m/s^2
theoretical_accel = g * np.sin(angles_rad)

# Plot results
plt.figure(figsize=(8, 6))
plt.plot(angles, velocities, 'bo-', label='Experimental')
plt.xlabel('Angle (degrees)')
plt.ylabel('Velocity (m/s)')
plt.title('Cart Velocity vs. Incline Angle')
plt.grid(True)
plt.legend()
plt.show()
<!-- /CODE -->

**Required fields:**
- `language` - Programming language for syntax highlighting

**Optional fields:**
- `reference_id` - Unique ID for cross-referencing
- `caption` - Code description/purpose
- `show_line_numbers` - Display line numbers: `true` or `false` (default: `false`)

**Note:** Code blocks support syntax highlighting for many languages:
- `python`, `matlab`, `r`, `cpp`, `java`, `javascript`, `bash`, `sql`, etc.

The analysis code (\ref{code-analysis}) processes the data from \ref{table-measurements}.

<!-- HEADING -->
reference_id: matlab-code
level: h3
---
Example: MATLAB Code Block
<!-- /HEADING -->

<!-- CODE -->
reference_id: code-matlab
language: matlab
caption: MATLAB code for linear regression analysis
show_line_numbers: false
---
% Linear fit to angle vs. acceleration data
angles = [5, 10, 15, 20, 25];
accel = [0.84, 1.68, 2.49, 3.28, 4.02];

% Perform linear regression
p = polyfit(angles, accel, 1);
fit_line = polyval(p, angles);

% Plot with fit
figure;
plot(angles, accel, 'ro', 'MarkerSize', 8);
hold on;
plot(angles, fit_line, 'b-', 'LineWidth', 2);
xlabel('Angle (degrees)');
ylabel('Acceleration (m/s^2)');
legend('Data', 'Linear Fit');
grid on;

% Display fit parameters
fprintf('Slope: %.3f m/s^2/degree\n', p(1));
fprintf('Intercept: %.3f m/s^2\n', p(2));
<!-- /CODE -->

<!-- HEADING -->
reference_id: results
level: h2
---
Results and Discussion
<!-- /HEADING -->

Our experimental results confirm Newton's Second Law (\ref{eq-newton-2nd}) \cite{young2020}. The data in \ref{table-measurements} shows a clear linear relationship between angle and velocity.

Using the photogate timing method \cite{peters2014} and analysis code (\ref{code-analysis}), we calculated the accelerations shown in \ref{table-calculations}. The measured values agree with theory to within 3%, which is excellent agreement given our measurement uncertainties.

The force diagram (\ref{fig-force-diagram}) helps explain why acceleration increases with angle - the component of gravitational force along the incline increases as $mg\sin\theta$. Our experimental values can be compared to the standard gravitational acceleration g = 9.80665 m/s² \cite{nist2023}.

<!-- HEADING -->
reference_id: error-analysis
level: h3
---
Error Analysis
<!-- /HEADING -->

Major sources of uncertainty include:

1. **Photogate timing precision**: ±0.001 s
2. **Distance measurement**: ±0.1 cm
3. **Angle measurement**: ±0.5°
4. **Air resistance** (neglected in theory)
5. **Friction** (assumed constant)

Uncertainty propagation follows standard methods \cite{taylor1997}. The combined uncertainty in acceleration was calculated using quadrature addition of individual error sources.

<!-- HEADING -->
reference_id: conclusions
level: h2
---
Conclusions
<!-- /HEADING -->

1. The experimental data strongly supports \ref{eq-newton-2nd}
2. Percent errors (see \ref{table-calculations}) are all below 3%
3. The linear fit (\ref{code-matlab}) yields a slope consistent with $g\sin\theta$
4. The apparatus (\ref{fig-apparatus}) provides reliable, repeatable measurements

**How to cite references:**

To cite sources in your lab guide, use the `\cite{reference_key}` syntax in your text:
- Single citation: "According to Young and Freedman \cite{young2020}, Newton's laws form the foundation of classical mechanics."
- Multiple citations: "Photogate timing methods have been validated experimentally \cite{peters2014, young2020}."

Citation examples by type:
- **Book**: "The theoretical framework is well-established \cite{young2020}."
- **Journal article**: "Recent experimental work confirms these predictions \cite{peters2014}."
- **Website**: "The accepted value for gravitational acceleration is g = 9.80665 m/s² \cite{nist2023}."
- **Historical reference**: "This experimental method dates back to early dynamics research \cite{atwood1784}."

**Important:** Bibliography entries are added in a separate **"# Bibliography"** section at the end of this document (after all content). See below for examples.

<!-- HEADING -->
reference_id: appendix-a
level: h2
---
Appendix A: Equipment List
<!-- /HEADING -->

<!-- HEADING -->
reference_id: required-equipment
level: h3
---
Required Equipment
<!-- /HEADING -->

- Inclined plane track (2 m length)
- Dynamics cart with low-friction wheels
- Two photogate sensors with timer
- Protractor (±0.5° precision)
- Digital balance (±0.1 g precision)
- Meter stick (±0.1 cm precision)

<!-- HEADING -->
reference_id: optional-equipment
level: h3
---
Optional Equipment
<!-- /HEADING -->

- Computer with data acquisition software
- Motion sensor (ultrasonic or infrared)
- Video camera for motion analysis

<!-- HEADING -->
reference_id: appendix-b
level: h2
---
Appendix B: Derivation of Theoretical Acceleration
<!-- /HEADING -->

Starting from Newton's Second Law (\ref{eq-newton-2nd}):

<!-- EQUATION -->
reference_id: eq-force-components
display_type: display
auto_number: true
spoken_version: Sum of F x equals m a x
---
\sum F_x = ma_x
<!-- /EQUATION -->

For an object on an incline at angle $\theta$:

<!-- EQUATION -->
reference_id: eq-incline-forces
display_type: display
auto_number: true
spoken_version: m g sine theta minus f equals m a
---
mg\sin\theta - f = ma
<!-- /EQUATION -->

Assuming negligible friction ($f \approx 0$):

<!-- EQUATION -->
reference_id: eq-final-accel
display_type: display
auto_number: true
spoken_version: Acceleration equals g sine theta
---
a = g\sin\theta
<!-- /EQUATION -->

This is the theoretical prediction we test in this experiment.

---

## TEMPLATE USAGE NOTES

### Getting Started
1. Copy this template to create a new lab guide
2. Update the frontmatter with your lab details
3. Replace example content with your own
4. Save images to `images/` directory
5. Validate before importing to Wagtail

### Block Type Summary

| Block Type      | Use For                          | Required Fields                           |
|-----------------|----------------------------------|-------------------------------------------|
| HEADING         | Major sections                   | level                                     |
| MARKDOWN        | Text, lists, basic formatting    | (none - default)                          |
| EQUATION        | Mathematical equations           | display_type, spoken_version, auto_number |
| FIGURE          | Images, diagrams, photos         | image_path/image_id, alt_text             |
| TABLE           | Data tables                      | caption                                   |
| CODE            | Code examples, scripts           | language                                  |
| SAFETY_WARNING  | Safety information               | severity, title                           |
| BIBENTRY        | Bibliography entries             | reference_key, authors, title, year           |

### Cross-Referencing Quick Guide

- **Equations**: `\ref{eq-newton-2nd}` → "Equation 1"
- **Figures**: `\ref{fig-apparatus}` → "Figure 1"
- **Tables**: `\ref{table-measurements}` → "Table 1"
- **Sections**: `\ref{introduction}` → "Section 1"
- **Citations**: `\cite{young2020}` → "[1]"
- **Multiple citations**: `\cite{halliday2013, serway2018}` → "[2, 3]"

### Best Practices

1. **Use descriptive reference IDs**: `eq-newton-2nd` not `eq1`
2. **Always add captions** to figures and tables
3. **Include alt text** for all images (accessibility - minimum 10 characters)
4. **Test cross-references** before importing
5. **Keep image files** in the `images/` subdirectory
6. **Use consistent naming**: lowercase with hyphens
7. **Validate markdown** before importing to catch errors early

### Common Mistakes to Avoid

- ❌ Forgetting closing block markers (e.g., `<!-- /EQUATION -->`)
- ❌ Missing required frontmatter fields
- ❌ Incorrect image paths (must be relative to markdown file)
- ❌ Using spaces in reference IDs (use hyphens or underscores)
- ❌ Forgetting to define bibliography entries for citations
- ❌ Inconsistent heading levels (don't skip from h2 to h4)
- ❌ Using wrong level format: use `h2`, `h3`, not `2`, `3`
- ❌ Missing heading text in HEADING block content section (after `---`)
- ❌ Missing `title` field in SAFETY_WARNING blocks
- ❌ Forgetting `---` separator between metadata and content (except BIBENTRY blocks)
- ❌ Using `author` instead of `authors` (plural) in BIBENTRY blocks
- ❌ Adding `---` or content section to BIBENTRY blocks (they are metadata-only)

### Need Help?

- **Validation**: Use the "Validate Markdown" button in Wagtail admin
- **Documentation**: See `docs/MARKDOWN_IMPORT_EXPORT_EXTENSIBILITY.md`
- **Field Reference**: See `FIELD_REFERENCE.md` for complete field lists
- **Examples**: This template demonstrates all available features

---

# Bibliography

**IMPORTANT:** This section is SEPARATE from the main content. Bibliography entries are stored in a dedicated `bibliography` field in the Wagtail admin, not in the main content StreamField.

When you **export** a lab guide, bibliography entries appear in this "# Bibliography" section at the end.
When you **import** a lab guide, BIBENTRY blocks are extracted and placed in the separate bibliography field.

**Example Bibliography Entries:**

<!-- BIBENTRY -->
reference_key: young2020
authors: Young, H. D. and Freedman, R. A.
title: University Physics with Modern Physics
publication: Pearson, 15th Edition
year: 2020
<!-- /BIBENTRY -->

<!-- BIBENTRY -->
reference_key: atwood1784
authors: Atwood, G.
title: A Treatise on the Rectilinear Motion and Rotation of Bodies
publication: Cambridge University Press
year: 1784
notes: Historical work on dynamics and inclined plane experiments
<!-- /BIBENTRY -->

<!-- BIBENTRY -->
reference_key: peters2014
authors: Peters, M. J. and Smith, R. L.
title: Experimental verification of acceleration on inclined planes using photogate timing
publication: American Journal of Physics, 82(5)
year: 2014
pages: 456-463
doi: 10.1119/1.4868901
<!-- /BIBENTRY -->

<!-- BIBENTRY -->
reference_key: nist2023
authors: National Institute of Standards and Technology
title: CODATA Value: standard acceleration of gravity
url: https://physics.nist.gov/cgi-bin/cuu/Value?gn
access_date: 2024-01-15
year: 2023
<!-- /BIBENTRY -->

<!-- BIBENTRY -->
reference_key: taylor1997
authors: Taylor, J. R.
title: An Introduction to Error Analysis
publication: University Science Books, 2nd Edition
year: 1997
<!-- /BIBENTRY -->

**BIBENTRY Field Reference:**

**Required fields:**
- `reference_key` - Unique identifier for citations
- `authors` - Author(s) name(s) (use "and" to separate multiple authors)
- `title` - Title of work
- `year` - Publication year

**Optional fields:**
- `publication` - Journal, book, or conference name (e.g., "Physical Review, 42(3)" or "Pearson, 15th Edition")
- `pages` - Page numbers (e.g., "234-256" or "pp. 15-20")
- `url` - Web address for online sources
- `doi` - Digital Object Identifier (e.g., "10.1103/PhysRev.47.777")
- `access_date` - Date accessed for online sources (YYYY-MM-DD format)
- `notes` - Additional notes about the reference

**Note:** BIBENTRY blocks are metadata-only (no `---` separator, no content section).
