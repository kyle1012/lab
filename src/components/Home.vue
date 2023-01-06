<template>
    <div>
       <BoardList></BoardList>
       <Footer></Footer>
    </div>
 </template>
 
 <script>
 import HelloWorldVue from "./HelloWorld.vue";
 import Footer from "./layout/Footer";
 import BoardList from "./BoardList"
 export default {
   name: "Home",
   components: {
     HelloWorldVue,
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
 