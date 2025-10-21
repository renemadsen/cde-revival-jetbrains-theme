# Contributing to CDE Revival Theme

Thank you for your interest in contributing to the CDE Revival Theme! This document provides guidelines and instructions for contributing to the project.

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [How to Contribute](#how-to-contribute)
3. [Development Setup](#development-setup)
4. [Theme Development Guidelines](#theme-development-guidelines)
5. [Testing Your Changes](#testing-your-changes)
6. [Submitting Changes](#submitting-changes)

## Code of Conduct

This project follows a simple code of conduct:
- Be respectful and professional
- Focus on constructive feedback
- Help maintain the authentic CDE/Motif aesthetic

## How to Contribute

There are several ways to contribute:

### Reporting Issues
- Use the GitHub issue tracker
- Provide clear descriptions and screenshots
- Include your IDE version and platform
- Specify which UI element looks incorrect

### Suggesting Enhancements
- Open an issue with the "enhancement" label
- Explain the improvement and why it fits the CDE aesthetic
- Provide examples or mockups if possible

### Improving the Theme
- Fix color inconsistencies
- Add support for more UI elements
- Improve syntax highlighting
- Enhance documentation

## Development Setup

### Prerequisites
- JDK 17 or later
- IntelliJ IDEA (recommended) or any JetBrains IDE
- Git

### Setting Up Your Development Environment

1. **Fork and Clone the Repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/cde-revival-jetbrains-theme.git
   cd cde-revival-jetbrains-theme
   ```

2. **Open in IntelliJ IDEA**
   - Open the project directory in IntelliJ IDEA
   - The IDE will automatically detect the Gradle project
   - Wait for Gradle to sync and download dependencies

3. **Run the Plugin in Development Mode**
   ```bash
   ./gradlew runIde
   ```
   This will launch a new IDE instance with your plugin installed.

## Theme Development Guidelines

### Understanding the Theme Structure

The theme consists of two main files:

1. **`src/main/resources/CDE_Revival_Theme.theme.json`**
   - UI theme definition
   - Colors for buttons, menus, toolbars, etc.
   - Layout properties (borders, arcs, spacing)

2. **`src/main/resources/CDE_Revival_Theme.xml`**
   - Editor color scheme
   - Syntax highlighting colors
   - Console colors
   - Code annotations

### Design Principles

When modifying the theme, follow these principles:

#### 1. Authentic CDE Aesthetic
- Use grey tones as the base (`#AEB2C3`, `#9CA0B1`, `#C7CBD6`)
- Keep blue accents subdued (`#627C9C`)
- Maintain the classic workstation feel

#### 2. Beveled 3D Look
- Use light borders on top/left (`#FFFFFF`)
- Use dark borders on bottom/right (`#5C6574`)
- Create depth with gradients (e.g., `startBackground` → `endBackground`)

#### 3. No Rounded Corners
- Always set `"arc": 0` for sharp, rectangular edges
- This is a key characteristic of the Motif toolkit

#### 4. Subdued Contrast
- Avoid bright, saturated colors
- Keep contrast moderate but readable
- Selection colors should be clearly visible but not jarring

#### 5. Consistency
- Use the color palette defined in `COLORS.md`
- Maintain consistent spacing and borders
- Test changes across different UI elements

### Color Palette Reference

Always refer to `COLORS.md` for the official color palette. When adding new colors:
- They should fit the overall grey/blue scheme
- Test them in both light and dark room conditions
- Document them in `COLORS.md`

### Modifying UI Elements

#### In `CDE_Revival_Theme.theme.json`:

```json
{
  "ComponentName": {
    "background": "#HEX_COLOR",
    "foreground": "#HEX_COLOR",
    "borderColor": "#HEX_COLOR",
    "selectionBackground": "#HEX_COLOR",
    "arc": 0
  }
}
```

Common properties:
- `background` / `foreground`: Basic colors
- `selectionBackground` / `selectionForeground`: Selected state
- `borderColor`: Border color
- `hoverBackground`: Hover state
- `startBackground` / `endBackground`: Gradient
- `arc`: Corner radius (always 0 for this theme)

#### In `CDE_Revival_Theme.xml`:

```xml
<option name="ELEMENT_NAME">
  <value>
    <option name="FOREGROUND" value="HEX_COLOR" />
    <option name="BACKGROUND" value="HEX_COLOR" />
    <option name="FONT_TYPE" value="0|1|2|3" />
    <option name="EFFECT_TYPE" value="0|1|2|3|5" />
    <option name="EFFECT_COLOR" value="HEX_COLOR" />
  </value>
</option>
```

Font types:
- `0`: Normal
- `1`: Bold
- `2`: Italic
- `3`: Bold + Italic

Effect types:
- `0`: None
- `1`: Underline
- `2`: Wave underline
- `3`: Strikethrough
- `5`: Border

## Testing Your Changes

### Visual Testing

1. **Run the Development IDE**
   ```bash
   ./gradlew runIde
   ```

2. **Apply the Theme**
   - Go to `Settings/Preferences` → `Appearance & Behavior` → `Appearance`
   - Select "CDE Revival Theme"
   - Restart the IDE if prompted

3. **Test Different Elements**
   - Open various file types (Java, Python, XML, JSON, etc.)
   - Test menus, toolbars, and dialogs
   - Try different tool windows
   - Test search, find, and replace
   - Check version control UI
   - Test completion popups

4. **Use Test Files**
   - Open files in `test-files/` directory
   - Verify syntax highlighting matches expectations
   - Check that all code elements are readable

### Verification Checklist

Before submitting changes, verify:

- [ ] All UI elements maintain beveled 3D look
- [ ] No rounded corners (arc: 0 everywhere)
- [ ] Colors are from the approved palette
- [ ] Text is readable on all backgrounds
- [ ] Selection colors are clearly visible
- [ ] Borders are consistent
- [ ] Hover states work correctly
- [ ] Syntax highlighting is clear
- [ ] Console colors are distinguishable
- [ ] Theme works in different IDEs (if possible)

### Building the Plugin

```bash
# Clean build
./gradlew clean

# Build the plugin
./gradlew buildPlugin

# The output will be in:
# build/distributions/cde-revival-jetbrains-theme-VERSION.zip
```

## Submitting Changes

### Before You Submit

1. Test your changes thoroughly
2. Update `CHANGELOG.md` if applicable
3. Update `COLORS.md` if you added new colors
4. Add screenshots for visual changes
5. Write clear commit messages

### Pull Request Process

1. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/issue-description
   ```

2. **Make Your Changes**
   - Follow the development guidelines
   - Test thoroughly
   - Update documentation

3. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "Clear description of changes"
   ```
   
   Good commit messages:
   - "Fix button borders in toolbar"
   - "Add support for new IDE 2024.1 components"
   - "Adjust selection color for better contrast"

4. **Push to Your Fork**
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Open a Pull Request**
   - Go to the GitHub repository
   - Click "New Pull Request"
   - Select your branch
   - Fill in the PR template
   - Add screenshots for visual changes
   - Link any related issues

### Pull Request Guidelines

- Keep changes focused and atomic
- One feature/fix per PR
- Include before/after screenshots for UI changes
- Explain why the change is needed
- Reference any related issues

## Style Guidelines

### JSON (theme.json)
```json
{
  "ComponentName": {
    "property": "#HEX_COLOR",
    "anotherProperty": "#HEX_COLOR"
  }
}
```
- Use 2 spaces for indentation
- Alphabetize properties when practical
- Use uppercase hex colors (e.g., `#AEB2C3`)

### XML (color scheme)
```xml
<option name="NAME">
  <value>
    <option name="PROPERTY" value="HEX_COLOR" />
  </value>
</option>
```
- Use 2 spaces for indentation
- Match the existing style
- Use uppercase hex colors without `#` prefix

## Getting Help

- **Questions**: Open a GitHub issue with the "question" label
- **Discussion**: Use GitHub Discussions for general topics
- **Bugs**: Report in GitHub Issues with clear reproduction steps

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## References

- [JetBrains Plugin Development Documentation](https://plugins.jetbrains.com/docs/intellij/welcome.html)
- [Theme Structure Reference](https://plugins.jetbrains.com/docs/intellij/themes-getting-started.html)
- [Color Scheme Reference](https://plugins.jetbrains.com/docs/intellij/color-scheme-management.html)

## Thank You!

Thank you for contributing to the CDE Revival Theme! Your efforts help bring the classic Unix workstation aesthetic to modern development environments.
