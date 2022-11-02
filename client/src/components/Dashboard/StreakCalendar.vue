<template>
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
</template>

<script lang="ts">
  import Vue from 'vue'

  export default Vue.extend({
    name: 'StreakCalendar',


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
    }),
  })
</script>