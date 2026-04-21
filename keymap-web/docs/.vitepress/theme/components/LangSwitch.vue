<script setup>
import { useData, useRoute } from 'vitepress'
import { computed, onMounted, ref } from 'vue'

const { page } = useData()
const route = useRoute()

const isClient = ref(false)

onMounted(() => {
  isClient.value = true
})

const isEn = computed(() => {
  if (!page.value || !page.value.relativePath) return false
  return page.value.relativePath.startsWith('en/')
})

const currentPath = computed(() => {
  if (!route.value || !route.value.path) return ''
  return route.value.path
})

const targetPath = computed(() => {
  const path = currentPath.value
  if (!path) return '/zh/'
  if (isEn.value) {
    return path.replace('/en/', '/zh/')
  } else {
    return path.replace('/zh/', '/en/')
  }
})

const targetLabel = computed(() => isEn.value ? '中文' : 'English')
</script>

<template>
  <a v-if="isClient" :href="targetPath" class="lang-switch">
    {{ targetLabel }}
  </a>
  <span v-else class="lang-switch-loading">Loading...</span>
</template>

<style scoped>
.lang-switch {
  padding: 0.5rem 1rem;
  color: var(--vp-c-text-1);
  text-decoration: none;
  transition: color 0.2s;
}
.lang-switch:hover {
  color: var(--vp-c-brand);
}
.lang-switch-loading {
  padding: 0.5rem 1rem;
  color: var(--vp-c-text-3);
}
</style>