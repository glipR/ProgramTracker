import axios from 'axios';

type CF_OBJ = {
  handle: string,
  last_created_submission_id: number,
  last_created_submission_time: number,
}
type CF_submission_return = {
  creationTimeSeconds: number,
  id: number,
  verdict: string,
}

type USER_DATA = {
  id: number,
  info: {
    coins: number,
    freezes: number,
    rating: number,
  },
  username: string,
  codeforces: CF_OBJ[],
}

const def_user_data:USER_DATA = {
  id: -1,
  info: {
    coins: 0,
    freezes: 0,
    rating: 0,
  },
  username: '',
  codeforces: [],
};


export default {
  API_URL: "http://127.0.0.1:8000/api/",
  USER_ID: "",
  PROBLEM_ID: "",

  user_data: def_user_data,

  initialise() {
    this.USER_ID = document.getElementById("user_id_read")?.innerHTML || "";
    this.PROBLEM_ID = document.getElementById("problem_id_read")?.innerHTML || "";
  },

  hasCurrentUser() {
    return this.USER_ID != "";
  },

  hasCurrentProblem() {
    return this.PROBLEM_ID != "";
  },

  async updateLinkSubmissions() {
    await axios
      .get(this.API_URL + "users/" + this.USER_ID + "/")
      .then(response => {
        this.user_data = response.data;
      })
      .catch(error => {
        console.error(error);
      });
    // CodeForces.
    let at_end = false;
    let start = 1;
    const batch_size = 20;
    const submissions:CF_submission_return[] = [];
    const non_ok:CF_submission_return[] = [];
    while (!at_end) {
      const cf_obj = this.user_data.codeforces[0];
      console.log(start);
      await axios
        .get("https://codeforces.com/api/user.status?handle=" + cf_obj.handle + "&from=" + start + "&count=" + batch_size)
        .then(response => {
          for (let idx=0; idx<response.data.result.length; idx++) {
            const sub:CF_submission_return = response.data.result[idx];
            if (sub.creationTimeSeconds < cf_obj.last_created_submission_time || cf_obj.last_created_submission_id == sub.id) {
              at_end = true;
              break;
            }
            if (sub.verdict == "OK") submissions.push(sub);
            else non_ok.push(sub);
          }
          start = start + response.data.result.length;
          if (response.data.result.length == 0) {
            at_end = true;
          }
        })
        .catch(error => {
          console.error(error);
        })
        .finally(() => {
          return new Promise<void>((resolve, reject) => setTimeout(resolve, 3000));
        });
    }
    await axios
      .post(this.API_URL + "links/cf/add_submissions/", {
        user_id: this.USER_ID,
        submissions: submissions,
      })
      .then()
      .catch(error => {
        console.error(error);
      });
  }
}