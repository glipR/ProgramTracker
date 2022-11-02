export default {
  API_URL: "http://127.0.0.1:8000/api/",
  USER_ID: "",
  PROBLEM_ID: "",

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

  updateLinkSubmissions() {
    // TODO
  }
}