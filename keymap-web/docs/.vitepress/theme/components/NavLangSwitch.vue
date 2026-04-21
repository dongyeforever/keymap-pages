<script setup>
import { useRoute } from 'vitepress'
import { computed } from 'vue'

const route = useRoute()

const currentPath = computed(() => route.value.path)
const base = '/keymap-pages'

const targetPath = computed(() => {
  const path = currentPath.value
  if (path.includes('/en/')) {
    return path.replace('/en/', '/zh/')
  } else if (path.includes('/zh/')) {
    return path.replace('/zh/', '/en/')
  } else if (path === base + '/' || path === base) {
    return base + '/en/'
  } else if (path.startsWith(base + '/shortcuts/')) {
    return path.replace('/shortcuts/', '/en/shortcuts/')
  } else if (path.startsWith(base + '/zh')) {
    return path.replace('/zh/', '/en/')
  } else if (path.startsWith(base + '/en')) {
    return path.replace('/en/', '/zh/')
  }
  return base + '/en/'
})

const targetLabel = computed(() => currentPath.value.includes('/en/') ? '中文' : 'English')
</script>

<template>
  <a :href="targetPath" class="nav-lang-link">{{ targetLabel }}</a>
</template>

<style scoped>
.nav-lang-link {
  padding: 0.5rem 0;
  color: var(--vp-c-text-1);
  text-decoration: none;
  transition: color 0.2s;
}
.nav-lang-link:hover {
  color: var(--vp-c-brand);
}
</style>