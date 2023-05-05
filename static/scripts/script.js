function Login() {
    window.location.replace("log-in.html")
}

function Signup() {
    window.location.replace("sign-up-form.html")
}

function Main() {
    window.location.replace("profile-view.html")
}
function buttonFunc() {
    var dots = document.getElementById("dots");
    var btntext = document.getElementById("readmore");
    var moretxt = document.getElementById("more");

    if (dots.style.display === "none") {
        dots.style.display = "inline";
        btntext.innerHTML = "Read More";
        moretxt.style.display = "none";
    }
    else {
        dots.style.display = "none";
        btntext.innerHTML = "Read Less";
        moretxt.innerHTML = "*MORE SKILLS*"
        moretxt.style.display = "inline";
    }
}

function buttonFunc1() {
    var dots = document.getElementById("dots1");
    var btntext = document.getElementById("readmore1");
    var moretxt = document.getElementById("more1");

    if (dots.style.display === "none") {
        dots.style.display = "inline";
        btntext.innerHTML = "Read More";
        moretxt.style.display = "none";
    }
    else {
        dots.style.display = "none";
        btntext.innerHTML = "Read Less";
        moretxt.innerHTML = "*MORE WORK EXPERIENCE*"
        moretxt.style.display = "inline";
    }
}

function buttonFunc2() {
    var dots = document.getElementById("dots2");
    var btntext = document.getElementById("readmore2");
    var moretxt = document.getElementById("more2");

    if (dots.style.display === "none") {
        dots.style.display = "inline";
        btntext.innerHTML = "Read More";
        moretxt.style.display = "none";
    }
    else {
        dots.style.display = "none";
        btntext.innerHTML = "Read Less";
        moretxt.innerHTML = "*MORE HOBBIES*"
        moretxt.style.display = "inline";
    }
}

function buttonFunc3() {
    var dots = document.getElementById("dots3");
    var btntext = document.getElementById("readmore3");
    var moretxt = document.getElementById("more3");

    if (dots.style.display === "none") {
        dots.style.display = "inline";
        btntext.innerHTML = "Read More";
        moretxt.style.display = "none";
    }
    else {
        dots.style.display = "none";
        btntext.innerHTML = "Read Less";
        moretxt.innerHTML = "*MORE PAST/CURRENT EDUCATION*"
        moretxt.style.display = "inline";
    }
}