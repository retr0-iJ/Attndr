<template>
    <div class="hero is-fullheight">
        <div class="hero-body">
            <div class="container">
                <div class="columns is-centered is-vcentered">
                    <div class="column is-5 box">
                        <div class="content m-2">
                            <div class="is-flex-direction-column is-align-items-space-between has-text-centered mb-6">
                                <div class="logo-wrapper is-flex is-justify-content-center is-align-items-center m-4">
                                    <router-link to='/'>
                                        <img class="logo" src="@/assets/img/logo.svg">
                                    </router-link>
                                </div>
                                <div class="description">
                                    <span class="is-size-5">
                                        Managing your event attendance at its finest
                                    </span>
                                </div>
                            </div>
                            <form @submit.prevent="submitForm">
                                <div class="field">
                                    <label for="name" class="label">Full Name</label>
                                    <div class="control">
                                        <input class="input" type="text" id="name" v-model="name"
                                            placeholder="e.g. Alex Jordan">
                                    </div>
                                </div>
                                <div class="field">
                                    <label for="phone" class="label">Mobile Number</label>
                                    <div class="field has-addons">
                                        <div class="control">
                                            <a class="button is-static">
                                                +62
                                            </a>
                                        </div>
                                        <div class="control is-expanded">
                                            <input class="input" type="tel" id="phone" v-model="phone"
                                                placeholder="e.g. 812xxxxxx">
                                        </div>
                                    </div>
                                </div>
                                <div class="field">
                                    <label for="email" class="label">Email</label>
                                    <div class="control">
                                        <input class="input" type="text" id="email" v-model="email"
                                            placeholder="e.g. alexjordan1@gmail.com">
                                    </div>
                                </div>
                                <div class="field">
                                    <div class="control">
                                        <label for="password" class="label">
                                            Password
                                            <span class="has-text-weight-normal"> (8 or more characters)</span>
                                        </label>
                                        <input class="input" type="password" id="password" v-model="password"
                                            placeholder="Password">
                                    </div>
                                </div>
                                <div class="field mb-5">
                                    <div class="control">
                                        <label for="repassword" class="label">
                                            Re-Enter Password
                                            <span class="has-text-weight-normal"> (must be equal to Password)</span>
                                        </label>
                                        <input class="input" type="password" id="repassword" v-model="repassword"
                                            placeholder="Re-Password">
                                    </div>
                                </div>
                                <div class="notification is-danger" v-if="errors.length">
                                    <p>{{ errors[0] }}</p>
                                </div>
                                <div class="notification is-success" v-if="success">
                                    <p>{{ success }}</p>
                                </div>
                                <div class="field has-text-centered">
                                    <button id="btnRegister" class="button is-info is-fullwidth is-medium">
                                        Sign Up
                                    </button>
                                    <span class="is-size-7">
                                        Already on Attndr?<router-link to="/login"> Sign in</router-link>
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

    export default {
        name: "Register",
        data(){
            return {
                name: '',
                phone: '',
                email: '',
                password: '',
                repassword: '',
                errors: [],
                success: ''
            }
        },
        created(){

        },
        methods: {
            submitForm(){
                $("#btnRegister").addClass("is-loading")

                this.errors = []
                this.success = ''

                const formData = {
                    name: this.name,
                    email: this.email,
                    phone: this.phone,
                    password: this.password,
                    re_password: this.repassword
                }

                axios
                    .post("/api/v1/users/", formData)
                    .then(response => {
                        this.success = 'Account successfully created, please check your email to ACTIVATE your account before login!'
                    })
                    .catch(error => {
                        if(error.response){
                            for(const property in error.response.data){
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }

                            console.log(JSON.stringify(error.response.data))
                        }else if(error.message){
                            this.errors.push('Something went wrong. Please try again!')

                            console.log(JSON.stringify(error))
                        }
                    }).then(function(){
                        $("#btnRegister").removeClass("is-loading")
                    })
            }
        },
        mounted(){
            document.title = "Register"
        }
    }
</script>
<style lang="scss" scoped>
    .logo{
        width: 30%
    }
</style>