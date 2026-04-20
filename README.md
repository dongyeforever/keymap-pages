# keymap-pages

Collaborative keyboard shortcuts for common software.

## What is keymap-pages?

keymap-pages is a collection of community-maintained keyboard shortcut pages for popular software. Similar to tldr-pages, it aims to provide simple, practical examples instead of comprehensive manuals.

## Available Software (14)

| Category | Software |
|----------|----------|
| Code Editor | VS Code, Sublime Text, Vim |
| IDE | IntelliJ IDEA, Android Studio, Xcode |
| Design | Figma, Photoshop |
| Terminal | iTerm2 |
| Browser | Chrome |
| Notes | Notion, Obsidian, Typora |
| Video | CapCut (剪映) |

## Installation

```bash
# Clone or download this repository
git clone https://github.com/your-username/keymap-pages.git
cd keymap-pages

# Add to PATH (optional)
export PATH="$PWD:$PATH"
```

## Usage

### CLI Commands

```bash
./keymap -h                    # Show help
./keymap list                  # List all software
./keymap show vscode           # Show VS Code shortcuts
./keymap show iterm2 -l zh     # Show iTerm2 in Chinese
./keymap search copy          # Search "copy"
./keymap search 分屏 --app iterm2    # Search in iTerm2
./keymap search debug --app intellij-idea  # Search in IntelliJ
./keymap config set-lang zh   # Set language to Chinese
./keymap config get-lang     # View current language
./keymap init -l zh           # Build Chinese index
```

### Parameters

| Parameter | Description |
|------------|-------------|
| `-l, --language` | Language: en (English), zh (中文) |
| `--app` | Search in specific app |
| `-p, --platform` | Platform: common, windows, macos, linux |

## Language Support

- `pages/` - English version
- `pages.zh/` - Chinese version

Run `./keymap config set-lang zh` to set default language to Chinese.

## Contributing

1. Add or edit shortcut pages in `pages/` or `pages.zh/` directory
2. Follow the Markdown format
3. Run `./keymap init -l en` and `./keymap init -l zh` to update index
4. Submit a pull request

## Markdown Format

```markdown
# Software Name

> Short description

## Category Name

| Shortcut | Description |
|----------|-------------|
| `Ctrl+C` | Copy |
| `Cmd+V` | Paste |
```

## License

MIT License