document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');
    const registerForm = document.getElementById('register-form');

    if (loginForm) {
        loginForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = {
                username: document.getElementById('username').value,
                password: document.getElementById('password').value,
            };

            const response = await fetch('http://localhost:8000/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData),
            });

            if (response.ok) {
                const result = await response.json();
                localStorage.setItem('access_token', result.access_token);
                alert('Вход выполнен успешно!');
                window.location.href = '/index.html';
            } else {
                alert('Ошибка входа. Проверьте имя пользователя и пароль.');
            }
        });
    }

    if (registerForm) {
        registerForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = {
                username: document.getElementById('username').value,
                email: document.getElementById('email').value,
                password: document.getElementById('password').value,
            };

            const response = await fetch('http://localhost:8000/register', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData),
            });

            if (response.ok) {
                alert('Регистрация прошла успешно!');
                window.location.href = '/login.html';
            } else {
                alert('Ошибка регистрации. Возможно, имя пользователя или email уже заняты.');
            }
        });
    }
});