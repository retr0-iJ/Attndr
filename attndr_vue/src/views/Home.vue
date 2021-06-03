<template>
  <div id="wrapper">
    <Landing_Page />
  </div>
</template>

<script>
import Landing_Page from "@/components/Landing_Page.vue"

export default {
  name: 'Home',
  components: {
    Landing_Page
  },
  mounted(){
    document.title = "Home"
  }
}
</script>