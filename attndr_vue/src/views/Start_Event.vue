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
                                Seminar: Computational
                            </h3>
                        </div>
                        <div class="page-content">
                            <div class="input-user-credential container m-6" v-if="false">
                                <div class="columns is-vcentered is-flex-direction-column">
                                    <div class="column is-5 is-flex is-flex-direction-column is-align-items-center">
                                        <AnalogClock />
                                    </div>
                                    <div class="column is-5">
                                        <form>
                                            <div class="field">
                                                <div class="control">
                                                    <input class="input is-large" type="tel" id="phone" v-model="phone"
                                                        placeholder="Enter your phone number" onblur="this.focus()" autofocus>
                                                </div>
                                            </div>
                                        </form>
                                    </div>
                                </div>
                            </div>
                            <div class="show-qr m-4" v-if="true">
                                <div class="columns is-vcentered is-flex-direction-column">
                                    <div class="column is-5 is-flex is-flex-direction-column is-align-items-center">
                                        <img src="https://upload.wikimedia.org/wikipedia/commons/d/d0/QR_code_for_mobile_English_Wikipedia.svg">
                                    </div>
                                    <div class="column is-7">
                                        <p class="subtitle is-4">
                                            <span v-if="false">Please scan the QR Code above with your installed Attndr. on phone,</span> 
                                            <span v-else-if="phone">Login <span class="has-text-success">Successful</span> !</span>
                                            <span v-else>
                                                Login <span class="has-text-danger">Failed</span> ! Please try again.<br>
                                                If you are having issues, please kindly contact our nearby support.
                                            </span>
                                        </p>
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

export default {
    Name: 'Start_Event',
    components: {
        AnalogClock
    },
    data(){
        return{
            phone: ''
        }
    }
}
</script>
<style lang="scss" scoped>
    .logo{
        width: 10% 
    }
</style>