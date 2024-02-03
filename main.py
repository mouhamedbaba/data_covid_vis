import sqlite3 as sql
import pandas as pd
import random as rand
connect = sql.connect('database.db')
cursor = connect.cursor()


def insert_data(query):
    cursor.execute(query)
    connect.commit()

    
insert_data('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, username TEXT, password TEXT)')
insert_data(f'INSERT INTO users VALUES ({rand.randint(1, 1000)}, "admin", "admin", "admin123")')

users= cursor.execute('SELECT * FROM users')
print(users.fetchall())
data = [user for user in users.fetchall()] 
print("data = > ", data)

table = pd.DataFrame(users, columns=['id', 'name', 'username', 'password'])
print(table) #prints table