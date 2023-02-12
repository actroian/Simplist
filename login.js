function verifyLogin(){
    let email = document.getElementById("login-input").value;
    let password = document.getElementById("password-input").value;
    if (email == "correct@email.com" && password == "password"){
        window.alert("login successful");
    }
    else{
        window.alert("invalid login. Hint: correct@email.com | password");
    }
}

function createAccount(){
    let email = document.getElementById("signup-input").value;
    let password = document.getElementById("signup-password").value;
    if (email != "" && password != ""){
        window.alert("account created");
    }
    else{
        window.alert("enter your information");
    }
}
