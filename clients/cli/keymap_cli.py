#!/usr/bin/env python3
"""keymap - CLI client for keymap-pages"""

import argparse
import json
import os
import sys
import re
from pathlib import Path
from typing import Optional

PAGES_DIR = Path(__file__).parent.parent.parent / "pages"
PAGES_DIR_ZH = Path(__file__).parent.parent.parent / "pages.zh"
INDEX_FILE = Path(__file__).parent.parent.parent / "index.json"

DEFAULT_LANGUAGE = "en"


def get_language() -> str:
    """Get language from env var or config file."""
    env_lang = os.environ.get("KEYMAP_LANGUAGE")
    if env_lang in ("en", "zh"):
        return env_lang

    config_file = Path.home() / ".keymap"
    if config_file.exists():
        try:
            lang = config_file.read_text().strip()
            if lang in ("en", "zh"):
                return lang
        except Exception:
            pass

    local_config = Path(__file__).parent.parent.parent / ".keymap"
    if local_config.exists():
        try:
            lang = local_config.read_text().strip()
            if lang in ("en", "zh"):
                return lang
        except Exception:
            pass

    return DEFAULT_LANGUAGE


def set_language(language: str) -> bool:
    """Set default language in local config."""
    config_file = Path(__file__).parent.parent.parent / ".keymap"
    try:
        config_file.write_text(f"{language}\n")
        return True
    except Exception:
        return False


def get_pages_dir(language: str = "en") -> Path:
    """Get the pages directory for the specified language."""
    if language == "zh":
        return PAGES_DIR_ZH
    return PAGES_DIR


def get_index_file(language: str = "en") -> Path:
    """Get the index file for the specified language."""
    if language == "zh":
        return INDEX_FILE.parent / "index.zh.json"
    return INDEX_FILE


def load_index(language: str = "en") -> dict:
    """Load the search index."""
    index_file = get_index_file(language)
    if index_file.exists():
        with open(index_file, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"software": {}}


def get_software_list(language: str = "en") -> list:
    """Get list of all software."""
    index = load_index(language)
    return list(index.get("software", {}).keys())


def search_keymaps(query: str, software: Optional[str] = None, language: str = "en") -> list:
    """Search for keymaps matching query."""
    index = load_index(language)
    results = []

    for name, data in index.get("software", {}).items():
        if software and name != software:
            continue

        shortcuts = data.get("shortcuts", [])
        for shortcut in shortcuts:
            if query.lower() in shortcut["description"].lower() or query.lower() in shortcut["shortcut"].lower():
                results.append({
                    "software": name,
                    "shortcut": shortcut["shortcut"],
                    "description": shortcut["description"],
                    "category": shortcut.get("category", "General")
                })

    return results


def show_keymap(software: str, platform: Optional[str] = None, language: str = "en") -> Optional[str]:
    """Display keymap for a software."""
    pages_dir = get_pages_dir(language)
    software_dir = pages_dir / software
    if not software_dir.exists():
        return None

    platform_file = software_dir / f"{platform}.md" if platform else software_dir / "common.md"
    if not platform_file.exists():
        platform_file = software_dir / "common.md"
    if not platform_file.exists():
        return None

    with open(platform_file, "r", encoding="utf-8") as f:
        return f.read()


def format_keymap(content: str, category: Optional[str] = None) -> str:
    """Format keymap content for display."""
    lines = content.split("\n")
    output = []
    current_category = None

    for line in lines:
        if line.startswith("## "):
            current_category = line[3:]
            if category and current_category != category:
                current_category = None
            if category and current_category == category:
                output.append(line)
        elif current_category is not None or category is None:
            output.append(line)

    return "\n".join(output)


def build_index(language: str = "en") -> dict:
    """Build search index from pages directory."""
    index = {"software": {}}
    pages_dir = get_pages_dir(language)

    if not pages_dir.exists():
        return index

    for software_dir in pages_dir.iterdir():
        if not software_dir.is_dir():
            continue

        software_name = software_dir.name
        index["software"][software_name] = {"shortcuts": [], "categories": []}

        for md_file in software_dir.glob("*.md"):
            try:
                with open(md_file, "r", encoding="utf-8") as f:
                    content = f.read()

                category = "General"
                in_section = False

                for line in content.split("\n"):
                    if line.startswith("## "):
                        category = line[3:]
                        in_section = True
                        if category not in index["software"][software_name]["categories"]:
                            index["software"][software_name]["categories"].append(category)
                    elif in_section and "|" in line and line.startswith("|"):
                        parts = [p.strip() for p in line.split("|")[1:-1]]
                        if len(parts) >= 2:
                            index["software"][software_name]["shortcuts"].append({
                                "shortcut": parts[0],
                                "description": parts[1],
                                "category": category
                            })
            except Exception:
                continue

    return index


def main():
    default_lang = get_language()

    parser = argparse.ArgumentParser(
        description="keymap - Search keyboard shortcuts for common software",
        epilog="""
Examples:
  keymap list                           # List all software
  keymap show vscode                    # Show VS Code shortcuts
  keymap show iterm2 -l zh              # Show iTerm2 in Chinese
  keymap search copy                  # Search "copy"
  keymap search 分屏 --app iterm2       # Search in iTerm2
  keymap search debug --app intellij-idea # Search in IntelliJ
  keymap config set-lang zh            # Set language to Chinese
  keymap config get-lang               # View current language
  keymap init -l zh                  # Build Chinese index

Available software:
  vscode, intellij-idea, android-studio, xcode, figma, vim, chrome,
  photoshop, iterm2, sublime-text, notion, obsidian, typora, capcut
        """
    )
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    list_parser = subparsers.add_parser(
        "list", help="List all available software",
        description="List all available software in the keymap pages"
    )
    list_parser.add_argument("-l", "--language", choices=["en", "zh"], default=default_lang,
                            help=f"Language: en=English, zh=中文 (default: {default_lang})")

    search_parser = subparsers.add_parser(
        "search", help="Search shortcuts",
        description="Search shortcuts. Example: keymap search copy --app vscode"
    )
    search_parser.add_argument("query", help="Search query, e.g., copy, 复制, 分屏")
    search_parser.add_argument("--app", help="Search in specific app, e.g., vscode, iterm2, vim")
    search_parser.add_argument("-l", "--language", choices=["en", "zh"], default=default_lang,
                             help="Language: en=English, zh=中文")

    show_parser = subparsers.add_parser(
        "show", help="Show shortcuts for software",
        description="Show all shortcuts for a software. Example: keymap show vscode"
    )
    show_parser.add_argument("software", help="Software name (e.g., vscode, iterm2, chrome)")
    show_parser.add_argument("-p", "--platform", choices=["common", "windows", "macos", "linux"],
                        default="common", help="Platform: common/all, windows, macos, linux")
    show_parser.add_argument("-l", "--language", choices=["en", "zh"], default=default_lang,
                         help=f"Language: en=English, zh=中文 (default: {default_lang})")

    init_parser = subparsers.add_parser(
        "init", help="Initialize/update search index",
        description="Build search index from pages directory"
    )
    init_parser.add_argument("-l", "--language", choices=["en", "zh"], default=default_lang,
                          help=f"Language: en=English, zh=中文 (default: {default_lang})")

    config_parser = subparsers.add_parser(
        "config", help="Configure keymap",
        description="Get or set default language"
    )
    config_parser.add_argument("action", choices=["set-lang", "get-lang"], nargs="?",
                              help="Action: set-lang (set language), get-lang (view current)")
    config_parser.add_argument("value", choices=["en", "zh"], nargs="?",
                              help="Language: en (English), zh (中文)")

    readme_parser = subparsers.add_parser(
        "readme", help="Show README",
        description="Show README in selected language"
    )
    readme_parser.add_argument("-l", "--language", choices=["en", "zh"], default=default_lang,
                          help="Language: en (English), zh (中文)")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    if args.command == "config":
        if args.action == "set-lang" and args.value:
            if set_language(args.value):
                print(f"Default language set to: {args.value}")
            else:
                print("Failed to set language")
        else:
            lang = get_language()
            print(f"Current language: {lang}")
            print(f"  (Use KEYMAP_LANGUAGE env var or .keymap config file to change)")
        return

    language = getattr(args, "language", default_lang)

    if args.command == "list":
        software_list = get_software_list(language)
        if not software_list:
            print(f"No software found. Run 'keymap init -l {language}' first.")
            return
        print("Available software:")
        for name in sorted(software_list):
            print(f"  - {name}")
        return

    if args.command == "search":
        results = search_keymaps(args.query, args.app, language)
        if not results:
            print(f"No results found for '{args.query}'")
            return
        current_software = None
        for result in results:
            if result["software"] != current_software:
                current_software = result["software"]
                print(f"\n{result['software']}:")
            print(f"  {result['shortcut']:30} {result['description']}")
        return

    if args.command == "show":
        content = show_keymap(args.software, args.platform, language)
        if not content:
            print(f"Software '{args.software}' not found")
            sys.exit(1)
        print(format_keymap(content))
        return

    if args.command == "init":
        index = build_index(language)
        index_file = get_index_file(language)
        with open(index_file, "w", encoding="utf-8") as f:
            json.dump(index, f, ensure_ascii=False, indent=2)
        print(f"Index built successfully for {language}")
        total = sum(len(s["shortcuts"]) for s in index["software"].values())
        print(f"Indexed {len(index['software'])} software, {total} shortcuts")
        return

    if args.command == "readme":
        readme_file = PAGES_DIR.parent / f"README.md" if language == "en" else PAGES_DIR.parent / f"README.zh.md"
        if readme_file.exists():
            print(readme_file.read_text(encoding="utf-8"))
        else:
            print(f"README not found: {readme_file}")
        return


if __name__ == "__main__":
    main()