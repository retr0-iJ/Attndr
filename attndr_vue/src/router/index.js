import { createRouter, createWebHistory } from 'vue-router'
import store from '@/store'

import Landing_Page from "@/views/Landing_Page.vue"
import Home from '@/views/Home.vue'
import Login from '@/views/Login.vue'
import Register from '@/views/Register.vue'

const routes = [
  {
    path: '/',
    name: 'Landing_Page',
    component: Landing_Page
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/register',
    name: 'Register',
    component: Register
  },
  {
    path: '/home',
    alias: '/upcoming',
    name: 'Home',
    component: Home
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if((["Landing_Page", "Register", "Login"].includes(to.name)) && store.state.isAuthenticated){
    next('/home')
  }else if((["Home"].includes(to.name)) && !store.state.isAuthenticated){
    next('/login')
  }else{
    next()
  }
})

export default router
