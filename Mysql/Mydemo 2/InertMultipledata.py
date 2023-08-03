import mysql.connector 

mydb = mysql.connector.connect(host = "localhost",user = "root",passwd = "aditya29",)


print(mydb)
mycursor = mydb.cursor()

mycursor.execute("""insert into MyData.studentdata values('3','Aditya3','Papal3','Ineuron3','9156020113','papaladitya3'),
                 ('4','Aditya4','Papal4','Ineuron4','9156020114','papaladitya4'),
                 ('5','Aditya5','Papal5','Ineuron5','9156020115','papaladitya5'),
                 ('6','Aditya6','Papal6','Ineuron6','9156020116','papaladitya6'),
                 ('7','Aditya7','Papal7','Ineuron7','9156020117','papaladitya7'),
                 ('8','Aditya8','Papal8','Ineuron8','9156020118','papaladitya8'),
                 ('9','Aditya9','Papal9','Ineuron9','9156020119','papaladitya9'),
                 ('10','Aditya10','Papal10','Ineuron10','9156020110','papaladitya10')
                 
                 """)


mydb.commit()