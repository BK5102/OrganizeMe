                          <!-- Back and Sign Out Buttons for all three  -->
<template>
  
    <div>    
      <button id="bckBtn"> Back </button>
      <button id="sgnOutBtn"> Sign Out </button>
      <createPg>  </createPg>
      
    </div>  
   
  </template>
  
  <script>
  import createPg from './CreatePage.vue'

  export default {
    components: {
      createPg
    }
  }
 
  </script>
  


  <style>

    #bckBtn {
      background-color: #8cdaea;
      border: none;
      color: rgb(42, 30, 30);
      border-radius: 8px;
      padding: 10px 15px;
      text-align: center;
      font-weight: bold;
      display: inline-block;
      font-size: 20px;
    }

    #bckBtn:hover{
    box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);
    }

    #sgnOutBtn{
      background-color: #8cdaea;
      border: none;
      color: rgb(42, 30, 30);
      border-radius: 8px;
      padding: 10px 15px;
      text-align: center;
      font-weight: bold;
      font-size: 20px;
      float:  right;
    }

    #sgnOutBtn:hover{
      box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);
    }

  
  </style>