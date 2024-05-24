
---

# CAMPUS CONTACTS 📚

**CAMPUS CONTACTS** provides a comprehensive directory of students and faculty members at IIIT Hyderabad. Whether you're looking for contact information for a fellow student or need to get in touch with a faculty member, our application has you covered. The application is user-friendly and easy to navigate, allowing authorities to insert, search, edit, and delete details of students and faculty.

## Project Structure

```
├── app.py
├── iiit.db
├── README.md
├── static
│   ├── app.js
│   ├── coursesforsl.txt
│   ├── courses(m).css
│   ├── courses(m).js
│   ├── courses(m).txt
│   ├── courses(s).js
│   ├── courses(s).txt
│   ├── fac.js
│   ├── h1.png
│   ├── h2.png
│   ├── h3.png
│   ├── home.js
│   ├── img1.png
│   ├── index .css
│   ├── logo.png
│   ├── profile.png
│   ├── student.css
│   ├── students_list.js
│   └── style.css
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
```

## Summary

### Home Page
The Home Page serves as the landing page, providing an overview of the application's features. The navigation bar links to the Students, Faculty, and Courses pages. This page also includes FAQs and contact details for user queries.

### Students Page
Allows users to search for information about individual students by name or roll number. Displays details such as roll number, name, email, contact details, courses enrolled, hostel, and house details. An 'Add New' button opens a form to add new student details.

### Faculty Page
Similar to the Students Page, it provides information about faculty members. Users can search by name or department. Displays details such as name, email, contact information, and department. An 'Add New' button opens a form to add new faculty details.

### Courses Page
Lists the course code and name of each course offered by the college. Useful for students registering for courses or learning about available courses.

### Security
Search and display options are available to everyone. Insert, edit, and delete options, along with student grades, are accessible only to authenticated authorities, ensuring data security and user privacy.

## Packages Used

- `flask` for building the web application.
- `sqlite3` for interacting with the SQLite database.
- `render_template` to render HTML templates.
- `request` for handling HTTP requests.
- `redirect` for HTTP redirects.

## Instructions to Set Up and Run the Web App

1. **Install Python**: Ensure Python is installed. Download it from the official website if not.
2. **Install Flask**: Install Flask using `pip install flask`.
3. **Clone the Repository**: Clone the repository to your computer.
4. **Install Required Packages**: Navigate to the cloned directory and install all required packages.
5. **Set Up the Database**: 
   - Run `sqlmain.py` to create the database.
   - Run `scrap.py` to populate the faculty table via web scraping.
   - Run `courses.py` to populate the courses table.
   - Run `key.py` to populate the keys table with authentication keys.
   - Run `addstudents.py` to manually add student details.
6. **Run the App**: Start the app using `python3 app.py`.

---
