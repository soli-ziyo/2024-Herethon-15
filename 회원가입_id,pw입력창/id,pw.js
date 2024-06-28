"use strict";

const loginId = document.getElementById('name_input');
const email = document.getElementById('email_input');
const loginPw = document.getElementById('password_input');
const loginPwCheck = document.getElementById('password_check_input');
const nextBtn = document.getElementById('next_btn');

function highlightBorder(event) {
    loginId.style.borderColor = "";
    email.style.borderColor = "";
    loginPw.style.borderColor = "";
    loginPwCheck.style.borderColor = "";
    
    event.target.style.borderColor = "#7D08D9";
}


function moveToMain() {
    location.replace("./main.html");
}

loginId.addEventListener('focus', highlightBorder);
email.addEventListener('focus', highlightBorder);
loginPw.addEventListener('focus', highlightBorder);
loginPwCheck.addEventListener('focus', highlightBorder);

nextBtn.addEventListener('click', moveToMain);
