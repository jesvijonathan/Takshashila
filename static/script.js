// Notify flyer function //

function accept_cookie() {
  notify_va.style.padding = "0vw 0vw";
  notify_va.style.opacity = "0";
  notify_va.style.zIndex = "-1";
}
function deccept_cookie() {
  notify_va.style.zIndex = "100";
  notify_va.style.padding = "1.8vw 1vw";
  notify_va.style.opacity = "1";
}
function notify(text, timeout) {
  not_con.innerHTML = text;
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

    input.addEventListener(
      "input",
      function () {
        element.style.display = "block";
      },
      { passive: true }
    );

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
  return hash;
}
function load_details() {
  load_hash();
  var first_name = getCookie("first_name");
  document.getElementById("first_name").value = first_name;
  var last_name = getCookie("last_name");
  document.getElementById("last_name").value = last_name;
  var ph_number = getCookie("phone");
  document.getElementById("ph_number").value = ph_number;
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

// Sign In check //
function sign_in_check(n) {
  h = getCookie("hash");
  var session_ = getCookie("session");
  console.log(h && session_);
  if (h) {
    // window.location.replace("/");
    switch (n) {
      case 0: {
        window.location.replace("/");
        break;
      }
      case 1: {
        var user_details = getCookie("user_details");
        if (user_details) {
          window.location.replace("/");
        }

        window.location.replace("/login");
        break;
      }
    }
  } else {
    switch (n) {
      case 0: {
        window.location.replace("/login");
        break;
      }
      case 1: {
        break;
      }
    }
  }
}

function get_acc() {
  if ((t = getCookie("hash"))) {
    top_link.innerHTML = "Account";
    top_link.href = "/profile/" + t;
    // top_link.innerHTML = getCookie("first_name");
  }
}

// Profile edit function //
function profile_edit(input_) {
  var element = document.getElementById(input_);
  element.disabled = false;
  element.readOnly = false;
  element.focus();
  var child_element = element.nextElementSibling.firstElementChild;
  child_element.classList.remove("fa-edit");
  child_element.classList.add("fa-save");
}
function profile_onblur(element, default_value) {
  element.disabled = true;
  element.readOnly = true;
  if (!element.value) {
    element.value = default_value;
  }

  var child_element = element.nextElementSibling.firstElementChild;
  child_element.classList.remove("fa-save");
  child_element.classList.add("fa-edit");
}

// Single page login register system //

function single_page_login(n) {
  let regi = document.getElementById("regi");
  if (n == 1) {
    regi.style.transform = "translate(-50%, 100%) scale(0)";
    window.history.pushState("page2", "Title", "/login");
  } else {
    regi.style.transform = "translate(-50%, -52%) scale(1)";
    window.history.pushState("page2", "Title", "/login#/signup");
  }
}

// Stacked courousel button function //

var slideIndex = 1;
onload = function () {
  showSlides(slideIndex);
};

function plusSlides(n) {
  showSlides((slideIndex += n));
}

function currentSlide(n) {
  showSlides((slideIndex = n));
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("locac");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {
    slideIndex = 1;
  }
  if (n < 1) {
    slideIndex = slides.length;
  }
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" current", "");
  }
  slides[slideIndex - 1].style.display = "block";
  dots[slideIndex - 1].className += " current";

  if (n == 1) {
    document.getElementById("Loconn").innerHTML = "Location";
  } else {
    document.getElementById("Loconn").innerHTML = "Contact";
  }
}

// Naviagtion Hider //
function myFunction(poy) {
  if (poy >= 200) {
    myvid.classList.add("blur");
  } else {
    myvid.classList.remove("blur");
  }
}
function nav_hide(poy) {
  // if (!graphic_high) {
  //   return;
  // }

  let currentScrollPos = poy;
  if (prevScrollpos > currentScrollPos) {
    document.getElementById("navbar").style.top = "89%";
  } else {
    document.getElementById("navbar").style.top = "100%";
  }
  prevScrollpos = currentScrollPos;
}

// Animation functions //
function fly_in(target, state) {
  if (state) {
    target.classList.add("fly_in");
  } else {
    target.classList.remove("fly_in");
  }
}

function lin() {
  let op = $(".card_l");
  let oop = $(".day_l");

  oop.addClass("l_in");
  op.addClass("l_in");
  return;
}

function l_in(target, state) {
  lin();
}

function r_in(target, state) {
  let op = $(".card_r");
  let oop = $(".day_r");

  if (state) {
    oop.addClass("l_in");
    op.addClass("l_in");
  }
  // else {
  //   $(".card_l").removeClass("l_in");
  // }
  lin();
}

function opa_rev(target, state) {
  if (state) {
    target.classList.add("fade_rot");
  } else {
    target.classList.remove("fade_rot");
  }
}

function fade_opaci(target, state) {
  if (state) {
    target.classList.add("opaci");
  } else {
    target.classList.remove("opaci");
  }
}

function splash_pop(target, state) {
  if (state) {
    target.classList.add("splash_slide");
  }
}

// observer //

function callbackRouter(entries, observer) {
  let entry = entries[0];
  let target = entry.target;

  if (entry.intersectionRatio > 0) {
    if (target.dataset.callback) {
      window[target.dataset.callback](target, true);
      if (target.dataset.once == "true") {
        target.classList.remove("jos");
        observer.unobserve(target);
      }
    }
  } else {
    if (target.dataset.callback) {
      window[target.dataset.callback](target, false);
    }
  }
}

// Graphics //
onload = function () {
  let image4 = document.getElementById("image4");
  let image3 = document.getElementById("image3");
  let image9 = document.getElementById("image9");
  let pro_sec = document.getElementById("pro_sec");
  let ripple = document.getElementById("ripple");
};
function graphic() {
  if (graphic_high == 1) {
    graphic_high = 0;
    myvid.style.display = "none";
    image4.style.display = "block";
    image3.style.display = "block";
    image9.style.display = "block";
    pro_sec.style.background = "#131313";

    ripple.classList.remove("rypol");

    notify("Acrylic Theme Deactivated !", 3000);
  } else {
    graphic_high = 1;
    myvid.style.display = "block";
    image4.style.display = "none";
    image3.style.display = "none";
    image9.style.display = "none";
    pro_sec.style.background = "transparent";

    ripple.classList.add("rypol");

    notify("Acrylic Theme Activated !", 3000);
  }

  // ripple.classList.add("rypol");
  // ripple.style.animationPlayState = "running";

  // if (ripple_var) {
  //   // ripple.style.display = "block";
  //   // ripple.classList.add("ripple");
  //   ripple.style.animationPlayState = "running";
  // }
}

// PWA Conifg //
if ("serviceWorker" in navigator) {
  navigator.serviceWorker
    .register("service-worker.js")
    .then((registration) => {
      // console.log("SW Registered!");
    })
    .catch((error) => {
      console.log("SW Registration Failed");
    });
} else {
  console.log("Not supported");
}
