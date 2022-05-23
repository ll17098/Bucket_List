import sqlite3
conn = sqlite3.connect('mydatabase.db') # Warning: This file is created in the current directory
conn.execute("CREATE TABLE bucket (id INTEGER PRIMARY KEY, task char(100) NOT NULL, status bool NOT NULL)")
conn.execute("INSERT INTO bucket (task,status) VALUES ('Climb a mountain',1)")
conn.execute("INSERT INTO bucket (task,status) VALUES ('Get a Job',1)")
conn.commit()