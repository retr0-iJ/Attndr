<template>
    <section class="hero is-fullheight-with-navbar">
        <div id="modalContactUs" class="modal animate__animated">
            <div class="modal-background"></div>
            <div class="modal-content">
                <div class="box">
                    <div class="field has-text-centered">
                        <h3 class="title">Contact Us</h3>
                        <h6 class="subtitle is-6">Leave your message to our email.</h6>
                    </div>
                    <form action="">
                        <div class="field">
                            <div class="control has-icons-left">
                                <input class="input" type="text" name="email" id="email" 
                                    placeholder="Your Email">
                                <span class="icon is-small is-left">
                                    <i class="fa fa-envelope"></i>
                                </span>
                            </div>
                        </div>
                        <div class="field">
                            <div class="control">
                                <label for="subject" class="label">Subject</label>
                                <input class="input" type="text" name="subject" id="subject" 
                                    placeholder="The subject of your message">
                            </div>
                        </div>
                        <div class="field">
                            <div class="control">
                                <label for="body" class="label">Message</label>
                                <textarea name="body" id="body" class="textarea" rows="6"></textarea>
                            </div>
                        </div>
                        <div class="field has-text-centered">
                            <button class="button is-info is-fullwidth">
                                Send Message
                            </button>
                        </div>
                    </form>
                </div>
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
    name: "Landing Page",
    data(){
        return {

        }
    },
    created(){

    },
    methods: {

    },
    mounted(){
        (function($){
            $(() => {
                document.title = "Home"
            })

            $(function(){
                $("#contactUs").click(function() {
                    $("#modalContactUs")
                    .removeClass("animate__fadeOut")
                    .addClass("animate__fadeIn")
                    .addClass("is-active");
                });
            });

            $(function(){
                $("#modalContactUs .modal-close, .modal-background").click(function() {
                    $("#modalContactUs")
                        .removeClass("animate__fadeIn")
                        .addClass("animate__fadeOut")
                        .one("animationend", function(){
                            $(this).removeClass("is-active")
                        });
                });
            });
        }(jQuery));
    }
}
</script>