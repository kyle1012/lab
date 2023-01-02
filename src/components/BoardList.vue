<template>
      <v-text-field label="Search Data..."
                    v-model="search"
                    >
      </v-text-field>
      <v-layout
    >
    <v-row>
      <v-col cols="2.5"><v-text-field label="분류" v-model="sort" placeholder="분류" outlined></v-text-field></v-col>
      <v-col cols="2.5"><v-text-field label="기안자" v-model="peo" placeholder="기안자" outlined></v-text-field></v-col>
      <v-col cols="2.5"><v-text-field label="부서" v-model="dep" placeholder="부서" outlined></v-text-field></v-col>
      <v-col cols="2.5"><v-text-field label="기안번호" v-model="doc" placeholder="기안번호" outlined></v-text-field></v-col>
      <v-col cols="1"><button type="button" class="w3-button w3-round w3-blue-gray" v-on:click="DBsearch">검색</button></v-col>
      <v-col cols="1"><button type="button" class="w3-button w3-round w3-gray" v-on:click="Reset">초기화</button></v-col>
    </v-row>
    </v-layout>
  <div class="ui icon input" style="width: 100%">
    <table class="w3-table-all">
      <thead>
      <tr>  
        <th>분류</th>
        <th>구분</th>
        <th>기안자</th>
        <th>부서</th>
        <th>기안일</th>
        <th>기안번호</th>
        <th>미리보기</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="(row, idx) in callist" :key="idx">
          <td><a @click="fnView(row)">{{ row[1] }}</a></td>
          <td>{{ row[3] }}</td>
          <td>{{ row[5] }}</td>
          <td>{{ row[9] }}</td>
          <td>{{ row[20] }}</td>
          <td>{{ row[19] }}</td>
          <td>    <v-icon
      large
      @click="preview(row)"
      color="orange darken-2"
    >
      mdi-arrow-up-bold-box-outline
    </v-icon></td>
        </tr>
      </tbody>
    </table>
    <v-pagination
        v-model="curPageNum"
        :length="numOfPages">
      </v-pagination>
  </div>
</template>

<script>
import axios from 'axios'



export default {
  components: {
  },
  data() { //변수생성
    return {
      list: {}, //리스트 데이터
      no: '', //게시판 숫자처리
      listData: [],
      searchData: [],
      search_length : '',
      dataPerPage: 10,
      curPageNum: 1,
      search: '',
      sort: '',
      peo: '',
      dep: '',
      doc: '',
    }
  },
  mounted() {
  this.fnGetList()
},
  methods: {
      fnGetList() {
      axios.get("http://10.1.30.202:5000/board")
      .then((res) => {      
        this.list = res.data
        this.listData = res.data
        console.log(res.data)


      }).catch((err) => {
        if (err.message.indexOf('Network Error') > -1) {
          alert('네트워크가 원활하지 않습니다.\n잠시 후 다시 시도해주세요.')
        }
      })
    },
    Reset(){
       this.doc = ''
       this.peo = ''
       this.dep = ''
       this.sort = ''
    },
    DBsearch() {
      const url = 'http://10.1.30.202:5000/search';
      const data = JSON.stringify({
        db_doc:this.doc,
        db_user:this.peo,
        db_sort:this.sort,
        db_dep:this.dep,
      })
      axios.post(url, data, {
        headers: {
            "Content-Type": `application/json`,
          },
      })
      .then((res) => {      
          console.log(res.data)
          var search_data = res.data
          this.listData = search_data
          //sessionStorage.setItem("store", this.listData);
          //console.log(sessionStorage.store)


      }).catch((err) => {
        console.log(err)
        alert("검색된 데이터가 없습니다.")
      })
    },
    fnView(index) {
          if(index[1] == "IP신청서"){

          this.$router.push({
          path: './BoardDetail',
          query: index
    })
}
      else if(index[1] == "인터넷차단해제신청서"){
          this.$router.push({
          path: './BoardDetail_int',
          query: index
    })
      }
      else if(index[1] == "방화벽정책신청서"){
          this.$router.push({
          path: './BoardDetail_firewall',
          query: index
    })
      }
      else if(index[1] == "계정신청서"){
          this.$router.push({
          path: './BoardDetail_account',
          query: index
    })
      }
  },
   preview(index){
          if(index[1] == "IP신청서"){
            var ip_file_path = index[22]
            var ip_file_name = ip_file_path.substr(11)
            window.open(ip_file_name, '_blank')
          }
      else if(index[1] == "인터넷차단해제신청서"){
            var ip_file_path = index[22]
            var ip_file_name = ip_file_path.substr(11)
            window.open(ip_file_name, '_blank')
      }
      else if(index[1] == "방화벽정책신청서"){
            var ip_file_path = index[22]
            var ip_file_name = ip_file_path.substr(11)
            window.open(ip_file_name, '_blank')
      }
      else if(index[1] == "계정신청서"){
            var ip_file_path = index[22]
            var ip_file_name = ip_file_path.substr(11)
            window.open(ip_file_name, '_blank')
      }

   }

  },
  computed:{
    startOffset() {
        return ((this.curPageNum - 1) * this.dataPerPage);
      },
      endOffset() {
        return (this.startOffset + this.dataPerPage);
      },
      numOfPages() {
        return Math.ceil(this.searchData.length / this.dataPerPage);
      },
      callist(){
        const searchWord = this.search.toLowerCase();

this.searchData = this.listData.filter((data) => {
  let flag = false;
  
    data.forEach((data2) => {
        if (data2 && data2.toString().toLowerCase().includes(searchWord)) {
      flag = true;
    }
    });

    return flag;
}).slice(0);
return this.searchData.slice(this.startOffset, this.endOffset);
      }
    }
    }
</script>
<style>

</style>