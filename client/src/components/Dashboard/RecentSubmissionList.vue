<template>
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
</template>

<script lang="ts">
  import Vue from 'vue'
  import axios from 'axios'
  import api_helper from "../../utils/api_helper";

  export default Vue.extend({
    name: 'RecentSubmissionList',

    mounted() {
      axios
        .get(api_helper.API_URL + "submissions/")
        .then(response => {
          this.recent_submissions = response.data.results;
          this.recent_submissions.splice(9);
        })
        .catch(error => {
          console.log(error);
        })
        .finally(() => this.loading = false);
    },

    data: () => ({
      recent_submissions: [],
      loading: true,
    }),
  })
</script>