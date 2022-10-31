<template>
  <v-container>
    <h1>{{ problem_info.name }}</h1>
    <!-- TODO: Subtext / Link. Tags, Difficulty etc. -->
    <v-row>
      <v-col cols="12" lg="6"> <!-- Problem Window 1 - Statement -->
        <v-sheet >
          Problem Text
          {{ problem_info }}

          <a :href="get_site_link()" target="_blank">View on CodeForces</a>

          <div class="ttypography">
            <div id="send_site_content"></div>
          </div>
        </v-sheet>
      </v-col>
      <v-col cols="12" lg="6"> <!-- Problem Window 2 - Code and Other -->
        <v-sheet >
          Code
          <div id="code_spot" style="height: 50vh"></div>
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
  import Vue from 'vue'
  import axios from 'axios'
  import * as monaco from 'monaco-editor';

  const API_URL = "http://127.0.0.1:8000/api/";
  const USER_ID = 1;

  declare global {
    interface Window { MathJax: any; }
  }

  export default Vue.extend({
    name: 'ProblemView',

    mounted() {
      this.problem_id = document.getElementById("problem_id_read")?.innerHTML || "";
      axios
        .get(API_URL + "problems/" + this.problem_id + "/get_statement/")
        .then(response => {
          var send_site_content = document.getElementById("send_site_content");
          if (send_site_content === null) return;
          send_site_content.innerHTML = response.data.join("");
          var statement = send_site_content.getElementsByClassName("problem-statement")[0]
          send_site_content.replaceWith(statement);
          window.MathJax.typeset();
          statement.removeChild(statement.getElementsByClassName("header")[0]);
        })
        .catch(error => {
          console.error(error);
        });
      axios
        .get(API_URL + "problems/" + this.problem_id + "/")
        .then(response => {
          this.problem_info = response.data;
        })
        .catch(error => {
          console.error(error);
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
            .finally(() => {
              this.loading = false;
              var spot = document.getElementById("code_spot");
              if (spot != null)
                monaco.editor.create(spot, {
                  value: ['def test():', '\tprint("Hello world!")'].join('\n'),
                  language: 'python'
                });
            })
        );
    },

    methods: {
      get_site_link() {
        return "https://codeforces.com/problemset/problem/" + this.problem_info.problem_id + "/"
      }
    },

    data: () => ({
      problem_id: '',
      problem_info: {
        problem_id: '',
      },
      recent_submissions: [],
      loading: true,
    }),
  })
</script>

<style>

@import "@/assets/codeforces_typography.css";
@import "@/assets/problem_statement.css";

.problem-statement p {
  font-size: 14px!important;
  line-height: 19.6px!important;
}
.problem-statement pre {
  font-size: 12.6px!important;
  line-height: 15.75px!important;
}

.problem-statement .section-title {
  font-size: 20px;
}

.problem-statement .sample-tests .title {
  font-size: 15px!important;
  font-family: Consolas, lucida console, andale mono, bitstream vera sans mono, courier new, Courier, monospace!important;
}

</style>