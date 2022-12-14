<template>
    <div>
       <Header></Header>
       <router-view></router-view>
       <router-view></router-view>
       <BoardList></BoardList>
       <Footer></Footer>
    </div>
 </template>
 
 <script>
 import HelloWorldVue from "./HelloWorld.vue";
 import Header from "./layout/Header";
 import Footer from "./layout/Footer";
 import BoardList from "./BoardList"
 export default {
   name: "Home",
   components: {
     HelloWorldVue,
     Header,
     Footer,
     BoardList,
   },
 };
 </script>
 
 <style>
 #app {
   font-family: Avenir, Helvetica, Arial, sans-serif;
   -webkit-font-smoothing: antialiased;
   -moz-osx-font-smoothing: grayscale;
   text-align: center;
   color: #2c3e50;
   margin-top: 60px;
 }
 </style>
 