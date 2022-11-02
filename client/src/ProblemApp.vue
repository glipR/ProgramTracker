<template>
  <v-app>
    <TopBar />

    <v-main>
      <ProblemView/>
    </v-main>
  </v-app>
</template>

<script lang="ts">
import Vue from 'vue';
import ProblemView from './components/ProblemView.vue';
import TopBar from './components/TopBar.vue';

export default Vue.extend({
  name: 'App',

  components: {
    ProblemView,
    TopBar,
  },
});
</script>
