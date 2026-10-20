const container = document.getElementById('container');

document.getElementById('signUp').addEventListener('click', () => {
    container.classList.add('signup-active');
});

document.getElementById('signIn').addEventListener('click', () => {
    container.classList.remove('signup-active');
});