var app = new Vue({
    el: '#interview',
    data: {
      interview: ''
    },
    mounted() {
        url = document.location.pathname;
        axios
          .get("http://127.0.0.1:8000/api"+url)
          .then(response => (this.interview = response.data));
      },
  })