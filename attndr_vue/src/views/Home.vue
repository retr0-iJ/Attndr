<template>
  <div class="hero m-4 mt-5">
    <div id="modalAddEvent" class="modal animate__animated">
        <div class="modal-background"></div>
        <div class="modal-content">
            <div class="box">
                <div class="field levels">
                  <div class="level-left">
                    <i class="fa fa-calendar-alt fa-2x level-item"></i>
                    <h3 class="title level-item">Add Event</h3>
                  </div>
                </div>
                <hr>
                <form action="">
                    <div class="field">
                        <div class="control">
                            <input class="input" type="text" id="event_nameInput" v-model="event_name" 
                                placeholder="Event Name">
                        </div>
                    </div>
                    <div class="field">
                        <div class="control">
                            <input class="input" type="text" id="speaker_nameInput" v-model="speaker_name" 
                                placeholder="Speaker Name">
                        </div>
                    </div>
                    <div class="field">
                        <div class="control">
                            <input class="input" type="text" id="locationInput" v-model="location" 
                                placeholder="Location">
                        </div>
                    </div>
                    <div class="field">
                        <div class="control">
                            <input class="input" type="date" id="dateInput" v-model="date"
                                placeholder="Date">
                            <!-- <span class="icon is-small is-right">
                                <i class="fa fa-calendar-plus"></i>
                            </span> -->
                        </div>
                    </div>
                    <div class="field">
                        <div class="control has-icons-right">
                            <input class="input" type="time" id="time_startInput" v-model="time_start"
                                placeholder="Time Start">
                            <!-- <span class="icon is-small is-right">
                                <i class="fa fa-clock"></i>
                            </span> -->
                        </div>
                    </div>
                    <div class="field">
                        <div class="control has-icons-right">
                            <input class="input" type="time" id="time_endInput" v-model="time_end"
                                placeholder="Time End">
                            <!-- <span class="icon is-small is-right">
                                <i class="fa fa-clock"></i>
                            </span> -->
                        </div>
                    </div>
                    <div class="field">
                        <div class="control has-icons-right">
                            <input class="input" type="text" id="list_participants" v-model="list_participants"
                                placeholder="List Of Participants">
                            <span class="icon is-small is-right">
                                <i class="fa fa-folder-plus"></i>
                            </span>
                        </div>
                    </div>
                    <hr>
                    <div class="levels">
                        <div class="level-right">
                          <button id="btnCancel" class="button px-6 level-item">Cancel</button>
                          <button id="btnSubmit" class="button px-6 is-info level-item">Submit</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
        <button class="modal-close is-large" aria-label="close"></button>
    </div>
    <div class="hero-head">
      <div class="level">
        <div class="level-left">
          <div class="level-item page-title">
            <h3 class="title is-3 has-text-grey-dark">
              Upcoming Events
            </h3>
          </div>
          <div class="level-item add-button">
            <button id="btnAddEvent" class="button is-link is-medium is-align-items-center">
              <i class="fa fa-plus fa-sm"></i>
              <span class="ml-2">Add Event</span>
            </button>
          </div>
        </div>
      </div>
    </div>
    <div class="hero-body">
      <div class="columns">
        <table id="my-dt" class="table">
          <thead>
              <tr>
                  <th v-for="th in columns" :key="th">
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
</template>

<script>
import axios from 'axios'
import moment from 'moment'

export default {
  name: 'Home',
  data() {
    return {
      columns: [
        { name: 'id', text: 'ID' },
        { name: 'event_name', text: 'Event Name' },
        { name: 'date', text: 'Date' },
        { name: 'time', text: 'Time' },
        { name: 'quota', text: 'Quota' },
        { name: 'action', text: 'Action' }
      ],
      event_name: '',
      speaker_name: '',
      location: '',
      date: Date,
      time_start: '',
      time_end: '',
      list_participants: '',
    }
  },
  components: {
  },
  created() {
    this.getAllUserEvents()
  },
  mounted() {
    (function($){
      document.title = "Home"
      $(function(){
        $("#btnAddEvent").click(function() {
            $("#modalAddEvent")
            .removeClass("animate__fadeOut")
            .addClass("animate__fadeIn")
            .addClass("is-active");
        });
      });

      $(function(){
        $("#modalAddEvent .modal-close, #btnCancel").click(function() {
            $("#modalAddEvent")
                .removeClass("animate__fadeIn")
                .addClass("animate__fadeOut")
                .one("animationend", function(){
                    $(this).removeClass("is-active")
                });
        });
      });
    }(jQuery))
  },
  methods: {
    getAllUserEvents() {
      axios
        .get("/api/v1/events")
        .then(response => {
          $('#my-dt').DataTable({
            data: response.data,
            columns: [
              { data: "id", width: "5%" },
              { data: "event_name", width: "50%" },
              { 
                data: "date", 
                render: function(data, type, row){
                  return moment(row.date).format("DD MMMM YYYY")
                },
                width: "12%" 
              },
              { 
                data: "time", 
                render: function(data, type, row){
                  return moment(row.time_start, "HH:mm:ss").format("HH:mm") + '-' + moment(row.time_end, "HH:mm:ss").format("HH:mm")
                },
                width: "14%" 
              },
              { data: "quota", width: "10%" },
              {
                data: "action",
                render: function(data, type, row){
                  return '<div class="action-buttons buttons are-small is-flex-direction-row"><router-link to="" id="btnView" class="button is-info py-0 px-2">VIEW</router-link><router-link to="" id="btnDelete" class="button is-danger py-0 px-2">DELETE</router-link></div>'
                },
                width: "10%"
              }
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