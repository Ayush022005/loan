// Select the "View All" button and add a click event listener to it
const viewAllButton = document.querySelector('.dashboard__content--button');
viewAllButton.addEventListener('click', () => {
  // Redirect the user to the "Transactions" page when the button is clicked
  window.location.href = '#transactions';
});

// Select all the navigation links and add a click event listener to each one
const navLinks = document.querySelectorAll('.dashboard__nav a');
navLinks.forEach(link => {
  link.addEventListener('click', (e) => {
    // Prevent the default link behavior
    e.preventDefault();

    // Add the "dashboard__nav--active" class to the clicked link
    navLinks.forEach(link => link.classList.remove('dashboard__nav--active'));
    link.classList.add('dashboard__nav--active');

    // Get the href attribute of the clicked link and scroll to the corresponding section
    const href = link.getAttribute('href');
    const section = document.querySelector(href);
    section.scrollIntoView({ behavior: 'smooth' });
  });
});