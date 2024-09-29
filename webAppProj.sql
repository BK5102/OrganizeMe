drop table student;
drop table class_organizer;
drop table task;

SELECT * FROM student;
SELECT * FROM task;
SELECT * FROM class_organizer;

CREATE TABLE student (
	studentID INT (255) AUTO_INCREMENT,
    firstName VARCHAR (20),
    lastName VARCHAR (20),
    email VARCHAR (50),
    pass CHAR (8),
    PRIMARY KEY (studentID)

);

CREATE TABLE class_organizer (
	organizerID INT (255) AUTO_INCREMENT,
    studentID INT (20),
	course VARCHAR (20),
	assignment VARCHAR (25),
	due_date DATE,
	PRIMARY KEY (organizerID),
	FOREIGN KEY (studentID) REFERENCES student(studentID)
);

CREATE TABLE task (
	taskID INT (255) AUTO_INCREMENT,
    studentID INT (20),
    user_task VARCHAR (50),
    PRIMARY KEY (taskID),
    FOREIGN KEY (studentID) REFERENCES student(studentID)
);


 
