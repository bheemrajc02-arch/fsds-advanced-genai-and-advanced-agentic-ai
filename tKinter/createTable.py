import mysql.connector

# 1. Connect without specifying the database first
conn = mysql.connector.connect(
    host='localhost', user='root', password='Bheema@123'
)
cursor = conn.cursor()

# 2. Create the database if it doesn't exist
cursor.execute('CREATE DATABASE IF NOT EXISTS pythondb')
print('Database pythondb created successfully!')