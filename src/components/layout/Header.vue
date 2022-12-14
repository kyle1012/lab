<template>
  <div class="header">
    <h1>LAB V.1.0 Test</h1>
    <router-link to="/home">Home</router-link> / <router-link to="/upload">Upload</router-link>
    <header>{{ this.$store.getters.getUserInfo }} </header>
  </div>
</template>
<script>

export default {
  methods: {
  }
}
</script>
<style scoped>
.header {
  text-align: center;
  background-color: lightgray;
}

a {
  color: #42b983;
}
</style>