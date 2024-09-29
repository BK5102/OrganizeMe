# OrganizeMe 
   Powerful tool that helps high school and college students to efficiently manage their assignments, projects and tasks. 
   
## Description
   Personally, I've always found it difficult to keep track of all the assignments, projects and tasks I have to complete by a certain date. This led me to develop a web application aimed to solve just that problem. Through this web application, students can create an account, add tasks to be completed, and assignments with due dates corresponding to their course. Everything is all in spot, so students can stay better organized and on top of their schedules. Additionally, email notifications will act as a reminder alerting them when assignments are coming up. 

## Getting Started
   *Install mySQL version 8.0
   *Login to mySQL client 
   *Create a schema called agenda_planner
   *Create tables in the schema using the script available in the DB folder

### Dependencies 
   *mySQL 8.0 
   *SQlAlchemy 8.0
   *Python 3.12.3

### Executing Program
   *To run server side app: 
      Navigate to webApplication directory and execute the following commands
         ```uvicorn Models.main:app``` 
         
   *To run client side:
      Navigate to webApplication directory and execute the following commands
         ```npm run serve```
      

## Version History
   1.1.0
   
## License 
   open source Apache license

Part 1 of Project completed: 7/23/24
Part 1.1 of Project (ReadMe updated for Hackathon): 9/28/24
**note: project is a WIP
