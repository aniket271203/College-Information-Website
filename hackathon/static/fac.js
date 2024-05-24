
function deleteData(name) {
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
      const data = {"name": name, "pin": authenticationPin};
      const options = {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      };
      fetch('/deletefaculty', options)
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