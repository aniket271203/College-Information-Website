#!/bin/python3
from flask import Flask, request, render_template, redirect, url_for
import sqlite3

headers = {
    'Content-Type': 'application/json'
}
app = Flask(__name__)


class DBclass:
    def __init__(self, path):
        self.path = path
        self.db = sqlite3.connect(self.path)
        self.cur = self.db.cursor()

    def execute(self, query):
        self.cur.execute(query)
        return [i[0] for i in self.cur.description], self.cur.fetchall()


@app.route('/')
@app.route('/home.html')
def home():
    return render_template("home.html")


@app.route('/fac.html')
def index():
    db = DBclass('iiit.db')
    getName = "SELECT name FROM faculty;"
    name = db.execute(getName)
    getposition = "SELECT position FROM faculty;"
    position = db.execute(getposition)
    geteducation = "SELECT education FROM faculty;"
    education = db.execute(geteducation)
    getresearcha = "SELECT research_area FROM faculty;"
    research_area = db.execute(getresearcha)
    getresearchl = "SELECT research_lab FROM faculty;"
    research_lab = db.execute(getresearchl)
    getemail = "SELECT email FROM faculty;"
    email = db.execute(getemail)
    geturl = "SELECT image_url FROM faculty"
    url = db.execute(geturl)
    return render_template("fac.html", name=name[1], position=position[1], education=education[1], research_area=research_area[1], research_lab=research_lab[1], email=email[1], url=url[1], length=len(name[1]))


@app.route('/students.html')
def students():
    db = DBclass('iiit.db')
    name = db.execute('SELECT name FROM students')
    rollno = db.execute('SELECT rollno FROM students')
    email = db.execute('SELECT email FROM students')
    house = db.execute('SELECT house FROM students')
    hostel = db.execute('SELECT hostel FROM students')
    yoj = db.execute('SELECT joinyear FROM students')
    branch = db.execute('SELECT branch FROM students')
    city = db.execute('SELECT city FROM students')
    country = db.execute('SELECT country FROM students')
    return render_template('students.html', name=name[1], rollno=rollno[1], email=email[1], house=house[1], hostel=hostel[1], yoj=yoj[1], branch=branch[1], city=city[1], country=country[1], length=len(name[1]))


@app.route('/courses(s).html')
def spring():
    return render_template("courses(s).html")


@app.route('/courses(m).html')
def monsoon():
    return render_template("courses(m).html")


@app.route('/students.html')
def add_student():
    return render_template("students.html")


@app.route('/add_faculty', methods=['POST'])
def submit_formf():
    name = request.form['name']
    position = request.form['position']
    email = request.form['email']
    eac = request.form['eac']
    researcharea = request.form['researcharea']
    lab = request.form['lab']
    key = request.form['key']

    conn = sqlite3.connect('iiit.db')
    c = conn.cursor()
    db = DBclass("iiit.db")
    keys = db.execute('SELECT key FROM keys')
    for k in keys[1]:
        if k[0] == key:
            c.execute("INSERT INTO faculty (name, position, education, research_area, research_lab, email,image_url) VALUES (?, ?, ?, ?, ?, ?,?)",
                      (name, position, eac, researcharea, lab, email, "none"))
            conn.commit()
    conn.close()

    return redirect("fac.html")


@app.route('/add_student', methods=['POST'])
def submit_forms():
    name = request.form['name']
    rollno = request.form['rollno']
    email = request.form['email']
    house = request.form['house']
    hostel = request.form['hostel']
    yoj = request.form['yoj']
    branch = request.form['branch']
    city = request.form['city']
    country = request.form['country']
    key = request.form['key']

    conn = sqlite3.connect('iiit.db')
    c = conn.cursor()
    db = DBclass("iiit.db")
    keys = db.execute('SELECT key FROM keys')
    for k in keys[1]:
        if k[0] == key:
            c.execute("INSERT INTO students (rollno, name, email, city, country, joinyear,courses, branch, hostel, house) VALUES (?,?,?,?, ?, ?, ?, ?, ?,?)",
                      (rollno, name, email, city, country, yoj, "no course added yet", branch, hostel, house))

            conn.commit()
    conn.close()

    return redirect("students.html")


@app.route('/search_faculty', methods=['GET', 'POST'])
def search_person():
    if request.method == 'POST':
        search_query = request.form['search']
        conn = sqlite3.connect('iiit.db')
        db = conn.cursor()
        db.execute("SELECT * FROM faculty WHERE name LIKE ? OR research_lab LIKE ?",
                   (f"%{search_query}%", f"%{search_query}%"))
        matching_person = db.fetchall()
        conn.close()
        return render_template('search-results.html', person=matching_person)
    return render_template('fac.html')


@app.route('/search_student', methods=['GET', 'POST'])
def search_student():
    if request.method == 'POST':
        search_query = request.form['search']
        conn = sqlite3.connect('iiit.db')
        db = conn.cursor()
        db.execute("SELECT * FROM students WHERE rollno LIKE ? OR name LIKE ? ",
                   (f"%{search_query}%", f"%{search_query}%"))
        matching_students = db.fetchall()
        conn.close()
        return render_template('search-result(student).html', person=matching_students)
    return render_template('students.html')


@app.route('/search_course', methods=['GET', 'POST'])
def search_courses():
    if request.method == 'POST':
        search_query = request.form['search']
        conn = sqlite3.connect('iiit.db')
        db = conn.cursor()
        db.execute("SELECT * FROM courses WHERE course_code LIKE ? ",
                   (f"%{search_query}%",))
        matching_students = db.fetchall()
        conn.close()
        return render_template('search-result(courses).html', courses=matching_students)
    return render_template('courses(s).html')


@app.route('/deletestudent', methods=['POST'])
def delete_student():
    if request.method == "POST":
        res = request.json
        rollno = res["rollno"]
        pin = res["pin"]
        conn = sqlite3.connect('iiit.db')
        c = conn.cursor()
        db = DBclass("iiit.db")
        keys = db.execute('SELECT key FROM keys')
        for k in keys[1]:
            if k[0] == pin:
                c.execute('DELETE FROM students WHERE rollno=?', (rollno,))
                conn.commit()
                conn.close()
        return {'data': 'received'}


@app.route('/deletefaculty', methods=['POST'])
def delete_faculty():
    if request.method == "POST":
        res = request.json
        name = res["name"]
        pin = res["pin"]
        conn = sqlite3.connect('iiit.db')
        c = conn.cursor()
        db = DBclass("iiit.db")
        keys = db.execute('SELECT key FROM keys')
        for k in keys[1]:
            if k[0] == pin:
                c.execute('DELETE FROM faculty WHERE name=?', (name,))
                conn.commit()
                conn.close()
        return {'data': 'received'}


@app.route('/view_student/<int:rollno>')
def view_student(rollno):
    conn = sqlite3.connect('iiit.db')
    db = conn.cursor()
    db.execute("SELECT * FROM students WHERE rollno=?", (rollno,))
    student_details = db.fetchone()
    conn.close()
    print(student_details)
    if student_details:
        return render_template('/student-details.html', student=student_details, flag=0)
    else:
        return "No student found with the given roll number."


@app.route('/view_grades/<details>')
def view_grades(details):
    print(details)
    lis = details.split("|")
    rollno = lis[0]
    pin = lis[1]
    print(rollno+" "+pin)
    conn = sqlite3.connect('iiit.db')
    db = conn.cursor()
    db.execute("SELECT * FROM students WHERE rollno=?", (rollno,))
    student_details = db.fetchone()
    d = DBclass("iiit.db")
    keys = d.execute('SELECT key FROM keys')
    for k in keys[1]:
        if k[0] == pin:
            return render_template('/student-details.html', student=student_details, flag=1)

    return render_template('/student-details.html', student=student_details, flag=0)


@app.route('/update_student', methods=['POST'])
def update_student():
    rollno = request.form['rollno']
    courses = request.form['courses']
    city = request.form['city']
    country = request.form['country']
    hostel = request.form['hostel']
    sem1 = request.form['sem1']
    sem2 = request.form['sem2']
    sem3 = request.form['sem3']
    sem4 = request.form['sem4']
    sem5 = request.form['sem5']
    sem6 = request.form['sem6']
    sem7 = request.form['sem7']
    sem8 = request.form['sem8']

    pin = request.form['pin']

    # Update the student details in the database
    conn = sqlite3.connect('iiit.db')
    cur = conn.cursor()
    db = DBclass("iiit.db")
    keys = db.execute('SELECT key FROM keys')
    for k in keys[1]:
        if k[0] == pin:
            cur.execute("UPDATE students SET courses=?, city=?, country=?, hostel=? WHERE rollno=?",
                        (courses, city, country, hostel, rollno))
            if sem1 != "":
                cur.execute("UPDATE students SET sem1=? WHERE rollno=?",
                        ( sem1, rollno))
            if sem2 != "":
                cur.execute("UPDATE students SET sem2=? WHERE rollno=?",
                        ( sem2, rollno))
            if sem3 != "":
                cur.execute("UPDATE students SET sem3=? WHERE rollno=?",
                        ( sem3, rollno))
            if sem4 != "":
                cur.execute("UPDATE students SET sem4=? WHERE rollno=?",
                        ( sem4, rollno))
            if sem5 != "":
                cur.execute("UPDATE students SET sem5=? WHERE rollno=?",
                        ( sem5, rollno))
            if sem6 != "":
                cur.execute("UPDATE students SET sem6=? WHERE rollno=?",
                        ( sem6, rollno))
            if sem7 != "":
                cur.execute("UPDATE students SET sem7=? WHERE rollno=?",
                        ( sem7, rollno))
            if sem8 != "":
                cur.execute("UPDATE students SET sem8=? WHERE rollno=?",
                        ( sem8, rollno))
            conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('view_student', rollno=rollno))


@app.route('/students-details.html')
def view():
    return render_template("/students-details.html")

@app.route('/inst.html')
def inst():
    return render_template("/inst.html")

if __name__ == "__main__":
    app.run(debug=True)
