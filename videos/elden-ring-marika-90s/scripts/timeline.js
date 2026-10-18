window.__timelines = window.__timelines || {};
const TM = __TIMING__;
const LS = TM.LS, ST = TM.ST, DUR = TM.DUR, TOTAL = TM.TOTAL, D = TM.D;
const tl = gsap.timeline({ paused: true });
const $ = (s) => document.querySelector(s), $$ = (s) => document.querySelectorAll(s);
const J = (i) => { const s = Math.sin(i * 127.1 + 311.7) * 43758.5453; return s - Math.floor(s); };
const T0 = (n, dt) => LS[n] + dt;              // waktu relatif awal VO baris n
const S0 = (n, dt) => ST[n] + dt;              // waktu relatif awal scene n

// ---------- umum: fade scene masuk/keluar ----------
for (let n = 1; n <= 11; n++) {
  tl.fromTo("#f" + n, { opacity: 0 }, { opacity: 1, duration: n === 1 ? 0.9 : 0.7, ease: "power1.out" }, ST[n]);
  tl.to("#f" + n, { opacity: 0, duration: n === 11 ? 2.0 : 0.45, ease: "power1.in" }, ST[n] + DUR[n] - (n === 11 ? 2.0 : 0.45));
}
// ---------- umum: partikel naik/turun, bg paralaks ----------
const drift = (n, dir, dist) => $$("#f" + n + " .pt").forEach((p, i) => {
  const d = DUR[n], sp = 0.6 + J(i + n) * 0.9;
  tl.fromTo(p, { y: 0 }, { y: dir * dist * sp, x: (J(i * 3 + n) - 0.5) * 80, duration: d, ease: "none" }, ST[n]);
});
const bgMove = (n, s0, s1, y0, y1, x0 = 0, x1 = 0) => tl.fromTo("#f" + n + "-bg", { scale: s0, y: y0, x: x0, transformOrigin: "50% 50%" }, { scale: s1, y: y1, x: x1, duration: DUR[n], ease: "none", transformOrigin: "50% 50%" }, ST[n]);
const lay = (sel, n, a, b) => tl.fromTo(sel, a, Object.assign({ duration: DUR[n], ease: "none" }, b), ST[n]);
const shake = (t, amp, n) => { for (let k = 0; k < 14; k++) tl.set("#f" + n, { x: (J(k + 5) - 0.5) * amp * (1 - k / 14), y: (J(k + 9) - 0.5) * amp * (1 - k / 14) }, t + k * 0.04); tl.set("#f" + n, { x: 0, y: 0 }, t + 14 * 0.04); };
const flash = (t, col, op) => { tl.fromTo("#flash", { opacity: op, backgroundColor: col }, { opacity: 0, duration: 0.55, ease: "power2.out", immediateRender: false }, t); };

// ---------- subtitle ----------
$$(".sub").forEach((el, i) => {
  const id = "#u" + String(i + 1).padStart(2, "0"), a = parseFloat(el.dataset.start);
  tl.fromTo(id, { opacity: 0, y: 14 }, { opacity: 1, y: 0, duration: 0.25, ease: "power2.out" }, a);
});

// ===== F1 hook =====
bgMove(1, 1.18, 1.0, 60, 0);
lay("#f1-marika", 1, { scale: 1.07, y: 40, transformOrigin: "50% 100%" }, { scale: 1.0, y: 0, transformOrigin: "50% 100%" });
lay("#f1-ring", 1, { rotation: -6, scale: 0.96, transformOrigin: "50% 50%" }, { rotation: 6, scale: 1.04, transformOrigin: "50% 50%" });
tl.fromTo("#f1-glow", { opacity: 0.3 }, { opacity: 0.65, duration: 3, yoyo: true, repeat: 3, ease: "sine.inOut" }, 0);
tl.fromTo("#f1-title", { opacity: 0, y: 40, scale: 1.08, transformOrigin: "50% 50%" }, { opacity: 1, y: 0, scale: 1, transformOrigin: "50% 50%", duration: 1.6, ease: "power3.out" }, 0.9);
tl.fromTo("#f1-warn", { opacity: 0 }, { opacity: 1, duration: 0.5 }, 0.5); tl.to("#f1-warn", { opacity: 0, duration: 0.6 }, 3.3);
tl.to("#f1-title", { opacity: 0.0, duration: 0.8 }, T0(1, 5.6));        // judul memudar sebelum 'Mengapa?'
tl.fromTo("#f1-ring", { filter: "drop-shadow(0 0 30px rgba(196,163,90,0.6))" }, { filter: "drop-shadow(0 0 90px rgba(255,220,130,1))", duration: 1.4, yoyo: true, repeat: 1, ease: "sine.inOut" }, T0(1, 7.2));
drift(1, -1, 260);

// ===== F2 Golden Order =====
bgMove(2, 1.0, 1.14, 0, -150);
lay("#f2-marika", 2, { y: 20, scale: 1.0, transformOrigin: "50% 100%" }, { y: -10, scale: 1.03, transformOrigin: "50% 100%" });
lay("#f2-ring", 2, { rotation: 0, transformOrigin: "50% 50%" }, { rotation: 20, transformOrigin: "50% 50%" });
tl.fromTo("#f2-ring", { opacity: 0.6 }, { opacity: 1, duration: 2.2, yoyo: true, repeat: 4, ease: "sine.inOut" }, ST[2]);
tl.fromTo("#f2 .chap", { opacity: 0, y: -20 }, { opacity: 1, y: 0, duration: 0.8 }, S0(2, 0.6));
drift(2, -1, 180);

// ===== F3 Night of Black Knives =====
bgMove(3, 1.0, 1.1, 0, -60, 0, -30);
lay("#f3-godwyn", 3, { y: 25, scale: 1.0, transformOrigin: "50% 100%" }, { y: 0, scale: 1.025, transformOrigin: "50% 100%" });
tl.set("#f3-soul", { opacity: 0 }, 0);
$$("#f3 .blade").forEach((b, i) => {
  const t = T0(3, 2.2 + i * 0.7);
  tl.fromTo(b, { x: i % 2 ? 1400 : -1400, opacity: 0 }, { x: 0, opacity: 1, duration: 0.55, ease: "power3.out" }, t);
  tl.to(b, { opacity: 0, duration: 0.5 }, t + 1.1);
});
tl.fromTo("#f3-soul", { opacity: 0, y: 160, scale: 0.6 }, { opacity: 0.9, y: -60, scale: 1.1, duration: 2.6, ease: "power1.out" }, T0(3, 4.6));
tl.to("#f3-soul", { opacity: 0, y: -380, duration: 1.8, ease: "power1.in" }, T0(3, 7.0));
tl.fromTo("#f3 .chap", { opacity: 0 }, { opacity: 1, duration: 0.8 }, S0(3, 0.5));
drift(3, -1, 200);

// ===== F4 Ranni =====
bgMove(4, 1.12, 1.0, 40, 0);
lay("#f4-ranni", 4, { y: 30, x: -10, transformOrigin: "50% 100%" }, { y: 0, x: 10, transformOrigin: "50% 100%" });
tl.fromTo("#f4-fingers", { y: -520, opacity: 0.0 }, { y: 0, opacity: 1, duration: 2.6, ease: "power2.out" }, T0(4, 3.7));
tl.to("#f4-fingers", { y: 22, duration: 1.4, yoyo: true, repeat: 1, ease: "sine.inOut" }, T0(4, 6.4));
tl.fromTo("#f4 .chap", { opacity: 0, y: 14 }, { opacity: 1, y: 0, duration: 0.7 }, T0(4, 3.4));
drift(4, -1, 120);

// ===== F5 Shattering =====
const hit5 = T0(5, 4.4);
bgMove(5, 1.0, 1.06, 0, -30);
$$("#f5 .shard").forEach((s) => { const dx = +s.dataset.dx, dy = +s.dataset.dy, r = +s.dataset.rot;
  tl.set(s, { x: -dx, y: -dy, rotation: 0, transformOrigin: "50% 50%" }, 0);
  tl.to(s, { x: 0, y: 0, rotation: r, duration: 0.6, ease: "power4.out" }, hit5);
  tl.to(s, { x: dx * 1.7, y: dy * 1.7 + 90, rotation: r * 3, duration: DUR[5] - (hit5 - ST[5]) - 0.8, ease: "power1.out" }, hit5 + 0.6);
});
$$("#f5 .crk").forEach((p) => { const L = p.getTotalLength(); tl.set(p, { strokeDasharray: L, strokeDashoffset: L }, 0); });
tl.set("#f5-cracks", { opacity: 0 }, 0);
tl.set("#f5-cracks", { opacity: 1 }, hit5 - 0.5);
tl.to("#f5 .crk", { strokeDashoffset: 0, duration: 0.5, stagger: 0.03, ease: "power2.out" }, hit5 - 0.5);
tl.to("#f5-cracks", { opacity: 0, duration: 0.5 }, hit5 + 0.4);
tl.fromTo("#f5-marika", { y: 40, scale: 1.0, transformOrigin: "50% 100%" }, { y: 0, scale: 1.0, duration: 1.6, ease: "power2.out", transformOrigin: "50% 100%" }, ST[5]);
tl.to("#f5-marika", { y: 38, scale: 1.04, duration: 0.5, ease: "power4.in", transformOrigin: "50% 100%" }, hit5 - 0.5);
tl.to("#f5-marika", { y: 0, scale: 1.0, duration: 1.4, ease: "power2.out", transformOrigin: "50% 100%" }, hit5 + 0.1);
tl.fromTo("#f5-glow", { opacity: 0.25 }, { opacity: 0.9, duration: 0.4, yoyo: true, repeat: 1 }, hit5);
flash(hit5, "#ffe9b0", 0.9); shake(hit5, 36, 5);
tl.fromTo("#f5 .chap", { opacity: 0 }, { opacity: 1, duration: 0.6 }, hit5 + 0.3);
drift(5, -1, 320);

// ===== F6 perang demigod =====
bgMove(6, 1.0, 1.1, 0, 0, 0, -40);
tl.fromTo("#f6-land", { opacity: 0 }, { opacity: 1, duration: 1.2 }, S0(6, 0.3));
$$("#f6 .dotg").forEach((g, i) => {
  const t = T0(6, 1.2 + i * 0.9);
  tl.fromTo(g.querySelector(".dcore"), { opacity: 0, attr: { r: 2 } }, { opacity: 1, attr: { r: 16 }, duration: 0.4, ease: "back.out(2)" }, t);
  tl.fromTo(g.querySelector(".dglow"), { opacity: 0, attr: { r: 6 } }, { opacity: 1, attr: { r: 70 }, duration: 1.4, ease: "power2.out" }, t);
  tl.fromTo(g.querySelector(".dring"), { attr: { r: 20 }, opacity: 0.9 }, { attr: { r: 90 }, opacity: 0, duration: 1.1, repeat: 2, ease: "power1.out" }, t + 0.3);
});
tl.fromTo("#f6 .chap", { opacity: 0, y: -20 }, { opacity: 1, y: 0, duration: 0.7 }, S0(6, 0.4));
drift(6, -1, 340);

// ===== F7 tanpa jawaban =====
bgMove(7, 1.0, 1.12, 0, -90);
tl.fromTo("#f7-marika", { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 1.8, ease: "power2.out" }, S0(7, 0.4));
lay("#f7-marika", 7, { scale: 1.0, transformOrigin: "50% 0%" }, { scale: 1.035, transformOrigin: "50% 0%" });
[["#f7-g1", 0], ["#f7-g2", 1], ["#f7-g3", 2]].forEach(([g, i]) => { tl.fromTo(g, { opacity: 0, scale: 0.4 }, { opacity: 0.8, scale: 1, duration: 1.2, ease: "power2.out", transformOrigin: "50% 50%" }, T0(7, 5.2 + i * 0.9)); tl.to(g, { opacity: 0.4, duration: 1.1, yoyo: true, repeat: 3, ease: "sine.inOut" }, T0(7, 6.4 + i * 0.9)); });
["#f7-t1", "#f7-t2", "#f7-t3"].forEach((g, i) => tl.fromTo(g, { opacity: 0, y: 18 }, { opacity: 1, y: 0, duration: 0.6 }, T0(7, 5.6 + i * 0.9)));
tl.fromTo("#f7 .chap", { opacity: 0 }, { opacity: 1, duration: 0.8 }, S0(7, 0.4));
drift(7, -1, 160);

// ===== F8 teori 1 =====
bgMove(8, 1.0, 1.08, 0, -40);
lay("#f8-marika", 8, { y: 10, scale: 1.0, transformOrigin: "50% 100%" }, { y: 0, scale: 1.03, transformOrigin: "50% 100%" });
tl.fromTo("#f8-godwyn", { opacity: 0, x: 40 }, { opacity: 0.4, x: 0, duration: 2.0 }, T0(8, 3.2));
tl.to("#f8-godwyn", { opacity: 0, x: -30, duration: 2.2 }, T0(8, 6.0));
tl.fromTo("#f8 .theory", { opacity: 0, y: -16 }, { opacity: 1, y: 0, duration: 0.7 }, S0(8, 0.5));
tl.fromTo("#f8 .tframe", { opacity: 0 }, { opacity: 0.75, duration: 1.0 }, S0(8, 0.5));
drift(8, 1, 360);

// ===== F9 teori 2 =====
const snap9 = T0(9, 6.3);
bgMove(9, 1.0, 1.08, 0, -30);
lay("#f9-marika", 9, { y: 14, scale: 1.0, transformOrigin: "50% 100%" }, { y: 0, scale: 1.03, transformOrigin: "50% 100%" });
tl.fromTo("#f9-fingers", { y: -460 }, { y: 0, duration: 2.4, ease: "power2.out" }, S0(9, 0.3));
$$("#f9 .chain").forEach((c, i) => { const L = c.getTotalLength(); tl.set(c, { strokeDasharray: "22 9", opacity: 0 }, 0);
  tl.fromTo(c, { opacity: 0 }, { opacity: 0.95, duration: 0.5 }, S0(9, 1.6 + i * 0.3));
  tl.to(c, { strokeWidth: 10, duration: 0.8, yoyo: true, repeat: 3 }, S0(9, 2.2 + i * 0.3));
  tl.to(c, { y: 260 + i * 70, x: (i - 1) * 90, rotation: (i - 1) * 18, opacity: 0, duration: 1.1, ease: "power2.in", transformOrigin: "50% 0%" }, snap9); });
tl.to("#f9-marika", { y: -26, scale: 1.05, duration: 0.5, ease: "power3.out", transformOrigin: "50% 100%" }, snap9 - 0.1);
tl.to("#f9-fingers", { y: -380, opacity: 0.6, duration: 1.8, ease: "power2.in" }, snap9 + 0.3);
flash(snap9, "#ff5a3c", 0.55); shake(snap9, 22, 9);
tl.fromTo("#f9 .theory", { opacity: 0, y: -16 }, { opacity: 1, y: 0, duration: 0.7 }, S0(9, 0.5));
tl.fromTo("#f9 .tframe", { opacity: 0 }, { opacity: 0.75, duration: 1.0 }, S0(9, 0.5));
drift(9, -1, 240);

// ===== F10 teori 3 =====
bgMove(10, 1.14, 1.0, 40, 0);
tl.fromTo("#f10-tarn", { x: -50, opacity: 0 }, { x: 0, opacity: 1, duration: 1.8, ease: "power2.out" }, S0(10, 0.3));
tl.fromTo("#f10-tarn", { y: 0 }, { y: -26, duration: 2.0, yoyo: true, repeat: 3, ease: "sine.inOut" }, S0(10, 1.0));
tl.fromTo("#f10-path", { opacity: 0 }, { opacity: 0.95, duration: 2.0, ease: "power1.inOut" }, T0(10, 3.0));
tl.fromTo("#f10 svg circle", { opacity: 0, scale: 0.3, transformOrigin: "50% 50%" }, { opacity: 1, scale: 1, duration: 0.5, stagger: 0.8, transformOrigin: "50% 50%" }, T0(10, 3.4));
tl.fromTo("#f10 .theory", { opacity: 0, y: -16 }, { opacity: 1, y: 0, duration: 0.7 }, S0(10, 0.5));
tl.fromTo("#f10 .tframe", { opacity: 0 }, { opacity: 0.75, duration: 1.0 }, S0(10, 0.5));
drift(10, -1, 260);

// ===== F11 penutup =====
bgMove(11, 1.0, 1.1, 0, -50);
$$("#f11 .shard").forEach((s, i) => { tl.set(s, { rotation: +s.dataset.rot, transformOrigin: "50% 50%" }, 0);
  tl.to(s, { y: "+=" + (14 + J(i) * 22), rotation: +s.dataset.rot + (J(i + 4) - 0.5) * 12, duration: 3.2, yoyo: true, repeat: 3, ease: "sine.inOut" }, ST[11]); });
tl.fromTo("#f11-title", { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 1.6, ease: "power2.out" }, T0(11, 0.1));
tl.fromTo("#f11-tarn", { opacity: 0 }, { opacity: 1, duration: 1.6 }, S0(11, 0.4));
tl.fromTo("#f11-tarn", { y: 0 }, { y: -12, duration: 3, yoyo: true, repeat: 3, ease: "sine.inOut" }, S0(11, 2));
tl.fromTo("#f11 .vig", { opacity: 0.8 }, { opacity: 1, duration: DUR[11] }, ST[11]);
drift(11, -1, 220);

window.__timelines["main"] = tl;
