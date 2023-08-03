import mysql.connector 

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "aditya29",
)


print(mydb)
mycursor = mydb.cursor()
mycursor.execute("Create table MyData.StudentData(Students int,FirstName varchar(50),LastnNme varchar(50),CourseName varchar(50),MobileNum varchar(10),EmailID varchar(50))")

