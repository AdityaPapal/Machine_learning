import mysql.connector 

mydb = mysql.connector.connect(host = "localhost",user = "root",passwd = "aditya29",)


print(mydb)
mycursor = mydb.cursor()

mycursor.execute("insert into MyData.studentdata values(1,'Aditya','Papal','Ineuron','9156020115','papaladitya')")

mycursor.execute("insert into MyData.studentdata values(2,'Aditya2','Papal2','Ineuron2','1234567890','papaladitya2')")

mydb.commit()