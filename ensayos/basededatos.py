import sqlite3

conn = sqlite3.connect('database.db')
print ("Opened database successfully");

conn.execute('CREATE TABLE reto2 (fecha TEXT, valor INT, clasificacion TEXT')
print ("Table created successfully");
conn.close()