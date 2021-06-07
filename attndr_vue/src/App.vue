<template>
  <div id="wrapper">
    <Navbar v-if="!['Login', 'Register', 'Start_Event'].includes($route.name)" />
    <router-view/>
  </div>
</template>

<script>
  import Navbar from '@/components/Navbar.vue'
  import axios from 'axios'

  export default{
    components: {
      Navbar
    },
    beforeCreate(){
      this.$store.commit('initializeAuth')

      const token = this.$store.state.token

      if(token){
        axios.defaults.headers.common['Authorization'] = "Token " + token
      }else{
        axios.defaults.headers.common['Authorization'] = ""
      }
    }
  }
</script>