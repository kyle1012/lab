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
        IP주소 : <input dense v-model=$route.query[2]>
      </div>
      <div class="board-contents">
        <span>기안일 : {{ $route.query[20] }}</span>
      </div>
      <div class="board-contents">
        기간 : <input dense v-model=$route.query[17]>
      </div>
      <div class="board-contents">
        요청사이트 :<textarea 
        style="width:800px; height: 100px;"
    class="textarea"
    v-model=$route.query[18]></textarea>
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
        update_data:{}
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
        db_ip:this.$route.query[2],
        db_period:this.$route.query[17],
        db_site:this.$route.query[18],
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