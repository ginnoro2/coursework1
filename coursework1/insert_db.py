import  sqlite3
conn=sqlite3.connect("student.db")
print("Database Opened successfully")

conn.execute("INSERT INTO ADMIN(USERNAME,PASSWORD) VALUES ('admin', 'admin')");

conn.execute("INSERT INTO ADMIN(USERNAME,PASSWORD) VALUES ('root', 'root')");

conn.commit()
print ("Records inserted successfully")
conn.close()
"""
###Output###
Database Opened successfully
Records inserted successfully
"""
