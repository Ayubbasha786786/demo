import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="Ayub@413",database="testdb")
mycursor=mydb.cursor()
#sql_query="insert into basicinfo3 (firstname,lastname,city_ID) values (%s,%s,%s)"
#data=[('madhu','sri',457),('Madhu','Basha',413457),]
#mycursor.excute(sql_query,data)  for single record
#mycursor.executemany(sql_query,data)
#mycursor.execute('select * from basicinfo3')
#results=mycursor.fetchall()
#print(results)
#for i in results: 
#    print(i[0])
#mycursor.execute("select * from basicinfo3 where Personid=427 or firstname like 'ay%'")
mycursor.execute("drop table if exists basicinfo2")
#results=mycursor.fetchall()
#print(results)
# Demo

