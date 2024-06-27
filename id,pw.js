"use strict";

const loginId = document.getElementById('name_input');
const email = document.getElementById('email_input');
const loginPw = document.getElementById('password_input');
const nextBtn = document.getElementById('next_btn');

function highlightBorder(event) {
    loginId.style.borderColor = "";
    email.style.borderColor = "";
    loginPw.style.borderColor = "";
    
    event.target.style.borderColor = "#7D08D9";
}

function enableButton() {
    if (loginId.value.length > 0 || email.value.length > 0 || loginPw.value.length > 0) {
        nextBtn.disabled = false;
    } else {
        nextBtn.disabled = true;
    }
}

function moveToMain() {
    location.replace("./main.html");
}

loginId.addEventListener('focus', highlightBorder);
email.addEventListener('focus', highlightBorder);
loginPw.addEventListener('focus', highlightBorder);

loginId.addEventListener('keyup', enableButton);
email.addEventListener('keyup', enableButton);
loginPw.addEventListener('keyup', enableButton);

nextBtn.addEventListener('click', moveToMain);
