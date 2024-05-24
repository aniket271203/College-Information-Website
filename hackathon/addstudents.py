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

names=["shreyansh","aniket","raushan","shahil","vaibhav","chandana","shaunak","faisal","prithvi","praneeth"]
rollno=["2022111002","2022101199","2022101195","20221011765","2022101354","3746346376","34376726326","23652648374","347683473","374632903"]
joinyear=["2022","2022","2022","2022","2022","2022","2022","2022","2022","2022"]
city=["agra","agra","agra","agra","agra","agra","agra","agra","agra","agra"]
country=["India","India","India","India","India","India","India","India","India","India"]
hostel=["bakul","bakul","bakul","bakul","bakul","bakul","bakul","bakul","bakul","bakul"]
house=["prithvi","prithvi","prithvi","prithvi","prithvi","prithvi","prithvi","prithvi","prithvi","prithvi"]
branch=["cse","cse","cse","cse","cse","cse","cse","cse","cse","cse"]
email="student@iiit.ac.in"
course="no course added yet"
for i in range(10):
    conn = sqlite3.connect('iiit.db')
    c = conn.cursor()
    c.execute('INSERT INTO students (rollno,name,email,city,country,joinyear,courses,branch,hostel,house,sem1,sem2,sem3,sem4,sem5,sem6,sem7,sem8) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', (rollno[i],names[i],email,city[i],country[i],joinyear[i],course,branch[i],hostel[i],house[i],8,7,9,9,9,8,9,8))
    conn.commit()
    conn.close()
db=DBclass("iiit.db")
getstudents="SELECT * FROM students"
datawhole=db.execute(getstudents)
print(datawhole)   
 