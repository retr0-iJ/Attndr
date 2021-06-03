import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import bulma from '../node_modules/bulma'

createApp(App).use(store).use(router, bulma).mount('#app')
