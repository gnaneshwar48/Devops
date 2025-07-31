import mysql.connector
 
# Connect to MySQL
conn = mysql.connector.connect(
    host="student_mysql",
    user="root",
    password="rootpass",
    database="student_db"
)
 
cursor = conn.cursor()
 
# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT
)
""")
 
# Insert students
students = [
    (100, 'Manoj', 22),
    (99, 'Mick', 24),
    (98, 'Raj', 25)
]
 
cursor.executemany("INSERT IGNORE INTO students (student_id, name, age) VALUES (%s, %s, %s)", students)
conn.commit()
 
# Fetch and print
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
 
for row in rows:
    print(row)
 
cursor.close()
conn.close()