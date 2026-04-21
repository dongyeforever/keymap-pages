import DefaultTheme from 'vitepress/theme'
import HomeFeatures from './components/HomeFeatures.vue'
import NavLangSwitch from './components/NavLangSwitch.vue'
import './style.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('HomeFeatures', HomeFeatures)
    app.component('NavLangSwitch', NavLangSwitch)
  },
  ThemeOptions: {
    hero: {
      actions: [
        { text: 'Browse Shortcuts', link: '/zh/shortcuts/vscode' }
      ]
    }
  }
}