(function () {
  var tl = gsap.timeline({ paused: true });
  var VC = { L: 270, R: 810 };
  var P = { L: { warm: 1 }, R: { warm: 0 } };
  function camVars(k, cx, cy, s) {
    var bs = 1 + (s - 1) * 0.7, fs = 1 + (s - 1) * 1.35;       // parallax: latar lambat, foreground cepat
    return {
      world: { x: VC[k] - cx * s, y: 960 - cy * s, scale: s },
      bg: { x: VC[k] - (cx * 0.85 + 540 * 0.15) * bs, y: 960 - (cy * 0.85 + 960 * 0.15) * bs, scale: bs },
      fg: { x: VC[k] - (cx * 1.15 - 81) * fs, y: 960 - (cy * 1.15 - 144) * fs, scale: fs }
    };
  }
  function targets(k) { return { world: "#" + k + "-world,#" + k + "-handw", bg: "#" + k + "-bg", fg: "#" + k + "-fgw" }; }
  function camSet(t, cx, cy, s) {
    ["L", "R"].forEach(function (k) {
      var v = camVars(k, cx, cy, s), g = targets(k);
      ["world", "bg", "fg"].forEach(function (n) { tl.set(g[n], v[n], t); });
    });
  }
  function camMove(t, dur, cx, cy, s, ease) {
    ["L", "R"].forEach(function (k) {
      var v = camVars(k, cx, cy, s), g = targets(k);
      ["world", "bg", "fg"].forEach(function (n) { tl.to(g[n], Object.assign({ duration: dur, ease: ease }, v[n]), t); });
    });
  }
  ["L", "R"].forEach(function (k) {
    var v = camVars(k, 750, 960, 1), g = targets(k);
    ["world", "bg", "fg"].forEach(function (n) { gsap.set(g[n], v[n]); });
    gsap.set("#" + k + "-hug," + "#" + k + "-shg-hug," + "#" + k + "-sum2," + "#" + k + "-shg-sum2", { opacity: 0 });
    gsap.set("#" + k + "-handw", { opacity: 0 });
  });

  // Satu fungsi blocking untuk dua panel; yang berbeda hanya aset pelukan, cahaya, dan hasil akhir.
  function blocking(k, p) {
    var tom = "#" + k + "-tom", sum = "#" + k + "-sum", hug = "#" + k + "-hug";
    var shT = "#" + k + "-shg-tom", shS = "#" + k + "-shg-sum", shH = "#" + k + "-shg-hug", sum2 = "#" + k + "-sum2", shS2 = "#" + k + "-shg-sum2";
    var glow = "#" + k + "-glow", world = ["#" + k + "-bg", "#" + k + "-world", "#" + k + "-fgw"];
    // A–B: berdiri berjarak, bernapas, bergoyang sangat halus (kaki tetap)
    tl.to(tom, { scaleY: 1.008, duration: 1.2, ease: "sine.inOut", yoyo: true, repeat: 3 }, 0);
    tl.to(sum, { scaleY: 1.008, duration: 1.2, ease: "sine.inOut", yoyo: true, repeat: 3 }, 0.6);
    tl.to(tom, { rotation: 0.5, duration: 1.9, ease: "sine.inOut", yoyo: true, repeat: 1 }, 0);
    tl.to(sum, { rotation: -0.7, duration: 1.9, ease: "sine.inOut", yoyo: true, repeat: 1 }, 0.2);
    if (p.warm) tl.to(glow, { opacity: 0.9, duration: 0.8, ease: "power1.out" }, 0.3);
    // rack focus latar pada bidikan B (sama di dua sisi)
    tl.set("#" + k + "-bg", { filter: "blur(2.5px)" }, 1.9);
    tl.set("#" + k + "-bg", { filter: "none" }, 3.9);
    // C: potongan ke pelukan (aset pelukan menggantikan dua figur di titik potong)
    tl.set([tom, sum, shT, shS], { opacity: 0 }, 3.9);
    tl.set([hug, shH], { opacity: 1 }, 3.9);
    tl.set(glow, { x: -170 }, 3.9);
    if (p.warm) {
      tl.fromTo("#L-flash", { opacity: 0.55 }, { opacity: 0, duration: 0.4, ease: "power2.out", immediateRender: false }, 3.9);
      tl.to(hug, { scaleY: 1.006, duration: 1.0, ease: "sine.inOut", yoyo: true, repeat: 1 }, 3.9);
      tl.to(hug, { rotation: 0.8, duration: 1.0, ease: "sine.inOut", yoyo: true, repeat: 1 }, 3.9);
    } else {
      tl.to(hug, { scaleY: 1.004, duration: 0.5, ease: "sine.inOut", yoyo: true, repeat: 1 }, 3.9);
      // pelukan kaku singkat lalu dilepas: dissolve cepat ke berdiri (Summer berdiri dekat, Tom melemas)
      tl.to(hug, { opacity: 0, duration: 0.2 }, 4.85); tl.to(shH, { opacity: 0, duration: 0.2 }, 4.85);
      tl.to([tom, sum2, shT, shS2], { opacity: 1, duration: 0.2 }, 4.85);
      tl.to(tom, { rotation: -3, duration: 0.6, ease: "power2.out" }, 4.95);
    }
    // D: sisipan tangan (potongan keras); latar & figur disembunyikan
    tl.set(world.concat(["#" + k + "-glow"]), { opacity: 0 }, 5.9);
    tl.set("#" + k + "-handw", { opacity: 1 }, 5.9);
    tl.fromTo("#" + k + "-handimg", { y: 14, rotation: -0.4, transformOrigin: "50% 50%" }, { y: -10, rotation: 0.5, duration: 1.6, ease: "sine.inOut" }, 5.9);
    if (p.warm) {
      tl.fromTo("#L-glint", { opacity: 0, scale: 0.25, rotation: -25 }, { opacity: 1, scale: 1, rotation: 12, duration: 0.35, ease: "power2.out" }, 6.45);
      tl.to("#L-glint", { opacity: 0, scale: 0.6, duration: 0.45, ease: "power1.in" }, 6.85);
    }
    // E: kembali ke ruangan. Ekspektasi: Summer larut jadi cahaya. Kenyataan: Summer tetap nyata, Tom melemas.
    tl.set("#" + k + "-handw", { opacity: 0 }, 7.5);
    tl.set(world, { opacity: 1 }, 7.5);
    tl.set([tom, sum2, shT, shS2], { opacity: 1 }, 7.5);
    tl.set([hug, shH], { opacity: 0 }, 7.5);
    tl.to(sum2, { scaleY: 1.008, duration: 1.2, ease: "sine.inOut", yoyo: true, repeat: 1 }, 7.5);
    tl.set(glow, { x: -70, opacity: p.warm ? 0.9 : 0 }, 7.5);
    tl.set(tom, { rotation: p.warm ? 0.5 : -3 }, 7.5);
    if (p.warm) {
      tl.set(sum2, { mixBlendMode: "screen" }, 8.0);
      tl.to(sum2, { filter: "blur(14px) brightness(2.2)", scale: 1.12, duration: 0.9, ease: "power1.in" }, 8.0);
      tl.to(sum2, { opacity: 0, duration: 0.5 }, 8.5);
      tl.to(shS2, { opacity: 0, duration: 0.7 }, 8.0);
      tl.to(glow, { opacity: 0, duration: 1.0 }, 8.4);
    } else {
      tl.to(tom, { rotation: -5, duration: 1.2, ease: "sine.inOut" }, 7.9);
    }
    // bokeh (hanya ekspektasi) hanyut perlahan
    if (p.warm) {
      var bks = document.querySelectorAll("#L .bk");
      for (var i = 0; i < bks.length; i++) tl.to(bks[i], { y: i % 2 ? 40 : -40, duration: 9.5, ease: "none" }, 0);
    }
  }
  blocking("L", P.L);
  blocking("R", P.R);

  // Kamera: parameter shot yang SAMA untuk dua panel; potongan keras antar shot.
  camSet(0, 750, 960, 1);
  camMove(0.2, 1.7, 760, 960, 1.05, "sine.inOut");                    // A  wide
  camSet(1.9, 900, 780, 1.5);                                         // B  medium Summer
  camMove(1.9, 2.0, 870, 780, 1.5, "sine.inOut");
  camSet(3.9, 770, 800, 1.1);                                         // C  pelukan
  camMove(3.9, 2.0, 770, 790, 1.2, "sine.inOut");
  camSet(5.9, 548, 800, 1.3);                                         // D  sisipan tangan
  camMove(5.9, 1.6, 548, 790, 1.9, "sine.inOut");
  camSet(7.5, 760, 900, 1.12);                                        // E  tarik mundur
  camMove(7.5, 2.0, 750, 960, 1.0, "sine.inOut");
  // akhir: panel kenyataan melebar menutup layar
  tl.to("#L", { opacity: 0, duration: 0.5, ease: "power1.in" }, 9.0);
  tl.to("#R", { clipPath: "inset(0px 0px 0px 0px)", duration: 0.5, ease: "power2.inOut" }, 9.0);
  tl.to("#R-in", { x: -270, duration: 0.5, ease: "power2.inOut" }, 9.0);
  tl.to("#split", { opacity: 0, duration: 0.3 }, 8.9);
  tl.to("#topgrad", { opacity: 0, duration: 0.3 }, 2.2);
  tl.to("#split", { height: 1920, duration: 0.3, ease: "power2.out" }, 0.1);
  tl.to(".label", { opacity: 1, duration: 0.3 }, 0.3);
  tl.to(".label", { opacity: 0, duration: 0.3 }, 2.2);

  var subs = [[0.17, 1.48, "Adegan paling terkenal:"], [1.79, 3.79, "ekspektasi lawan kenyataan."],
    [4.58, 7.0, "Tom ternyata lebih mencintai bayangannya tentang Summer,"], [7.0, 9.25, "bukan Summer yang nyata."]];
  subs.forEach(function (s) {
    tl.set("#sub", { opacity: 1, innerHTML: s[2] }, s[0]);
    tl.set("#sub", { opacity: 0 }, s[1]);
  });
  tl.to("#subgrad", { opacity: 0, duration: 0.3 }, 9.2);
  window.__timelines = window.__timelines || {};
  window.__timelines["evr"] = tl;
})();
