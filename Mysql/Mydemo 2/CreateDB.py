import mysql.connector 

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "aditya29",
)


print(mydb)
mycursor = mydb.cursor()
mycursor.execute("Create database MyData")

