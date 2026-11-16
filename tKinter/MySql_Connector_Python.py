
import mysql.connector

conn = mysql.connector.connect(host = 'localhost',user='root',password='4005')

  if conn.is_connected():
      print('connection established')
# print(conn)
# print(conn.is_connected())


mycursor = conn.cursor()   

mycursor.execute('Show databases')

for x in mycursor:
    print(x)