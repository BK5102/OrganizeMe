import mysql.connector
from mysql.connector import errorcode 
from mysql.connector import connect

try:
    connect = mysql.connector.connect(user= 'root', password= 'root123', 
                                      host='localhost', database='agenda_planner')
    
    cursor = connect.cursor()
    query = ("SELECT firstName FROM student")
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)
    
    cursor.close()
    connect.close()


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_CON_COUNT_ERROR:
        print("Too many connections")
    elif err.errno == errorcode.ER_KEY_NOT_FOUND:
        print("Key not found, invalid key")
    else:
       errorStatement = str(err) 
       print("Error: " + errorStatement) #errno, sqlstate, msg values






