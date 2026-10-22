const container = document.getElementById('container');

document.getElementById('signUp').addEventListener('click', () => {
    container.classList.add('signup-active');
});

document.getElementById('signIn').addEventListener('click', () => {
    container.classList.remove('signup-active');
});

function validatePassword() {
    const password = document.getElementById("signupPassword").value;
    const confirmPassword = document.getElementById("confirmPassword").value;
    const warning = document.getElementById("password-warning");

    if (password.length === 0) {
        warning.textContent = "";
        return;
    }

    if (password.length < 8 || password.length > 20) {
        warning.textContent = "Password must be between 8 and 20 characters.";
    }
    else if (!/[A-Z]/.test(password)) {
        warning.textContent = "Password must have at least one uppercase letter.";
    }
    else if (!/[a-z]/.test(password)) {
        warning.textContent = "Password must have at least one lowercase letter.";
    }
    else if (!/[0-9]/.test(password)) {
        warning.textContent = "Password must contain a number.";
    }
    else if (confirmPassword.length > 0 && confirmPassword !== password) {
        warning.textContent = "Passwords do not match.";
    }
    else {
        warning.textContent = "";
    }
}