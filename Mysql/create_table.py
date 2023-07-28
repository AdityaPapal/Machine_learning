import mysql.connector 

mydb = mysql.connector.connect(host = "localhost",user = "root",passwd = "aditya29",)


print(mydb)
mycursor = mydb.cursor()

mycursor.execute("create table demo.mlbootcamp(StudentId int,FirstName varchar(20),lastName varchar(20),EmailId varchar(60),MobileNum varchar(10))")


# for x in mycursor:
#     print(x)
