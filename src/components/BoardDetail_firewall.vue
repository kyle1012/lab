<template>
  <Header></Header>
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
        <span font-weight: bold>대상 : {{ $route.query[13] }}</span>
      </div>
      <div class="board-contents">
        <span>기안일 : {{ $route.query[20] }}</span>
      </div>
      <div class="board-contents">
        <span>기간 : {{ $route.query[17] }}</span>
      </div>
      <div class="board-contents" style="white-space:pre-wrap">
         방화벽 정책<p>{{ $route.query[14] }}</p>
      </div>
      <div class="board-contents" style="white-space:pre-wrap">
         요청사유 <p>{{ $route.query[15] }}</p>
      </div>
      <div class="board-contents">
        <span>기안번호 : {{ $route.query[19] }}</span>
      </div>
      <div class="common-buttons">
        <button type="button" class="w3-button w3-round w3-blue-gray" v-on:click="fnUpdate">수정</button>&nbsp;
        <button type="button" class="w3-button w3-round w3-gray" v-on:click="fnList">목록</button>&nbsp;
        <button type="button" class="w3-button w3-round w3-blue" v-on:click="download">다운로드</button>&nbsp;
        <button type="button" class="w3-button w3-round w3-red" v-on:click="Dbdelete">삭제</button>
      </div>
    </div>
    <Footer></Footer>
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
      }
    },
    mounted() {
    },
    methods: {
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
          path: './BoardUpdate_firewall',
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