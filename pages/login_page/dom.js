// dom.js

document.addEventListener('DOMContentLoaded', () => {
    const loginButton = document.getElementById('loginButton');
    const getCardButton = document.getElementById('getCardButton');
    const surveyForm = document.getElementById('surveyForm');

    loginButton.addEventListener('click', () => {
        alert('登录功能待实现');
    });

    getCardButton.addEventListener('click', () => {
        surveyForm.style.display = 'block';
    });

    surveyForm.addEventListener('submit', (event) => {
        event.preventDefault();
        alert('表单提交成功');
        // Here you can handle the form data submission (e.g., send it to a server)
    });
});
