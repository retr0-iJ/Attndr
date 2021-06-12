<template>
    <div class="hero is-fullheight-with-navbar">
        <div class="hero-head">

        </div>
        <div class="hero-body">
            <div class="container has-text-centered">
                <h1 class="title is-1">
                    Click the button below to activate your account.
                </h1>
                <div class="columns is-vcentered is-flex-direction-column">
                    <div class="column is-6">
                        <div class="notification is-danger" v-if="errors.length">
                            <p>{{ errors[0] }}</p>
                        </div>
                    </div>
                    <div class="column is-4">
                        <button id="btnActivate" class="button is-link is-large is-fullwidth" @click="activateUserAccount">
                            Activate
                        </button>
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
    name: "UserActivation",
    data() {
        return{
            uid: '',
            token: '',
            errors: []
        }
    },
    created() {
        this.uid = this.$route.params.uid
        this.token = this.$route.params.token
    },
    methods: {
        activateUserAccount(){
            $("#btnActivate").addClass("is-loading")

            this.erros = []

            const formData = {
                uid: this.uid,
                token: this.token
            }

            axios
                .post("api/v1/users/activation/", formData)
                .then(response => {
                    toast({
                            message: 'Account is Activated! You will be redirected to do Login.',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 1500,
                            position: 'center'
                    })

                    setTimeout(() => {
                        this.$router.push('/login')
                    }, 2000)
                })
                .catch(error => {
                    if(error.response && !error.message.includes('500')){
                        if(error.message.includes('400')){
                            this.errors.push('Activation Code not found!')
                        }
                        console.log(JSON.stringify(error))
                    }else if(error.message){
                        this.errors.push('Something went wrong. Please try again!')

                        console.log(JSON.stringify(error))
                    }
                })
                .then(function(){
                    $("#btnActivate").removeClass("is-loading")
                })
                
        }
    },
}
</script>