import mysql.connector
conn = mysql.connector.connect(
      host="127.0.0.1",
      user="root",
      password="Tek@12345",
      database="testdb"
  )
cursor = conn.cursor()
cursor.execute("SELECT * FROM employee")
rows = cursor.fetchall()
for row in rows:
      print(row)
conn.close()