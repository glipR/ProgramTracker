<template>
  <v-app>

    <TopBar/>

    <v-main>
      <UserDashboard/>
    </v-main>

  </v-app>
</template>

<script lang="ts">
import Vue from 'vue';
import UserDashboard from './components/UserDashboard.vue';
import TopBar from './components/TopBar.vue';

import api_helper from './utils/api_helper';

export default Vue.extend({
  name: 'App',

  components: {
    UserDashboard,
    TopBar,
  },

  mounted() {
    api_helper.initialise();
  }

});
</script>
