(function () {
  var FLOOR = 1500;
  var tl = gsap.timeline({ paused: true });
  var VC = { L: 270, R: 810 };
  var D = { L: { warm: 1 }, R: { warm: 0 } };
  function camVars(k, cx, cy, s) {
    var bs = 1 + (s - 1) * 0.7;                       // parallax: latar bergerak lebih lambat
    return {
      world: { x: VC[k] - cx * s, y: 960 - cy * s, scale: s },
      bg: { x: VC[k] - (cx * 0.85 + 540 * 0.15) * bs, y: 960 - (cy * 0.85 + 960 * 0.15) * bs, scale: bs }
    };
  }
  function camSet(t, cx, cy, s) {
    ["L", "R"].forEach(function (k) {
      var v = camVars(k, cx, cy, s);
      tl.set("#" + k + "-world", v.world, t); tl.set("#" + k + "-bg", v.bg, t);
    });
  }
  function camMove(t, dur, cx, cy, s, ease) {
    ["L", "R"].forEach(function (k) {
      var v = camVars(k, cx, cy, s);
      tl.to("#" + k + "-world", Object.assign({ duration: dur, ease: ease }, v.world), t);
      tl.to("#" + k + "-bg", Object.assign({ duration: dur, ease: ease }, v.bg), t);
    });
  }
  function $(id) { return document.getElementById(id); }
  ["L", "R"].forEach(function (k) {
    var v = camVars(k, 540, 960, 1);
    gsap.set("#" + k + "-world", v.world); gsap.set("#" + k + "-bg", v.bg);
  });
  // Satu fungsi blocking dipakai untuk dua panel; hanya parameter pose/cahaya yang berbeda.
  function blocking(k, p) {
    var tom = "#" + k + "-tom", lean = "#" + k + "-sum-lean", twirl = "#" + k + "-sum-twirl";
    var shT = "#" + k + "-shT", shS = "#" + k + "-shS";
    // pose Summer per panel: ekspektasi pakai twirl (melayang, hangat), kenyataan pakai lean (berdiri kaku)
    var S = p.warm ? twirl : lean, Sx = p.warm ? lean : twirl;
    gsap.set(Sx, { opacity: 0 });
    gsap.set(twirl, { opacity: p.warm ? 1 : 0 });
    gsap.set(lean, { opacity: p.warm ? 0 : 1 });
        // napas (Tom & Summer, fase berbeda) - sama di dua sisi
    tl.to(tom, { scaleY: 1.012, duration: 1.2, ease: "sine.inOut", yoyo: true, repeat: 7 }, 0);
    tl.to(S, { scaleY: 1.01, duration: 1.2, ease: "sine.inOut", yoyo: true, repeat: 7 }, 0.6);
    tl.to(tom, { rotation: 0.6, duration: 2.0, ease: "sine.inOut", yoyo: true, repeat: 4 }, 0);
    // Shot A: Summer masuk (busur melayang di ekspektasi; kenyataan: sudah berdiri, hanya miring sedikit)
    if (p.warm) {
      tl.fromTo(S, { x: 160, y: -40, rotation: -30 }, { x: 0, y: 0, rotation: 0, duration: 0.6, ease: "power2.out" }, 0.3);
      tl.fromTo(shS, { opacity: 0 }, { opacity: 1, duration: 0.6 }, 0.3);
    } else {
      tl.fromTo(S, { rotation: -2 }, { rotation: 0, duration: 0.8, ease: "power2.out" }, 0.3);
    }
    // Shot C: kedekatan. Kaki TIDAK bergeser: jarak ditetapkan saat potongan keras, lalu hanya rotasi dari pinggul.
    var T = 3.9;
    if (p.warm) { tl.set(twirl, { opacity: 0 }, T); tl.set(lean, { opacity: 1 }, T); }
    tl.set(lean, { x: -55 }, T); tl.set(shS, { x: -55 }, T); tl.set(tom, { x: 0 }, T);
    if (p.warm) {
      tl.to(tom, { rotation: 6, duration: 0.5, ease: "power2.out" }, 4.3);
      tl.to(lean, { rotation: -4, duration: 0.5, ease: "power2.out" }, 4.35);
      tl.to([tom, lean], { y: -8, duration: 0.55, ease: "sine.inOut", yoyo: true, repeat: 3 }, 4.9);   // goyang berdua (kaki terangkat sedikit)
    } else {
      tl.to(tom, { rotation: 4, duration: 0.4, ease: "power2.out" }, 4.3);
      tl.to(lean, { rotation: 1.5, duration: 0.4, ease: "power2.out" }, 4.35);   // Summer tidak ikut condong
      tl.to(tom, { rotation: 7, duration: 0.2 }, 4.9);                // Tom memeluk sendirian, kaku singkat
      tl.to(lean, { rotation: 3.5, duration: 0.2 }, 4.9);               // Summer sedikit condong menjauh, tangan tetap di belakang
      tl.to([tom, lean], { rotation: 0, duration: 0.35, ease: "power2.inOut" }, 5.5);
      tl.to(tom, { rotation: -4, duration: 0.5, ease: "power2.out" }, 5.35);   // Tom melemas
    }
        // Shot D: sisipan tangan; figur disembunyikan (potongan keras)
    var figs = [tom, lean, twirl, shT, shS, "#" + k + "-fg"];
    tl.set(figs, { opacity: 0 }, 5.9);
    tl.set("#" + k + "-hand", { opacity: 1 }, 5.9);
    tl.fromTo("#" + k + "-hand", { y: 24, rotation: -2 }, { y: -8, rotation: 1.5, duration: 1.6, ease: "sine.inOut" }, 5.9);
    if (!p.warm) {
      tl.set("#" + k + "-hand .ring", { opacity: 1 }, 6.55);
      tl.fromTo("#" + k + "-hand .glint", { opacity: 0, x: 0 }, { opacity: 0.95, x: 0, duration: 0.5, ease: "power1.inOut" }, 6.55);
      tl.to("#" + k + "-hand .glint", { opacity: 0, duration: 0.2 }, 7.05);
    }
    tl.set("#" + k + "-hand", { opacity: 0 }, 7.5);
    // Shot E: kembali ke figur. Summer: ekspektasi larut jadi cahaya; kenyataan tetap nyata
    tl.set([tom, shT, shS, "#" + k + "-fg"], { opacity: 1 }, 7.5);
    tl.set(shT, { opacity: 1 }, 7.5);
    tl.set(lean, { opacity: 1, x: -55 }, 7.5);
    tl.set(shS, { x: -55 }, 7.5);
    tl.set(tom, { rotation: p.warm ? 2 : -4, x: 0, y: 0 }, 7.5);
    if (p.warm) {
      tl.set(lean, { mixBlendMode: "screen" }, 8.1);
      tl.to(lean, { filter: "blur(14px) brightness(2.2)", scale: 1.15, duration: 0.9, ease: "power1.in" }, 8.1);
      tl.to(lean, { opacity: 0, duration: 0.5 }, 8.6);
      tl.to(shS, { opacity: 0, duration: 0.7 }, 8.1);
    } else {
      tl.to(tom, { rotation: -6, duration: 1.2, ease: "sine.inOut" }, 7.9);
    }
  }
  blocking("L", D.L);
  blocking("R", D.R);

  // bayangan Tom menari di dinding (ekspektasi, shot A): ganti pose tiap 0.35 dtk
  var da = "#L-dance-a", db = "#L-dance-b";
  var t = 0.2, on = 0;
  while (t < 1.9) {
    tl.set(on ? db : da, { opacity: 0.4 }, t);
    tl.set(on ? da : db, { opacity: 0 }, t);
    tl.to(on ? db : da, { x: 14, duration: 0.35, ease: "sine.inOut" }, t);
    on = 1 - on; t += 0.35;
  }
  tl.set([da, db], { opacity: 0 }, 1.9);
  // bokeh bergerak lambat (ekspektasi)
  var bks = document.querySelectorAll("#L .bk");
  for (var i = 0; i < bks.length; i++) {
    tl.to(bks[i], { y: (i % 2 ? 40 : -40), duration: 9.5, ease: "none" }, 0);
  }

  // Kamera: parameter shot yang SAMA dipakai dua panel. Potongan keras antar shot.
  camSet(0, 540, 960, 1);
  camMove(0.2, 1.7, 545, 960, 1.05, "sine.inOut");                      // A
  camSet(1.9, 720, 1010, 1.6);                                          // B
  camMove(1.9, 2.0, 670, 1010, 1.6, "sine.inOut");
  camSet(3.9, 545, 1040, 1.12);                                         // C
  camMove(3.9, 2.0, 540, 1040, 1.2, "sine.inOut");
  camSet(5.9, 560, 1000, 1.9);                                          // D
  camMove(5.9, 1.6, 560, 1000, 2.05, "sine.inOut");
  camSet(7.5, 545, 1000, 1.15);                                         // E
  camMove(7.5, 2.0, 540, 960, 1.0, "sine.inOut");
  // akhir: panel kenyataan melebar menutup layar
  tl.to("#L", { opacity: 0.0, duration: 0.5, ease: "power1.in" }, 9.0);
  tl.to("#R", { clipPath: "inset(0px 0px 0px 0px)", duration: 0.5, ease: "power2.inOut" }, 9.0);
  tl.to("#R-in", { x: -270, duration: 0.5, ease: "power2.inOut" }, 9.0);
  tl.to("#split", { opacity: 0, duration: 0.3 }, 8.9);
  tl.to("#topgrad", { opacity: 0, duration: 0.3 }, 2.2);
  tl.to("#split", { height: 1920, duration: 0.3, ease: "power2.out" }, 0.1);
  tl.to(".label", { opacity: 1, duration: 0.3 }, 0.3);
  tl.to(".label", { opacity: 0, duration: 0.3 }, 2.2);

  // Subtitle: tanpa kotak, hanya gradasi; mengikuti chunk VO05 (+0.05)
  var subs = [
    [0.17, 1.48, "Adegan paling terkenal:"],
    [1.79, 3.79, "ekspektasi lawan kenyataan."],
    [4.58, 7.0, "Tom ternyata lebih mencintai bayangannya tentang Summer,"],
    [7.0, 9.25, "bukan Summer yang nyata."]
  ];
  subs.forEach(function (s) {
    tl.set("#sub", { opacity: 1, innerHTML: s[2] }, s[0]);
    tl.set("#sub", { opacity: 0 }, s[1]);
  });
  tl.to("#subgrad", { opacity: 0, duration: 0.3 }, 9.2);
  window.__timelines = window.__timelines || {};
  window.__timelines["evr"] = tl;
})();
