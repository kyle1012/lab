<template>
              <v-app>
<v-app-bar
      color="deep-purple"
      elevation="4"
      dark>
<v-app-bar-nav-icon @click="drawer = true"></v-app-bar-nav-icon>
  <v-toolbar-title><router-link to="/home" style="text-decoration:none">LAB V.1.0</router-link></v-toolbar-title>
  <v-spacer></v-spacer><v-spacer></v-spacer><v-spacer></v-spacer>
  <v-spacer></v-spacer><v-spacer></v-spacer><v-spacer></v-spacer><v-spacer></v-spacer><v-spacer></v-spacer>
  <v-spacer></v-spacer><v-spacer></v-spacer><v-spacer></v-spacer><v-spacer></v-spacer><v-spacer></v-spacer>
        {{ this.$store.getters.getUserInfo }}
    </v-app-bar>
    <v-navigation-drawer
      v-model="drawer"
      absolute
      temporary
    >
    <v-list
        nav
        dense
      >
        <v-list-item>
          <v-list-item-title><router-link to="/upload" style="text-decoration:none">IP신청서</router-link></v-list-item-title>
        </v-list-item>
        <v-list-item>
          <v-list-item-title><router-link to="/upload_internet" style="text-decoration:none">인터넷차단해제신청서</router-link></v-list-item-title>
        </v-list-item>
        <v-list-item>
          <v-list-item-title><router-link to="/upload_firewall" style="text-decoration:none">방화벽정책신청서</router-link></v-list-item-title>
        </v-list-item>
        <v-list-item>
          <v-list-item-title><router-link to="/upload_vpn" style="text-decoration:none">계정신청서</router-link></v-list-item-title>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-container>
    <div class="board-detail">
      <div class="board-contents">
        <h3>[{{$route.query[3]}}]  {{ $route.query[1] }}</h3>
        <div>
          <strong class="w3-large">{{ $route.query[4] }}</strong>
          <br>
          <strong class="w3-large">{{ $route.query[9] }}</strong>
          <br>
          <div class="box1">{{ $route.query[5] }}</div>
          <div class="box2">작성자 : {{ $route.query[21] }}</div>
        </div>
        <br>
      </div>
      <div class="board-contents">
        VPN 계정 : <input dense v-model=$route.query[24]>
      </div>
      <div class="board-contents">
        <span>기안일 : {{ $route.query[20] }}</span>
      </div>
      <div class="board-contents">
        기간 : <input dense v-model=$route.query[17]>
      </div>
      <div class="board-contents">
        접근대상 IP/Port :<textarea 
        style="width:800px; height: 100px;"
    class="textarea"
    v-model=$route.query[2]></textarea>
      </div>
      <div class="board-contents">
        요청사유 :<textarea 
        style="width:800px; height: 100px;"
    class="textarea"
    v-model=$route.query[15]></textarea>
      </div>
      <div class="board-contents">
        기안번호 : <input dense v-model=$route.query[19]>
      </div>
      <div class="common-buttons">
        <button type="button" class="w3-button w3-round w3-blue-gray" v-on:click="fnUpdate">업로드</button>&nbsp;
        <button type="button" class="w3-button w3-round w3-gray" v-on:click="fnList">목록</button>
      </div>
      </div>
      </v-container>
      </v-app>
      </template>

<script>
import HelloWorldVue from "./HelloWorld.vue";
import BoardList from "./BoardList"
import axios from 'axios';

 export default {
   components: {
    HelloWorldVue,
    BoardList,
  },
   data() { //변수생성
     return {
        update_data:{},
        drawer: false,
     }
   },
   mounted() {
   },
   methods: {
     fnList() {
       this.$router.push('home')
     },
     fnUpdate() {
      let self = this
      const url = 'http://10.1.30.202:5000/update';
      const update_data = JSON.stringify({
        db_no:this.$route.query[0],
        db_division_doc:this.$route.query[1],
        db_vpn:this.$route.query[24],
        db_period:this.$route.query[17],
        db_ip:this.$route.query[2],
        db_why:this.$route.query[15],
        db_doc:this.$route.query[19],
      })
      axios.post(url, update_data, {
        headers: {
            "Content-Type": `application/json`,
          },
      })
      .then(function(response) {
          console.log(response)
          alert(response.data)
          self.$router.push('home')
        })
        .catch(function(error) {
          console.log(error);
          alert(error.response.data)
        });
    }       
       //this.$router.push({
         //path: './upload',
         //query: this.$route.query
       //})
     },
   }
 </script>
 <style scoped>
.box1 {
 float:left; }
.box2 {
 float:right;} 
 input {
		border-style: double;
		width: 650px;
 }
 textarea{
    border-style: double;
 }
 </style>