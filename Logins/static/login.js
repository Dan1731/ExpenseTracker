const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const signupLink = document.getElementById('signupLink');
const signinLink = document.getElementById('signinLink');
const container = document.getElementById('container');

function showSignUp() {
    container.classList.add('signup-active');
}

function showSignIn() {
    container.classList.remove('signup-active');
}

signUpButton.addEventListener('click', showSignUp);
signInButton.addEventListener('click', showSignIn);

signupLink.addEventListener('click', (event) => {
    event.preventDefault();
    showSignUp();
});

signinLink.addEventListener('click', (event) => {
    event.preventDefault();
    showSignIn();
});

// Front-end testing only
document.getElementById('loginForm').addEventListener('submit', e => {
    e.preventDefault();
});

document.getElementById('signupForm').addEventListener('submit', e => {
    e.preventDefault();
});