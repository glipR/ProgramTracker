<template>
  <v-container>
    <v-row>
      <v-col cols="12" lg="8"> <!-- Weeklies, freeze calendar -->
        <v-sheet >
          <h2 style="margin-bottom: 20px;">Weekly Problems</h2>
          <WeeklyProblems />
          <h2 style="margin-top: 40px; margin-bottom: 20px;">Freeze Calendar</h2>
          <StreakCalendar />
        </v-sheet>
      </v-col>
      <v-col cols="12" lg="4"> <!-- Recently solved problems by others -->
        <v-sheet>
          <h2 style="margin-bottom: 20px;">Recently Solved</h2>
          <RecentSubmissionList />
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
  import Vue from 'vue'
  import WeeklyProblems from './Dashboard/WeeklyProblems.vue';
  import StreakCalendar from './Dashboard/StreakCalendar.vue';
  import RecentSubmissionList from './Dashboard/RecentSubmissionList.vue';

  export default Vue.extend({
    name: 'UserDashboard',

    components: {
      WeeklyProblems,
      StreakCalendar,
      RecentSubmissionList,
    },
  })
</script>
