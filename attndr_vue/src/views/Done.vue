<template>
  <div class="hero m-4 mt-5">
    <div class="hero-head">
      <div class="level">
        <div class="level-left">
          <div class="level-item page-title">
            <h3 class="title is-3 has-text-grey-dark">
              Done Events
            </h3>
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
        .get("http://localhost:8000/api/v1/events")
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
                  return '<div class="action-buttons buttons are-small is-flex-direction-row"><router-link to="" id="btnView" class="button is-info py-0 px-2">VIEW</router-link></div>'
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