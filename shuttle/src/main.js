import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axiosInstance from './axios' // 导入 Axios 实例


const app = createApp(App)

app.config.globalProperties.$axios = axiosInstance // 将 Axios 实例添加到全局属性

app.use(store)
app.use(router)
app.mount('#app')
