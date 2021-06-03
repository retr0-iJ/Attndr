<template>
    <nav class="navbar">
      <div class="navbar-brand">
        <router-link to='/' class="navbar-item"><img src="@/assets/img/logo.svg"></router-link>
      </div>
      
      <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu">
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>

      <div class="navbar-menu" id="navbar-menu">
        <div class="navbar-item is-expanded is-justify-content-center is-align-items-center">
          <span class="mr-2 mt-1"><i class="fas fa-chevron-left fa-2x"></i></span>
          <div class="has-text-centered" id="server-time">
            {{ 'Server Time: ' + timestamp }}
          </div>
          <span class="ml-2 mt-1"><i class="fas fa-chevron-right fa-2x"></i></span>
        </div>
        <div class="navbar-end">
          <div class="navbar-item">
            <div class="buttons-">
              <router-link to="/login" class="button is-light mr-2">Login</router-link>
              <router-link to="/register" class="button is-info">Register</router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>
</template>
<script>
    import moment from 'moment'

    export default {
        data() {
            return {
                timestamp: ''
            }
        },
        created() {
            setInterval(() => {
                this.getServerTime();
            }, 1000)
        },
        methods: {
            getServerTime: function() {
                this.timestamp = moment(new Date()).format("MMMM Do YYYY, hh:mm:ss a")
            }
        }   
    }
</script>