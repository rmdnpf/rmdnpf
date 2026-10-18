(function () {
  var tl = gsap.timeline({ paused: true });
  function camVars(cx, cy, s) { return { x: 540 - cx * s, y: 960 - cy * s, scale: s }; }
  function camSet(t, cx, cy, s) { tl.set("#world", camVars(cx, cy, s), t); }
  function camMove(t, dur, cx, cy, s, ease) { tl.to("#world", Object.assign({ duration: dur, ease: ease }, camVars(cx, cy, s)), t); }
  gsap.set("#world", camVars(540, 960, 1.0));
  gsap.set(".sks", { strokeDashoffset: 1 });
  gsap.set(".sk", { strokeDashoffset: 1 });
  var b = CFG.board;
  // napas Tom dan Rachel (kaki tetap)
  tl.to("#tom", { scaleY: 1.006, duration: 1.1, ease: "sine.inOut", yoyo: true, repeat: 3 }, 0);
  // Rachel masuk lewat cahaya pintu (tanpa berjalan): cahaya terbuka, lalu ia muncul
  tl.to("#door", { opacity: 0.85, duration: 0.45, ease: "power1.out" }, 0.3);
  tl.set("#rach", { opacity: 0, rotation: 0 }, 0);
  tl.to("#rach", { opacity: 1, duration: 0.3 }, 0.8);
  tl.to("#door", { opacity: 0.25, duration: 0.6 }, 1.3);
  // menjangkau bahu Tom
  tl.to("#rach", { rotation: CFG.rotate, duration: 0.6, ease: "power2.inOut" }, 1.4);
  tl.fromTo("#lab", { opacity: 0 }, { opacity: 1, duration: 0.4, immediateRender: false }, 0.9);
  tl.to("#lab", { opacity: 0, duration: 0.4 }, 2.5);
  // foto kenangan hangat tergeser, halaman abu muncul di sela-selanya
  for (var i = 0; i < 5; i++) {
    tl.to("#pg" + i, { opacity: 1, duration: 0.3 }, 1.7 + i * 0.1);
    tl.to("#ph" + i, { x: (i % 2 ? 26 : -26), y: (i % 2 ? -18 : 14), rotation: "+=" + (i % 2 ? 5 : -5), duration: 0.5, ease: "power2.out" }, 1.7 + i * 0.1);
    tl.to("#ph" + i, { opacity: 0.55, duration: 0.5 }, 2.2 + i * 0.1);
  }
  // Rachel mundur; garis pertama gedung tergambar di papan
  tl.to("#rach", { rotation: -2, duration: 0.6, ease: "power2.inOut" }, 3.0);
  tl.to("#sktop path", { strokeDashoffset: 0, duration: 0.8, ease: "power1.inOut", stagger: 0.1 }, 2.6);
  // lembar sketsa menumpuk menjadi portofolio
  tl.to("#folder", { opacity: 1, duration: 0.3 }, 3.2);
  for (var j = 0; j < 3; j++) {
    tl.set("#sh" + j, { opacity: 1, x: 0, y: 0, rotation: -17, scale: 1 }, 3.4 + j * 0.4);
    tl.to("#sh" + j + " path", { strokeDashoffset: 0, duration: 0.25 }, 3.4 + j * 0.4);
    tl.to("#sh" + j, { x: 850 + j * 6 - (b[0] - 75), y: 1150 - j * 8 - (b[1] - 55), rotation: -4 + j * 3, duration: 0.5, ease: "power2.inOut" }, 3.55 + j * 0.4);
  }
  // kamera: lebar lalu mendorong ke Tom dan papan
  camMove(2.4, 2.3, 760, 1000, 1.45, "sine.inOut");
  var subs = [[1.4, 3.0, "Adiknya mengingatkan: Tom hanya mengingat yang indah."], [3.0, 4.7, "Ia pun kembali menggambar."]];
  subs.forEach(function (s) { tl.set("#sub", { opacity: 1, innerHTML: s[2] }, s[0]); tl.set("#sub", { opacity: 0 }, s[1]); });
  tl.to("#subgrad", { opacity: 0, duration: 0.2 }, 4.5);
  window.__timelines = window.__timelines || {};
  window.__timelines["draw"] = tl;
})();
