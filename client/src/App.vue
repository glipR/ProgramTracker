<template>
  <v-app>

    <v-main>
      <HelloWorld/>
    </v-main>

    <!-- Ensure toolbar is rendered on-top. -->
    <v-card
      elevation="1"
      style="position: fixed; right: 0; top: 0;"
    >
      <v-card-title>
        <v-avatar
          size="48"
          rounded="lg"
          class="text-center"
          style="margin-right: 10px;"
        >
          <img
            alt="user"
            src="./assets/logo.png"
            v-if="user_image"
          >
          <div v-else class="white--text" style="background-color: blue; width: 100%; height: 100%; font-size: 24px;">
            <p style="margin: 0; padding-top: 8px; padding-bottom: 8px">JG</p>
          </div>
        </v-avatar>
        <v-sheet>
          <div>
            {{ user_data.username }}
          </div>
          <v-row class="text-center">
            <v-col cols="4">
              <v-icon
                color="red darken-2"
              >mdi-fire</v-icon>
              <span style="font-size: 14px; width: 33px; display: inline-block">
                x
              </span>
            </v-col>
            <v-col cols="4">
              <v-icon
                color="yellow darken-2"
              >mdi-checkbox-blank-circle</v-icon>
              <span style="font-size: 14px; width: 33px; display: inline-block">
                {{ user_data.info.coins }}
              </span>
            </v-col>
            <v-col cols="4">
              <v-icon
                color="blue darken-2"
              >mdi-hexagon-slice-6</v-icon>
              <span style="font-size: 14px; width: 33px; display: inline-block">
                {{ user_data.info.freezes }}
              </span>
            </v-col>
          </v-row>
        </v-sheet>
      </v-card-title>
    </v-card>

  </v-app>
</template>

<script lang="ts">
import Vue from 'vue';
import HelloWorld from './components/HelloWorld.vue';
import axios from 'axios';

const API_URL = "http://127.0.0.1:8000/api/";

export default Vue.extend({
  name: 'App',

  components: {
    HelloWorld,
  },

  mounted() {
    this.user_id = document.getElementById("user_id_read")?.innerHTML || "";
    axios
      .get(API_URL + "users/" + this.user_id + "/")
      .then(response => {
        this.user_data = response.data;
      })
      .catch(error => {
        console.error(error);
      });
  },

  data: () => ({
    user_image: "",
    user_id: "",
    user_data: {},
  }),
});
</script>
