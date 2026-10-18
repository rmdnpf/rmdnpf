(function () {
  var tl = gsap.timeline({ paused: true });
  var F = 0.92, VC = 540;
  function camVars(cx, cy, s) {
    var bs = 1 + (s - 1) * F;                       // latar hampir ikut zoom (lantai tetap menempel pada kaki)
    return {
      world: { x: VC - cx * s, y: 960 - cy * s, scale: s },
      bg: { x: VC - (cx * F + 540 * (1 - F)) * bs, y: 960 - (cy * F + 960 * (1 - F)) * bs, scale: bs }
    };
  }
  function camSet(t, cx, cy, s) { var v = camVars(cx, cy, s); tl.set("#world", v.world, t); tl.set("#bg", v.bg, t); }
  function camMove(t, dur, cx, cy, s, ease) {
    var v = camVars(cx, cy, s);
    tl.to("#world", Object.assign({ duration: dur, ease: ease }, v.world), t);
    tl.to("#bg", Object.assign({ duration: dur, ease: ease }, v.bg), t);
  }
  var c0 = camVars(540, 960, 1); gsap.set("#world", c0.world); gsap.set("#bg", c0.bg);
  gsap.set("#bgs", { x: 0 });
  var POSES = ["strut", "jump", "land", "point"], CASTS = ["strut", "land", "point"];
  function show(t, p) {
    POSES.forEach(function (q) { tl.set("#d-" + q, { opacity: q === p ? 1 : 0 }, t); });
    CASTS.forEach(function (q) { tl.set("#c-" + q, { opacity: q === p ? 0.4 : 0 }, t); });
  }
  gsap.set("#d-strut", { opacity: 1 }); gsap.set("#c-strut", { opacity: 0.4 });

  // --- penari: 5 fase pose
  // A (0,2-1,8) langkah percaya diri: pose strut, naik-turun di tempat; latar bergulir (kamera mengikuti)
  tl.to("#dancer", { y: -10, rotation: 1.2, duration: 0.225, ease: "sine.inOut", yoyo: true, repeat: 6 }, 0.2);
  tl.to("#bgs", { x: -300, duration: 1.7, ease: "sine.inOut" }, 0.1);
  // B (1,8-3,3) antisipasi, lompat, mendarat
  tl.set("#dancer", { y: 0, rotation: 0 }, 1.8);
  show(1.8, "land");
  tl.to("#dancer", { scaleY: 0.93, duration: 0.2, ease: "power1.in" }, 1.8);
  show(2.0, "jump");
  tl.to("#dancer", { y: -380, scaleY: 1.04, duration: 0.45, ease: "power2.out" }, 2.0);
  tl.to("#dancer", { y: 0, scaleY: 1, duration: 0.45, ease: "power2.in" }, 2.45);
  tl.to("#dground", { scaleX: 0.55, opacity: 0.4, duration: 0.45, ease: "power2.out" }, 2.0);
  tl.to("#dground", { scaleX: 1, opacity: 1, duration: 0.45, ease: "power2.in" }, 2.45);
  tl.fromTo("#flash", { opacity: 0.25 }, { opacity: 0, duration: 0.25, immediateRender: false }, 2.0);
  show(2.9, "land");
  tl.fromTo("#dancer", { scaleY: 0.9 }, { scaleY: 1, duration: 0.4, ease: "elastic.out(1,0.55)", immediateRender: false }, 2.9);
  tl.fromTo("#flash", { opacity: 0.3 }, { opacity: 0, duration: 0.25, immediateRender: false }, 2.9);
  // C (3,3-4,3) menunjuk ke langit; burung hinggap
  show(3.3, "point");
  tl.to("#dancer", { rotation: 1.2, duration: 0.5, ease: "sine.inOut", yoyo: true, repeat: 1 }, 3.3);
  // D (4,3-6,1) rangkaian pose pada ketukan
  show(4.3, "strut");
  tl.to("#dancer", { y: -10, duration: 0.2, ease: "sine.inOut", yoyo: true, repeat: 1 }, 4.3);
  show(4.7, "land");
  tl.fromTo("#dancer", { scaleY: 0.94 }, { scaleY: 1, duration: 0.3, ease: "power2.out", immediateRender: false }, 4.7);
  show(5.1, "jump");
  tl.to("#dancer", { y: -150, duration: 0.2, ease: "power2.out" }, 5.1);
  tl.to("#dancer", { y: 0, duration: 0.2, ease: "power2.in" }, 5.3);
  show(5.45, "land");
  tl.fromTo("#dancer", { scaleY: 0.94 }, { scaleY: 1, duration: 0.25, ease: "power2.out", immediateRender: false }, 5.45);
  show(5.75, "point");

  // --- kerumunan siluet (dari kode): muncul bergantian, menari dengan fase berbeda
  var starts = [3.2, 3.35, 3.5, 3.65, 3.8, 3.95], seq = ["strut", "land", "point", "land"];
  for (var i = 0; i < starts.length; i++) {
    (function (i) {
      var g = "#cr" + i, el = document.querySelector(g);
      var imgs = el.querySelectorAll("img");
      if (el.getAttribute("data-flip") === "1")
        for (var m = 0; m < imgs.length; m++) gsap.set(imgs[m], { transformOrigin: (-parseFloat(imgs[m].style.left)) + "px 0px", scaleX: -1 });
      tl.fromTo(g, { opacity: 0, scale: 0.5 }, { opacity: 1, scale: 1, duration: 0.3, ease: "back.out(2)", immediateRender: false }, starts[i]);
      var j = 0;
      for (var t = starts[i]; t < 6.1; t += 0.45, j++) {
        var p = seq[(j + i) % seq.length];
        ["strut", "land", "point"].forEach(function (q) { tl.set("#cr" + i + "-" + q, { opacity: q === p ? 0.5 : 0 }, t); });
      }
      tl.to(g, { y: -10, duration: 0.225, ease: "sine.inOut", yoyo: true, repeat: Math.floor((6.0 - starts[i]) / 0.225) - 1 }, starts[i] + 0.3);
    })(i);
  }
  // pejalan di latar depan lewat sebentar (oklusi)
  tl.fromTo("#fgs", { x: 1240, y: 820, opacity: 0.5, scaleX: -1 }, { x: -700, duration: 1.3, ease: "none", immediateRender: false }, 0.25);
  tl.set("#fgs", { opacity: 0 }, 1.6);

  // --- burung biru
  var h = CFG.hand, bx = h[0] - 6, by = h[1] + 20;
  tl.set("#bird", { x: -140, y: 300, opacity: 0 }, 3.3);
  tl.set("#bird", { opacity: 1 }, 3.4);
  tl.to("#bird", { x: bx, duration: 0.55, ease: "power1.inOut" }, 3.4);
  tl.to("#bird", { y: 240, duration: 0.25, ease: "power1.out" }, 3.4);
  tl.to("#bird", { y: by, duration: 0.3, ease: "power2.in" }, 3.65);
  tl.to("#bwing", { scaleY: 0.25, duration: 0.07, ease: "none", yoyo: true, repeat: 7 }, 3.4);
  tl.to("#bird", { y: by - 8, duration: 0.15, ease: "sine.inOut", yoyo: true, repeat: 1 }, 4.0);
  tl.to("#bird", { x: 1300, y: 80, duration: 0.8, ease: "power2.in" }, 4.25);
  tl.to("#bwing", { scaleY: 0.25, duration: 0.07, ease: "none", yoyo: true, repeat: 9 }, 4.25);
  tl.set("#bird", { opacity: 0 }, 5.1);

  // --- sketsa arsitektur tergambar di menara lalu terisi warna
  tl.to("#sketch path", { strokeDashoffset: 0, duration: 0.5, ease: "power1.inOut", stagger: 0.05 }, 5.0);
  tl.to("#skfill", { opacity: 1, duration: 0.4 }, 5.7);

  // --- kamera: potongan keras tiap bagian, gerak sebagai pengikut penari
  camSet(0, 540, 960, 1.0);
  camMove(0.2, 1.6, 540, 960, 1.08, "sine.inOut");                         // A  mengikuti langkah
  camSet(1.8, 540, 1010, 1.25);                                            // B  lebih dekat untuk lompatan
  camMove(2.0, 0.45, 540, 880, 1.25, "power2.out");
  camMove(2.45, 0.5, 540, 1010, 1.25, "power2.in");
  camSet(3.3, 540, 990, 1.0);                                              // C  lebar: burung dan kerumunan
  camMove(3.3, 1.3, 540, 960, 1.05, "sine.inOut");
  camMove(4.6, 1.1, 540, 520, 1.0, "power2.inOut");                        // D  menyapu naik ke gedung
  camMove(5.7, 0.45, 540, 760, 1.0, "power1.inOut");

  // --- pembekuan seperti foto, lalu memutih ke kertas (menuju adegan berikutnya)
  tl.fromTo("#flash", { opacity: 0.9 }, { opacity: 0, duration: 0.25, immediateRender: false }, 6.15);
  tl.to("#in", { scale: 0.94, duration: 0.35, ease: "power2.out" }, 6.2);
  tl.to("#freeze", { boxShadow: "inset 0 0 0 40px #efe3cf", duration: 0.2 }, 6.2);
  tl.to("#in", { opacity: 0, duration: 0.2 }, 6.4);

  // --- subtitle: tanpa kotak; mengikuti jeda ucapan VO 06 (+0,05 dtk)
  var subs = [[0.2, 2.15, "Tapi ada juga tarian di jalan,"], [2.33, 3.9, "lagu-lagu indie,"], [4.16, 6.3, "dan kota Los Angeles yang jadi saksi."]];
  subs.forEach(function (s) {
    tl.set("#sub", { opacity: 1, innerHTML: s[2] }, s[0]);
    tl.set("#sub", { opacity: 0 }, s[1]);
  });
  tl.to("#subgrad", { opacity: 0, duration: 0.2 }, 6.3);
  window.__timelines = window.__timelines || {};
  window.__timelines["dance"] = tl;
})();
