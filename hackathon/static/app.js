const slides = document.querySelectorAll('.slider'); // Get all the slider images
  let currentSlide = 0; // Set the index of the current slide to 0
  
  // Function to show the current slide
  function showCurrentSlide() {
    // Hide all the slides except the current slide
    for (let i = 0; i < slides.length; i++) {
      if (i === currentSlide) {
        slides[i].style.display = 'block';
      } else {
        slides[i].style.display = 'none';
      }
    }
  }
  
  // Show the initial slide
  showCurrentSlide();
  
  // Function to show the next slide
  function showNextSlide() {
    currentSlide = (currentSlide + 1) % slides.length; // Calculate the index of the next slide
    showCurrentSlide(); // Display the next slide
  }
  
  // Set an interval to automatically show the next slide every 3 seconds
  setInterval(showNextSlide, 3000);

var swiper = new Swiper('.swiper-container', {
    autoplay: {
      delay: 5000,
    },
    loop: true,
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
    },
  });

  
  
  function showMore() {
    const moreText = `Whether you're looking for the contact information of a fellow student or need to get in touch with a faculty member, our application has you covered. The application is user-friendly and easy to navigate, making it simple to find the information you need.
  
  With our application, authorities can easily insert, search, edit, and delete details of students and faculty, ensuring that the directory is always up-to-date and accurate.
  
  We are proud to provide this valuable resource to the IIIT Hyderabad community, and we are committed to making it the best it can be. If you have any questions or feedback, please don't hesitate to contact us.`;
  
    document.getElementById("more").innerHTML = moreText;
  }
  