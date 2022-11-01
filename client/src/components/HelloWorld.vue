<template>
  <v-container>
    <v-row>
      <v-col cols="12" lg="8"> <!-- Weeklies, freeze calendar -->
        <v-sheet >
          <h2 style="margin-bottom: 20px;">Weekly Problems</h2>
          <v-row v-if="!loading">
            <v-col cols="12" sm="4" v-for="problem in weeklies" v-bind:key="problem.problem_id">
              <v-btn
                elevation="7"
                x-large
                width="100%"
                height="150"
                color="green"
                class="text-center"
                :href="'/problems/'+problem.id"
                target="_blank"
                dark
              >
                <v-row style="display: block; padding: 20px;">
                  <v-col cols="12" style="height: 30px;">
                  </v-col>
                  <v-col cols="12">
                    {{ problem.name }}
                    <v-divider></v-divider>
                    <small>{{ problem.source }} {{ problem.problem_id }}</small>
                  </v-col>
                  <v-col cols="12" style="height: 30px;">
                    {{ problem.coin_value }} <v-icon
                      color="yellow darken-2"
                    >mdi-checkbox-blank-circle</v-icon> 1 <v-icon
                      color="blue darken-2"
                    >mdi-hexagon-slice-6</v-icon>
                  </v-col>
                </v-row>
              </v-btn>
            </v-col>
          </v-row>
          <v-row v-else>
            <v-progress-circular
              indeterminate
              color="primary"
            ></v-progress-circular>
          </v-row>
          <h2 style="margin-top: 40px; margin-bottom: 20px;">Freeze Calendar</h2>
          <v-calendar
            :weekdays="[0, 1, 2, 3, 4, 5, 6]"
            type="month"
          >
            <template v-slot:day="{ }">
              <div>
              </div>
            </template>
            <template v-slot:day-label="{ day, date }">
              <div
                :style="'min-height: 30px; background-color: ' + (date == today() ? 'rgb(251, 192, 45)' : 'rgba(0, 0, 0, 0)')"
              >
                <v-btn 
                  v-if="streakDays()[0].includes(date) || streakDays()[1].includes(date)"
                  :color="streakDays()[0].includes(date) ? 'green' : 'rgb(25, 118, 210)'"
                >
                  {{ day }}
                </v-btn>
                <span v-else>
                  {{ day }}
                </span>
              </div>
            </template>
          </v-calendar>
        </v-sheet>
      </v-col>
      <v-col cols="12" lg="4"> <!-- Recently solved problems by others -->
        <v-sheet>
          <h2 style="margin-bottom: 20px;">Recently Solved</h2>
          <v-card
            tile
            v-if="!loading"
          >
            <v-list-item two-line v-for="sub in recent_submissions" v-bind:key="sub.submission_id">
              <v-list-item-content>
                <v-list-item-title>{{ sub.problem.name }}</v-list-item-title>
                <v-list-item-subtitle>Solved by {{ sub.user.username }}</v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </v-card>
          <v-card v-else>
            <v-progress-circular
              indeterminate
              color="primary"
            ></v-progress-circular>
          </v-card>
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
  import Vue from 'vue'
  import axios from 'axios'

  const API_URL = "http://127.0.0.1:8000/api/";
  const USER_ID = 1

  export default Vue.extend({
    name: 'HelloWorld',

    mounted() {
      axios
        .get(API_URL + "weeklies/get_user_weeklies/", { params: { user_id: USER_ID} })
        .then(response => {
          this.weeklies = response.data.problem_list;
        })
        .catch(error => {
          console.log(error);
        })
        .finally(() => 
          axios
            .get(API_URL + "submissions/")
            .then(response => {
              this.recent_submissions = response.data.results;
              this.recent_submissions.splice(9);
            })
            .catch(error => {
              console.log(error);
            })
            .finally(() => this.loading = false)
        );
    },

    methods: {
      streakDays() {
        var d1 = new Date("Nov 2 2022");
        var d2 = new Date("Nov 1 2022");
        var d3 = new Date("Oct 31 2022");
        return [
          [d1.toISOString().split("T")[0], d3.toISOString().split("T")[0]],
          [d2.toISOString().split("T")[0]]
        ]
      },
      today() {
        var d1 = new Date();
        return d1.toISOString().split("T")[0];
      }
    },

    data: () => ({
      weeklies: [],
      recent_submissions: [],
      loading: true,
    }),
  })
</script>
