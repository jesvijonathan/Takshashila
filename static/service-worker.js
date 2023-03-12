self.addEventListener("install", (t) => {
  t.waitUntil(
    caches
      .open("static")
      .then((t) =>
        t.addAll([
          "./style.css",
          "./script.js",
          "./cursor.js",
          "./manifest.json",
          "./",
        ])
      )
  );
}),
  self.addEventListener("fetch", (t) => {
    t.respondWith(caches.match(t.request).then((e) => e || fetch(t.request)));
  });
