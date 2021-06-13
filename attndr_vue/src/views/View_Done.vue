<template>
    <div class="hero m-4 mt-5 ml-5">
        <div class="hero-head">
            <div class="columns is-vcentered">
                <div class="column is-5 mr-2">
                    <a @click="$router.go(-1)" class="is-size-4">
                        <span class="icon-text">
                            <span class="icon">
                                <i class="fas fa-chevron-left"></i>
                            </span>
                            <span>Back</span>
                        </span>
                    </a>
                </div>
            </div>
        </div>

        <div class="hero-body">
            <div class="event-column mb-5">
                <div class="columns is-vcentered" v-for="item in getColumnsData" :key="item.column">
                    <div class="column is-one-fifth">
                        <p class="title is-4">
                            {{ item.column }}
                        </p>
                    </div>
                    <div class="column">
                        <p class="subtitle is-4">
                            {{ item.data }}
                        </p>
                    </div>
                </div>
            </div>

            <div class="columns is-vcentered is-centered event-summarization mb-4">
                <div class="column is-4 event-performance has-text-centered">
                    <p class="title is-4">
                        Event Perfomarmance
                    </p>
                    <div class="holder">
                        <canvas
                            id="performChart" class="doughnut-chart">
                        </canvas>
                    </div>
                </div>
                <div class="column is-4 event-attendees has-text-centered">
                    <p class="title is-4">
                        Event Attendees
                    </p>
                    <div class="holder">
                        <canvas
                            id="attendeesChart" class="doughnut-chart">
                        </canvas>
                    </div>
                </div>
            </div>

            <div class="event-datatable">
                <p class="title is-4 mb-5">
                    List of Participants
                </p>
                <div class="columns m-4">
                    <table id="my-dt" class="table">
                    <thead>
                        <tr>
                            <th v-for="th in participantColumns" :key="th">
                                <div>
                                    <span>{{ th.text }}</span>
                                </div>
                            </th>
                        </tr>
                    </thead>
                    <tbody></tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import moment from 'moment'

export default {
    name: "View_Home",
    data(){
        return {
            id: 0,
            columns: [
                { name: 'event_name', text: 'Event Name' },
                { name: 'speaker_name', text: 'Speaker Name' },
                { name: 'location', text: 'Location' },
                { name: 'date', text: 'Date' },
                { name: 'time', text: 'Time' },
                { name: 'quota', text: 'Quota' },
            ],
            events: {
                id: '',
                event_name: '',
                speaker_name: '',
                location: '',
                date: '',
                time_start: '',
                time_end: '',
                quota: '',
                participants: []
            },
            participantColumns: [
                { name: 'id', text: 'ID' },
                { name: 'name', text: 'Name' },
                { name: 'email', text: 'Email' },
                { name: 'phone', text: 'Phone Number' },
                { name: 'address', text: 'Address (City)' },
                { name: 'time_in', text: 'Time In' },
                { name: 'time_out', text: 'Time Out' }
            ],
            chartOptions: {
                responsive: true, 
                maintainAspectRatio: false, 
                animation: {
                    animateRotate: false
                },
                plugins: {
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                return `${context.label}: ${context.parsed/context.dataset.data.reduce((total, num) => {return total + num})*100}%`;
                            }
                        }
                    }
                }
            },
            createEmptyChart: {
                type: 'doughnut',
                data: {
                    labels: ['No Data'],
                    datasets: [{
                        label: ['Dataset 1'],
                        data: [1],
                        backgroundColor: '#006ca3'
                    }],
                },
                options: {
                    responsive: true, 
                    maintainAspectRatio: false, 
                    animation: {
                        animateRotate: false
                    },
                    plugins: {
                        tooltip: {
                            callbacks: {
                                label: function(context) {
                                    return `${context.label}`;
                                }
                            }
                        }
                    }
                }
            },
            performChartData: {
                labels: ['Boring', 'Not Bad', 'Great'],
                datasets: [
                    {
                        backgroundColor: [ '#006ca3', '#0098bc', '#00c4cc'],
                        data: [1]
                    },
                ]
            },
            attendeesChartData: {
                labels: ['Absent', 'Present'],
                datasets: [
                    {
                        backgroundColor: [ '#006ca3', '#0098bc' ],
                        data: [1]
                    },
                ]
            }
        }
    },
    created() {
        this.id = this.$route.params.id
        this.getEventDetails()
    },
    computed: {
        getColumnsData(){
            return this.columns.map((column, i) => {
                if(!["date", "time"].includes(column.name))
                    return{
                        column: column.text,
                        data: this.events[column.name]
                    }
                else if(column.name === "date")
                    return{
                        column: column.text,
                        data: moment(this.events.date).format("DD MMMM YYYY")
                    }
                else
                    return{
                        column: column.text,
                        data: moment(this.events.time_start, "HH:mm:ss").format("HH:mm") + '-' + moment(this.events.time_end, "HH:mm:ss").format("HH:mm")
                    }
            })
        },
    },
    methods: {
        async getEventDetails() {            
            await axios
                .get("/api/v1/events/detail/" + this.id + "/")
                .then(response => {
                    this.events = response.data
                    axios
                        .get("/api/v1/events/participant/" + this.events.id + "/")
                        .then(response => {
                            this.events.participants = response.data
                            axios
                            .get("/api/v1/events/attendance/" + this.events.id + "/")
                            .then(response => {
                                let op = this.events.participants.map((e,i) => {
                                    let temp = response.data.find(element => element.participant_id === e.id)
                                    if(temp.event_id){
                                        e.time_in = temp.time_in
                                        e.time_out = temp.time_out
                                    }
                                    return e
                                })
                                $('#my-dt').DataTable({
                                    data: this.events.participants,
                                    columns: [
                                        { data: "id", width: "5%" },
                                        { data: "name", width: "25%" },
                                        { data: "email", width: "25%" },
                                        { data: "phone", width: "15%" },
                                        { data: "city", width: "10%" },
                                        { data: "time_in", width: "10%" },
                                        { data: "time_out", width: "10%" },
                                    ],
                                    autoWidth: false,
                                    createdRow: function(row, data, dataIndex){
                                        if(data.time_in === '')
                                            $(row).css({"background-color": "red"})
                                    }
                                })
                            }).catch(error => {
                                if(error.response){
                                    console.log(JSON.stringify(error.response.data))
                                }else if(error.message){
                                    console.log(JSON.stringify(error))
                                }
                                $('#my-dt').DataTable()
                                var performChart = new Chart($('#performChart'), this.createEmptyChart)
                                var eventChart = new Chart($('#attendeesChart'), this.createEmptyChart)
                            })
                        }).catch(error => {
                            if(error.response){
                                console.log(JSON.stringify(error.response.data))
                            }else if(error.message){
                                console.log(JSON.stringify(error))
                            }
                            $('#my-dt').DataTable()
                            var performChart = new Chart($('#performChart'), this.createEmptyChart)
                            var eventChart = new Chart($('#attendeesChart'), this.createEmptyChart)
                        })
                })
                .catch(error => {
                    if(error.response){
                        console.log(JSON.stringify(error.response.data))
                    }else if(error.message){
                        console.log(JSON.stringify(error))
                    }
                    $('#my-dt').DataTable()
                    var performChart = new Chart($('#performChart'), this.createEmptyChart)
                    var eventChart = new Chart($('#attendeesChart'), this.createEmptyChart)
                })
        }
    }
}
</script>
<style lang="scss" scoped>
    #my-dt{
        width: 100%
    }
</style>