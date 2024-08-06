<template>
  <div id="app" > 

    <h2 > To-Do List</h2>
    <p class="description"> The to-do list functionality allows you to manage your tasks efficiently. 
    <br>
    It is designed to be intuitive and user-friendly, enabling you to organize, track, and prioritize your activities.
    </p>

    <p class="howToUse">
      Click on "Create A Task" to add a new task. Enter a task below. Click Submit.  
      <br>
      Use the "Show All" button to view all tasks logged.
      <!-- <br>
      Use the vertical ellipses located next to each task to delete the logged task. -->
      <!-- <br>
      Use the vertial ellipses located to the right to change the type of List Format.  -->
    </p>

<!-- -----------------------------CREATE AND SHOW ALL BUTTONS------------------------------------------------------ -->

    <div class="d-grid gap-5 d-md-block">

      <button @click="createTaskBtn" type="button" id="createBtn" class="btn btn-space btn-">
        <span v-if="showNewTask"> Create A Task </span>
        <span v-else> Cancel </span>
      </button>

      <button @click="showAllTasksBtn" type="button" id="showBtn" class="btn btn-space btn-"> 
        <span v-if="showTasks"> Show All Tasks </span>
        <span v-else> Hide All Tasks</span>
      </button>

    </div>

<!-------------------------------------FORM SUBMISSION W/ TOAST----------------------------------------------------->

    <form id="form" >
      <div v-if="!showNewTask"> 
        <div class="col-md-4-center">
          <label for="validationCustomUsername" class="form-label">Add a New Task</label>
          <div class="input-group has-validation">
            <input type="text" class="form-control" name = "task" id="validationCustomUsername" aria-describedby="inputGroupPrepend" required>
            <div class="invalid-feedback">
              Please enter a task.
            </div>
          </div>
        </div>

        <button @click="submitNewTask" onclick="showToast()" type="submit" id="submitBtn" class="btn btn-space btn-">Submit</button>
        
          <div class="toast-container position-fixed bottom-0 end-0 p-3">
            <div id="liveToast" class="toast" role="alert" aria-live="assertive" aria-atomic="true">
              <div class="toast-header">
                <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
              </div>

              <div v-if="isTaskSuccess">
                <div id="successToast" class="toast-body">
                  Task successfully created!
                </div>
              </div>

              <div v-else>
                <div id="existsToast" class="toast-body">
                  Task already exists. Enter a new task.
                </div>
              </div>

            </div>
          </div>
    
      </div>
    </form>

<!-- --------------------------------TABLE W/ DELETE BUTTON & TOAST---------------------------------------------- -->

    <table class="table table-bordered table-hover" v-if="!showTasks">
      <thead>
        <tr class="table-primary">
          <th scope="col">Task ID</th>
          <th scope="col">Task</th>
          <th scope="col">More Actions</th>
        </tr>
      </thead>
      <tbody>                 
        <tr v-for="task in allTasks" :key="task.taskID" >
          <th class="table-warning" scope="row"> {{ task.taskID }}</th> 
            <td class="table-info"> {{ task.task }}</td>
            <!-- <button @click="deleteTaskBtn(task.taskID)" onclick="showToast()" type="button" class="btn btn-danger btn-space btn-">Delete Task</button> -->
            <button @click="deleteTaskBtn(task.taskID)" type="button" id="delBtn" class="btn btn-space btn-"><i class="fa fa-trash"></i> Delete Task</button>

  <!-- ----------------------------------------- DELETE W/ TOAST ----------------------------------------------------- -->
        
          <div class="toast-container position-fixed bottom-0 end-0 p-3">
            <div id="liveToast" class="toast" role="alert" aria-live="assertive" aria-atomic="true">
              <div class="toast-header">
                <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
              </div>

              <div v-if="isDelSuccess">
                <div id="delToast" class="toast-body">
                  Task successfully deleted!
                </div>

            </div>
          </div>
        </div>

        </tr>
      </tbody>
    </table>

    

  </div> 
</template>

<!-- -----------------------------------------VUE COMPONENT ----------------------------------------------------------------------- -->

<script>

  export default {
    data() {  
      return { 
        showTasks: true, 
        showNewTask: true,
        isTaskSuccess: true,
        isDelSuccess: true,
        removedTask: null,
        allTasks: ""}      
    }, 
    methods: {   
      showAllTasksBtn() {
        fetch('http://localhost:8080/tasks', { method: "GET"})
        .then((response) => response.json())
        .then((data) => { 
          console.log(data);
          this.allTasks = data; 
        })
        this.showTasks = !this.showTasks
      },

      createTaskBtn(){
        this.showNewTask = !this.showNewTask
      },

      submitNewTask(event){
        event.preventDefault();

          var form = document.getElementById("form");
          var frmdata = new FormData(form);
          frmdata.append("stuIDT", 1);

          var frmObj = Object.fromEntries(frmdata);
          var  frmjson = JSON.stringify(frmObj);
          
          fetch('http://localhost:8080/task', 
            {
              method: "POST", 
              headers: { 'Content-Type': "application/json"},
              body: frmjson
            })
            .then((response) => {
              if(response.ok){
                console.log("Task created")
                this.isTaskSuccess = true
                
              }
              else{
                console.log("Task already exists.")
                this.isTaskSuccess = false  
              }
              frmObj.task = null
        })
      },
    
      deleteTaskBtn(taskParam){
          console.log(taskParam)
          fetch(`http://localhost:8080/task/${taskParam}`, 
            { method: "DELETE",
              headers: { 'Content-Type': "application/json"},
            })
            .then((response) =>{ 
              if(response.ok){
                this.isDelSuccess = true               
              }})
      
      }
    
    }
  }

</script>

<!-- ------------------------------------------------  STYLING ----------------------------------------------------------- -->

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
 
}

h2 {
  color:blue;
  font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
  font-weight: 600;
  padding: 8px;
}

.description{
  color:darkred;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  font-weight:bold;
  font-size: larger;
  padding: 2.5px;

}

.howToUse{
  color: black;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  font-weight:bold;
  font-size: medium;
  padding: 1.5px;
}

.deleteTaskBtn{
  display: none;
}

#createBtn{
  color:rgb(255, 253, 252);
  background-color:rgb(184, 77, 0);
  font-weight: 700;
  font-family: Georgia, 'Times New Roman', Times, serif;
  font-size: medium;
  padding: 5px 5px;
}

#showBtn{
  color:rgb(255, 253, 252);
  background-color:rgb(151, 172, 29);
  font-weight: 700;
  font-family: Georgia, 'Times New Roman', Times, serif;
  font-size: medium;
  padding: 5px 5px;
}

#delBtn {
  background-color:rgb(255, 91, 91);
  color:rgb(0, 0, 0);
  font-weight: 600;
  font-family: Verdana, Geneva, Tahoma, sans-serif;
  font-size: medium;
}

#submitBtn{
  background-color:rgb(8, 187, 32);
  color: rgb(201, 253, 255);
  font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif ;
  font-weight: bold;
  font-size: large;

}

#successToast{
  color:rgb(0, 160, 40);
  font-weight: 700;
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
  font-size: medium;
  padding: 1.5px;
}

#existsToast{
  color: rgb(104, 39, 255);
  font-weight: 700;
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
  font-size: medium;
  padding: 1.5px;
}

#delToast{
  color: crimson;
  font-weight: 700;
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
  font-size: medium;
  padding: 1.5px;
  
}



label {
  color: #604cf9;
  font-weight: bold;
  display: block;
  font-size: 16px;
}


</style>
