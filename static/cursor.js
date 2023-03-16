try {
  document.querySelector("#image1"), document.querySelector("#image2");
} catch (r) {
  console.log("Error: " + r);
}
const image1 = document.querySelector("#image1"),
  image2 = document.querySelector("#image2"),
  image5 = document.querySelector("#image5");

const cursor = document.querySelector("#cursor"),
  cursor_border = document.querySelector("#cursor_border"),
  cursor_circle = document.querySelector("#cursor_circle");

document.addEventListener("mousemove", (event) => {
  const mouseX = event.clientX,
    mouseY = event.clientY;
  (cursor.style.transform = `translate3d(${mouseX - 20}px, ${
    mouseY - 20
  }px, 0)`),
    (cursor.style.transform = `translate3d(${mouseX - 20}px, ${
      mouseY - 20
    }px, 0)`);
  let y = mouseY / window.innerHeight,
    x = mouseX / window.innerHeight;

  (image1.style.transform = `translate(${-2 * x}vw, ${1 * y}vw)`),
    (image1.style.transform = `scale(1) translate(${-80 * x}px, ${20 * y}px)`),
    (image2.style.transform = `scale(1.5) rotate(${-14 * x}deg) translate(${
      70 * x
    }px, ${180 * y}px)`),
    (image5.style.transform = `translate(${-7 * x}px, ${-7 * y}px)`);

  $(".link_cur").hover(
    function () {
      y <= 0.5
        ? (cursor_circle.style.transform = "scale(7) translate(10px, 10px)")
        : (cursor_circle.style.transform = "scale(7) translate(10px, -10px)"),
        (cursor_circle.innerHTML = $(this).data("text"));
    },
    function () {
      (cursor_circle.style.transform = "scale(1)"),
        (cursor_circle.innerHTML = "");
    }
  );

  document.addEventListener("mousedown", function () {
    cursor_circle.classList.add("cursor_circle_click");
    cursor_border.style.background = "white";
    // document.body.style.background = "white";

    // document.body.style.mixBlendMode = " difference";

    // setTimeout(function () {
    //   cursor_circle.style.transform = `scale(1)`;
    // }, 100);
  });

  document.addEventListener("mouseup", function () {
    cursor_circle.classList.remove("cursor_circle_click");
    cursor_border.style.background = "transparent";

    // document.body.style.mixBlendMode = " unset";
    // document.body.style.background = "#282828 ";
  });
});

document.addEventListener("mouseout", () => {
  let e = event.clientX,
    n = event.clientY;
  (n <= 0 || e <= 0 || e >= window.innerWidth || n >= window.innerHeight) &&
    (cursor.style.display = "none");
}),
  document.addEventListener("mouseenter", () => {
    cursor.style.display = "block";
  });
