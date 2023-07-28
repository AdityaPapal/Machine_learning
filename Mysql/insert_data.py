import mysql.connector 

mydb = mysql.connector.connect(host = "localhost",user = "root",passwd = "aditya29",)


print(mydb)
mycursor = mydb.cursor()

mycursor.execute("insert into demo.mlbootcamp values(1,'Aditya','Papal','papaladitya','9156020115')")

mydb.commit()
