<template>
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
</template>

<script lang="ts">
  import Vue from 'vue';
  import axios from 'axios';
  import api_helper from '../../utils/api_helper';

  export default Vue.extend({
    name: 'WeeklyProblems',

    mounted() {
      api_helper.initialise();
      axios
        .get(api_helper.API_URL + "weeklies/get_user_weeklies/", { params: { user_id: api_helper.USER_ID} })
        .then(response => {
          this.weeklies = response.data.problem_list;
        })
        .catch(error => {
          console.log(error);
        })
        .finally(() => this.loading = false);
    },

    methods: {
    },

    data: () => ({
      weeklies: [],
      loading: true,
    }),
  })
</script>