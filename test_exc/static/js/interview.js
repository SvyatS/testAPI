var app = new Vue({
    el: '#interviews',
    data: {
      interview_list: ''
    },
    mounted() {
        axios
          .get("http://127.0.0.1:8000/api/interviews/")
          .then(response => (this.interview_list = response.data));
      },
  })