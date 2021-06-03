<template>
    <div class="hero is-fullheight">
        <div class="hero-body">
            <div class="container">
                <div class="columns is-centered is-vcentered">
                    <div class="column is-4 box">
                        <div class="content m-2">
                            <div class="is-flex-direction-column is-align-items-space-between has-text-centered mb-5">
                                <div class="logo is-justify-content-center is-align-items-center m-4">
                                    <router-link to='/'>
                                        <img src="@/assets/img/logo.svg" width="120">
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
                            <form action="">
                                <div class="field">
                                    <div class="control has-icons-left">
                                        <input class="input" type="text" name="emailorphone" id="emailorphone" 
                                            placeholder="Email or mobile number">
                                        <span class="icon is-small is-left">
                                            <i class="fa fa-envelope"></i>
                                        </span>
                                    </div>
                                </div>
                                <div class="field">
                                    <div class="control has-icons-left">
                                        <input class="input" type="password" name="password" id="password" 
                                            placeholder="Password">
                                        <span class="icon is-small is-left">
                                            <i class="fa fa-lock"></i>
                                        </span>
                                    </div>
                                </div>
                                <div class="field mb-4">
                                    <label for="rememberme" class="checkbox">
                                        <input type="checkbox" name="rememberme" id="rememberme">
                                        Remember me
                                    </label>
                                    <router-link to="/forget" class="is-pulled-right">Forget login details?</router-link>
                                </div>
                                <div class="field has-text-centered">
                                    <button class="button is-info is-fullwidth">
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
    export default {
        
    }
</script>