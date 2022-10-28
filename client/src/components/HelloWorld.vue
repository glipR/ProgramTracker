<template>
  <v-container>
    <v-row>
      <v-col cols="12" lg="8"> <!-- Weeklies, freeze calendar -->
        <v-sheet >
          <h2 style="margin-bottom: 20px;">Weekly Problems</h2>
          <v-row>
            <v-col cols="12" sm="4">
              <v-btn
                elevation="7"
                x-large
                width="100%"
                height="150"
                color="green"
                dark
              >
                <v-row style="display: block; padding: 20px;">
                  <v-col cols="12" style="height: 30px;">
                  </v-col>
                  <v-col cols="12">
                    Problem Name
                    <v-divider></v-divider>
                    <small>CF 802/C</small>
                  </v-col>
                  <v-col cols="12" style="height: 30px;">
                    1500 Coins
                  </v-col>
                </v-row>
              </v-btn>
            </v-col>
            <v-col cols="12" sm="4">
              <v-btn
                elevation="7"
                x-large
                width="100%"
                height="150"
                color="red"
                dark
              >
                <v-row style="display: block; padding: 20px;">
                  <v-col cols="12" style="height: 30px;">
                  </v-col>
                  <v-col cols="12">
                    Problem Name
                    <v-divider></v-divider>
                    <small>CF 802/C</small>
                  </v-col>
                  <v-col cols="12" style="height: 30px;">
                    1500 Coins
                  </v-col>
                </v-row>
              </v-btn>
            </v-col>
            <v-col cols="12" sm="4">
              <v-btn
                elevation="7"
                x-large
                width="100%"
                height="150"
                color="red"
                dark
              >
                <v-row style="display: block; padding: 20px;">
                  <v-col cols="12" style="height: 30px;">
                  </v-col>
                  <v-col cols="12">
                    Problem Name
                    <v-divider></v-divider>
                    <small>CF 802/C</small>
                  </v-col>
                  <v-col cols="12" style="height: 30px;">
                    1500 Coins
                  </v-col>
                </v-row>
              </v-btn>
            </v-col>
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
              <div style="min-height: 30px">
                <v-btn 
                  v-if="streakDays()[0].includes(date) || streakDays()[1].includes(date)"
                  :color="streakDays()[0].includes(date) ? 'green' : 'blue'"
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
          >
            <v-list-item two-line>
              <v-list-item-content>
                <v-list-item-title>Card Game</v-list-item-title>
                <v-list-item-subtitle>Solved by xyz</v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
            <v-list-item two-line>
              <v-list-item-content>
                <v-list-item-title>Diabolical Defuser</v-list-item-title>
                <v-list-item-subtitle>Solved by noone</v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </v-card>
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
  import Vue from 'vue'

  export default Vue.extend({
    name: 'HelloWorld',

    methods: {
      streakDays() {
        var d1 = new Date("Oct 26 2022");
        var d2 = new Date("Oct 25 2022");
        var d3 = new Date("Oct 24 2022");
        var d4 = new Date("Oct 23 2022");
        return [
          [d1.toISOString().split("T")[0], d3.toISOString().split("T")[0], d4.toISOString().split("T")[0]],
          [d2.toISOString().split("T")[0]]
        ]
      }
    },

    data: () => ({
      ecosystem: [
        {
          text: 'vuetify-loader',
          href: 'https://github.com/vuetifyjs/vuetify-loader',
        },
        {
          text: 'github',
          href: 'https://github.com/vuetifyjs/vuetify',
        },
        {
          text: 'awesome-vuetify',
          href: 'https://github.com/vuetifyjs/awesome-vuetify',
        },
      ],
      importantLinks: [
        {
          text: 'Documentation',
          href: 'https://vuetifyjs.com',
        },
        {
          text: 'Chat',
          href: 'https://community.vuetifyjs.com',
        },
        {
          text: 'Made with Vuetify',
          href: 'https://madewithvuejs.com/vuetify',
        },
        {
          text: 'Twitter',
          href: 'https://twitter.com/vuetifyjs',
        },
        {
          text: 'Articles',
          href: 'https://medium.com/vuetify',
        },
      ],
      whatsNext: [
        {
          text: 'Explore components',
          href: 'https://vuetifyjs.com/components/api-explorer',
        },
        {
          text: 'Select a layout',
          href: 'https://vuetifyjs.com/getting-started/pre-made-layouts',
        },
        {
          text: 'Frequently Asked Questions',
          href: 'https://vuetifyjs.com/getting-started/frequently-asked-questions',
        },
      ],
    }),
  })
</script>
