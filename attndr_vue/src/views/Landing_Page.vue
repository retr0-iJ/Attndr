<template>
    <section class="hero is-fullheight-with-navbar">
        <div class="modal">
            <div class="modal-background"></div>
            <div class="modal-content">
                <span>aaaa</span>
            </div>
            <button class="modal-close is-large" aria-label="close"></button>
        </div>
        <div class="hero-body p-0">
            <div class="columns is-vcentered">
                <div class="column ml-6">
                    <div class="title">
                        <h3 class="title is-3">
                            Managing Attendance Administration Never Been Easier.
                        </h3>
                    </div>
                    <div class="description mb-5">
                        <p>
                            Attendance is an important factor in an organization or event in achieving goals. 
                            Attendance will affect the discipline of participants in order to gathering 
                            information about quality of human resources. It is very important to have an 
                            Attendance Management System to assist an organization or event on monitoring, 
                            tracking, and managing participant attendance. Attndr offers you the best Attendance
                            Management System, that rely on three principles: Systematic, Simplicity, and 
                            Efficiency. 
                        </p>
                    </div>
                    <div class="buttons">
                        <router-link to="/register" class="button is-black is-rounded mr-4">
                            Join Us Now
                        </router-link>
                        <button id="contactUs" class="button is-rounded">
                            Contact Us
                        </button>
                    </div>
                </div>
                <div class="column has-text-centered">
                    <figure class="image is-4by3">
                        <img src="@/assets/img/landing-photo.jpg">
                    </figure>
                    <a href='https://www.freepik.com/vectors/business' target="_blank" class="is-size-7">
                        Picture attribute
                    </a>
                </div>
            </div>
        </div>
        <div class="hero-footer">
            <hr class="mt-0">
            <div class="column is-12 ml-3">
                <p>
                    Attndr is a simple, yet solid solution to Attendance Management System problem. 
                    It offers a great experience on managing Event Attendance. Attndr utilizes One-Time Password 
                    (OTP) concept in the form of Quick Response Code (QR Code). It consisted of a web-based 
                    framework as well as a mobile application to record participant attendance at events, in a 
                    systematic, secure, and efficient manner. 
                </p>
            </div>
        </div>
    </section>
</template>
<script>
export default {
    data(){
        return {

        }
    },
    created(){

    },
    methods: {

    },
    mounted(){
        $("#contactUs").click(function() {
            $(".modal").addClass("is-active");  
        });

        $(".modal-close").click(function() {
            $(".modal").removeClass("is-active");
        });
    }
}
</script>