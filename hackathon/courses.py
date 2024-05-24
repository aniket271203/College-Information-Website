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
f1=open("coursesm.txt",'r')
mlines=f1.readlines()
for line in mlines:
    data_list=line.split("|")
    course_code=data_list[0].strip()
    course_name=data_list[1].strip()
    course_faculty=data_list[2].strip()
    conn = sqlite3.connect('iiit.db')
    c = conn.cursor()
    c.execute('SELECT * FROM courses WHERE course_name = ? AND course_code=? AND course_faculty=?', (course_name,course_code,course_faculty))
    if c.fetchone() is None:
        c.execute('INSERT INTO courses (course_code,course_name,course_faculty) VALUES (?, ?, ?)', (course_code,course_name,course_faculty))
        conn.commit()
        conn.close()
f1.close()

f2=open("coursess.txt",'r')
mlines2=f2.readlines()
for line in mlines2:
    data_list=line.split("|")
    course_code=data_list[0].strip()
    course_name=data_list[1].strip()
    course_faculty=data_list[2].strip()
    conn = sqlite3.connect('iiit.db')
    c = conn.cursor()
    c.execute('SELECT * FROM courses WHERE course_name = ? AND course_code=? AND course_faculty=?', (course_name,course_code,course_faculty))
    if c.fetchone() is None:
        c.execute('INSERT INTO courses (course_code,course_name,course_faculty) VALUES (?, ?, ?)', (course_code,course_name,course_faculty))
        conn.commit()
        conn.close()
f2.close()

db = DBclass('iiit.db')
datawhole=db.execute('SELECT * FROM courses')
print(datawhole)   
