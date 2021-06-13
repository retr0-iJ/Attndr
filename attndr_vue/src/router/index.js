import { createRouter, createWebHistory } from 'vue-router'
import store from '@/store'

import Landing_Page from "@/views/Landing_Page.vue"
import Home from '@/views/Home.vue'
import Login from '@/views/Login.vue'
import Register from '@/views/Register.vue'
import User_Activation from '@/views/User_Activation.vue'
import Start_Event from '@/views/Start_Event.vue'
import Done from '@/views/Done.vue'
import View_Home from '@/views/View_Home'
import View_Done from '@/views/View_Done'

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
    path: '/activate/:uid/:token',
    name: 'User_Activation',
    component: User_Activation
  },
  {
    path: '/home',
    alias: '/upcoming',
    name: 'Home',
    component: Home
  },
  {
    path: '/done',
    name: 'Done',
    component: Done
  },
  {
    path: '/start_event',
    name: 'Start_Event',
    props: true,
    component: Start_Event
  },
  {
    path: '/view_home/:id',
    name: 'View_Home',
    component: View_Home
  },
  {
    path: '/view_done/:id',
    name: 'View_Done',
    component: View_Done
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if((["Landing_Page", "Register", "Login"].includes(to.name)) && store.state.isAuthenticated){
    next('/home')
  }else if((["Home", "Done", "Start_Event"].includes(to.name)) && !store.state.isAuthenticated){
    next('/login')
  }else{
    next()
  }
})

export default router
