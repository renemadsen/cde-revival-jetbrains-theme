# CDE Revival Theme for JetBrains IDEs

A JetBrains IDE theme plugin that recreates the classic CDE (Common Desktop Environment) / Motif aesthetic from the HP-UX / Solaris / AIX era.

## Theme Features

This theme brings back the nostalgic look of the CDE desktop with:

- **Classic Grey Tones**: Authentic grey color palette (#AEB2C3, #9CA0B1) reminiscent of CDE's signature look
- **Beveled 3D Effects**: Strong light/dark bevel edges that give UI elements depth and dimension
- **Blue and Steel Accents**: Subdued blue tones (#627C9C) for selections and focus indicators
- **Subdued Selections**: Lower contrast selections that feel authentic to the era
- **Retro Console Colors**: Period-appropriate terminal color scheme
- **No Rounded Corners**: Everything uses sharp, square corners (arc: 0)

*Inspired by CDE. No logos, no official affiliation.*

## Installation

### From JetBrains Marketplace (Recommended)

1. Open your JetBrains IDE (IntelliJ IDEA, PyCharm, WebStorm, etc.)
2. Go to `Settings/Preferences` → `Plugins`
3. Search for "CDE Revival Theme"
4. Click `Install`
5. Restart your IDE
6. Go to `Settings/Preferences` → `Appearance & Behavior` → `Appearance`
7. Select "CDE Revival Theme" from the Theme dropdown

### Manual Installation

1. Download the plugin `.jar` file from the [releases page](https://github.com/renemadsen/cde-revival-jetbrains-theme/releases)
2. Open your JetBrains IDE
3. Go to `Settings/Preferences` → `Plugins`
4. Click the gear icon (⚙️) → `Install Plugin from Disk...`
5. Select the downloaded `.jar` file
6. Restart your IDE
7. Go to `Settings/Preferences` → `Appearance & Behavior` → `Appearance`
8. Select "CDE Revival Theme" from the Theme dropdown

## Building from Source

### Prerequisites

- JDK 17 or later
- Gradle 8.5 or later (or use the included wrapper)

### Build Instructions

```bash
# Clone the repository
git clone https://github.com/renemadsen/cde-revival-jetbrains-theme.git
cd cde-revival-jetbrains-theme

# Build the plugin
./gradlew buildPlugin

# The plugin will be available at:
# build/distributions/cde-revival-jetbrains-theme-*.zip
```

### Development

```bash
# Run IDE with the plugin for testing
./gradlew runIde

# Verify plugin structure
./gradlew verifyPlugin
```

## Color Palette

The theme uses these key colors from the CDE era:

| Element | Color | Hex |
|---------|-------|-----|
| Main Background | Medium Grey | `#AEB2C3` |
| Editor Background | Light Grey | `#C7CBD6` |
| Dark Grey (Borders) | Steel Grey | `#5C6574` |
| Selection | Subdued Blue | `#627C9C` |
| Inactive Selection | Grey Blue | `#8E9AAB` |
| Button/Panel | Grey Blue | `#9CA0B1` |
| Keywords | Dark Steel | `#3C4C5C` |
| Strings | Muted Green | `#2C6C3C` |
| Comments | Grey | `#5C6574` |

## Compatibility

- **Platform**: IntelliJ Platform 2023.2+
- **IDEs**: All JetBrains IDEs (IntelliJ IDEA, PyCharm, WebStorm, PhpStorm, CLion, GoLand, RubyMine, etc.)
- **Supported Versions**: 232.* through 242.*

## Plugin Information

- **Plugin ID**: `com.renemadsen.cderevival`
- **Display Name**: CDE Revival Theme
- **Version**: 1.0.0
- **License**: MIT
- **Author**: René Schultz Madsen
- **Repository**: https://github.com/renemadsen/cde-revival-jetbrains-theme

## Screenshots

(Screenshots will be added after plugin is built and tested)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

This theme is inspired by the classic CDE (Common Desktop Environment) that was prevalent on Unix workstations in the 1990s and early 2000s. It aims to bring that nostalgic aesthetic to modern development environments.

**Note**: This is an independent project with no official affiliation to the original CDE or any Unix vendor.