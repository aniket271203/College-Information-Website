// select the courses dropdown
const coursesDropdown = document.getElementById("courses");

// read the courses text file
fetch("static/coursesforsl.txt")
  .then(response => response.text())
  .then(courses => {
    // split the courses by new line
    const coursesArray = courses.split("\n");
    
    // loop through the courses and add each option to the dropdown
    coursesArray.forEach(course => {
      // create a label element for the course with the checkbox
      const label = document.createElement("label");
      const checkbox = document.createElement("input");
      checkbox.type = "checkbox";
      checkbox.name = "courses[]";
      checkbox.value = course;
      label.appendChild(checkbox);
      label.appendChild(document.createTextNode(course));
      
      // create an option element and add the label to it
      const option = document.createElement("option");
      option.value = course;
      option.appendChild(label);
      
      // add the option to the dropdown
      coursesDropdown.appendChild(option);
    });
  });
  
  function deleteData(rollno) {
    const confirmed = confirm("Are you sure you want to delete this data?");
    if (confirmed) {
      const passwordField = document.createElement("input");
      passwordField.type = "password";
      const dialogBox = window.prompt("Please enter authentication pin:", "");
      if (dialogBox === null) {
        return;
      }
      passwordField.value = dialogBox;
      const authenticationPin = passwordField.value;
      const data = {"rollno": rollno, "pin": authenticationPin};
      const options = {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      };
      fetch('/deletestudent', options)
        .then(response => {
          if (response.ok) {
            location.reload();
          } else {
            console.log('Error: ' + response.statusText);
          }
        })
        .catch(error => {
          console.log('Error: ' + error);
        });
    }
  }
  
  function viewStudent(rollno) {
    window.location.href = `/view_student/${rollno}`;
  }