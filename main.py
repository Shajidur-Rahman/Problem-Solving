import sqlite3
conn = sqlite3.connect('facebook.db')
cursor = conn.cursor()

#

cursor.execute("SELECT * FROM Users")
conn.commit()

users = cursor.fetchall()
print(users)
