                        <!-- To Do List and Course Organizer options  -->

<template >
  <div class="create">   

    <h1 align="center"> OrganizeMe  </h1>

    <h2 align="center" class="greeting"> Welcome (firstName)!  </h2>

    <button type="button" class="btn btn-space btn-" id="btnBg" @click="showListMthd"> 
      <button type="button" class="btn btn-space btn-" id="tdListBtn" @click="list = 'ToDoList'">  
        <span v-if="showList"> To-Do List </span>
        <span v-else> Cancel </span>
      </button>
    </button>

    <button type="button" class="btn btn-space btn-" id="btnBg" @click="showOrganizerMthd"> 
      <button type="button" class="btn btn-space btn-" id="COBtn" @click="organizer = 'ClassOrganizer'">  
        <span v-if="showOrganizer"> Course Organizer  </span>
        <span v-else> Cancel </span>
      </button>
    </button>
  
    <br>
    
    <div v-if="!showList"> 
      <div v-show="showComponent"> 
        <component :is="list"> </component>
      </div>
    </div>

    <br>

    <div v-if="!showOrganizer">
      <div v-show="showComponent"> 
        <component :is="organizer"> </component>
      </div>
    </div>

  </div>
 
</template>

<script>
import ToDoList from './ToDoList.vue'
import ClassOrganizer from './ClassOrganizer.vue';

export default {
  components: {
    ToDoList,
    ClassOrganizer
  },

  data(){
    return{ 
      list: ToDoList,
      organizer: ClassOrganizer,
      showList: true,
      showOrganizer: true,
      showComponent: true

    }
  },
  
  methods:{
    showListMthd(){
      this.showList = !this.showList
    },

    showOrganizerMthd(){
      this.showOrganizer = !this.showOrganizer
    }

  }


}


</script>

<style>

  body{
    background-color: rgb(236, 212, 196);
  }

  .create{
    text-align: center;
    padding: 10;
  }

   h1{
    font-size: 45px;
    color:rgb(255, 0, 0); 
    font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
    font-weight:700; 
  }

  .greeting{
    font-size: 25px;
    font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
    font-style: italic;
    color:rgb(154, 111, 0);
  }

  #tdListBtn{
    background-color: #b20133;
    border: none;
    color: rgb(255, 255, 255);
    border-radius: 8px;
    padding: 15px 32px;
    text-align: center;
    font-weight: bold;
    font-size: 18px; 
    }

    #tdListBtn:hover{
      box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);
    }

  #btnBg{
    color:rgb(236, 212, 196);
  }

  #COBtn{
    background-color: #b20133;
    border: none;
    color: rgb(255, 255, 255);
    border-radius: 8px;
    padding: 15px 32px;
    text-align: center;
    font-weight: bold;
    font-size: 18px;
  }
    #COBtn:hover{
      box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);
    }


</style>