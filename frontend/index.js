const loginForm = document.querySelector('.login-form');
const registerForm = document.querySelector('.register-form');

const registerLink = document.getElementById('register-link');
const loginLink = document.getElementById('login-link');

const password = document.getElementById('register-password');
const confirmPassword = document.getElementById('confirm-password');
const errorMessage = document.getElementById('password-error');

const toggles = document.querySelectorAll('.toggle-password');

registerLink.addEventListener('click', (e) => {
    e.preventDefault();
    loginForm.style.display = 'none';
    registerForm.style.display = 'block';
});

loginLink.addEventListener('click', (e) => {
    e.preventDefault();
    registerForm.style.display = 'none';
    loginForm.style.display = 'block';
});

registerForm.addEventListener('submit', (e) => {
    if (password.value !== confirmPassword.value) {
        e.preventDefault();
        errorMessage.style.display = 'block';
    } else {
        errorMessage.style.display = 'none';
    }
});

confirmPassword.addEventListener('input', () => {
    errorMessage.style.display = 'none';
});

toggles.forEach(toggle => {
    toggle.addEventListener('click', () => {
        const targetId = toggle.getAttribute('data-target');
        const input = document.getElementById(targetId);
        if (input.type === 'password') {
            input.type = 'text';
            toggle.classList.replace('bx-show', 'bx-hide');
        } else {
            input.type = 'password';
            toggle.classList.replace('bx-hide', 'bx-show');
        }
    });
});