!(function (e) {
  function t() {
    var i = this;
    (this.defaults = {
      wrapperId: "butter",
      wrapperDamper: 0.07,
      cancelOnTouch: !1,
    }),
      (this.validateOptions = function (e) {
        for (var t in e)
          i.defaults.hasOwnProperty(t) &&
            Object.defineProperty(i.defaults, t, {
              value: Object.getOwnPropertyDescriptor(e, t).value,
            });
      }),
      this.wrapperDamper,
      this.wrapperId,
      this.cancelOnTouch,
      this.wrapper,
      (this.wrapperOffset = 0),
      this.animateId,
      (this.resizing = !1),
      (this.active = !1),
      this.wrapperHeight,
      this.bodyHeight;
  }
  (t.prototype = {
    init: function (e) {
      e && this.validateOptions(e),
        (this.active = !0),
        (this.resizing = !1),
        (this.wrapperDamper = this.defaults.wrapperDamper),
        (this.wrapperId = this.defaults.wrapperId),
        (this.cancelOnTouch = this.defaults.cancelOnTouch),
        (this.wrapper = document.getElementById(this.wrapperId)),
        (this.wrapper.style.position = "fixed"),
        (this.wrapper.style.width = "100%"),
        (this.wrapperHeight = this.wrapper.clientHeight),
        (document.body.style.height = this.wrapperHeight + "px"),
        window.addEventListener("resize", this.resize.bind(this)),
        this.cancelOnTouch &&
          window.addEventListener("touchstart", this.cancel.bind(this)),
        (this.wrapperOffset = 0),
        (this.animateId = window.requestAnimationFrame(
          this.animate.bind(this)
        ));
    },
    wrapperUpdate: function () {
      var e =
        null != document.scrollingElement
          ? document.scrollingElement.scrollTop
          : document.documentElement.scrollTop || 0;
      (this.wrapperOffset += (e - this.wrapperOffset) * this.wrapperDamper),
        (this.wrapper.style.transform =
          "translate3d(0," + -this.wrapperOffset.toFixed(2) + "px, 0)");
    },
    checkResize: function () {
      this.wrapperHeight != this.wrapper.clientHeight && this.resize();
    },
    resize: function () {
      var e = this;
      e.resizing ||
        ((e.resizing = !0),
        window.cancelAnimationFrame(e.animateId),
        window.setTimeout(function () {
          (e.wrapperHeight = e.wrapper.clientHeight),
            parseInt(document.body.style.height) != parseInt(e.wrapperHeight) &&
              (document.body.style.height = e.wrapperHeight + "px"),
            (e.animateId = window.requestAnimationFrame(e.animate.bind(e))),
            (e.resizing = !1);
        }, 150));
    },
    animate: function () {
      this.checkResize(),
        this.wrapperUpdate(),
        (this.animateId = window.requestAnimationFrame(
          this.animate.bind(this)
        ));
    },
    cancel: function () {
      this.active &&
        (window.cancelAnimationFrame(this.animateId),
        window.removeEventListener("resize", this.resize),
        window.removeEventListener("touchstart", this.cancel),
        this.wrapper.removeAttribute("style"),
        document.body.removeAttribute("style"),
        (this.active = !1),
        (this.wrapper = ""),
        (this.wrapperOffset = 0),
        (this.resizing = !0),
        (this.animateId = ""));
    },
  }),
    (e.butter = new t());
})(this);
