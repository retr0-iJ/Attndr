<template>
    <div class="hero is-fullheight">
        <div class="hero-body">
            <div class="container">
                <div class="columns is-centered is-vcentered">
                    <div class="column is-5 box">
                        <div class="content m-2">
                            <div class="is-flex-direction-column is-align-items-space-between has-text-centered mb-6">
                                <div class="logo is-justify-content-center is-align-items-center m-4">
                                    <router-link to='/'>
                                        <img src="@/assets/img/logo.svg" width="120">
                                    </router-link>
                                </div>
                                <div class="description">
                                    <span class="is-size-5">
                                        Managing your event attendance at its finest
                                    </span>
                                </div>
                            </div>
                            <form action="">
                                <div class="field">
                                    <label for="name" class="label">Full Name</label>
                                    <div class="control">
                                        <input class="input" type="text" name="name" id="name" 
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
                                            <input class="input" type="tel" name="phone" id="phone" 
                                                placeholder="e.g. 812xxxxxx">
                                        </div>
                                    </div>
                                </div>
                                <div class="field">
                                    <label for="email" class="label">Email</label>
                                    <div class="control">
                                        <input class="input" type="text" name="email" id="email" 
                                            placeholder="e.g. alexjordan1@gmail.com">
                                    </div>
                                </div>
                                <div class="field">
                                    <div class="control">
                                        <label for="password" class="label">
                                            Password
                                            <span class="has-text-weight-normal"> (6 or more characters)</span>
                                        </label>
                                        <input class="input" type="password" name="password" id="password" 
                                            placeholder="Password">
                                    </div>
                                </div>
                                <div class="field mb-5">
                                    <div class="control">
                                        <label for="repassword" class="label">
                                            Re-Enter Password
                                            <span class="has-text-weight-normal"> (must be equal to Password)</span>
                                        </label>
                                        <input class="input" type="password" name="repassword" id="repassword" 
                                            placeholder="Re-Password">
                                    </div>
                                </div>
                                <div class="field has-text-centered">
                                    <button class="button is-info is-fullwidth">
                                        Register
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
    export default {
        
    }
</script>