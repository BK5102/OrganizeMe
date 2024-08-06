                                  <!-- Title and Descriptions -->
<template>
  <div class="organizer">    
    <h2>  Class Organizer  </h2>

    <p class="description"> The Class Organizer allows students to efficiently manage class assignments and due dates.
    <br>
    Assignments can be created and tracked within the organizer corresponding to each class.
    <br>
    Upcoming due dates will be emailed to the student as a reminder.
    </p>

    <p class="howToUse"> Use the dropdown to select a class or log one of your own. 
    <br>
    Add an assignment with the due date for the specific class.
    <br>
    Click on the Show All button to see all assignments logged with due dates and their corresponding class. 
    </p>

                              <!--  SHOW ALL ASSIGNMENTS -->

    <button @click="showAllAssignsBtn" type="button" class="btn btn-space btn-" id="sAllBtn"> 
      <span v-if="showAssignments"> Show All Assignments </span>
      <span v-else> Hide All Assignments</span>
    </button>

    <br>
    <br>
  
                              <!--  DROPDOWN W/ CLASSES -->

    <div class="dropdown">
      
      <button type="button" class= "dropbtn"> View Classes: </button>
      <div class="dropdown-content">
        <br>
        <button onclick="showToast()" @click="englishBtn" type="button" id="dropdownOptionsBtn">English</button>
        <div class="toast-container position-fixed bottom-0 end-0 p-3">
          <div id="liveToast" class="toast" role="alert" aria-live="assertive" aria-atomic="true">
              <div class="toast-header">
                <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
              </div>

              <div v-if="showToastEnglish">
                <div id="successToast" class="toast-body">
                  English Selected
                </div>
              </div>

          </div>
        </div>

        <br>
        <br>

        <button onclick="showToast()" @click="mathBtn" type="button" id="dropdownOptionsBtn">Math</button>
        <div class="toast-container position-fixed bottom-0 end-0 p-3">
          <div id="liveToast" class="toast" role="alert" aria-live="assertive" aria-atomic="true">
              <div class="toast-header">
                <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
              </div>

              <div v-if="showToastMath">
                <div id="successToast" class="toast-body">
                  Math Selected
                </div>
              </div>

          </div>
        </div>
        
        <br>
        <br>

        <button onclick="showToast()" @click="scienceBtn" type="button" id="dropdownOptionsBtn">Science</button>
        <div class="toast-container position-fixed bottom-0 end-0 p-3">
          <div id="liveToast" class="toast" role="alert" aria-live="assertive" aria-atomic="true">
              <div class="toast-header">
                <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
              </div>

              <div v-if="showToastScience">
                <div id="successToast" class="toast-body">
                  Science Selected
                </div>
              </div>

          </div>
        </div>
        
        <br>
        <br>

        <button onclick="showToast()" @click="historyBtn" type="button" id="dropdownOptionsBtn">History/Social Sciences </button>
        <div class="toast-container position-fixed bottom-0 end-0 p-3">
          <div id="liveToast" class="toast" role="alert" aria-live="assertive" aria-atomic="true">
              <div class="toast-header">
                <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
              </div>

              <div v-if="showToastHistory">
                <div id="successToast" class="toast-body">
                  History Selected
                </div>
              </div>

          </div>
        </div>
      
      </div>

    </div>

                            <!--  CREATE COURSE W/ FORM SUBMISSION -->
    <button @click="createCourseBtn" type="button" class="btn btn-space btn-" id="addClassBtn"> 
      <span v-if="showNewCourse"> Add a Class  </span>
      <span v-else> Cancel </span>
    </button>

    <form id="form" >
      <div v-if="!showNewCourse"> 
        <div class="col-md-4-center">
          <center><label for="validationCustomUsername" class="form-label">Add a New Course</label></center>
          <div class="input-group has-validation">
            <input type="text" class="form-control" name = "assignment" id="validationCustomUsername" aria-describedby="inputGroupPrepend" required>
            <div class="invalid-feedback">
              Please enter a course.
            </div>
          </div>
        </div>

        <button @click="submitNewCourse" onclick="showToast()" type="submit" id="submitBtn" class="btn btn-space btn-">Submit</button>
        
          <div class="toast-container position-fixed bottom-0 end-0 p-3">
            <div id="liveToast" class="toast" role="alert" aria-live="assertive" aria-atomic="true">
              <div class="toast-header">
                <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
              </div>

              <div v-if="isCourseSuccess">
                <div id="successToast" class="toast-body">
                  Course successfully created!
                </div>
              </div>

              <div v-else>
                <div id="existsToast" class="toast-body">
                  Course already exists. Enter a new Course.
                </div>
              </div>

            </div>
          </div>
    
      </div>
    </form>


    <button type="button" class="btn btn-space btn-" id="delClassBtn"> Delete a Class </button>
    <br>
    <br>
    <br>

                          <!--  LOG ASSIGNMENT W/ FORM SUBMISSION -->
    <button @click="createAssignBtn" type="button" class="btn btn-space btn-" id="newAssignBtn">  
      <span v-if="showNewAssign"> Log New Assignment </span>
      <span v-else> Cancel </span>
    </button>

    <form id="form" >
      <div v-if="!showNewAssign"> 
        <div class="col-md-4-center">
          <center><label for="validationCustomUsername" class="form-label">Log New Assignment</label></center>
          <div class="input-group has-validation">
            <input type="text" class="form-control" name = "assignment" id="validationCustomUsername" aria-describedby="inputGroupPrepend" required>
            <div class="invalid-feedback">
              Please enter an assignment.
            </div>
          </div>
        </div>

        <button @click="submitNewAssign" onclick="showToast()" type="submit" id="submitBtn" class="btn btn-space btn-">Submit</button>
        
          <div class="toast-container position-fixed bottom-0 end-0 p-3">
            <div id="liveToast" class="toast" role="alert" aria-live="assertive" aria-atomic="true">
              <div class="toast-header">
                <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
              </div>

              <div v-if="isAssignSuccess">
                <div id="successToast" class="toast-body">
                  Assignment successfully created!
                </div>
              </div>

              <div v-else>
                <div id="existsToast" class="toast-body">
                  Assignment already exists. Enter a new Assignment.
                </div>
              </div>

            </div>
          </div>
    
      </div>
    </form>

    <!-- ---------------------------------------DUE DATE PICKER----------------------------------------------- -->
    <label id=dueDateLbl for="dueDate">Due Date:</label>
      <input type="date" id="completionDate" name="dueDate">
      <span id="dateSelected"></span>
    <form> 
      <!-- <label id=dueDateLbl for="dueDate">Due Date:</label>
      <input type="date" id="completionDate" name="dueDate">
      <span id="dateSelected"></span> -->  

      <button @click="submitDueDateBtn" class="btn btn-space btn-" id="submitBtnDD" type="submit"> Submit </button>
    </form>
     

<!-- --------------------------------ASSIGNMENTS TABLE W/ DELETE BUTTON & TOAST---------------------------------------------- -->
      <table class="table table-bordered table-hover" v-if="!showAssignments">
        <thead>
          <tr class="table-primary">
            <th scope="col">Organizer ID</th>
            <th scope="col">Class</th>
            <th scope="col">Assignment</th>
            <th scope="col">Due Date</th>
            <th scope="col">More Actions</th>
          </tr>
        </thead>
        <tbody>                 
          <tr v-for="assignment in allAssigns" :key="assignment.organizerID" >
            <th class="table-warning" scope="row"> {{ assignment.organizerID }}</th> 
              <td class="table-info"> {{ assignment.stuCourse }}</td>
              <td class="table-info"> {{ assignment.stuAssign }}</td>
              <td class="table-info"> {{ assignment.date }}</td>
                
            <button @click="deleteAssignBtn(assignment.organizerID)" type="button" id="delBtn" class="btn btn-space btn-"><i class="fa fa-trash"></i> Delete Assignment</button>
          
    <!-- ----------------------------------------- DELETE W/ TOAST ----------------------------------------------------- -->
         <div class="toast-container position-fixed bottom-0 end-0 p-3">
            <div id="liveToast" class="toast" role="alert" aria-live="assertive" aria-atomic="true">
              <div class="toast-header">
                <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
              </div>

              <div v-if="isDelSuccess">
                <div id="delToast" class="toast-body">
                  Assignment successfully deleted!
                </div>

            </div>
          </div>
        </div>
          
           </tr>
        </tbody>
      </table>



      

  </div>
</template>

<script>

export default {
  
  data(){
    return{ 
      showNewAssign: true,
      showAssignments: true,
      isAssignSuccess: true,
      isDelSuccess: true,
      allAssigns: "",
      
      showNewCourse: true,
      isCourseSuccess: true,

      showToastEnglish: true,
      showToastMath: true,
      showToastScience: true,
      showToastHistory: true

    }
  },

  methods:{
                                          // assignments
    showAllAssignsBtn(){
      fetch('http://localhost:8080/assignments', { method: "GET"})
        .then((response) => response.json())
        .then((data) => { 
          console.log(data);
          this.allAssigns = data; 
        })
        this.showAssignments = !this.showAssignments
    },

    createAssignBtn(){
      this.showNewAssign = !this.showNewAssign
    },

    submitNewAssign(event){
      event.preventDefault();
      var form = document.getElementById("form");
      var frmdata = new FormData(form);
      frmdata.append("stuIDCO", 1);

      var frmObj = Object.fromEntries(frmdata);
      var frmjson = JSON.stringify(frmObj);
          
        fetch('http://localhost:8080/assignment', 
            {
              method: "POST", 
              headers: { 'Content-Type': "application/json"},
              body: frmjson
            })
            .then((response) => {
              if(response.ok){
                console.log("Assignment created")
                this.isAssignSuccess = true
              }
              else{
                console.log("Assignment already exists.")
                this.isAssignSuccess = false  
              }
            })
              
    },

    deleteAssignBtn(assignParam) {
      console.log(assignParam),
      fetch (`http://localhost:8080/assignment/${assignParam}`, 
        { method: "DELETE",
          headers: { 'Content-Type': "application/json"},
        })
        .then((response) =>{ 
          if(response.ok){
            this.isDelSuccess = true               
        }})
    },

                                        // courses

    createCourseBtn(){
      this.showNewCourse = !this.showNewCourse
    },

    submitNewCourse(event){
      event.preventDefault();
      var form = document.getElementById("form");
      var frmdata = new FormData(form);
      frmdata.append("stuIDCO", 1);

      var frmObj = Object.fromEntries(frmdata);
      var frmjson = JSON.stringify(frmObj);
          
        fetch('http://localhost:8080/course', 
            {
              method: "POST", 
              headers: { 'Content-Type': "application/json"},
              body: frmjson
            })
            .then((response) => {
              if(response.ok){
                console.log("Course created")
                this.isCourseSuccess = true
              }
              else{
                console.log("Course already exists.")
                this.isCourseSuccess = false  
              }
            })
              
    },


                                      //due date
    submitDueDateBtn(event){
      event.preventDefault()

      var datejson;
      let date = document.getElementById('dueDateLbl')
      date.addEventListener('change',(e)=>{
        let dateVal = e.target.value
        document.getElementById('dateSelected').innerText = dateVal
        
        var dateObj = Object.fromEntries(dateVal);
        datejson = JSON.stringify(dateObj);
      }) 
        fetch('http://localhost:8080/dueDate', 
              {
                method: "POST", 
                headers: { 'Content-Type': "application/json"},
                body: datejson
              })
              .then((response) => {
                if(response.ok){
                  console.log("Date created")
                  //this.isAssignSuccess = true
                }
                else{
                  console.log("Date already exists.")
                  //this.isAssignSuccess = false  
                }
              })
    
    
   },
                                /* DROPDOWNS BUTTONS TOAST */
   englishBtn(){
    this.showToastEnglish = true
   },

   mathBtn(){
    this.showToastMath = true
   },

   scienceBtn(){
    this.showToastScience = true
   },

   historyBtn(){
    this.showToastHistory = true
   }


  }

                                  
  


}



</script>



<style>
.h2{
  color:blue;
  font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
  font-weight: 600;
  padding: none;
}

.description{
  color:darkred;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  font-weight:bold;
  font-size: large;
  padding: none;
  text-align: center;

}

.howToUse{
  color: black;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  font-weight:bold;
  font-size: medium;
  padding: none;
  text-align: center;
}

#sAllBtn{
    background-color: #5aac77;
    border: none;
    color: rgb(255, 254, 254);
    border-radius: 8px;
    padding: 15px 32px;
    text-align: center;
    font-weight: bold;
    float: left;
    font-size: 15px;
}
  #sAllBtn:hover{
    box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);
  }

#addClassBtn{
  background-color: #87aa3c;
  border: none;
  color: rgb(255, 254, 254);
  border-radius: 8px;
  padding: 15px 32px;
  text-align: center;
  font-weight: bold;
  font-size: 15px;
}

  #addClassBtn:hover{
    box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);
  }

#delClassBtn{
  background-color: #2a848b;
  border: none;
  color: rgb(255, 254, 254);
  border-radius: 8px;
  padding: 15px 32px;
  text-align: center;
  font-weight: bold;
  font-size: 15px;
}

  #delClassBtn:hover{
    box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);
  }

#chsnClassBox{
  float: left;
  border-radius: 2px;
  padding: 10px 34px;
  text-align: center;
  background-color:rgb(70, 65, 219);
  color:rgb(255, 254, 254);
  font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
  font-weight: bold;
  font-size: 16px;
}

#newAssignBtn{
  float: left;
  color:rgb(255, 253, 252);
  background-color:rgb(184, 77, 0);
  font-weight: 700;
  font-family: Georgia, 'Times New Roman', Times, serif;
  font-size: medium;
  padding: 5px 10px;
}

  #newAssignBtn:hover{
    box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);
  }

#completionDate{
  float: left;
}

#dueDateLbl{
  float: left;
}

#submitBtnDD{
  background-color:rgb(8, 187, 32);
  color: rgb(201, 253, 255);
  font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif ;
  font-weight: bold;
  font-size: large;
  float: left;
}

          /* dropdown styling */
.dropbtn{
  border-radius: 2px;
  padding: 10px 34px;
  text-align: center;
  position: relative;
  background-color:rgb(183, 74, 96);
  color:rgb(255, 254, 254);
  font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
  font-size: 20px;
}

.dropdown {
  position: relative;
  display: inline-block;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

.dropdown-content a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
}

.dropdown-content a:hover {background-color: #f1f1f1}

.dropdown:hover .dropdown-content {
  display: block;
}

.dropdown:hover .dropbtn {
  background-color: rgb(183, 74, 96);
}

#dropdownOptionsBtn{
  border:none;
  background-color: #f9f9f9;

}



</style>