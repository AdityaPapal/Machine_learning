import mysql.connector 

mydb = mysql.connector.connect(host = "localhost",user = "root",passwd = "aditya29",)


print(mydb)
mycursor = mydb.cursor()

#mycursor.execute(("select * from MyData.studentdata"))
mycursor.execute(("select students,FirstName,LastnNme,MobileNum from MyData.studentdata"))
for i in mycursor:
    print(i)