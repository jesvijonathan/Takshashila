// Notify flyer function //

function accept_cookie() {
  document.querySelector(".notify").style.padding = "0vw 0vw";

  document.querySelector(".notify").style.opacity = "0";
  document.querySelector(".notify").style.zIndex = "-1";
}
function deccept_cookie() {
  document.querySelector(".notify").style.padding = "1.8vw 1vw";

  document.querySelector(".notify").style.opacity = "1";
  document.querySelector(".notify").style.zIndex = "1";
}

function notify(text, timeout) {
  document.getElementById("not-cont").innerHTML = text;
  // document.querySelector("#not-cont").style.color = "red";

  deccept_cookie();

  if (timeout != -1) {
    setTimeout(function () {
      accept_cookie();
    }, timeout);
  }
}
// Login error function //

var login_error_list = [
  "Error !",
  "Invalid email !",
  "Wrong Credentials, Try again !",
  "Try again..",
];

function login_error(error_flag = null) {
  if (error_flag) {
    notify(login_error_list[error_flag], 3000);
    // Do something related to the specific error
  }
}

// Popup container for url function //

function popstasticopener(
  popup_window_url = "/",
  popup_window_title = "Takshashila Google Authentication",
  popup_window_size = "height=600,width=450"
) {
  var newWindow = window.open(
    popup_window_url,
    popup_window_title,
    popup_window_size
  );
  if (window.focus) {
    newWindow.focus();
  }
}

// Password eye opener //

function password_eye() {
  onload = function () {
    const passwordEye = document.getElementById("passwordEye");
    const password_input = document.getElementById("password_input");

    passwordEye.onclick = function (e) {
      // toggle the type attribute
      const type =
        password_input.getAttribute("type") === "password"
          ? "text"
          : "password";
      password_input.setAttribute("type", type);
      // toggle the eye slash icon
      this.classList.toggle("fa-eye-slash");
    };

    var input = document.getElementById("password_input");
    var element = document.getElementById("passwordEye");

    input.addEventListener("input", function () {
      element.style.display = "block";
    });

    input.onblur = function () {
      if (this.value == "") {
        element.style.display = "none";
      }
    };
  };
}

// password validation //

function validatePassword() {
  const password = document.getElementById("password"),
    confirm_password = document.getElementById("repassword");
  if (password.value != confirm_password.value) {
    confirm_password.setCustomValidity("Password Does Not Match !");
    console.log("Password Does Not Match !");
  } else {
    confirm_password.setCustomValidity("");
  }
}
// document.getElementById("submit").onsubmit = validatePassword();

// Default graduation dates //

function set_deafult_graduation_date() {
  const monthControl = document.getElementById("graduate_year");
  const date = new Date();
  const month = ("0" + (date.getMonth() + 1)).slice(-2);
  const year = date.getFullYear();
  monthControl.value = `${year + 3}-${month}`;
}

// get cookie function //

function getCookie(cname) {
  let name = cname + "=";
  let decodedCookie = decodeURIComponent(document.cookie);
  let ca = decodedCookie.split(";");
  for (let i = 0; i < ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == " ") {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}

// Load data function //

function load_hash() {
  var hash = getCookie("hash");
  document.getElementById("hash").value = hash;
}
function load_details() {
  load_hash();
  var first_name = getCookie("first_name");
  document.getElementById("first_name").value = first_name;
  var last_name = getCookie("last_name");
  document.getElementById("last_name").value = last_name;
}

// Date loader //
function load_date(set_default = false) {
  var date_extend = 8;
  var current_date = new Date().getFullYear();

  let endYear = current_date + date_extend;
  let startYear = current_date - date_extend;

  var data_list = document.getElementById("graduate_year");

  for (i = startYear; i < endYear; i++) {
    data_list.add(new Option(i));
  }

  if (set_default == true) {
    data_list.selectedIndex = date_extend + 4;
  }
  /*
  else {
    data_list.add(new Option((text = "Graduation Year"), (value = "")));
    data_list.selectedIndex = date_extend * 2;
    document.querySelector(
      'select[name="graduate_year"] option[value=""]'
    ).disabled = true;
  } */
}
