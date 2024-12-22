document.addEventListener('DOMContentLoaded', () => {
    const toggleButton = document.getElementById('toggle-dark-mode');
    const body = document.body;
  
    // Load saved theme preference from localStorage
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
      body.classList.add(savedTheme);
    }
  
    toggleButton.addEventListener('click', () => {
      body.classList.toggle('dark-mode');
  
      // Save the theme preference in localStorage
      if (body.classList.contains('dark-mode')) {
        localStorage.setItem('theme', 'dark-mode');
      } else {
        localStorage.setItem('theme', '');
      }
    });
  });
  