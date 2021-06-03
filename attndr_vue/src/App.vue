<template>
  <div id="wrapper">
    <Navbar v-if="!['Login', 'Register'].includes($route.name)" />
    <router-view/>
  </div>
</template>

<script>
  import Navbar from '@/components/Navbar.vue'

  export default{
    components: {
      Navbar
    },
  }
</script>