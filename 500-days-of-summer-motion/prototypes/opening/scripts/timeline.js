(function () {
  var tl = gsap.timeline({ paused: true });
  function camVars(cx, cy, s) { return { x: 540 - cx * s, y: 960 - cy * s, scale: s }; }
  function camSet(t, cx, cy, s) { tl.set("#world", camVars(cx, cy, s), t); }
  function camMove(t, dur, cx, cy, s, ease) { tl.to("#world", Object.assign({ duration: dur, ease: ease }, camVars(cx, cy, s)), t); }
  gsap.set("#world", camVars(237, 378, 2.7));
  gsap.set("#lean", { opacity: 0 });
  gsap.set("#card3", { opacity: 0 });
  gsap.set(".sk2", { strokeDashoffset: 1 });
  for (var k = 1; k < 12; k++) { gsap.set("#sh" + k + " i,#sh" + k + " b", { opacity: 0 }); tl.set("#sh" + k + " i,#sh" + k + " b", { opacity: 1 }, 0.5 + (k - 1) * 0.12 + 0.05); }

  // ===== ADEGAN 1 (0,0–5,5) =====
  tl.set("#lamp", { opacity: 0.75 }, 0);
  camSet(0, 237, 378, 2.7);
  camMove(0.5, 1.6, 540, 960, 1.0, "power2.inOut");                              // tarik mundur dari kalender
  for (var i = 0; i < 11; i++) {                                                  // halaman disobek mundur 500 -> 1
    tl.to("#sh" + i, { x: -140, y: 540, rotation: -16, opacity: 0, duration: 0.35, ease: "power2.in" }, 0.5 + i * 0.12);
  }
  camMove(2.1, 1.3, 500, 1020, 1.1, "sine.inOut");
  tl.to("#deskg", { y: 0, duration: 0.01 }, 0);
  tl.to("#desk", { scaleY: 1.006, duration: 1.3, ease: "sine.inOut", yoyo: true, repeat: 3 }, 0);
  // kartu muncul di meja, dibalik ke arah kamera, tulisan tergambar, lalu memenuhi layar
  tl.set("#c1", { opacity: 1, scale: 0.25, scaleX: -0.25, x: 0, y: 0, rotation: 6 }, 2.5);
  tl.to("#c1", { scale: 0.5, scaleX: -0.5, duration: 0.25, ease: "back.out(2)" }, 2.5);
  tl.to("#c1", { scaleX: 0.5, duration: 0.3, ease: "power2.inOut" }, 2.75);
  tl.to("#c1t", { clipPath: "inset(0 0% 0 0)", duration: 1.0, ease: "none" }, 3.4);
  tl.to("#c1", { x: 70, y: -185, scale: 4.2, scaleX: 4.2, rotation: -2, duration: 1.1, ease: "power2.inOut" }, 3.6);

  // ===== ADEGAN 2 (5,5–11,8): kartu terbuka, judul =====
  tl.set("#s2", { opacity: 1 }, 5.5);
  tl.set("#c1", { opacity: 0 }, 5.5);
  tl.set("#sh11", { opacity: 0 }, 5.5);
  tl.set("#pl .bk", { opacity: 0 }, 6.3);
  gsap.set("#pl", { rotationY: 180 });
  gsap.set("#cardg", { x: -245 });
  tl.set("#pl", { rotationY: 180 }, 5.5);
  tl.fromTo("#wrap2", { scale: 1 }, { scale: 1, duration: 0.01, immediateRender: false }, 5.5);
  tl.to("#pl", { rotationY: 0, duration: 1.0, ease: "power2.inOut" }, 5.75);
  tl.to("#cardg", { x: 0, duration: 1.0, ease: "power2.inOut" }, 5.75);
  tl.fromTo("#leak", { opacity: 0, x: -300 }, { opacity: 0.8, x: 100, duration: 0.8, ease: "power1.inOut", immediateRender: false }, 5.8);
  tl.to("#leak", { opacity: 0, duration: 0.6 }, 6.7);
  tl.to("#ttl", { clipPath: "inset(0 0% 0 0)", duration: 1.6, ease: "none" }, 5.9);
  tl.fromTo("#yr", { opacity: 0, y: 14 }, { opacity: 1, y: 0, duration: 0.5, immediateRender: false }, 8.1);
  tl.fromTo("#dir", { opacity: 0, y: 14 }, { opacity: 1, y: 0, duration: 0.5, immediateRender: false }, 9.98);
  tl.to("#sk2 path", { strokeDashoffset: 0, duration: 0.6, ease: "power1.inOut", stagger: 0.12 }, 9.9);
  tl.to("#wrap2", { scale: 2.6, duration: 0.8, ease: "power2.in" }, 11.0);
  tl.to("#white", { opacity: 1, duration: 0.5, ease: "power1.in" }, 11.3);

  // ===== ADEGAN 3 (11,8–20,6): dua dunia =====
  tl.set("#s2", { opacity: 0 }, 11.8);
  tl.set("#sh11", { opacity: 1 }, 11.8);
  tl.set("#plate", { filter: "brightness(1) saturate(1)" }, 11.8);
  tl.set("#desk", { filter: "none" }, 11.8);
  tl.set(["#nightov", "#lamp"], { opacity: 0 }, 11.8);
  tl.set("#lean", { opacity: 1 }, 11.8);
  tl.set("#world", { filter: "none" }, 11.8);
  camSet(11.8, 440, 1080, 1.55);
  tl.to("#white", { opacity: 0, duration: 0.5, ease: "power1.out" }, 11.85);
  // fokus: Tom tajam, latar dan Summer buram
  tl.set(["#plate", "#sumg"], { filter: "blur(3.5px)" }, 11.8);
  tl.to("#deskg", { x: 0, duration: 0.01 }, 11.8);
  tl.to("#desk", { rotation: 0.5, duration: 1.0, ease: "sine.inOut", yoyo: true, repeat: 3, transformOrigin: "50% 100%" }, 12.0);
  // pan lateral, fokus berpindah ke Summer; cahaya biru merembes ke meja Tom
  camMove(16.3, 1.3, 790, 880, 1.8, "sine.inOut");
  tl.to("#sumg", { filter: "blur(0px)", duration: 0.7 }, 16.3);
  tl.to("#plate", { filter: "blur(1px)", duration: 0.7 }, 16.3);
  tl.to("#deskg", { filter: "blur(3.5px)", duration: 0.7 }, 16.3);
  tl.to("#bluecreep", { opacity: 0.55, duration: 1.2 }, 16.4);
  // kartu melayang dari meja Tom ke arah Summer, berhenti di garis cahaya, lalu turun pelan
  camMove(18.2, 0.9, 600, 980, 1.2, "sine.inOut");
  tl.to("#sumg", { filter: "blur(0px)", duration: 0.01 }, 18.2);
  tl.to("#deskg", { filter: "blur(0px)", duration: 0.5 }, 18.2);
  tl.to("#plate", { filter: "blur(0px)", duration: 0.5 }, 18.2);
  tl.to("#lline", { opacity: 1, duration: 0.4 }, 18.5);
  tl.set("#card3", { opacity: 1, x: 0, y: 0, rotation: -4, scale: 0.7 }, 18.7);
  tl.to("#card3", { x: 250, y: -170, rotation: 8, duration: 0.5, ease: "power2.out" }, 18.7);
  tl.to("#card3", { x: 330, y: -150, rotation: 4, duration: 0.4, ease: "sine.inOut" }, 19.2);
  tl.to("#card3", { y: 120, rotation: -3, duration: 0.5, ease: "power1.in" }, 19.6);
  // halaman kalender menutup layar
  tl.to("#pagetear", { clipPath: "inset(0% 0 0 0)", duration: 0.9, ease: "power2.in" }, 19.65);
  tl.to("#bluecreep", { opacity: 0, duration: 0.2 }, 20.4);

  // ===== subtitle (tanpa kotak) mengikuti jeda ucapan =====
  var subs = [[0.55, 1.65, "Cowok bertemu cewek."], [2.6, 3.68, "Tapi sejak awal,"], [3.97, 5.3, "ini bukan kisah cinta."],
    [5.79, 7.5, "(500) Days of Summer."], [8.1, 9.26, "Tahun 2009."], [9.98, 11.46, "Sutradara Marc Webb."],
    [12.0, 15.59, "Tom, penulis kartu ucapan yang percaya cinta sejati."], [16.32, 18.5, "Summer, asisten baru bosnya,"], [18.7, 20.34, "yang tak mau hubungan serius."]];
  subs.forEach(function (s) {
    tl.set("#sub", { opacity: 1, innerHTML: s[2] }, s[0]);
    tl.set("#sub", { opacity: 0 }, s[1]);
  });
  window.__timelines = window.__timelines || {};
  window.__timelines["opening"] = tl;
})();
