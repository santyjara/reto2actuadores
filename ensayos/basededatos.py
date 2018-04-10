import sqlite3

conn = sqlite3.connect('database.db')
print ("Opened database successfully");

conn.execute('CREATE TABLE reto(fecha TEXT, valor REAL, clasificacion TEXT)')
print ("Table created successfully");
conn.close()