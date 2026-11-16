
import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Bheema@123'
)
cursor = conn.cursor()

# 1. Create the 'webgui' database
cursor.execute("CREATE DATABASE IF NOT EXISTS webgui")
cursor.execute("USE webgui")

# 2. Create the table matching your GUI columns (id, name, course, fee)
# Note: Check your EmployeeRegistration.py SQL queries to see if the table is named 'student' or 'students'
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        course VARCHAR(100),
        fee DECIMAL(10, 2)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS student (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        course VARCHAR(100),
        fee DECIMAL(10, 2)
    )
""")

conn.commit()
conn.close()
print("Database 'webgui' and tables created successfully!")