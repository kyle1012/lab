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
          <strong class="w3-large">{{ $route.query[9] }}</strong>
          <br>
          <strong class="w3-large">{{ $route.query[5] }}</strong>
          <br>
          <div class="box1">{{ $route.query[23] }}</div>
          <div class="box2">작성자 : {{ $route.query[21] }}</div>
        </div>
        <br>
      </div>
      <div class="board-contents">
        <span font-weight: bold>IP주소 : {{ $route.query[2] }}</span>
      </div>
      <div class="board-contents">
        <span>기안일 : {{ $route.query[20] }}</span>
      </div>
      <div class="board-contents">
        <span>기간 : {{ $route.query[17] }}</span>
      </div>
      <div class="board-contents" style="white-space:pre-wrap">
         요청 사이트<p>{{ $route.query[18] }}</p>
      </div>
      <div class="board-contents" style="white-space:pre-wrap">
         요청사유<p>{{ $route.query[15] }}</p>
      </div>
      <div class="board-contents">
        <span>기안번호 : {{ $route.query[19] }}</span>
      </div>
      <div class="common-buttons">
        <button type="button" class="w3-button w3-round w3-blue-gray" v-on:click="fnUpdate">수정</button>&nbsp;
        <button type="button" class="w3-button w3-round w3-gray" v-on:click="fnList">목록</button>&nbsp;
        <button type="button" class="w3-button w3-round w3-green" v-on:click="preview">미리보기</button>&nbsp;
        <button type="button" class="w3-button w3-round w3-blue" v-on:click="download">다운로드</button>&nbsp;
        <button type="button" class="w3-button w3-round w3-red" v-on:click="Dbdelete">삭제</button>
      </div>
    </div>
    </v-container>
    </v-app>
  </template>
  
  <script>
 import HelloWorldVue from "./HelloWorld.vue";
 import BoardList from "./BoardList"
 import axios from 'axios';
 import Header from "./layout/Header";
 import Footer from "./layout/Footer";

  export default {
    components: {
     HelloWorldVue,
     BoardList,
     Header,
     Footer,
   },
    data() { //변수생성
      return {
        drawer: false,
      }
    },
    mounted() {
    },
    methods: {
      preview(){
      var ip_file_name = this.$route.query[22].substr(11)
            window.open(ip_file_name, '_blank')
      },
      download(){
      const url = 'http://10.1.30.202:5000/download';
      const data2 = JSON.stringify({
	     id : this.$route.query[0]
	  })
      axios.post(url, data2,  {
        headers: {
            "Content-Type": `application/json`,
          },
          responseType: 'blob',
      })
      .then(function(response) {
        var fileURL = window.URL.createObjectURL(new Blob([response.data]));
                     var fileLink = document.createElement('a');
   
                     fileLink.href = fileURL;
                     fileLink.setAttribute('download', 'download_pdf.pdf');
                     document.body.appendChild(fileLink);
   
                     fileLink.click();
                })
        .catch(function(error) {
          console.log(error);
          alert("실패")
        });
      },
      fnList() {
        this.$router.push('home')
      },
      fnUpdate() {
        this.$router.push({
          path: './BoardUpdate_int',
          query: this.$route.query
        })
      },
      Dbdelete(){
        var conf = confirm("정말 삭제하시겠습니까?")
      if(!conf) e.preventDefault();
        let self = this
        const url = 'http://10.1.30.202:5000/delete';
      const data3 = JSON.stringify({
	     id : this.$route.query[0]
	  })
    axios.post(url, data3, {
        headers: {
            "Content-Type": `application/json`,
          },
      })
      .then(function(response) {
          alert(response.data)
          self.$router.push('home')
        })
        .catch(function(error) {
          alert(error.response.data)
        });
      },
    }
  }
  </script>
  <style scoped>
 .box1 {
  float:left; }
 .box2 {
  float:right;} 
  p{
    border-style: inset;
 }
  </style>