<template>
   <div class="hmPg">    

      <button id="abtBtn"> About </button>
      <h1> OrganizeMe </h1>
      <br>
      <br>
      <br>

    <body>
        <button type="button" class="btn btn-space btn-" id="signUpBtn"> Sign Up </button>
        <br>
        <br>
        <button type="button" class="btn btn-space btn-" id="signInBtn"> Sign In </button>

    </body>
    </div>   
</template>

<script>
export default {

}
</script>

<style>

body{   background-color: rgb(255, 230, 195);   }

h1{ 
    font-size: 45px;
    font-family:Georgia, 'Times New Roman', Times, serif;
    color: black;
    text-align: center;
}

.hmPg{
    text-align: center;
    padding: 15px 32px;
    
  }


#abtBtn {
    background-color: #8cdaea;
    border: none;
    color: rgb(42, 30, 30);
    border-radius: 8px;
    padding: 15px 32px;
    text-align: center;
    font-weight: bold;
    float: left;
    font-size: 20px;
}

    #abtBtn:hover{
    box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);
    }

#signUpBtn{
    background-color: #003496;
    border: none;
    color: rgb(255, 255, 255);
    border-radius: 8px;
    padding: 14px 40px;
    text-align: center;
    font-weight: bold;
    font-size: 25px;
}

    #signUpBtn:hover{
        box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);
    }

#signInBtn{
    background-color: #003496;
    border: none;
    color: rgb(255, 255, 255);
    border-radius: 8px;
    padding: 14px 47px;
    text-align: center;
    font-weight: bold;
    font-size: 25px;
}

    #signInBtn:hover{
        box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);
    }

</style>