window.__timelines = window.__timelines || {};
const tl = gsap.timeline({ paused: true });
const T = __T__, S = T.ST, L = T.LS, D = T.D, DUR = T.DUR, TOTAL = T.TOTAL, CAPS = T.CAPS;
const J = (i) => { const s = Math.sin(i * 127.1 + 311.7) * 43758.5453; return s - Math.floor(s); };
const $ = (s) => document.querySelector(s);
const shake = (sel, t0, n, step, amp) => {
  for (let k = 0; k < n; k++) tl.set(sel, { x: (J(k + t0 * 7) - 0.5) * amp, y: (J(k + 31 + t0) - 0.5) * amp }, t0 + k * step);
  tl.set(sel, { x: 0, y: 0 }, t0 + n * step);
};
const draw = (sel, t0, dur, stag) => {
  document.querySelectorAll(sel).forEach((p) => { const len = p.getTotalLength(); tl.set(p, { strokeDasharray: len, strokeDashoffset: len }, 0); });
  tl.to(sel, { strokeDashoffset: 0, duration: dur, stagger: stag, ease: "power2.out" }, t0);
};
const altTo = (pid, p0, p1, t0, dur, ease) => tl.fromTo(`#${pid} .alt-mark`, { y: 0 }, { y: (p0 - p1) * 1120, duration: dur, ease: ease || "power2.inOut" }, t0);
const fmt = (v) => String(Math.round(v)).replace(/\B(?=(\d{3})+(?!\d))/g, ".");
const flash = (t, col, op) => tl.fromTo("#flash", { opacity: op || 0.7, backgroundColor: col || "#ffffff" }, { opacity: 0, duration: 0.35, ease: "power2.out", immediateRender: false }, t);
const drift = (scene) => tl.fromTo(`#${scene} .pt`, { y: 0 }, { y: -140, duration: DUR[scene.slice(1)], ease: "none" }, S[scene.slice(1)]);

// kilatan antar scene
for (let n = 2; n <= 10; n++) flash(S[n], n === 5 || n === 8 ? "#B3202A" : "#ffffff", n === 5 || n === 8 ? 0.45 : 0.55);

// subtitle
CAPS.forEach((c, i) => { tl.set(`#cap${i}`, { opacity: 1 }, c[1]); tl.set(`#cap${i}`, { opacity: 0 }, c[2]); });

// ===== F1 hook: foto keluarga
tl.fromTo("#f1-bg", { scale: 1 }, { scale: 1.07, duration: DUR[1], ease: "none", transformOrigin: "50% 45%" }, S[1]);
tl.fromTo("#f1-fwrap", { opacity: 0, scale: 0.94 }, { opacity: 1, scale: 1, duration: 0.9, ease: "power2.out", transformOrigin: "50% 50%" }, 0.2);
tl.fromTo("#f1-warn", { y: -90, opacity: 0 }, { y: 0, opacity: 1, duration: 0.45, ease: "back.out(2)" }, 0.5);
tl.to("#f1-warn", { opacity: 0.45, duration: 0.6, yoyo: true, repeat: 5, ease: "sine.inOut" }, 1.4);
altTo("f1-alt", 0.03, 0.05, 0.3, 9);
drift("f1");
draw("#f1-crack .crk", L[1] + 8.4, 0.5, 0.15);
shake("#f1-fwrap", L[1] + 8.4, 6, 0.05, 8);

// ===== F2 judul
tl.fromTo("#f2-bg", { x: 0 }, { x: 600, duration: DUR[2], ease: "none" }, S[2]);
tl.fromTo("#f2-title", { scale: 1.35, opacity: 0, transformOrigin: "50% 50%" }, { scale: 1, opacity: 1, duration: 0.55, ease: "power4.out", transformOrigin: "50% 50%" }, L[2] + 0.1);
shake("#f2-title", L[2] + 0.65, 5, 0.05, 14);
tl.fromTo("#f2-line", { scaleX: 0, transformOrigin: "0% 50%" }, { scaleX: 1, duration: 0.5, ease: "power3.out", transformOrigin: "0% 50%" }, L[2] + 0.9);
tl.fromTo("#f2-sub", { y: 30, opacity: 0 }, { y: 0, opacity: 1, duration: 0.5, ease: "power3.out" }, L[2] + 1.3);
drift("f2");

// ===== F3 Mark
tl.fromTo("#f3-bg", { x: 60 }, { x: -40, duration: DUR[3], ease: "none" }, S[3]);
tl.fromTo("#f3-mark", { y: 140, opacity: 0 }, { y: 0, opacity: 1, duration: 0.7, ease: "power3.out" }, S[3] + 0.15);
tl.fromTo("#f3-mark", { scale: 1, transformOrigin: "50% 100%" }, { scale: 1.04, duration: DUR[3] - 0.9, ease: "none", transformOrigin: "50% 100%" }, S[3] + 0.9);
tl.fromTo("#f3 .chip", { x: -80, opacity: 0 }, { x: 0, opacity: 1, duration: 0.4, ease: "power3.out" }, L[3] + 0.3);
tl.fromTo("#f3 .mono", { opacity: 0 }, { opacity: 1, duration: 0.5 }, L[3] + 0.9);
altTo("f3-alt", 0.14, 0.18, 0.3, 6);

// ===== F4 terbang
tl.fromTo("#f4-bg", { scale: 1, transformOrigin: "50% 100%" }, { scale: 1.16, duration: DUR[4], ease: "none", transformOrigin: "50% 100%" }, S[4]);
tl.fromTo("#f4-speed", { y: -260 }, { y: 300, duration: 0.9, ease: "none", repeat: Math.ceil(DUR[4] / 0.9) }, S[4]);
tl.fromTo("#f4-omni", { y: 520, x: 120, opacity: 0 }, { y: 0, x: 0, opacity: 1, duration: 1.1, ease: "power3.out" }, S[4] + 0.2);
tl.fromTo("#f4-mark", { y: 600, x: -80, opacity: 0 }, { y: 0, x: 0, opacity: 1, duration: 1.1, ease: "power3.out" }, S[4] + 0.5);
tl.fromTo("#f4-omni", { rotation: -2 }, { rotation: 2, duration: 1.6, yoyo: true, repeat: 5, ease: "sine.inOut", transformOrigin: "50% 60%" }, S[4] + 1.4);
tl.fromTo("#f4-mark", { rotation: 3 }, { rotation: -3, duration: 1.3, yoyo: true, repeat: 6, ease: "sine.inOut", transformOrigin: "50% 60%" }, S[4] + 1.6);
const altv = { v: 0 };
tl.to(altv, { v: 2000, duration: 7, ease: "power1.out", onUpdate: () => { const t = $("#f4-alt .alt-mark text"); if (t) t.textContent = fmt(altv.v) + " M"; } }, S[4] + 0.6);
altTo("f4-alt", 0.4, 0.62, 0.6 + S[4], 7, "power1.out");

// ===== F5 Guardians tewas
tl.set("#f5-guard", { rotation: -7 }, 0);
tl.fromTo("#f5-bg", { scale: 1 }, { scale: 1.1, duration: DUR[5], ease: "none", transformOrigin: "50% 60%" }, S[5]);
tl.fromTo("#f5-guard", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.8, ease: "power2.out" }, S[5] + 0.2);
tl.fromTo("#f5-omni", { opacity: 0, y: 70 }, { opacity: 1, y: 0, duration: 0.9, ease: "power3.out" }, S[5] + 0.5);
tl.fromTo("#f5-red", { opacity: 0.2 }, { opacity: 1, duration: 0.7, yoyo: true, repeat: 7, ease: "sine.inOut" }, S[5] + 1);
tl.to("#f5-guard", { rotation: -14, y: 260, opacity: 0.25, duration: 1.4, ease: "power2.in" }, L[5] + 5.6);
flash(L[5] + 5.6, "#B3202A", 0.5);
shake("#f5-bg", L[5] + 5.6, 10, 0.05, 16);
tl.fromTo("#f5-omni", { scale: 1, transformOrigin: "50% 60%" }, { scale: 1.07, duration: 2.6, ease: "power1.inOut", transformOrigin: "50% 60%" }, L[5] + 6.6);
altTo("f5-alt", 0.5, 0.52, S[5], DUR[5]);
drift("f5");

// ===== F6 foto pecah
tl.fromTo("#f6-bg", { scale: 1 }, { scale: 1.06, duration: DUR[6], ease: "none", transformOrigin: "50% 40%" }, S[6]);
tl.set("#f6-right", { x: -34, y: 18 }, 0);
tl.fromTo("#f6-fwrapL, #f6-fwrapR", { opacity: 0, scale: 0.94 }, { opacity: 1, scale: 1, duration: 0.8, ease: "power2.out", transformOrigin: "50% 50%" }, S[6] + 0.2);
tl.fromTo("#f6-right", { filter: "brightness(1) saturate(1)" }, { filter: "brightness(1) saturate(1)", duration: 0.01 }, S[6]);
tl.to("#f6-right", { filter: "brightness(.4) saturate(.7)", duration: 1.0, ease: "power2.inOut" }, L[6] + 7.3);
draw("#f6-cracks .crk", L[6] + 5.0, 0.7, 0.07);
tl.set("#f6-cracks .shard", { opacity: 0 }, 0);
tl.to("#f6-right", { x: 0, y: 0, duration: 0.6, ease: "power3.out" }, L[6] + 8.1);
tl.to("#f6-fwrapL", { rotation: -3, x: -20, duration: 0.8, ease: "power2.out" }, L[6] + 8.1);
tl.to("#f6-fwrapR", { rotation: 4, x: 30, duration: 0.8, ease: "power2.out" }, L[6] + 8.1);
tl.fromTo("#f6-cracks .shard", { opacity: 0, y: 0 }, { opacity: 1, duration: 0.15, stagger: 0.05 }, L[6] + 8.1);
tl.to("#f6-cracks .shard", { y: 340, rotation: 120, opacity: 0, duration: 1.2, ease: "power2.in", stagger: 0.05 }, L[6] + 8.5);
flash(L[6] + 8.1, "#ffffff", 0.4);
altTo("f6-alt", 0.7, 0.74, S[6], DUR[6]);

// ===== F7 Viltrum
tl.fromTo("#f7-bg", { scale: 1.05, transformOrigin: "50% 100%" }, { scale: 1.2, duration: DUR[7], ease: "none", transformOrigin: "50% 100%" }, S[7]);
tl.fromTo("#f7-sym", { scale: 0.2, rotation: -120, opacity: 0, transformOrigin: "0px 0px" }, { scale: 1, rotation: 0, opacity: 1, duration: 1.0, ease: "back.out(1.6)", transformOrigin: "0px 0px" }, L[7] + 1.0);
tl.fromTo("#f7-name", { y: 30, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: "power3.out" }, L[7] + 1.6);
tl.fromTo("#f7 .ship", { y: -320, opacity: 0 }, { y: 0, opacity: 1, duration: 0.9, ease: "power3.out", stagger: 0.15 }, L[7] + 3.4);
tl.fromTo("#f7 .ship", { y: 0 }, { y: 50, duration: 1.2, yoyo: true, repeat: 2, ease: "sine.inOut", stagger: 0.1 }, L[7] + 4.8);
altTo("f7-alt", 0.9, 0.95, S[7], DUR[7]);

// ===== F8 pertarungan
tl.set("#f8-mark", { rotation: 150 }, 0);
tl.fromTo("#f8-bg", { scale: 1 }, { scale: 1.12, duration: DUR[8], ease: "none", transformOrigin: "50% 50%" }, S[8]);
tl.fromTo("#f8-omni", { x: 200, opacity: 0 }, { x: 0, opacity: 1, duration: 0.7, ease: "power3.out" }, S[8] + 0.2);
tl.fromTo("#f8-mark", { y: 260, opacity: 0 }, { y: 0, opacity: 1, duration: 0.7, ease: "power3.out" }, S[8] + 0.3);
[1.6, 3.2, 4.8].forEach((dt, k) => {
  tl.fromTo("#f8-wave", { scale: 0.4, opacity: 1, transformOrigin: "420px 860px" }, { scale: 1.6, opacity: 0, duration: 0.9, ease: "power2.out", transformOrigin: "420px 860px" }, L[8] + dt);
  shake("#f8-mark", L[8] + dt, 6, 0.04, 22 + k * 6);
  flash(L[8] + dt, "#F2C230", 0.25);
});
tl.to("#f8-mark", { y: 150, duration: 1.8, ease: "power1.in" }, L[8] + 4.9);
tl.fromTo("#f8-tear", { opacity: 0, y: 0 }, { opacity: 1, y: 0, duration: 0.3 }, L[8] + 6.4);
tl.to("#f8-tear", { y: 280, duration: 1.4, ease: "power2.in" }, L[8] + 6.7);
tl.to("#f8-tear", { opacity: 0, duration: 0.3 }, L[8] + 7.8);
tl.to("#f8-omni", { y: -1300, x: 120, duration: 1.8, ease: "power3.in" }, L[8] + 7.3);
altTo("f8-alt", 0.6, 0.85, S[8], DUR[8]);

// ===== F9 tafsiran
tl.fromTo("#f9-bg", { scale: 1 }, { scale: 1.05, duration: DUR[9], ease: "none", transformOrigin: "50% 45%" }, S[9]);
tl.fromTo("#f9 .theory", { y: -70, opacity: 0 }, { y: 0, opacity: 1, duration: 0.5, ease: "back.out(2)" }, S[9] + 0.2);
tl.fromTo("#f9-fwrap", { opacity: 0, scale: 0.94 }, { opacity: 1, scale: 1, duration: 0.8, ease: "power2.out", transformOrigin: "50% 50%" }, S[9] + 0.3);
tl.fromTo("#f9-omni", { x: 0 }, { x: 26, duration: DUR[9] - 1, ease: "sine.inOut" }, S[9] + 1);
tl.fromTo("#f9-mark", { x: 0 }, { x: -26, duration: DUR[9] - 1, ease: "sine.inOut" }, S[9] + 1);
draw("#f9-crack .crk", L[9] + 4.2, 0.8, 0.1);
tl.fromTo("#f9 .tframe", { opacity: 0 }, { opacity: 0.55, duration: 0.6 }, S[9] + 0.5);

// ===== F10 penutup
tl.fromTo("#f10-bg", { x: 40 }, { x: -50, duration: DUR[10], ease: "none" }, S[10]);
tl.fromTo("#f10-mark", { y: 100, opacity: 0 }, { y: 0, opacity: 1, duration: 0.8, ease: "power3.out" }, S[10] + 0.2);
tl.fromTo("#f10-mark", { scale: 1, transformOrigin: "50% 100%" }, { scale: 1.05, duration: DUR[10] - 1, ease: "none", transformOrigin: "50% 100%" }, S[10] + 1);
tl.fromTo("#f10-title", { scale: 1.4, opacity: 0, transformOrigin: "50% 50%" }, { scale: 1, opacity: 1, duration: 0.5, ease: "power4.out", transformOrigin: "50% 50%" }, L[10] + 3.6);
shake("#f10-title", L[10] + 4.1, 5, 0.05, 12);
tl.to("#f10 .theory", { opacity: 1, duration: 0.6 }, L[10] + 6.0);
tl.fromTo("#fade", { opacity: 0 }, { opacity: 1, duration: 1.2, ease: "power1.in" }, TOTAL - 1.2);

window.__timelines["main"] = tl;
