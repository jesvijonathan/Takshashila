onload = function () {
  document.body.style.cursor = "none";
  let e = !1;
  try {
    let t = document.querySelector("#image1"),
      s = document.querySelector("#image2"),
      r = document.querySelector("#image0_4_41"),
      n = document.querySelector("#image4"),
      a = document.querySelector("#image5");
    t && s && r && n && a && (e = !0);
  } catch (l) {
    e = !1;
  }
  let i = document.querySelector("#cursor"),
    c = document.querySelector("#cursor_border"),
    o = document.querySelector("#cursor_circle");
  e
    ? document.addEventListener(
        "mousemove",
        (e) => {
          let t = e.clientX,
            s = e.clientY;
          (i.style.transform = `translate3d(${t - 20}px, ${s - 20}px, 0)`),
            (i.style.transform = `translate3d(${t - 20}px, ${s - 20}px, 0)`);
          let r = t / window.innerWidth,
            n = s / window.innerHeight;
          (image1.style.transform = `scale(1) translate(${-80 * r}px, ${
            20 * n
          }px)`),
            (image2.style.transform = `scale(1.5) rotate(${
              -14 * r
            }deg) translate(${70 * r}px, ${180 * n}px)`),
            (image3.style.y = `${20 * n}`),
            (image4.style.y = `${-50 * r}`),
            (image5.style.transform = `translate(${-7 * r}px, ${-7 * n}px)`),
            $(".link_cur").hover(
              function () {
                n <= 0.5
                  ? (o.style.transform = "scale(7) translate(0.6vw, 0.6vw)")
                  : (o.style.transform = "scale(7) translate(0.6vw, -0.6vw)"),
                  (o.innerHTML = $(this).data("text"));
              },
              function () {
                (o.style.transform = "scale(1)"), (o.innerHTML = "");
              }
            ),
            document.addEventListener(
              "mousedown",
              function () {
                o.classList.add("cursor_circle_click"),
                  (c.style.background = "white");
              },
              { passive: !0 }
            ),
            document.addEventListener(
              "mouseup",
              function () {
                o.classList.remove("cursor_circle_click"),
                  (c.style.background = "transparent");
              },
              { passive: !0 }
            );
        },
        { passive: !0 }
      )
    : document.addEventListener(
        "mousemove",
        (e) => {
          let t = e.clientX,
            s = e.clientY;
          (i.style.transform = `translate3d(${t - 20}px, ${s - 20}px, 0)`),
            (i.style.transform = `translate3d(${t - 20}px, ${s - 20}px, 0)`);
          let r = s / window.innerHeight;
          $(".link_cur").hover(
            function () {
              r <= 0.5
                ? (o.style.transform = "scale(7) translate(0.6vw, 0.6vw)")
                : (o.style.transform = "scale(7) translate(0.6vw, -0.6vw)"),
                (o.innerHTML = $(this).data("text"));
            },
            function () {
              (o.style.transform = "scale(1)"), (o.innerHTML = "");
            }
          ),
            document.addEventListener(
              "mousedown",
              { passive: !0 },
              function () {
                o.classList.add("cursor_circle_click"),
                  (c.style.background = "white");
              }
            ),
            document.addEventListener("mouseup", { passive: !0 }, function () {
              o.classList.remove("cursor_circle_click"),
                (c.style.background = "transparent");
            });
        },
        { passive: !0 }
      ),
    document.addEventListener(
      "mouseout",
      (e) => {
        let t = e.clientX,
          s = e.clientY;
        (s <= 0 ||
          t <= 0 ||
          t >= window.innerWidth ||
          s >= window.innerHeight) &&
          (i.style.display = "none");
      },
      { passive: !0 }
    ),
    document.addEventListener(
      "mouseenter",
      () => {
        i.style.display = "block";
      },
      { passive: !0 }
    );
};
