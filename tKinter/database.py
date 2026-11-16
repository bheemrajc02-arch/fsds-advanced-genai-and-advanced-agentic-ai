import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Bheema@123'
)

mycursor = conn.cursor()

mycursor.execute('show databases')
# In this code it will show list of databases in python
for x in mycursor:
    print(x)