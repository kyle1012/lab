<template>
          <v-app>
<v-app-bar
      color="deep-purple"
      elevation="4"
      dark>
<v-app-bar-nav-icon @click="drawer = true"></v-app-bar-nav-icon>
  <v-toolbar-title><router-link to="/home" style="text-decoration:none">LAB V.1.0</router-link></v-toolbar-title>
  <v-spacer></v-spacer><v-spacer></v-spacer><v-spacer></v-spacer>
  <v-spacer></v-spacer><v-spacer></v-spacer>
  <strong><h2>방화벽정책신청서</h2></strong>
 <v-spacer></v-spacer>
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
      <v-container grid-list-xl>
      <v-layout
        wrap
        justify-space-between
      >
      <v-col cols="3" class="border_style">
      <Dashboard
        ref="dash"
        :uppy="uppy"
      /></v-col>
      <v-col cols="5" class="border_style"> <iframe v-bind:src="pdf_file" style="width:700px; height:800px;" frameborder="0"></iframe></v-col>
      <v-col cols="4" class="border_style">
      <div>
        <div>기안구분 :
          <label><input type="radio" v-bind:value="radioValue1" v-model="gubun" />생성</label>
          <label><input type="radio" v-bind:value="radioValue2" v-model="gubun" />변경</label>
          <label><input type="radio" v-bind:value="radioValue3" v-model="gubun" />삭제</label>
        </div>
        <div>대상 :
          <label><input type="radio" v-bind:value="radioValue4" v-model="firewall" />본사 방화벽</label>
          <label><input type="radio" v-bind:value="radioValue5" v-model="firewall" />HIP 방화벽</label>
          <label><input type="radio" v-bind:value="radioValue6" v-model="firewall" />Cloud 방화벽</label>
          <label><input type="radio" v-bind:value="radioValue7" v-model="firewall" />IDC 방화벽</label>
        </div>
        <v-text-field label="담당자" dense name="peo" v-model="peo"/>
        <v-text-field label="부서" dense name="dep" v-model="dep"/>
        <v-text-field label="기간" dense name="period" v-model="period"/>
        <v-textarea label="방화벽 정책" rows="3" dense name="policy" v-model="policy"/>
        <v-textarea label="요청사유" name="whyy" rows="3" v-model="whyy"/>
        <v-text-field label="기안번호" name="num" dense v-model="num"/>
      <v-btn color="success" @click="upload()">업로드</v-btn>
      </div>
      </v-col>
      </v-layout>
      </v-container>
      </v-app>
  </template>
  <script>
  import { Dashboard } from "@uppy/vue";
  import "@uppy/core/dist/style.css";
  import Uppy from "@uppy/core";
  import XHRUpload from "@uppy/xhr-upload";
  import "@uppy/core/dist/style.css";
  import "@uppy/dashboard/dist/style.css";
  import App from "../App.vue"
  import axios from 'axios';
  import Home from "./Home.vue"
  
  
  export default{
    name: 'Hello',
    components: {
      Dashboard,
      App,
      Home,
    },
    
    data: () => {
      return {
        why : '',
        dep: '',
        num:'',
        peo:'',
        whyy:'',
        period:'',
        policy:'',
        gubun:'생성',
        firewall:'본사 방화벽',
        radioValue1:'생성',
        radioValue2:'변경',
        radioValue3:'삭제',
        radioValue4:'본사 방화벽',
        radioValue5:'HIP 방화벽',
        radioValue6:'Cloud 방화벽',
        radioValue7:'IDC 방화벽',
        time:'',
        title:'',
        file_path:'',
        pdf_file:'',
        file_name:'',
        drawer: false,
      };
    },
    methods: {
      upload(){
      let self = this
      var conf = confirm(
               "기안구분 : " + this.gubun + "\n"
              +"대상 : " + this.firewall + "\n"
              +"담당자 : " + this.peo + "\n"
              +"부서 : " + this.dep + "\n"
              +"기간 : " + this.period + "\n"
              +"방화벽정책 : " + this.policy + "\n"
              +"요청사유 : " + this.whyy + "\n"
              +"기안번호 : " + this.num)
        if(!conf) e.preventDefault();
        const url = 'http://10.1.30.202:5000/firewall_insert';
        const data = JSON.stringify({
          db_form:this.gubun,
          db_firewall:this.firewall,
          db_user:this.peo,
          db_dep:this.dep,
          db_period:this.period,
          db_policy:this.policy,
          db_why:this.whyy,
          db_doc:this.num,
          db_time:this.time,
          db_title:this.title,
          db_file_path:this.file_path,
          db_manager:this.$store.state.userId,
        })
        axios.post(url, data, {
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
    },
    computed: {
      uppy(){
        return new Uppy()
  
      .use(XHRUpload, {
        endpoint: "http://10.1.30.202:5000/firewall_upload",
        fieldName: "file",
        bundle: true,
        autoProceed: false,
        })
  
      .on('upload-success', (file, response) => {
      console.log(file.name, response)
      const doc = response.body
      this.dep = doc.dep
      this.peo = doc.peo
      this.period = doc.period
      this.policy = doc.policy
      this.whyy = doc.why
      this.doc = doc.doc
      this.time = doc.time
      this.title = doc.title
      this.file_path = doc.file_path
      this.file_name = doc.file_name
      this.pdf_file = '/FIREWALL_Doc/' + this.file_name
  })
      },
    },
    beforeDestroy () {
      this.uppy.close({ reason: 'unmount' })
    }
  }
  </script>