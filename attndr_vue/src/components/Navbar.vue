<template>
    <nav class="navbar">
      <div class="navbar-brand">
        <router-link to='/' class="navbar-item"><img src="@/assets/img/logo.svg"></router-link>
        <div class="events-nav navbar-item" @click="switchActiveNav" v-if="$store.state.isAuthenticated">
          <router-link  to='/upcoming' class="navbar-item">
            <h5 id="titleUp" class="title is-5 has-text-weight-bold is-italic">Upcoming</h5>
          </router-link>
          <router-link to='/done' class="navbar-item">
            <h5 id="titleDone" class="title is-5">Done</h5>
          </router-link>
        </div> 
      </div>
      
      <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu">
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>

      <div class="navbar-menu" id="navbar-menu">
        <div class="time-wrapper navbar-item is-expanded is-justify-content-center is-align-items-center">
          <span class="mr-2 mt-1"><i class="fas fa-chevron-left fa-2x"></i></span>
          <div class="has-text-centered" id="server-time">
            {{ 'Server Time: ' + timestamp }}
          </div>
          <span class="ml-2 mt-1"><i class="fas fa-chevron-right fa-2x"></i></span>
        </div>
        <div class="navbar-end">
          <div class="navbar-item authenticated">
            <div class="buttons" v-if="!$store.state.isAuthenticated">
              <router-link to="/login" class="button is-light mr-2">Login</router-link>
              <router-link to="/register" class="button is-info">Register</router-link>
            </div>
            <div class="dropdown is-right authenticated" v-else>
              <div class="dropdown-trigger">
                <button class="button" aria-haspopup="true" aria-controls="dropdown-menu">
                  <span>Hello, <span>{{ this.name }}</span></span>
                  <span class="icon is-small">
                    <i class="fas fa-angle-down" aria-hidden="true"></i>
                  </span>
                </button>
              </div>
              <div class="dropdown-menu" id="dropdown-menu" role="menu">
                <div class="dropdown-content">
                  <a href="#" class="dropdown-item">
                    Profile
                  </a>
                  <hr class="dropdown-divider">
                  <a class="dropdown-item" @click="logout">
                    Logout
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </nav>
</template>
<script>
    import moment from 'moment'
    import axios from 'axios'

    export default {
        data() {
            return {
                timestamp: '',
                name: '',
                isDoneActive: false
            }
        },
        beforeCreate: function(){
          
          if(this.$store.state.isAuthenticated){
            $(function(){
              $('.time-wrapper').addClass("mr-6")
              $('.authenticated').addClass("ml-6")
            })
          }else{
            $(function(){
              $('.time-wrapper').removeClass("mr-6")
              $('.authenticated').removeClass("ml-6")
            })
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
              this.name = this.$store.state.name
            },
            async logout(){
              await axios
                .post("/api/v1/token/logout")
                .then(response => {
                  axios.defaults.headers.common["Authorization"] = ""

                  localStorage.removeItem("token")
                  localStorage.removeItem("name")
                  localStorage.removeItem("userid")

                  this.$store.commit('removeToken')
                  
                  this.$route.push('/')
                })
                .catch(error => {

                })
            },
            switchActiveNav: function(){
              if(this.isDoneActive){
                this.isDoneActive = false
                $('#titleDone').removeClass("has-text-weight-bold is-italic")
                $('#titleUp').addClass(("has-text-weight-bold is-italic"))
              }else{
                this.isDoneActive = true
                $('#titleUp').removeClass("has-text-weight-bold is-italic")
                $('#titleDone').addClass(("has-text-weight-bold is-italic"))
              }
            }
        },
        mounted() {
          (function($){
            
            $(function(){
              $('.dropdown').on('click', function(){
                $(this).toggleClass("is-active")
              })
            })

            $(function(){
              $('.dropdown-item').on('click', function(){
                $(this).toggleClass("is-active")
              })
            })

          }(jQuery))
          
        } 
    }
</script>