<template>
  <v-app-bar
    app
    color="primary"
    dark
    height="68px;"
  >
    <div class="d-flex align-center">
      <v-icon
        large
        color="white"
        aria-hidden="false"
      >mdi-balloon</v-icon>

      <h2 class="ml-2">ConstantTime</h2>
    </div>

    <v-spacer></v-spacer>

    <v-card rounded="0">
      <v-card-title>
        <v-avatar
          size="48"
          rounded="lg"
          class="text-center"
          style="margin-right: 10px;"
        >
          <img
            alt="user"
            src="../assets/logo.png"
            v-if="user_image"
          >
          <div v-else class="white--text" style="background-color: blue; width: 100%; height: 100%; font-size: 24px;">
            <p style="margin: 0; padding-top: 8px; padding-bottom: 8px">JG</p>
          </div>
        </v-avatar>
        <div style="display: block">
          <div>
            {{ user_data.username }}
          </div>
          <v-row class="text-center">
            <v-col cols="4">
              <v-icon
                color="red darken-2"
                aria-hidden="false"
                aria-label="Streak"
              >mdi-fire</v-icon>
              <span style="font-size: 14px; width: 33px; display: inline-block">
                x
              </span>
            </v-col>
            <v-col cols="4">
              <v-icon
                color="yellow darken-2"
                aria-hidden="false"
                aria-label="Coins"
              >mdi-checkbox-blank-circle</v-icon>
              <span style="font-size: 14px; width: 33px; display: inline-block">
                {{ user_data.info.coins }}
              </span>
            </v-col>
            <v-col cols="4">
              <v-icon
                color="blue darken-2"
                aria-hidden="false"
                aria-label="Freezes"
              >mdi-hexagon-slice-6</v-icon>
              <span style="font-size: 14px; width: 33px; display: inline-block">
                {{ user_data.info.freezes }}
              </span>
            </v-col>
          </v-row>
        </div>
      </v-card-title>
    </v-card>
  </v-app-bar>
</template>

<script lang="ts">
import Vue from 'vue';
import axios from 'axios';
import api_helper from '../utils/api_helper';

export default Vue.extend({
  name: 'TopBar',

  mounted() {
    api_helper.initialise();
    axios
      .get(api_helper.API_URL + "users/" + api_helper.USER_ID + "/")
      .then(response => {
        this.user_data = response.data;
      })
      .catch(error => {
        console.error(error);
      });
  },

  data: () => ({
    user_image: "",
    user_data: {},
  }),
});
</script>

<style>
.v-toolbar__content {
  padding-right: 0;
}
.v-card__title {
  padding-bottom: 0;
  padding-top: 0;
}
</style>