<script setup>
import { useData } from 'vitepress'
import { computed } from 'vue'

const { page } = useData()
const isEn = computed(() => page.value.relativePath.startsWith('en/'))
const base = '/keymap-pages'

const categories = [
  {
    title: computed(() => isEn.value ? 'Code Editor' : '代码编辑器'),
    items: computed(() => [
      { name: 'VS Code', link: base + (isEn.value ? '/en' : '/zh') + '/shortcuts/vscode' },
      { name: 'Sublime Text', link: base + (isEn.value ? '/en' : '/zh') + '/shortcuts/sublime-text' },
      { name: 'Vim', link: base + (isEn.value ? '/en' : '/zh') + '/shortcuts/vim' }
    ])
  },
  {
    title: computed(() => isEn.value ? 'IDE' : 'IDE'),
    items: computed(() => [
      { name: 'IntelliJ IDEA', link: base + (isEn.value ? '/en' : '/zh') + '/shortcuts/intellij-idea' },
      { name: 'Android Studio', link: base + (isEn.value ? '/en' : '/zh') + '/shortcuts/android-studio' },
      { name: 'Xcode', link: base + (isEn.value ? '/en' : '/zh') + '/shortcuts/xcode' }
    ])
  },
  {
    title: computed(() => isEn.value ? 'Design' : '设计'),
    items: computed(() => [
      { name: 'Figma', link: base + (isEn.value ? '/en' : '/zh') + '/shortcuts/figma' },
      { name: 'Photoshop', link: base + (isEn.value ? '/en' : '/zh') + '/shortcuts/photoshop' }
    ])
  },
  {
    title: computed(() => isEn.value ? 'Terminal' : '终端'),
    items: computed(() => [
      { name: 'iTerm2', link: base + (isEn.value ? '/en' : '/zh') + '/shortcuts/iterm2' }
    ])
  },
  {
    title: computed(() => isEn.value ? 'Browser' : '浏览器'),
    items: computed(() => [
      { name: 'Chrome', link: base + (isEn.value ? '/en' : '/zh') + '/shortcuts/chrome' }
    ])
  },
  {
    title: computed(() => isEn.value ? 'Notes' : '笔记'),
    items: computed(() => [
      { name: 'Notion', link: base + (isEn.value ? '/en' : '/zh') + '/shortcuts/notion' },
      { name: 'Obsidian', link: base + (isEn.value ? '/en' : '/zh') + '/shortcuts/obsidian' },
      { name: 'Typora', link: base + (isEn.value ? '/en' : '/zh') + '/shortcuts/typora' }
    ])
  },
  {
    title: computed(() => isEn.value ? 'Video' : '视频'),
    items: computed(() => [
      { name: 'CapCut', link: base + (isEn.value ? '/en' : '/zh') + '/shortcuts/capcut' }
    ])
  }
]
</script>

<template>
  <div class="home-features">
    <div v-for="category in categories" :key="category.title.value" class="feature-category">
      <h3>{{ category.title.value }}</h3>
      <div class="feature-items">
        <a v-for="item in category.items.value" :key="item.name" :href="item.link" class="feature-link">
          {{ item.name }}
        </a>
      </div>
    </div>
  </div>
</template>

<style scoped>
.home-features {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
  gap: 1.5rem;
  padding: 2rem 0;
}
.feature-category h3 {
  font-size: 1rem;
  font-weight: 600;
  margin-bottom: 0.75rem;
  color: var(--vp-c-text-1);
}
.feature-items {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}
.feature-link {
  display: block;
  padding: 0.5rem 1rem;
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  color: var(--vp-c-text-1);
  text-decoration: none;
  transition: all 0.2s;
}
.feature-link:hover {
  border-color: var(--vp-c-brand);
  background: var(--vp-c-brand-light);
  color: var(--vp-c-brand-dark);
}
</style>