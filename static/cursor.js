onload = function () {
  document.body.style.cursor = "none";
  let e = !1;
  try {
    let t = document.querySelector("#image1"),
      r = document.querySelector("#image2"),
      n = document.querySelector("#image0_4_41"),
      s = document.querySelector("#image4"),
      l = document.querySelector("#image5");
    t && r && n && s && l && (e = !0);
  } catch (a) {
    e = !1;
  }
  let c = document.querySelector("#cursor"),
    o = document.querySelector("#cursor_border"),
    i = document.querySelector("#cursor_circle");
  e
    ? document.addEventListener(
        "mousemove",
        (e) => {
          let t = e.clientX,
            r = e.clientY;
          (c.style.transform = `translate3d(${t - 20}px, ${r - 20}px, 0)`),
            (c.style.transform = `translate3d(${t - 20}px, ${r - 20}px, 0)`);
          let n = t / window.innerWidth,
            s = r / window.innerHeight;
          (image1.style.transform = `scale(1) translate(${-80 * n}px, ${
            20 * s
          }px)`),
            (image2.style.transform = `scale(1.5) rotate(${
              -14 * n
            }deg) translate(${70 * n}px, ${180 * s}px)`),
            (image3.style.y = `${20 * s}`),
            (image4.style.y = `${-50 * n}`),
            (image5.style.transform = `translate(${-7 * n}px, ${-7 * s}px)`),
            $(".link_cur").hover(
              function () {
                s <= 0.5
                  ? (i.style.transform = "scale(7) translate(0.6vw, 0.6vw)")
                  : (i.style.transform = "scale(7) translate(0.6vw, -0.6vw)"),
                  (i.innerHTML = $(this).data("text"));
              },
              function () {
                (i.style.transform = "scale(1)"), (i.innerHTML = "");
              }
            ),
            document.addEventListener(
              "mousedown",
              function () {
                i.classList.add("cursor_circle_click"),
                  (o.style.background = "white");
              },
              { passive: true }
            ),
            document.addEventListener(
              "mouseup",
              function () {
                i.classList.remove("cursor_circle_click"),
                  (o.style.background = "transparent");
              },
              { passive: true }
            );
        },
        { passive: true }
      )
    : document.addEventListener(
        "mousemove",
        (e) => {
          let t = e.clientX,
            r = e.clientY;
          (c.style.transform = `translate3d(${t - 20}px, ${r - 20}px, 0)`),
            (c.style.transform = `translate3d(${t - 20}px, ${r - 20}px, 0)`);
          let n = r / window.innerHeight;
          $(".link_cur").hover(
            function () {
              n <= 0.5
                ? (i.style.transform = "scale(7) translate(0.6vw, 0.6vw)")
                : (i.style.transform = "scale(7) translate(0.6vw, -0.6vw)"),
                (i.innerHTML = $(this).data("text"));
            },
            function () {
              (i.style.transform = "scale(1)"), (i.innerHTML = "");
            }
          ),
            document.addEventListener(
              "mousedown",
              { passive: true },
              function () {
                i.classList.add("cursor_circle_click"),
                  (o.style.background = "white");
              }
            ),
            document.addEventListener(
              "mouseup",
              { passive: true },
              function () {
                i.classList.remove("cursor_circle_click"),
                  (o.style.background = "transparent");
              }
            );
        },
        { passive: true }
      ),
    document.addEventListener(
      "mouseout",
      (e) => {
        let t = e.clientX,
          r = e.clientY;
        (r <= 0 ||
          t <= 0 ||
          t >= window.innerWidth ||
          r >= window.innerHeight) &&
          (c.style.display = "none");
      },
      { passive: true }
    ),
    document.addEventListener(
      "mouseenter",
      () => {
        c.style.display = "block";
      },
      { passive: true }
    );
};
