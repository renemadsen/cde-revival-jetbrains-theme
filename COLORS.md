# CDE Revival Theme - Color Reference

This document provides a comprehensive reference of all colors used in the CDE Revival Theme, organized by function.

## Base Colors

### Background Colors
| Color Name | Hex Code | RGB | Usage |
|------------|----------|-----|-------|
| Editor Background | `#C7CBD6` | rgb(199, 203, 214) | Main editor area, text fields |
| Main Background | `#AEB2C3` | rgb(174, 178, 195) | Toolbars, menu bars, main panels |
| Secondary Background | `#9CA0B1` | rgb(156, 160, 177) | Tool windows, tabs background |
| Hover Background | `#B9BDC9` | rgb(185, 189, 201) | Hover states for lists/trees |

### Foreground Colors
| Color Name | Hex Code | RGB | Usage |
|------------|----------|-----|-------|
| Primary Text | `#000000` | rgb(0, 0, 0) | Main text, labels |
| Disabled Text | `#6B6F7A` | rgb(107, 111, 122) | Disabled elements |
| Info Text | `#3C4C5C` | rgb(60, 76, 92) | Hints, secondary information |

### Selection Colors
| Color Name | Hex Code | RGB | Usage |
|------------|----------|-----|-------|
| Active Selection | `#627C9C` | rgb(98, 124, 156) | Selected items, focused selections |
| Selection Text | `#FFFFFF` | rgb(255, 255, 255) | Text on active selections |
| Inactive Selection | `#8E9AAB` | rgb(142, 154, 171) | Unfocused selections |
| Inactive Selection Text | `#000000` | rgb(0, 0, 0) | Text on inactive selections |

### Border Colors
| Color Name | Hex Code | RGB | Usage |
|------------|----------|-----|-------|
| Primary Border | `#5C6574` | rgb(92, 101, 116) | Main borders, separators |
| Light Border | `#FFFFFF` | rgb(255, 255, 255) | Top/left beveled edges |
| Focus Border | `#627C9C` | rgb(98, 124, 156) | Focused element borders |

## Editor Colors

### Syntax Highlighting
| Element | Hex Code | RGB | Style |
|---------|----------|-----|-------|
| Keywords | `#3C4C5C` | rgb(60, 76, 92) | Bold |
| Strings | `#2C6C3C` | rgb(44, 108, 60) | Normal |
| Numbers | `#5C3C7C` | rgb(92, 60, 124) | Normal |
| Comments | `#5C6574` | rgb(92, 101, 116) | Italic |
| Functions | `#3C5C7C` | rgb(60, 92, 124) | Bold (declarations) |
| Classes | `#3C5C7C` | rgb(60, 92, 124) | Normal |
| Constants | `#5C3C7C` | rgb(92, 60, 124) | Bold |

### Editor UI Elements
| Element | Hex Code | RGB | Usage |
|---------|----------|-----|-------|
| Caret | `#000000` | rgb(0, 0, 0) | Cursor |
| Current Line | `#B9BDC9` | rgb(185, 189, 201) | Caret row background |
| Line Numbers | `#5C6574` | rgb(92, 101, 116) | Gutter line numbers |
| Gutter Background | `#AEB2C3` | rgb(174, 178, 195) | Editor gutter |
| Selection | `#627C9C` | rgb(98, 124, 156) | Selected text background |
| Search Result | `#9CAC5C` | rgb(156, 172, 92) | Find/replace highlights |

### Console Colors
| ANSI Color | Hex Code | RGB |
|------------|----------|-----|
| Black | `#000000` | rgb(0, 0, 0) |
| Red | `#8B0000` | rgb(139, 0, 0) |
| Green | `#2C6C3C` | rgb(44, 108, 60) |
| Yellow | `#8B7000` | rgb(139, 112, 0) |
| Blue | `#3C5C7C` | rgb(60, 92, 124) |
| Magenta | `#7C3C7C` | rgb(124, 60, 124) |
| Cyan | `#3C7C7C` | rgb(60, 124, 124) |
| White/Grey | `#8E9AAB` | rgb(142, 154, 171) |
| Dark Grey | `#5C6574` | rgb(92, 101, 116) |

## UI Component Colors

### Buttons
| State | Background | Border Start | Border End |
|-------|-----------|--------------|------------|
| Normal | `#AEB2C3` → `#9CA0B1` | `#FFFFFF` | `#5C6574` |
| Hover | `#B9BDC9` | `#5C6574` | `#5C6574` |
| Pressed | `#8E9AAB` | `#5C6574` | `#5C6574` |
| Focused Border | - | - | `#627C9C` |

### Progress Bar
| State | Hex Code | RGB |
|-------|----------|-----|
| Track | `#9CA0B1` | rgb(156, 160, 177) |
| Progress | `#627C9C` | rgb(98, 124, 156) |
| Success | `#2C6C3C` → `#4C8C5C` | Green gradient |
| Error | `#8B0000` → `#AB2020` | Red gradient |

### Status Colors
| Status | Hex Code | RGB | Usage |
|--------|----------|-----|-------|
| Error | `#8B0000` | rgb(139, 0, 0) | Error messages, underlines |
| Warning | `#8B7000` | rgb(139, 112, 0) | Warnings, typos |
| Info | `#3C5C7C` | rgb(60, 92, 124) | Information messages |
| Success | `#2C6C3C` | rgb(44, 108, 60) | Success indicators |

### Version Control
| Element | Hex Code | RGB |
|---------|----------|-----|
| Current Branch | `#8EA5BB` | rgb(142, 165, 187) |
| HEAD Icon | `#627C9C` | rgb(98, 124, 156) |
| Local Branch | `#2C6C3C` | rgb(44, 108, 60) |
| Remote Branch | `#8B5A00` | rgb(139, 90, 0) |
| Tag | `#5C3C7C` | rgb(92, 60, 124) |

### File Colors (Optional Project View Coloring)
| Color | Hex Code | RGB |
|-------|----------|-----|
| Blue | `#8EA5BB` | rgb(142, 165, 187) |
| Green | `#8EBB9E` | rgb(142, 187, 158) |
| Orange | `#BBAA8E` | rgb(187, 170, 142) |
| Yellow | `#BBBB8E` | rgb(187, 187, 142) |
| Rose | `#BB8E9E` | rgb(187, 142, 158) |
| Violet | `#9E8EBB` | rgb(158, 142, 187) |

## Design Principles

### Beveled 3D Effect
The theme creates depth using a combination of:
- Light borders (`#FFFFFF`) on top and left edges
- Dark borders (`#5C6574`) on bottom and right edges
- Gradient backgrounds (e.g., `#AEB2C3` → `#9CA0B1`)

### No Rounded Corners
All UI elements use `arc: 0`, maintaining sharp, rectangular corners consistent with the original CDE aesthetic.

### Subdued Contrast
Colors are chosen to be clearly distinguishable but not jarring:
- Medium grey base prevents eye strain
- Blue accents are muted rather than bright
- Selection colors have moderate contrast

### Authentic Unix Workstation Feel
The color palette is inspired by actual CDE installations from HP-UX, Solaris, and AIX systems of the 1990s and early 2000s.
