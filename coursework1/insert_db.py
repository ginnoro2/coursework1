import  sqlite3
conn=sqlite3.connect("student.db")
print("Database Opened successfully")

conn.execute("INSERT INTO ADMIN(USERNAME,PASSWORD) VALUES ('sudip', 'aila')");

conn.execute("INSERT INTO ADMIN(USERNAME,PASSWORD) VALUES ('danger', 'zone')");

conn.commit()
print ("Records inserted successfully")
conn.close()
"""
###Output###
Database Opened successfully
Records inserted successfully
"""
