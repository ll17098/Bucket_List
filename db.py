import sqlite3
conn = sqlite3.connect('mydatabase.db') # Warning: This file is created in the current directory
conn.execute("CREATE TABLE IF NOT EXISTS bucket (id INTEGER PRIMARY KEY, task char(100) NOT NULL, status bool NOT NULL)")
conn.execute("CREATE TABLE IF NOT EXISTS userInfo (id INTEGER PRIMARY KEY, username char(100) NOT NULL, password char(100) NOT NULL)")
conn.execute("INSERT INTO userInfo(username, password) VALUES('admin', 'admin') ")
conn.commit()