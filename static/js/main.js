// const Local_Storage_Key = "logStatus";
// let home = document.getElementById("home");
// let about = document.getElementById("about");
// let stock = document.getElementById("navbarDropdown");
// let dropDown = document.getElementById("dropdownHover");
// let logOption = document.getElementById("logOption");
// localStorage.setItem(Local_Storage_Key, "loggedIn");
// //localStorage.setItem(Local_Storage_Key, "loggedOut");
// console.log(localStorage.getItem(Local_Storage_Key));

if (window.location.pathname == '/') {
    console.log("Home");
    home.classList.add("active");
    about.classList.remove("active");
    ticker.classList.remove("active");
}
if (window.location.pathname == '/about') {
    console.log("About");
    about.classList.add("active");
    home.classList.remove("active");
    ticker.classList.remove("active");
}
if (window.location.pathname == '/ticker') {
    console.log("Ticker");
    ticker.classList.add("active");
    about.classList.remove("active");
    home.classList.remove("active");
}

// logOption.addEventListener("click", () => {
//     if (localStorage.getItem(Local_Storage_Key) == "loggedOut") {
//         //stock.setAttribute("aria-disabled", "true");
//         stock.classList.add("disabled");
//         dropDown.classList.remove("dropdown");
//         logOption.innerHTML = "LogIn";
//     } else {
//         //stock.setAttribute("aria-disabled", "false");
//         stock.classList.remove("disabled");
//         dropDown.classList.add("dropdown");
//         logOption.innerHTML = "LogOut";
//     }
// })