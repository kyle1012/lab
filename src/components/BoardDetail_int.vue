<template>
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
        <span font-weight: bold>IP주소 : {{ $route.query[2] }}</span>
      </div>
      <div class="board-contents">
        <span>기안일 : {{ $route.query[20] }}</span>
      </div>
      <div class="board-contents">
        <span>기간 : {{ $route.query[17] }}</span>
      </div>
      <div class="board-contents">
        <span>요청사이트 : {{ $route.query[18] }}</span>
      </div>
      <div class="board-contents">
        <span>요청사유 : {{ $route.query[15] }}</span>
      </div>
      <div class="board-contents">
        <span>기안번호 : {{ $route.query[19] }}</span>
      </div>
      <div class="common-buttons">
        <button type="button" class="w3-button w3-round w3-blue-gray" v-on:click="fnUpdate">수정</button>&nbsp;
        <button type="button" class="w3-button w3-round w3-gray" v-on:click="fnList">목록</button>&nbsp;
        <button type="button" class="w3-button w3-round w3-blue" v-on:click="download">다운로드</button>
      </div>
    </div>
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
          path: './BoardUpdate_int',
          query: this.$route.query
        })
      },
    }
  }
  </script>
  <style scoped>
 .box1 {
  float:left; }
 .box2 {
  float:right;} 
  
  </style>