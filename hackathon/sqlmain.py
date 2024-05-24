#!/bin/python3
import sqlite3

conn = sqlite3.connect('iiit.db')
c = conn.cursor()
c.execute('''CREATE TABLE faculty
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT,
              position TEXT,
              education TEXT,
              research_area TEXT,
              research_lab TEXT,
              email TEXT,
              image_url)''')
conn.commit()
c.execute('''CREATE TABLE courses
           (id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_code TEXT,
            course_name TEXT,
            course_faculty TEXT)''')
conn.commit()
c.execute('''CREATE TABLE students
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             rollno TEXT,
             name TEXT,
             email TEXT,
             city TEXT,
             country TEXT,
             joinyear TEXT,
             courses TEXT,
             branch TEXT,
             hostel TEXT,
             house TEXT,
             sem1 INT,
             sem2 INT,
             sem3 INT,
             sem4 INT,
             sem5 INT,
             sem6 INT,
             sem7 INT,
             sem8 INT)''')
conn.commit()
c.execute('''CREATE TABLE grades
           (id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT,
            course_code TEXT,
            grade TEXT)''')
conn.commit()
c.execute('''CREATE TABLE keys
           (id INTEGER PRIMARY KEY AUTOINCREMENT,
            key TEXT)''')
conn.commit()
conn.close()