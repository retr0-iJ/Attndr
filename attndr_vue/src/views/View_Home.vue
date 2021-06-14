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
                <div class="column" v-if="isStartEventOn">
                    <router-link :to="{ name: 'Start_Event', params: { id: id, name: events.event_name }}" class="button is-link is-medium" v-if="events.event_name != ''">
                        Start Event
                    </router-link>
                </div>
            </div>
        </div>

        <div class="hero-body">
            <div class="event-column mb-6">
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
                { name: 'address', text: 'Address (City)' }
            ]
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
        isStartEventOn(){
            return new Date() >= new Date(this.events.date + ' ' + this.events.time_start)
        }
    },
    methods: {
        async getEventDetails() {            
            await axios
                .get("/api/v1/events/detail/" + this.id + "/")
                .then(response => {
                    this.events = response.data.event
                    this.events.participants = response.data.participant
                    $('#my-dt').DataTable({
                        data: this.events.participants,
                        columns: [
                            { data: "id", width: "5%" },
                            { data: "name", width: "30%" },
                            { data: "email", width: "30%" },
                            { data: "phone", width: "20%" },
                            { data: "city", width: "15%" },
                        ],
                        autoWidth: false
                    })
                })
                .catch(error => {
                    if(error.response){
                        console.log(JSON.stringify(error.response.data))
                    }else if(error.message){
                        console.log(JSON.stringify(error))
                    }
                    $('#my-dt').DataTable()
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