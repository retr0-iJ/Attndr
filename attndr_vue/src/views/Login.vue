<template>
    <div class="hero is-fullheight">
        <div class="hero-body">
            <div class="container">
                <div class="columns is-centered is-vcentered">
                    <div class="column is-4 box">
                        <div class="content m-2">
                            <div class="is-flex-direction-column is-align-items-space-between has-text-centered mb-5">
                                <div class="logo-wrapper is-flex is-justify-content-center is-align-items-center m-4">
                                    <router-link to='/'>
                                        <img class="logo" src="@/assets/img/logo.svg">
                                    </router-link>
                                </div>
                                <div class="greetings mb-2">
                                    <h4 class="subtitle is-4 m-0">Welcome Back</h4>
                                </div>
                                <div class="description">
                                    <span>
                                        Never worry, everything is under control. Are you ready to establish great events?
                                    </span>
                                </div>
                            </div>
                            <form @submit.prevent="submitForm">
                                <div class="field">
                                    <div class="control has-icons-left">
                                        <input class="input" type="text" id="email" v-model="email" 
                                            placeholder="Email">
                                        <span class="icon is-small is-left">
                                            <i class="fa fa-envelope"></i>
                                        </span>
                                    </div>
                                </div>
                                <div class="field">
                                    <div class="control has-icons-left">
                                        <input class="input" type="password" id="password" v-model="password"
                                            placeholder="Password">
                                        <span class="icon is-small is-left">
                                            <i class="fa fa-lock"></i>
                                        </span>
                                    </div>
                                </div>
                                <div class="field mb-4">
                                    <label for="rememberme" class="checkbox">
                                        <input type="checkbox" id="rememberme" v-model="rememberme">
                                        Remember me
                                    </label>
                                    <router-link to="/forget" class="is-pulled-right">Forget login details?</router-link>
                                </div>
                                <div class="notification is-danger" v-if="errors.length">
                                    <p>{{ errors[0] }}</p>
                                </div>
                                <div class="field has-text-centered">
                                    <button id="btnLogin" class="button is-info is-fullwidth">
                                        Login
                                    </button>
                                    <span class="is-size-7">
                                        New to Attndr?<router-link to="/register"> Register now</router-link>
                                    </span>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

    export default {
        name: "Login",
        data(){
            return {
                email: '',
                password: '',
                rememberme: false,
                errors: []
            }
        },
        created(){

        },
        methods: {
            async submitForm(){
                $('#btnLogin').addClass('is-loading')

                axios.defaults.headers.common['Authorization'] = ""
                localStorage.removeItem["token"]

                this.errors = []

                const formData = {
                    email: this.email,
                    password: this.password
                }

                await axios
                    .post("/api/v1/token/login", formData)
                    .then(response => {
                        toast({
                            message: 'Login Successful!',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right'
                        })

                        const token = response.data.auth_token
                        this.$store.commit('setToken', token)
                        axios.defaults.headers.common['Authorization'] = "Token " + token
                        localStorage.setItem("token", token)
                        const toPath = this.$route.query.to || '/'

                        setTimeout(() => {
                            this.$router.push(toPath)
                        }, 1500)
                        
                        axios
                            .get("/api/v1/users/me")
                            .then(response => {
                                const name = response.data["name"].split(" ")[0]
                                localStorage.setItem("name", name)
                                this.$store.commit('setName', name)
                            })
                    })
                    .catch(error => {
                        if(error.response && error.response.code != 500){
                            for(const property in error.response.data){
                                this.errors.push(`${property} = ${error.response.data[property]}`)
                            }

                            console.log(JSON.stringify(error.response.data))
                        }else if(error.message){
                            this.errors.push('Something went wrong. Please try again!')

                            console.log(JSON.stringify(error))
                        }
                    }).then(function(){
                        $("#btnLogin").removeClass("is-loading")
                    })
            }
        },
        mounted(){
            document.title = "Login"
        }
    }
</script>
<style lang="scss" scoped>
    .logo{
        width: 40%
    }
</style>