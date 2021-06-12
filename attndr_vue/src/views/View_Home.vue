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
                <div class="column">
                    <button class="button is-link is-medium">
                        Start Event
                    </button>
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

export default {
name: "View_Home",
    data(){
        return {
            columns: [
                { name: 'event_name', text: 'Event Name' },
                { name: 'speaker_name', text: 'Speaker Name' },
                { name: 'location', text: 'Location' },
                { name: 'date', text: 'Date' },
                { name: 'time', text: 'Time' },
                { name: 'quota', text: 'Quota' },
            ],
            events: {
                event_name: '',
                speaker_name: '',
                location: '',
                date: '',
                time_start: '',
                time_end: '',
                quota: ''
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
        this.getEventDetails()
    },
    computed: {
        getColumnsData(){
            return this.columns.map((column, i) => {
                if(column.name !== "time")
                    return{
                        column: column.text,
                        data: this.events[column.name]
                    }
                else
                    return{
                        column: column.text,
                        data: this.events["time_start"] + '-' + this.events["time_end"]
                    }
            })
        }
    },
    methods: {
        getEventDetails() {
            axios
                .get("http://localhost:8000/api/v1/events")
                .then(response => {
                    $('#my-dt').DataTable({
                        data: response.data,
                        columns: [
                            { data: "id", width: "5%" },
                            { data: "name", width: "50%" },
                            { data: "email", width: "50%" },
                            { data: "phone", width: "50%" },
                            { data: "address", width: "50%" },
                        ],
                        columnDefs: [
                        {
                            targets: [ -1,-2,-3 ],
                            searchable: false
                        },
                        {
                            targets: -1,
                            orderable: false
                        }
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