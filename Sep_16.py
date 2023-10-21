import os

import mysql.connector

password = os.getenv("Password")
db = mysql.connector.connect(host="localhost", user="root", password=password, database="test", auth_plugin="mysql_native_password")
# print(db)

cursor_obj = db.cursor()
# cursor_obj.execute("CREATE DATABASE test")

# cursor_obj.execute("CREATE TABLE details (Name VARCHAR(50), Age smallint UNSIGNED, ID int PRIMARY KEY AUTO_INCREMENT)")

# cursor_obj.execute("DESCRIBE details")

# for i in cursor_obj:
#     print(i)

# cursor_obj.execute("INSERT INTO details (Name, Age) VALUES (%s,%s)", ("Khan", 30))
# cursor_obj.execute("DELETE FROM details WHERE ID=1")
# cursor_obj.execute("INSERT INTO details (Name, Age) VALUES (%s,%s)", ("Chandler", 30))
# cursor_obj.execute("INSERT INTO details (Name, Age) VALUES (%s,%s)", ("Monica", 30))
# db.commit()

cursor_obj.execute("SELECT * FROM details")

for x in cursor_obj:
    print(x)
