let mode = document.getElementById("mode");
console.log(mode.value);    


toggleLogin = document.getElementById("login-account_label");
toggleSignin = document.getElementById("create-account__label");

passwordinput = document.getElementById("firstpass");
confirmpasswordinput = document.getElementById("secondpass");

buttonsign= document.getElementById("sign-btn");

signform = document.getElementById("signin-form");
loginform = document.getElementById("login-form");

isSignInOpen = false;
loginform.style.zIndex = "1";

function loginBringToFront(){
    loginform.style.zIndex = "1";
}
function loginSendToBack(){
    loginform.style.zIndex = "0";
}

function signinBringToFront(){
    signform.style.zIndex = "1";
}
function signinSendToBack(){
    signform.style.zIndex = "0";
}

window.addEventListener("keyup", ()=>{
    
    if (!((passwordinput.value == confirmpasswordinput.value) || (passwordinput.value.length == 0) || (confirmpasswordinput.value.length == 0))) {
        passwordinput.style.borderColor = "red";
        confirmpasswordinput.style.borderColor = "red";
        console.log(passwordinput.value);
        buttonsign.disabled = true;
        
    }
    else {
        if(passwordinput.value.length > 7 ) {
            passwordinput.style.borderColor = "green";
        confirmpasswordinput.style.borderColor = "green";
        buttonsign.disabled = false;
        }
        
        
    }
});

window.addEventListener("load", (event)=>{
    
    console.log(mode.value === "true");

    if(mode.value ==="false"){
        loginSendToBack();
        loginform.style.opacity = "0";
        signform.style.opacity = "1";
        isSignInOpen = true;
    }
});

toggleSignin.addEventListener("click", ()=>{
    loginform.style.opacity = "0";
    signform.style.opacity = "1";
    document.getElementById("bg-div").style.filter = "blur(7px)";
    isSignInOpen = true;
});

loginform.addEventListener("transitionend", ()=>{
    if(isSignInOpen){
        loginSendToBack();
    }
    else {
        loginBringToFront();
    }
});

toggleLogin.addEventListener("click", ()=>{
    signform.style.opacity = "0";
    loginform.style.opacity = "1";
    document.getElementById("bg-div").style.filter = "blur(5px)"; 
    isSignInOpen = false;
});