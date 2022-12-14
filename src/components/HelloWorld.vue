<template>
  <v-container grid-list-xl>
    <v-layout
    >
    <v-row>
      <v-col cols="3"><router-link to="/upload">IP신청서</router-link></v-col>
      <v-col cols="3"><router-link to="/upload_internet">인터넷차단해제신청서</router-link></v-col>
      <v-col cols="3"><router-link to="/upload_firewall">방화벽정책신청서</router-link></v-col>
      <v-col cols="3"><router-link to="/upload_vpn">vpn계정신청서</router-link></v-col>
    </v-row>
    </v-layout>
    </v-container>
    <v-container grid-list-xl>
    <v-layout
      wrap
      justify-space-between
    >
    <v-col cols="4" class="border_style">
    <Dashboard
      ref="dash"
      :uppy="uppy"
    /></v-col>
    <v-col cols="4" class="border_style"> 3등분 3개 //이부분에 pdf 미리보기</v-col>
    <v-col cols="4" class="border_style">
    <div>
      <div>기안구분 :
	      <label><input type="radio" v-bind:value="radioValue7" v-model="doc" />생성</label>
        <label><input type="radio" v-bind:value="radioValue8" v-model="doc" />변경</label>
        <label><input type="radio" v-bind:value="radioValue9" v-model="doc" />삭제</label>
      </div>
      <v-text-field label="IP주소 입력" dense v-model="IP"></v-text-field>
      <v-text-field label="담당자" dense name="peo" v-model="peo"/>
      <v-text-field label="유선mac" dense name="mac1" v-model="mac1"/>
      <v-text-field label="무선mac" dense name="mac2" v-model="mac2"/>
      <div>구분 : 
	      <label><input type="radio" v-bind:value="radioValue1" v-model="picked" />임직원</label>
        <label><input type="radio" v-bind:value="radioValue2" v-model="picked" />외부인력</label>
        <label><input type="radio" v-bind:value="radioValue3" v-model="picked" />외부자</label>
      </div>
      <v-text-field label="부서" dense name="dep" v-model="dep"/>
      <v-text-field label="email" dense name="email" v-model="email"/>
      <v-text-field label="용도 입력 ex>업무, vm 등" dense v-model="why"/>
      <div>단말기 : 
	      <label><input type="radio" v-bind:value="radioValue4" v-model="elec" />노트북</label>
        <label><input type="radio" v-bind:value="radioValue5" v-model="elec" />데스크탑</label>
	      <label><input type="radio" v-bind:value="radioValue6" v-model="elec" />기타</label>
      </div>
      <v-textarea label="사유" name="whyy" rows="3" v-model="whyy"/>
      <v-text-field label="기안번호" name="num" dense v-model="num"/>
    <v-btn color="success" @click="upload()">업로드</v-btn>
    </div>
    </v-col>
    </v-layout>
    </v-container>
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
      user_auth: '',
      IP : '',
      why : '',
      reason : '',
      dep: '',
      email: '',
      mac1:'',
      mac2:'',
      num:'',
      peo:'',
      whyy:'',
      doc:'생성',
      picked:'임직원',
      elec:'노트북',
      radioValue1:'임직원',
      radioValue2:'외부인력',
      radioValue3:'외부자',
      radioValue4:'노트북',
      radioValue5:'데스크탑',
      radioValue6:'기타',
      radioValue7:'생성',
      radioValue8:'변경',
      radioValue9:'삭제',
      userID:'',
      time:'',
      title:'',
      file_path:'',
    };
  },
  methods: {
    upload(){
    let self = this
    var conf = confirm(
             "기안구분 : " + this.doc + "\n"
            +"IP주소 : " + this.IP + "\n"
            +"담당자 : " + this.peo + "\n"
            +"유선 MAC : " + this.mac1 + "\n"
            +"무선 MAC : " + this.mac2 + "\n"
            +"구분 : " + this.picked + "\n"
            +"부서 : " + this.dep + "\n"
            +"ID : " + this.email + "\n"
            +"용도 : " + this.why + "\n"
            +"단말기 : " + this.elec + "\n"
            +"사유 : " + this.whyy + "\n"
            +"기안번호 : " + this.num)
      if(!conf) e.preventDefault();
      const url = 'http://10.1.30.202:5000/insert';
      const data = JSON.stringify({
        db_form:this.doc,
        db_ip:this.IP,
        db_user:this.peo,
        db_mac1:this.mac1,
        db_mac2:this.mac2,
        db_division:this.picked,
        db_dep:this.dep,
        db_email:this.email,
        db_purpose:this.why,
        db_terminal:this.elec,
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
      endpoint: "http://10.1.30.202:5000/upload",
      fieldName: "file",
      bundle: true,
      autoProceed: false,
      })

    .on('upload-success', (file, response) => {
    console.log(file.name, response)
    const users = response.body
    this.dep = users.dep
    this.email = users.email
    this.mac1 = users.mac1
    this.mac2 = users.mac2
    this.num = users.num
    this.peo = users.peo
    this.whyy = users.whyy
    this.time = users.time
    this.title = users.title
    this.file_path = users.file_path
})
    },
  },
  beforeDestroy () {
    this.uppy.close({ reason: 'unmount' })
  }
}
</script>