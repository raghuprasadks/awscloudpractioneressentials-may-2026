// Simple client-side form validation and feedback

document.getElementById('signupForm').onsubmit = function(e) {
    e.preventDefault();
    const name = document.getElementById('signupName').value.trim();
    const email = document.getElementById('signupEmail').value.trim();
    const password = document.getElementById('signupPassword').value;
    if (name && email && password.length >= 6) {
        document.getElementById('signupMsg').textContent = 'Sign up successful!';
        this.reset();
    } else {
        document.getElementById('signupMsg').textContent = 'Please fill all fields and use a password with at least 6 characters.';
    }
};

document.getElementById('loginForm').onsubmit = function(e) {
    e.preventDefault();
    const email = document.getElementById('loginEmail').value.trim();
    const password = document.getElementById('loginPassword').value;
    if (email && password.length >= 6) {
        document.getElementById('loginMsg').textContent = 'Login successful!';
        this.reset();
    } else {
        document.getElementById('loginMsg').textContent = 'Invalid email or password.';
    }
};

document.getElementById('contactForm').onsubmit = function(e) {
    e.preventDefault();
    const name = document.getElementById('contactName').value.trim();
    const email = document.getElementById('contactEmail').value.trim();
    const message = document.getElementById('contactMessage').value.trim();
    if (name && email && message) {
        document.getElementById('contactMsg').textContent = 'Message sent!';
        this.reset();
    } else {
        document.getElementById('contactMsg').textContent = 'Please fill all fields.';
    }
};