fetch('/static/courses(s).txt')
  .then(response => response.text())
  .then(data => {
    const courses = data.split('\n').map(course => {
      const [code,coursename, prof] = course.split(' | ');
      return { code, coursename ,prof };
    });
    const coursesDiv = document.getElementById('courses');
    courses.forEach(course => {
      const card = createCard(course);
      coursesDiv.appendChild(card);
    });
  });

function createCard(course) {
  const card = document.createElement('div');
  card.className = 'card';
  
  const container = document.createElement('div');
  container.className = 'container';
  
  const courseCode = document.createElement('div');
  courseCode.className = 'course-code';
  courseCode.innerHTML = course.code;

  const courseName = document.createElement('div');
  courseName.className = 'course-name';
  courseName.innerHTML = `Course_Name: ${course.coursename}`;
  
  const profName = document.createElement('div');
  profName.className = 'prof-name';
  profName.innerHTML = `Professor: ${course.prof}`;
  
  container.appendChild(courseCode);
  container.appendChild(courseName);
  container.appendChild(profName);
  card.appendChild(container);
  
  return card;
}
