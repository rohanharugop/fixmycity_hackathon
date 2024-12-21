function showSignUp() {
    document.querySelector('.login-form').style.display = 'none';
    document.querySelector('.signup-form').style.display = 'block';
}

function showLogin() {
    document.querySelector('.signup-form').style.display = 'none';
    document.querySelector('.login-form').style.display = 'block';
}

function login(event) {
    event.preventDefault();
    const email = document.getElementById('login-email').value;
    const password = document.getElementById('login-password').value;

    // Example: Update with your own validation for email and password
    if (email === "rohan@mail.com" && password === "abcde") {
        console.log('Login successful');
        window.location.href = "/user-dashboard.html"; // Redirect to the dashboard
    } else {
        alert("Invalid credentials. Please try again.");
    }
}

function signUp(event) {
    event.preventDefault();
    const username = document.getElementById('signup-username').value;
    const email = document.getElementById('signup-email').value;
    const password = document.getElementById('signup-password').value;
    const role = document.getElementById('role').value;

    // Add registration logic here
    console.log('Signed up with', username, email, password, role);

    // Redirect to login page after successful registration
    alert('Registration successful! Please log in.');
    showLogin();
}
