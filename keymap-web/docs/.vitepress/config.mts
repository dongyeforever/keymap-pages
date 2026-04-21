import {defineConfig} from 'vitepress'

export default defineConfig({
  title: '快捷键集合',
  description: '常用软件键盘快捷键集合',
  lang: 'zh-CN',
  locales: {
    root: {
      label: '中文',
      lang: 'zh-CN',
      title: '快捷键集合',
      description: '常用软件键盘快捷键集合',
      link: '/zh/'
    },
    en: {
      label: 'English',
      lang: 'en-US',
      title: 'Keymap Collection',
      description: 'Collaborative keyboard shortcuts for common software',
      link: '/en/'
    }
  },
  themeConfig: {
    nav: [
      { text: '首页', link: '/zh/' }
    ],
    sidebar: {
      '/zh/': [
        {
          text: '代码编辑器',
          items: [
            { text: 'VS Code', link: '/zh/shortcuts/vscode' },
            { text: 'Sublime Text', link: '/zh/shortcuts/sublime-text' },
            { text: 'Vim', link: '/zh/shortcuts/vim' }
          ]
        },
        {
          text: 'IDE',
          items: [
            { text: 'IntelliJ IDEA', link: '/zh/shortcuts/intellij-idea' },
            { text: 'Android Studio', link: '/zh/shortcuts/android-studio' },
            { text: 'Xcode', link: '/zh/shortcuts/xcode' }
          ]
        },
        {
          text: '设计',
          items: [
            { text: 'Figma', link: '/zh/shortcuts/figma' },
            { text: 'Photoshop', link: '/zh/shortcuts/photoshop' }
          ]
        },
        {
          text: '终端',
          items: [
            { text: 'iTerm2', link: '/zh/shortcuts/iterm2' }
          ]
        },
        {
          text: '浏览器',
          items: [
            { text: 'Chrome', link: '/zh/shortcuts/chrome' }
          ]
        },
        {
          text: '笔记',
          items: [
            { text: 'Notion', link: '/zh/shortcuts/notion' },
            { text: 'Obsidian', link: '/zh/shortcuts/obsidian' },
            { text: 'Typora', link: '/zh/shortcuts/typora' }
          ]
        },
        {
          text: '视频',
          items: [
            { text: 'CapCut', link: '/zh/shortcuts/capcut' }
          ]
        }
      ],
      '/en/': [
        {
          text: 'Code Editor',
          items: [
            { text: 'VS Code', link: '/en/shortcuts/vscode' },
            { text: 'Sublime Text', link: '/en/shortcuts/sublime-text' },
            { text: 'Vim', link: '/en/shortcuts/vim' }
          ]
        },
        {
          text: 'IDE',
          items: [
            { text: 'IntelliJ IDEA', link: '/en/shortcuts/intellij-idea' },
            { text: 'Android Studio', link: '/en/shortcuts/android-studio' },
            { text: 'Xcode', link: '/en/shortcuts/xcode' }
          ]
        },
        {
          text: 'Design',
          items: [
            { text: 'Figma', link: '/en/shortcuts/figma' },
            { text: 'Photoshop', link: '/en/shortcuts/photoshop' }
          ]
        },
        {
          text: 'Terminal',
          items: [
            { text: 'iTerm2', link: '/en/shortcuts/iterm2' }
          ]
        },
        {
          text: 'Browser',
          items: [
            { text: 'Chrome', link: '/en/shortcuts/chrome' }
          ]
        },
        {
          text: 'Notes',
          items: [
            { text: 'Notion', link: '/en/shortcuts/notion' },
            { text: 'Obsidian', link: '/en/shortcuts/obsidian' },
            { text: 'Typora', link: '/en/shortcuts/typora' }
          ]
        },
        {
          text: 'Video',
          items: [
            { text: 'CapCut', link: '/en/shortcuts/capcut' }
          ]
        }
      ]
    },
    search: {
      provider: 'local'
    },
    socialLinks: [
      { icon: 'github', link: 'https://github.com/dongyeforever/keymap-pages' }
    ]
  }
})