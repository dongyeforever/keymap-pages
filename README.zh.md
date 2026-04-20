# keymap-pages

常用软件快捷键集合。

## 什么是 keymap-pages？

keymap-pages 是一个类似 tldr-pages 的社区维护快捷键页面集合，收录了常用软件的键盘快捷键，旨在提供简洁实用的示例而非冗长的官方手册。

## 支持的软件 (14)

| 分类 | 软件 |
|----------|----------|
| 代码编辑器 | VS Code, Sublime Text, Vim |
| IDE | IntelliJ IDEA, Android Studio, Xcode |
| 设计工具 | Figma, Photoshop |
| 终端 | iTerm2 |
| 浏览器 | Chrome |
| 笔记 | Notion, Obsidian, Typora |
| 视频 | CapCut (剪映) |

## 安装

```bash
# 克隆或下载此仓库
git clone https://github.com/your-username/keymap-pages.git
cd keymap-pages

# 添加到 PATH（可选）
export PATH="$PWD:$PATH"
```

## 使用方法

### 命令行

```bash
./keymap -h                    # 显示帮助
./keymap list                  # 列出所有软件
./keymap show vscode           # 查看 VS Code 快捷键
./keymap show iterm2 -l zh     # 查看 iTerm2 中文快捷键
./keymap search copy          # 搜索 "copy"
./keymap search 分屏 --app iterm2    # 在 iTerm2 中搜索
./keymap search debug --app intellij-idea  # 在 IntelliJ 中搜索
./keymap config set-lang en    # 设置为英文
./keymap config get-lang    # 查看当前语言设置
./keymap init -l zh           # 构建中文索引
```

### 参数说明

| 参数 | 说明 |
|------------|-------------|
| `-l, --language` | 语言: en (英文), zh (中文) |
| `--app` | 在指定软件中搜索 |
| `-p, --platform` | 平台: common, windows, macos, linux |

## 语言版本

- `pages/` - 英文版
- `pages.zh/` - 中文版

运行 `./keymap config set-lang zh` 可设置默认语言为中文。

## 贡献指南

1. 在 `pages/` 或 `pages.zh/` 目录下添加或编辑快捷键页面
2. 遵循 Markdown 格式规范
3. 运行 `./keymap init -l en` 和 `./keymap init -l zh` 更新索引
4. 提交 Pull Request

## Markdown 格式

```markdown
# 软件名称

> 简短描述

## 分类名称

| 快捷键 | 说明 |
|----------|-------------|
| `Ctrl+C` | 复制 |
| `Cmd+V` | 粘贴 |
```

## 许可证

MIT License