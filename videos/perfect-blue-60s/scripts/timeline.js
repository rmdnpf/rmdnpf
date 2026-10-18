window.__timelines = window.__timelines || {};
const tl = gsap.timeline({ paused: true });
const S = __ST__, L = __LS__, TOTAL = __TOTAL__;
const J = (i) => { const s = Math.sin(i * 127.1 + 311.7) * 43758.5453; return s - Math.floor(s); };
const $ = (s) => document.querySelector(s);
const typeIn = (sel, t0, per) => document.querySelectorAll(sel + " .ch").forEach((e, i) => tl.set(e, { opacity: 1 }, t0 + i * per));
const jitter = (sel, t0, n, step, amp, skew) => {
  for (let k = 0; k < n; k++) tl.set(sel, { x: (J(k + t0 * 7) - 0.5) * amp, skewX: (J(k + 31 + t0) - 0.5) * (skew || 0) }, t0 + k * step);
  tl.set(sel, { x: 0, skewX: 0 }, t0 + n * step);
};
const blink = (sel, t0, t1) => { for (let t = t0; t < t1; t += 0.5) tl.set(sel, { opacity: Math.round((t - t0) / 0.5) % 2 ? 0 : 1 }, t); };

// kilatan antar scene
["f2", "f3", "f4", "f5", "f6", "f7", "f8"].forEach((k) => tl.fromTo("#flash", { opacity: 0.75 }, { opacity: 0, duration: 0.28, ease: "power2.out", immediateRender: false }, S[k]));

// ===== F1 peringatan
tl.fromTo("#f1-win", { scale: 0.7, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.35, ease: "back.out(2)" }, 0.1);
jitter("#f1-title", 0.25, 9, 0.085, 22, 8);
tl.fromTo("#f1-cursor", { x: -240, y: -260 }, { x: 0, y: 0, duration: 0.8, ease: "power2.out" }, 0.55);
tl.fromTo("#f1-btn", { scale: 1 }, { scale: 0.9, duration: 0.08, yoyo: true, repeat: 1 }, 1.5);
tl.fromTo("#f1-cursor", { scale: 1 }, { scale: 0.82, duration: 0.08, yoyo: true, repeat: 1 }, 1.5);

// ===== F2 hook: zoom-out dari mata
tl.fromTo("#f2-world", { scale: 3.3, transformOrigin: "540px 600px" }, { scale: 1, duration: 3.0, ease: "power3.out", transformOrigin: "540px 600px" }, S.f2);
tl.fromTo("#f2-eye", { scale: 1 }, { scale: 1.035, duration: 1.4, yoyo: true, repeat: 3, ease: "sine.inOut", transformOrigin: "50% 50%" }, S.f2 + 2.6);
["#f2-c1", "#f2-c2", "#f2-c3"].forEach((id, i) => tl.fromTo(id, { scale: 0, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.3, ease: "back.out(3)" }, S.f2 + 1.3 + i * 0.5));
["#f2-h1", "#f2-h2", "#f2-h3"].forEach((id, i) => tl.fromTo(id, { y: 90, opacity: 0 }, { y: 0, opacity: 1, duration: 0.4, ease: "power3.out" }, L[1] + 3.35 + i * 0.28));
jitter("#f2-h3", L[1] + 4.3, 5, 0.07, 18, 6);

// ===== F3 judul
tl.fromTo("#f3-win", { scale: 0.8, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.35, ease: "back.out(2)" }, S.f3 + 0.1);
[[0, -14, 1], [1, 12, 1], [2, -9, 1], [3, 16, 1], [4, 6, 1], [5, -12, 1]].forEach(([i, r], k) => {
  tl.set("#f3-ic" + i, { rotation: r }, 0);
  tl.fromTo("#f3-ic" + i, { y: -700, opacity: 0 }, { y: 0, opacity: 1, duration: 0.8, ease: "bounce.out" }, S.f3 + 0.15 + k * 0.17);
});
typeIn("#f3-t1", L[2] + 0.15, 0.075); typeIn("#f3-t2", L[2] + 0.72, 0.1); blink("#f3-caret", L[2] + 0.2, L[2] + 6.8);
typeIn("#f3-yr", L[2] + 2.0, 0.12); typeIn("#f3-dir", L[2] + 4.4, 0.13);
document.querySelectorAll("#f3-win .seg").forEach((e, i) => { if (i < 15) { tl.set(e, { opacity: 0 }, 0); tl.set(e, { opacity: 1 }, L[2] + 0.3 + i * 0.4); } });
const pct = { v: 0 };
tl.to(pct, { v: 78, duration: 6.0, ease: "none", onUpdate: () => { $("#f3-pct").textContent = "MEMUAT… " + Math.round(pct.v) + "%"; } }, L[2] + 0.3);
tl.fromTo("#f3-cursor", { x: -160, y: 80 }, { x: 0, y: 0, duration: 2.6, ease: "power2.out" }, S.f3 + 0.5);

// ===== F4 Mima
tl.fromTo("#f4-stage", { opacity: 0, y: 60 }, { opacity: 1, y: 0, duration: 0.5, ease: "power2.out" }, S.f4 + 0.1);
tl.fromTo("#f4-beams", { x: -26 }, { x: 26, duration: 2.2, yoyo: true, repeat: 3, ease: "sine.inOut" }, S.f4);
tl.fromTo("#f4-title", { scale: 2.3, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.3, ease: "power4.in" }, L[3] + 0.1);
jitter("#f4-title", L[3] + 0.4, 5, 0.06, 20, 0);
tl.fromTo("#f4-sub", { opacity: 0, y: 20 }, { opacity: 1, y: 0, duration: 0.4 }, L[3] + 1.0);
tl.fromTo("#f4-mima", { y: 160, opacity: 0 }, { y: 0, opacity: 1, duration: 0.7, ease: "power3.out" }, S.f4 + 0.35);
tl.fromTo("#f4-idolL", { opacity: 0 }, { opacity: 0.62, duration: 0.5 }, L[3] + 1.2);
tl.fromTo("#f4-idolR", { opacity: 0 }, { opacity: 0.62, duration: 0.5 }, L[3] + 1.4);
for (let k = 0; k < 10; k++) tl.fromTo("#f4-s" + (k % 3), { opacity: 0, scale: 0.4 }, { opacity: 1, scale: 1, duration: 0.12, yoyo: true, repeat: 1, transformOrigin: "50% 50%" }, S.f4 + 0.9 + k * 0.6);
tl.fromTo("#f4-crowd", { x: -10 }, { x: 10, duration: 0.5, yoyo: true, repeat: 14, ease: "sine.inOut" }, S.f4);
tl.fromTo("#f4-win", { y: 70, opacity: 0, scale: 0.92 }, { y: 0, opacity: 1, scale: 1, duration: 0.35, ease: "back.out(2)" }, L[3] + 1.6);
tl.fromTo("#f4-cursor", { x: 280, y: -140 }, { x: 0, y: 0, duration: 0.9, ease: "power2.out" }, L[3] + 2.0);
tl.fromTo("#f4-ya", { scale: 1 }, { scale: 0.88, duration: 0.08, yoyo: true, repeat: 1 }, L[3] + 3.1);
tl.to(["#f4-idolL", "#f4-idolR"], { opacity: 0, duration: 0.6 }, L[3] + 3.25);
tl.fromTo("#f4-curL", { scaleX: 1, transformOrigin: "0% 50%" }, { scaleX: 4.6, duration: 0.8, ease: "power3.inOut", transformOrigin: "0% 50%" }, L[3] + 3.3);
tl.fromTo("#f4-curR", { scaleX: 1, transformOrigin: "100% 50%" }, { scaleX: 4.6, duration: 0.8, ease: "power3.inOut", transformOrigin: "100% 50%" }, L[3] + 3.3);
tl.to("#f4-win", { opacity: 0, y: 40, duration: 0.35 }, L[3] + 3.5);
tl.to("#f4-cursor", { opacity: 0, duration: 0.2 }, L[3] + 3.5);
tl.fromTo("#f4-dot", { scale: 0, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.3, ease: "back.out(3)" }, L[3] + 4.7);
tl.fromTo("#f4-ring", { scale: 1, opacity: 1 }, { scale: 3.2, opacity: 0, duration: 0.9, repeat: 3, ease: "power1.out" }, L[3] + 4.9);

// ===== F5 situs
tl.fromTo("#f5-win", { scale: 0.85, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.35, ease: "back.out(2)" }, S.f5 + 0.1);
[[0, 0.4], [1, 1.95], [2, 3.3]].forEach(([i, dt]) => typeIn("#f5-e" + i, L[4] + dt, 0.026));
const cnt = { v: 0 };
tl.to(cnt, { v: 742, duration: 4.0, ease: "power1.out", onUpdate: () => { const s = String(Math.round(cnt.v)).padStart(5, "0"); for (let k = 0; k < 5; k++) $("#f5-d" + k).textContent = s[k]; } }, L[4] + 0.3);
tl.fromTo("#f5-c0", { x: -80, opacity: 0 }, { x: 0, opacity: 1, duration: 0.3 }, L[4] + 4.0);
tl.fromTo("#f5-c1", { x: -80, opacity: 0 }, { x: 0, opacity: 1, duration: 0.3 }, L[4] + 4.35);
tl.fromTo("#f5-eye", { opacity: 0, scale: 0.6 }, { opacity: 1, scale: 1, duration: 0.4, ease: "back.out(2)", transformOrigin: "50% 50%" }, L[4] + 4.4);
tl.fromTo("#f5-eye", { scaleY: 1 }, { scaleY: 0.1, duration: 0.07, yoyo: true, repeat: 1, transformOrigin: "50% 50%" }, L[4] + 5.6);
tl.fromTo("#f5-t1", { x: 700 }, { x: 0, duration: 0.35, ease: "power4.out" }, L[4] + 5.3);
tl.fromTo("#f5-t2", { x: 700 }, { x: 0, duration: 0.35, ease: "power4.out" }, L[4] + 6.3);
for (let k = 0; k < 10; k++) {
  const t = L[4] + 6.8 + k * 0.07;
  tl.set("#f5-win", { x: (J(k + 3) - 0.5) * 40 }, t);
  tl.set("#f5-bar1", { opacity: 0.6, x: (J(k + 9) - 0.5) * 120, y: (J(k + 5) - 0.5) * 200 }, t);
  tl.set("#f5-bar2", { opacity: 0.6, x: (J(k + 17) - 0.5) * 160, y: (J(k + 11) - 0.5) * 240 }, t);
  tl.set("#f5-red", { opacity: k % 2 ? 0.55 : 0.1 }, t);
}
tl.set("#f5-win", { x: 0 }, L[4] + 7.5); tl.set(["#f5-bar1", "#f5-bar2"], { opacity: 0 }, L[4] + 7.5); tl.set("#f5-red", { opacity: 0.18 }, L[4] + 7.5);

// ===== F6 realitas kabur
const nests = ["#f6-n0", "#f6-n1", "#f6-n2", "#f6-n3", "#f6-n4"], rots = [-2, 1.5, -1, 2.5, -3];
nests.forEach((id, i) => { tl.set(id, { rotation: rots[i] }, 0); tl.fromTo(id, { scale: 2.3, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.7, ease: "power3.out" }, S.f6 + 0.2 + i * 0.18); });
tl.fromTo("#f6-world", { scale: 1 }, { scale: 1.1, duration: S.f7 - S.f6, ease: "none", transformOrigin: "540px 860px" }, S.f6);
tl.fromTo("#f6-tag1", { scale: 0, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.3, ease: "back.out(3)" }, S.f6 + 1.0);
tl.fromTo("#f6-tag2", { scale: 0, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.3, ease: "back.out(3)" }, S.f6 + 1.4);
tl.fromTo("#f6-pink", { x: -520, opacity: 0 }, { x: 0, opacity: 0.95, duration: 0.8, ease: "power3.out" }, S.f6 + 2.5);
tl.fromTo("#f6-blue", { x: 520, opacity: 0 }, { x: 0, opacity: 0.92, duration: 0.8, ease: "power3.out" }, S.f6 + 2.8);
tl.fromTo("#f6-pink", { y: 0 }, { y: -10, duration: 1.2, yoyo: true, repeat: 4, ease: "sine.inOut" }, S.f6 + 3.4);
tl.fromTo("#f6-blue", { y: 0 }, { y: 10, duration: 1.2, yoyo: true, repeat: 4, ease: "sine.inOut" }, S.f6 + 3.4);
jitter("#f6-blue", L[5] + 4.2, 6, 0.06, 36, 0);
tl.to("#f6-tag1", { x: 750, y: 1160, duration: 0.55, ease: "power4.inOut" }, L[5] + 5.55);
tl.to("#f6-tag2", { x: -800, y: -1160, duration: 0.55, ease: "power4.inOut" }, L[5] + 5.55);
document.querySelectorAll("#f6-cracks .crk").forEach((p) => { const len = p.getTotalLength(); tl.set(p, { strokeDasharray: len, strokeDashoffset: len }, 0); });
tl.to("#f6-cracks .crk", { strokeDashoffset: 0, duration: 0.35, stagger: 0.03, ease: "power2.out" }, L[5] + 6.95);
tl.set("#f6-shards .shard", { opacity: 0 }, 0);
tl.fromTo("#f6-shards .shard", { opacity: 0, scale: 0.3, y: 0, transformOrigin: "50% 50%" }, { opacity: 1, scale: 1, duration: 0.2, stagger: 0.04 }, L[5] + 7.1);
tl.to("#f6-shards .shard", { y: 380, rotation: 90, opacity: 0, duration: 1.2, ease: "power2.in", stagger: 0.05 }, L[5] + 7.45);
typeIn("#f6-msg", L[5] + 7.6, 0.03);

// ===== F7 pengungkapan
[["#f7-p1", 0.12], ["#f7-p2", 0.35], ["#f7-p3", 0.3]].forEach(([id, o], i) => tl.fromTo(id, { opacity: 0, scale: 0.5 }, { opacity: o, scale: 1, duration: 0.6 }, S.f7 + 0.1 + i * 0.12));
tl.fromTo("#f7-mirror", { scale: 0.8, opacity: 0, transformOrigin: "50% 50%" }, { scale: 1, opacity: 1, duration: 0.7, ease: "back.out(1.4)", transformOrigin: "50% 50%" }, S.f7 + 0.3);
tl.fromTo("#f7-mgr", { opacity: 0 }, { opacity: 1, duration: 0.6 }, L[6] + 2.85);
tl.fromTo("#f7-tag", { scale: 0, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.3, ease: "back.out(3)", transformOrigin: "0% 50%" }, L[6] + 4.5);
typeIn("#f7-q", L[6] + 5.3, 0.06);
tl.to("#f7-mgr", { opacity: 0, duration: 0.4 }, L[6] + 6.2);
tl.fromTo("#f7-idol", { opacity: 0 }, { opacity: 1, duration: 0.4 }, L[6] + 6.2);
jitter("#f7-mirror", L[6] + 6.2, 6, 0.05, 22, 0);
tl.fromTo("#f7-strike", { scaleX: 0 }, { scaleX: 1, duration: 0.25, ease: "power3.out" }, L[6] + 7.0);

// ===== F8 makna
tl.fromTo("#f8-win", { scale: 0.85, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.35, ease: "back.out(2)" }, S.f8 + 0.2);
tl.fromTo("#f8-gh1", { opacity: 0, y: 30 }, { opacity: 0.16, y: 0, duration: 1.6 }, S.f8 + 0.5);
tl.fromTo("#f8-gh2", { opacity: 0, y: 30 }, { opacity: 0.14, y: 0, duration: 1.6 }, S.f8 + 0.9);
typeIn("#f8-win div:nth-of-type(1)", L[7] + 3.45, 0.07);
typeIn("#f8-win div:nth-of-type(2)", L[7] + 8.85, 0.06);
blink("#f8-caret", L[7] + 0.5, TOTAL);
tl.fromTo("#f8-line", { scaleX: 0 }, { scaleX: 1, duration: 0.5, ease: "power3.out" }, L[7] + 10.1);
tl.fromTo("#f8-title", { scale: 1.35, opacity: 0, transformOrigin: "50% 50%" }, { scale: 1, opacity: 1, duration: 0.4, ease: "back.out(2)", transformOrigin: "50% 50%" }, L[7] + 10.2);
tl.fromTo("#f8-year", { y: 40, opacity: 0 }, { y: 0, opacity: 1, duration: 0.4, ease: "power3.out" }, L[7] + 10.55);

window.__timelines["main"] = tl;
