The name of our site is "CAMPUS CONTACTS".Our application provides a comprehensive directory of students and faculty members.Whether you're looking for the contact information of a fellow student or need to get in touch with a faculty member, our application has you covered. The application is user-friendly and easy to navigate. With our application, authorities can insert, search, edit, and delete details of students and faculty. 

Structure:

├── app.py
├── iiit.db
├── README.md
├── static
│   ├── app.js
│   ├── coursesforsl.txt
│   ├── courses(m).css
│   ├── courses(m).js
│   ├── courses(m).txt
│   ├── courses(s).js
│   ├── courses(s).txt
│   ├── fac.js
│   ├── h1.png
│   ├── h2.png
│   ├── h3.png
│   ├── home.js
│   ├── img1.png
│   ├── index .css
│   ├── logo.png
│   ├── profile.png
│   ├── student.css
│   ├── students_list.js
│   └── style.css
└── templates
    ├── courses(m).html
    ├── courses(s).html
    ├── fac.html
    ├── home.html
    ├── inst.html
    ├── search-result(courses).html
    ├── search-results.html
    ├── search-result(student).html
    ├── student-details.html
    └── students.html



SUMMARY:

Home Page:
The Home Page of our application serves as the landing page and provides a brief overview of the application's features. The navigation bar on the top of the page provides links to the Students, Faculty, and Courses pages. This page also contains the frequently asked questions. Also, it the contains the contact details to clarify the user's queries.

Students Page:
The Students Page of our application allows users to search for information about individual students. It has a search bar that lets users search for a specific student based on their name or roll number. If a match is found, the page displays the student's information such as their roll number, name, email, contact details, courses enrolled, hostel and house details. The page also has an 'Add New' button that opens up a form for adding new student details to the database.

Faculty Page:
The Faculty Page of our application is similar to the Students page but is tailored to provide information about the college's faculty members. It allows users to search for faculty members by their name or department. The page displays the faculty member's name, email, contact details, department, and other relevant information. It also has an 'Add New' button that opens up a form for adding new faculty member details to the database.

Courses Page:
The Courses Page of our application provides information about the various courses offered by the college. It lists the course code and name of each course. This page is particularly useful for students who need to refer to the course details while registering for courses or for those who want to know about the courses offered by the college.

Though the Search and Display options are available for everyone, the Insert, Edit and Delete options and the Grades of the students are accessible only to the authorities who have an authentication key, thus ensuring the security of the data and privacy of the users.

In summary, our application is a comprehensive contact directory for the college, providing easy access to information about the students, faculty, and courses. The user-friendly interface makes it simple to navigate the application and find the required information quickly.

PACKAGES:

The following packages and frameworks were used:
    "flask" for building the web application.
    "sqlite3" for interacting with the SQLite database.
    "render_template" to render the HTML templates in response to the client requests.
    "request" for handling HTTP requests from the client.
    "redirect" for HTTP redirects to other URLs in response to the client requests.

INSTRUCTIONS TO SET UP AND RUN THE WEB APP ON SOMEONE ELSE'S COMPUTER:

To set up and run the web app on someone else's computer, follow these steps:

(1) Install Python: First, ensure that Python is installed on the target computer. If not, download Python from the official website.
(2) Install Flask: Flask is the Python web framework used to develop this app. You can install it using the following command: pip install flask.
(3) Clone the repository: Clone the repository to the target computer.
(4) Install the required packages: Navigate to the directory where you cloned the repository and run the  command to install all the required packages.
(5) Set up the database
(6) Run the app: Once the database is set up, run the app using the following command: python3 app.py .


Python files: 

we have added these as they are responsible to populate the database 
for the details we already want on our website.
(1) sqlmain.py :
running this code will create a database with specified tables in it (make sure to delete old one while running it)
(2) scrap.py:
running this code will populate the faculty table in database with details of faculty by web scraping method
(3) courses.py:
running this code will populate courses table in iiit.db database
(4) key.py:
running this code will populate the keys table of database with 5 high sensitive keys which gonna be used in authentication verification
(5) addstudents.py:
running this code will populate table students of database with 10 students wrote manually


** so basically .. 1. sqlmain.py (will create database) 2. scrap.py 3.courses.py 4. key.py 5.addstudents.py
database will get populated
## make sure to delete the old database before doing so



Contribution:

All three of us very hard towards making our appliction as good as possible. The work was evenly divided wherin all the input pages(pop up) and the instruction page along with the data on the home page wa made by Chandana, the backend and the frontend of the rest of the pages was done by me(Aniket) and shreyansh equally and also chandana helped us doing that.( this readme was also wrtten by her) 