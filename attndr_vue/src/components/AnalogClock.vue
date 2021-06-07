<template>
    <div class="times is-flex is-flex-direction-column is-align-items-center has-text-centered">
        <div class="clock">

            <div class="hour">
                <div class="hr" id="hr">
                    
                </div>
            </div>

            <div class="min">
                <div class="mn" id="mn">

                </div>
            </div>

            <div class="sec">
                <div class="sc" id="sc">

                </div>
            </div>

        </div>
        <div class="timestamp m-4">
            <h4 class="title is-4 has-text-weight-normal">{{ timestamp }}</h4>
        </div>
    </div>
</template>
<script>
import moment from 'moment'

export default {
    Name: 'AnalogClock',
    data() {
        return{
            timestamp: ''
        }
    },
    mounted() {
        const deg = 6; 

        const hr = document.querySelector('#hr');
        const mn = document.querySelector('#mn');
        const sc = document.querySelector('#sc');


        setInterval(() => {
            
            let day = new Date();
            this.timestamp = moment(day).format("MMMM Do YYYY, hh:mm:ss a")
            let hh = day.getHours() * 30;
            let mm = day.getMinutes() * deg;
            let ss = day.getSeconds() * deg;
                        
            hr.style.transform = `rotateZ(${(hh) + (mm / 12)}deg)`;
            mn.style.transform = `rotateZ(${mm}deg)`;
            sc.style.transform = `rotateZ(${ss}deg)`;

        })
    }
}
</script>
<style>
@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@500&display=swap');

.clock {
    width: 150px;
    height: 150px;
    display: flex;
    justify-content: center;
    align-items: center;
    background: url(../assets/clock.png);
    background-size: cover;
    border: 4px;
    /* box-shadow: 15px 15px 15px rgba(255, 255, 255, 0.5); */
    box-shadow: 0em -1.2em 1.2em rgba(255, 255, 255, 0.06),
                inset 0em -1.2em 1.2em rgba(255, 255, 255, 0.06),
                0em 0.5em 0.5em rgba(0, 0, 0, 0.3),
                inset 0em 1.2em 1.2em rgba(0, 0, 0, 0.3);
    border-radius: 50%;
}

.clock :hover {
    /* yet to be completed; when hovered, diplay complete information about time, `new Date().toLocaleString();` */
    cursor: pointer;

}



/* The small circle int the center */
.clock:before {
    content: '';
    position: absolute;
    width: 8px;
    height: 8px;
    background: #1a74be;
    border-radius: 50%;

    /* The z-index property specifies the stack order of an element.
    /* An element with greater stack order is always in front of an element with a lower stack order.  */
    /* Note: z-index only works on positioned elements (position: absolute, position: relative, position: fixed, or position: sticky). */
    z-index: 10000;
    /* kept as a high value, since wanted at top */
}


.clock .hour,
.clock .min,
.clock .sec {
    position: absolute;
}

/* length of respective arms; */
.clock .hour, .hr {
    width: 75px;
    height: 75px;
} 

.clock .min, .mn {
    width: 110px;
    height: 110px;
}

.clock .sec, .sc {
    width: 125px;
    height: 125px;
}


.hr, .mn, .sc {
    display: flex;
    justify-content: center;
    position: absolute;
    border-radius: 50%;
    
}


.hr:before {
    content: '';
    position: absolute;
    width: 5px;
    height: 40px;
    background: #f81460;
    z-index: 10;
    /* z-index least */
    border-radius: 2.8px;
}

.mn:before {
    content: '';
    position: absolute;
    width: 3px;
    height: 55px;
    background: #091921;
    z-index: 11;
    /* z-index more than hour hand */
    border-radius: 3px;
}


.sc:before {
    content: '';
    position: absolute;
    width: 1px;
    height: 65px;
    background: #0075fa80;
    z-index: 12;
    /* z-index more than hour minute hand */
    border-radius: 3px;
}
</style>