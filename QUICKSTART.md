# Quick Start Guide

This guide will help you quickly get started with the CDE Revival Theme for JetBrains IDEs.

## Installation

### Option 1: From JetBrains Marketplace (Recommended - When Published)

1. Open your JetBrains IDE
2. Go to **Settings/Preferences** (Ctrl+Alt+S / Cmd+,)
3. Navigate to **Plugins**
4. Search for "CDE Revival Theme"
5. Click **Install**
6. Click **OK** and restart your IDE

### Option 2: Manual Installation

1. Download the latest release from the [Releases page](https://github.com/renemadsen/cde-revival-jetbrains-theme/releases)
2. Open your JetBrains IDE
3. Go to **Settings/Preferences** → **Plugins**
4. Click the gear icon (⚙️) and select **Install Plugin from Disk...**
5. Select the downloaded `.zip` file
6. Click **OK** and restart your IDE

### Option 3: Build from Source

```bash
# Clone the repository
git clone https://github.com/renemadsen/cde-revival-jetbrains-theme.git
cd cde-revival-jetbrains-theme

# Build the plugin
./gradlew buildPlugin

# The plugin will be in: build/distributions/
```

Then follow Option 2 steps to install the built plugin.

## Activating the Theme

1. Go to **Settings/Preferences** → **Appearance & Behavior** → **Appearance**
2. In the **Theme** dropdown, select **CDE Revival Theme**
3. Click **OK**
4. The theme will be applied immediately (restart may be required for full effect)

## What to Expect

After applying the theme, you'll see:

- **Grey color palette** reminiscent of classic Unix workstations
- **Beveled 3D buttons and panels** with authentic light/dark edges
- **Sharp, rectangular corners** (no rounded edges)
- **Blue accents** for selections and focus (#627C9C)
- **Subdued colors** that are easy on the eyes for long coding sessions
- **Classic console colors** in terminal windows

## Customization

### Adjusting Font Size

The theme doesn't change font sizes. To adjust:

1. Go to **Settings/Preferences** → **Editor** → **Font**
2. Adjust **Size** to your preference
3. Recommended: 12-14pt for modern displays

### Using with Custom Color Schemes

The theme includes a matched editor color scheme. However, you can use your own:

1. Go to **Settings/Preferences** → **Editor** → **Color Scheme**
2. Select a different scheme
3. Note: Other schemes may not match the CDE aesthetic

### Combining with Other Plugins

The CDE Revival Theme works well with:
- **Material Theme UI** (disable, as it conflicts)
- **Rainbow Brackets** (compatible, but may clash visually)
- **Custom Syntax Highlighter** (may override theme colors)

## Troubleshooting

### Theme Not Appearing in Dropdown

1. Make sure you restarted the IDE after installation
2. Check **Settings** → **Plugins** to verify the plugin is enabled
3. Try **Help** → **Find Action** → search "Invalidate Caches" and restart

### Colors Look Wrong

1. Ensure you're using the latest version
2. Check if other theme plugins are interfering
3. Try resetting to default: **Settings** → **Appearance & Behavior** → **Appearance** → **Reset**

### Build Failed

If building from source fails:

1. Ensure you have JDK 17 or later installed
2. Check your internet connection (Gradle needs to download dependencies)
3. Try: `./gradlew clean build`

### Can't Install Plugin

- Make sure you're using a compatible IDE version (2023.2 or later)
- Check that you downloaded the correct `.zip` file
- Verify the file isn't corrupted (re-download if necessary)

## Tips for Best Experience

1. **Use a good monitor**: The theme looks best on displays with good color accuracy
2. **Adjust brightness**: The grey tones work well in moderate lighting
3. **Try the test files**: Open files in `test-files/` to see syntax highlighting
4. **Customize sparingly**: The theme is designed as a cohesive whole
5. **Report issues**: If something looks off, [open an issue](https://github.com/renemadsen/cde-revival-jetbrains-theme/issues)

## Keyboard Shortcuts Reference

Useful shortcuts for theme-related settings:

- **Settings**: Ctrl+Alt+S (Windows/Linux) or Cmd+, (macOS)
- **Quick Switch Scheme**: Ctrl+` (Windows/Linux) or Cmd+` (macOS)
- **Editor Colors**: Settings → Editor → Color Scheme
- **Appearance**: Settings → Appearance & Behavior → Appearance

## Getting Help

- **Issues**: [GitHub Issues](https://github.com/renemadsen/cde-revival-jetbrains-theme/issues)
- **Documentation**: See [README.md](README.md) and [COLORS.md](COLORS.md)
- **Contributing**: See [CONTRIBUTING.md](CONTRIBUTING.md)

## Uninstalling

To remove the theme:

1. Go to **Settings/Preferences** → **Plugins**
2. Find "CDE Revival Theme"
3. Click the dropdown next to the plugin
4. Select **Uninstall**
5. Restart your IDE
6. Select a different theme in **Settings** → **Appearance & Behavior** → **Appearance**

## Next Steps

- Explore the [color reference](COLORS.md)
- Read about [contributing](CONTRIBUTING.md)
- Check the [changelog](CHANGELOG.md) for updates
- Star the repo on GitHub!

---

**Enjoy your nostalgic coding experience with the CDE Revival Theme!**

*Inspired by the classic CDE desktop environment from HP-UX, Solaris, and AIX workstations.*
