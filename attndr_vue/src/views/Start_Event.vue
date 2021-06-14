<template>
    <div class="hero is-fullheight">
        <div class="hero-head p-5">
            <div class="level">
                <div class="level-item">
                    <img class="logo" src="@/assets/img/logo.svg">
                </div>
            </div>
        </div>
        <div class="hero-body py-0">
            <div class="container">
                <div class="columns is-centered has-text-centered">
                    <div class="column">
                        <div class="event-title">
                            <h3 class="title is-3">
                                {{ event_name }}
                            </h3>
                        </div>
                        <div class="page-content">
                            <div class="input-user-credential container m-6" v-if="!entered">
                                <div class="columns is-vcentered is-flex-direction-column">
                                    <div class="column is-5 is-flex is-flex-direction-column is-align-items-center">
                                        <AnalogClock />
                                    </div>
                                    <div class="column is-5">
                                        <form>
                                            <div class="field">
                                                <div class="control">
                                                    <form @submit.prevent="submitParticipantCredential">
                                                        <div id="controlPhone" class="control is-large">
                                                            <input class="input is-large" type="tel" id="inputPhone" v-model="phone"
                                                                placeholder="Enter your phone number" onblur="this.focus()" autocomplete="off" autofocus>
                                                        </div>
                                                    </form>
                                                </div>
                                            </div>
                                        </form>
                                    </div>
                                </div>
                            </div>
                            <div class="show-qr m-4" v-else>
                                <div class="columns is-vcentered is-flex-direction-column">
                                    <div class="column is-5 is-flex is-flex-direction-column is-align-items-center">
                                        <img :src="qr_location">
                                    </div>
                                    <div class="column is-7">
                                        <p class="subtitle is-4">
                                            <span v-if="qr_error != undefined">{{ qr_error }}</span>
                                            <span v-else-if="login_message == '' && qr_error == undefined">Please scan the QR Code above with your installed Attndr. on phone and if Succeed / Failed, please click the button below.</span> 
                                            <span v-else-if="login_message == 'Success'">Login <span class="has-text-success">Successful</span> !</span>
                                            <span v-else>
                                                Login <span class="has-text-danger">Failed</span> ! Please try again.<br>
                                                If you are having issues, please kindly contact our nearby support.
                                            </span>
                                        </p>
                                        <button id="btnContinue" class="button is-warning is-large" @click="straightCheckLogin" v-if="login_message == '' && qr_error == undefined">
                                            Continue
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import AnalogClock from '@/components/AnalogClock.vue'
import axios from 'axios'

export default {
    Name: 'Start_Event',
    props: [ "id", "name" ],
    components: {
        AnalogClock
    },
    data(){
        return{
            phone: '',
            entered: false,
            event_id: 0,
            event_name: '',
            qr_error: '',
            qr_location: '',
            login_message: '',
            body: {},
            checkLogin: null
        }
    },
    created(){
        this.getEventData()
    },
    methods: {
        getEventData(){
            this.resetData()
            if(this.name != undefined){
                localStorage.setItem("currentRunningEventID", this.id)
                localStorage.setItem("currentRunningEventName", this.name)
                this.event_name = this.name
                this.event_id = this.id
            }
            else{
                this.event_id = localStorage.getItem("currentRunningEventID")
                this.event_name = localStorage.getItem("currentRunningEventName")
            }      
        },
        resetData(){
            this.phone = ''
            this.entered = false
            this.error = ''
            this.qr_location = ''
            this.login_message = ''
            this.body = {}
        },
        async submitParticipantCredential(){
            $('#controlPhone').addClass("is-loading")

            this.body = {
                event_id: this.event_id,
                phone_number: this.phone
            }

            await axios
                .post("/api/v1/qr_code/", this.body)
                .then(response => {
                    this.qr_location = response.data.location 
                    this.qr_error = response.data.error_message

                    if(this.qr_location != undefined){
                        this.checkLogin = setTimeout(() => {
                            axios
                                .post("/api/v1/qr_code/response/", this.body)
                                .then(response => {
                                    this.login_message = response.login_message
                                })
                                .catch(error => {
                                    this.login_message = "Failed"
                                })
                                .then(() => {
                                    setTimeout(() => {
                                        this.resetData()
                                    }, 1500);
                                })
                        }, 15000)
                    }
                })
                .catch(error => {
                    if(error.response){
                        console.log(JSON.stringify(error.response.data))
                    }else if(error.message){
                        console.log(JSON.stringify(error))
                    }
                    this.error = "Something went wrong, please try again!"
                    setTimeout(() => {
                        this.resetData()
                    }, 1500);
                })
                .then(() => {
                    this.entered = true
                    $('#controlPhone').removeClass("is-loading")
                    if(this.qr_location == undefined)
                        setTimeout(() => {
                            this.resetData()
                        }, 1500);
                })
        },
        straightCheckLogin(){
            $('#btnContinue').addClass("is-loading")
            clearTimeout(this.checkLogin)
            this.checkLogin = null
            axios
                .post("/api/v1/qr_code/response/", this.body)
                .then(response => {
                    this.login_message = response.data.login_message
                })
                .catch(error => {
                    this.login_message = "Failed"
                })
                .then(() => {
                    $('#btnContinue').removeClass("is-loading")
                    setTimeout(() => {
                        this.resetData()
                    }, 1500);
                })
        }
    },
    mounted() {
        document.title = "Start Event"
    },
    computed: {
        
    }
}
</script>
<style lang="scss" scoped>
    .logo{
        width: 10% 
    }
</style>