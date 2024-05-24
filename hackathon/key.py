#!/bin/python3
import sqlite3
class DBclass:
    def __init__(self, path):
        self.path = path
        self.db = sqlite3.connect(self.path)
        self.cur = self.db.cursor()

    def execute(self, query):
        self.cur.execute(query)
        return [i[0] for i in self.cur.description], self.cur.fetchall()

mlines=['qwer@123','asdf@123','zxcv@123','poiu@123','lkjh@123']
for line in mlines:
    conn = sqlite3.connect('iiit.db')
    c = conn.cursor()
    c.execute('INSERT INTO keys (key) VALUES (?)', (line,))
    conn.commit()
    conn.close()

db = DBclass('iiit.db')
datawhole=db.execute('SELECT * FROM keys')
print(datawhole)   
