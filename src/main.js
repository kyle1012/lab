import { createApp } from 'vue'
import App from './App.vue'
import router from './router/router'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'
import store from "./store/store";
import axios from 'axios'
import './assets/common.css'


loadFonts()


const app = createApp(App)
app.config.globalProperties.$store = store
app.config.globalProperties.$axios = axios
app.use(router)
app.use(store)
app.use(vuetify)
app.mount('#app')