<template>
  <div>
    <div>
      <h2>Please Log In</h2>
      <div id="loginForm">
        <form v-on:submit.prevent="submitForm">
          <p>
            <input class="w3-input" name="username" placeholder="Enter your ID" v-model="username"><br>
          </p>
          <p>
            <input name="password" class="w3-input" placeholder="Enter your password" v-model="password" type="password">
          </p>
          <p>
            <button type="submit" class="w3-button w3-green w3-round">Login</button>
          </p>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data: function() {
    return {
      username: '',
      password: '',
    }
  },
  methods: {
    submitForm: function() {
      // event.preventDefault();
      let self = this;
      console.log(this.username, this.password);
      const url = 'http://10.1.30.202:5000/login';
      const data = JSON.stringify({
        username: this.username,
        password: this.password
      })
      axios.post(url, data, {
        headers: {
            "Content-Type": `application/json`,
          },
      })
        .then(function(response) {
          console.log(response);
          alert(response.data);
          self.$store.commit("setUserInfo", self.username)
          //alert(self.$store.getters.getUserInfo)
          self.$router.push('home');
        })
        .catch(function(error) {
          console.log(error);
          alert(error.response.data);
        });
    }
  }
}
</script>

<style>
#loginForm {
  width: 500px;
  margin: auto;
}
</style>