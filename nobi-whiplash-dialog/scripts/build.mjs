// Generator index.html: timing dari durasi asli assets/vo/NN.wav (atau nominal bila belum ada),
// subtitle, dan lip-sync (mulut) dari envelope volume tiap file VO.
// Pakai:  node scripts/build.mjs
import { execFileSync } from "node:child_process";
import { existsSync, writeFileSync } from "node:fs";

const LINES = [
  { id: "01", who: "F", text: "Kamu terlambat satu menit.", nominal: 2.4 },
  { id: "02", who: "A", text: "Maaf, Pak. Macet.", nominal: 2.0 },
  { id: "03", who: "F", text: "Di panggung, tidak ada macet. Hanya ada yang siap, dan yang tersingkir.", nominal: 6.0 },
  { id: "04", who: "A", text: "Saya siap, Pak. Hitung dari awal.", nominal: 3.0 },
  { id: "05", who: "F", text: "Lagi. Sampai tanganmu berdarah.", nominal: 3.2 },
  { id: "06", who: "A", text: "Satu ronde lagi.", nominal: 1.8 },
];
const TITLE = 1.6, GAP = 0.45, END = 3.8, STEP = 1 / 20;

// ---------- durasi + envelope ----------
function probe(f) {
  return parseFloat(execFileSync("ffprobe", ["-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]).toString());
}
function mouthStates(f, dur) {
  // placeholder deterministik bila VO belum ada
  if (!f) {
    const out = []; const pat = [1, 2, 1, 0, 2, 1, 2, 0];
    for (let i = 0, t = 0.1; t < dur - 0.1; i++, t += 0.11) out.push([+t.toFixed(2), pat[i % pat.length]]);
    return out;
  }
  const raw = execFileSync("ffmpeg", ["-v", "error", "-i", f, "-ac", "1", "-ar", "16000", "-f", "s16le", "-"], { maxBuffer: 1 << 28 });
  const n = Math.floor(raw.length / 2), win = Math.round(16000 * STEP), rms = [];
  for (let i = 0; i + win <= n; i += win) {
    let s = 0;
    for (let j = 0; j < win; j++) { const v = raw.readInt16LE((i + j) * 2) / 32768; s += v * v; }
    rms.push(Math.sqrt(s / win));
  }
  const sorted = [...rms].sort((a, b) => a - b), ref = sorted[Math.floor(sorted.length * 0.95)] || 1;
  let st = rms.map((r) => { const x = r / ref; return x < 0.12 ? 0 : x < 0.42 ? 1 : 2; });
  st = st.map((v, i) => (i > 0 && i < st.length - 1 && st[i - 1] === st[i + 1] && v !== st[i - 1] ? st[i - 1] : v)); // buang kedip 1 jendela
  const out = []; let last = -1;
  st.forEach((v, i) => { if (v !== last) { out.push([+(i * STEP).toFixed(2), v]); last = v; } });
  return out;
}

// ---------- timing ----------
let cursor = TITLE + 0.3;
const L = LINES.map((l) => {
  const file = `assets/vo/${l.id}.wav`, has = existsSync(file);
  const dur = has ? probe(file) : l.nominal;
  const o = { ...l, file, has, dur, start: +cursor.toFixed(2) };
  o.mouth = mouthStates(has ? file : null, dur).map(([t, s]) => [+(o.start + t).toFixed(2), s]);
  o.end = +(o.start + dur).toFixed(2);
  cursor = o.end + GAP;
  return o;
});
const dEnd = +(L[L.length - 1].end + 0.6).toFixed(2);
const total = +(dEnd + END).toFixed(2);

// ---------- subtitle (pecah per kalimat, proporsional jumlah huruf) ----------
const subs = [];
for (const l of L) {
  const parts = l.text.match(/[^.?!]+[.?!]?/g).map((s) => s.trim()).filter(Boolean);
  const tot = parts.reduce((a, p) => a + p.length, 0);
  let t = l.start;
  for (const p of parts) {
    const d = (l.dur * p.length) / tot;
    subs.push({ who: l.who, text: p, start: +t.toFixed(2), dur: +(d + (p === parts[parts.length - 1] ? 0.15 : 0)).toFixed(2) });
    t += d;
  }
}

// ---------- karakter (gaya hitam-putih garis tebal) ----------
const INK = "#111";
const mouths = (p, kind) => {
  const closed = kind === "F" ? `<path d="M452 334 L508 334" fill="none" stroke="${INK}" stroke-width="8" stroke-linecap="round"/>`
                              : `<path d="M450 328 Q480 342 510 328" fill="none" stroke="${INK}" stroke-width="7" stroke-linecap="round"/>`;
  const half = `<ellipse cx="480" cy="334" rx="${kind === "F" ? 26 : 20}" ry="9" fill="${INK}"/>`;
  const open = `<path d="M452 322 Q480 316 508 322 Q506 354 480 356 Q454 354 452 322Z" fill="${INK}"/><ellipse cx="480" cy="347" rx="12" ry="6" fill="#c8102e"/>`;
  return `<g id="${p}-m0">${closed}</g><g id="${p}-m1" opacity="0">${half}</g><g id="${p}-m2" opacity="0">${open}</g>`;
};
const andrew = `<svg width="960" height="560" viewBox="0 0 960 560">
  <g stroke="${INK}" stroke-width="6" stroke-linejoin="round" stroke-linecap="round">
    <path d="M232 560 Q244 424 360 396 L600 396 Q716 424 728 560Z" fill="#fff"/>
    <path d="M416 396 Q480 446 544 396" fill="none"/>
    <path d="M452 340 L508 340 L508 402 Q480 424 452 402Z" fill="#fff"/>
    <g id="a-head">
      <ellipse cx="380" cy="256" rx="18" ry="28" fill="#fff"/><ellipse cx="580" cy="256" rx="18" ry="28" fill="#fff"/>
      <ellipse cx="480" cy="246" rx="100" ry="112" fill="#fff"/>
      <path d="M374 232 Q368 120 480 112 Q592 120 586 232 Q574 172 520 162 Q490 150 462 160 Q384 176 374 232Z" fill="${INK}"/>
      <path d="M410 222 L462 232 M550 222 L498 232" fill="none" stroke-width="9"/>
      <circle cx="440" cy="258" r="19" fill="#fff"/><circle cx="520" cy="258" r="19" fill="#fff"/>
      <circle cx="444" cy="260" r="8" fill="${INK}" stroke="none"/><circle cx="524" cy="260" r="8" fill="${INK}" stroke="none"/>
      <path d="M480 270 L470 304 Q480 311 492 304" fill="none" stroke-width="5"/>
      ${mouths("a", "A")}
      <path d="M392 170 q-10 18 0 24 q10 -5 0 -24z" fill="#9ad6ff" stroke-width="3"/>
    </g>
  </g></svg>`;
const fletcher = `<svg width="960" height="560" viewBox="0 0 960 560">
  <g stroke="${INK}" stroke-width="6" stroke-linejoin="round" stroke-linecap="round">
    <path d="M232 560 Q244 424 360 396 L600 396 Q716 424 728 560Z" fill="${INK}"/>
    <path d="M452 340 L508 340 L508 402 Q480 430 452 402Z" fill="#fff"/>
    <path d="M436 396 L480 448 L524 396Z" fill="#fff"/>
    <g id="f-head">
      <ellipse cx="380" cy="256" rx="18" ry="28" fill="#fff"/><ellipse cx="580" cy="256" rx="18" ry="28" fill="#fff"/>
      <ellipse cx="480" cy="246" rx="100" ry="112" fill="#fff"/>
      <path d="M430 160 Q480 148 530 160 M440 178 Q480 168 520 178" fill="none" stroke-width="4"/>
      <path d="M402 214 L468 238 M558 214 L492 238" fill="none" stroke-width="14"/>
      <circle cx="440" cy="262" r="15" fill="#fff"/><circle cx="520" cy="262" r="15" fill="#fff"/>
      <circle cx="442" cy="264" r="7" fill="${INK}" stroke="none"/><circle cx="522" cy="264" r="7" fill="${INK}" stroke="none"/>
      <path d="M480 274 L468 306 Q480 313 494 306" fill="none" stroke-width="5"/>
      ${mouths("f", "F")}
    </g>
  </g></svg>`;

// ---------- HTML ----------
const css = `
*{margin:0;padding:0;box-sizing:border-box}
html,body{margin:0;background:#0b0b0f}
#root{position:relative;width:100%;height:100%;overflow:hidden;background:#0b0b0f;font-family:Inter,sans-serif;color:#f4ebd9}
.scene{position:absolute;inset:0;overflow:hidden}
.bg-spot{position:absolute;inset:0;background:radial-gradient(ellipse 80% 45% at 50% 28%,rgba(242,169,59,.28),rgba(242,169,59,0) 70%),radial-gradient(ellipse 120% 80% at 50% 110%,rgba(200,16,46,.22),rgba(200,16,46,0) 65%)}
.abs{position:absolute}.center{left:0;right:0;text-align:center}
.display{font-family:"League Gothic",sans-serif;text-transform:uppercase;line-height:.92;letter-spacing:.01em}
.tag{font-weight:900;font-size:34px;letter-spacing:.18em;text-transform:uppercase;color:#f2a93b}
.card{position:absolute;left:60px;width:960px;height:560px;background:#f4ebd9;border-radius:28px;overflow:hidden}
.card .bar{position:absolute;left:0;right:0;bottom:0;height:16px}
.name{position:absolute;left:24px;top:22px;padding:6px 22px;background:#111;color:#f4ebd9;font-family:"League Gothic",sans-serif;font-size:60px;text-transform:uppercase;border-radius:6px}
.sub{position:absolute;left:60px;right:60px;top:1330px;height:190px;display:flex;align-items:center;justify-content:center}
.sub span{display:inline-block;padding:14px 30px;border-radius:18px;background:rgba(11,11,15,.82);color:#f4ebd9;text-align:center;font-weight:900;font-size:58px;line-height:1.18;letter-spacing:-.01em;max-width:960px}`;

const subHtml = subs.map((s, i) =>
  `<div class="sub clip" id="sub${String(i + 1).padStart(2, "0")}" data-start="${s.start}" data-duration="${s.dur}" data-track-index="5"><span id="u${String(i + 1).padStart(2, "0")}">${s.text}</span></div>`).join("\n      ");
const audioHtml = L.filter((l) => l.has).map((l) =>
  `<audio id="vo${l.id}" src="${l.file}" data-start="${l.start}" data-track-index="7" data-volume="1"></audio>`).join("\n      ");

const js = `
window.__timelines = window.__timelines || {};
const tl = gsap.timeline({ paused: true });
const L = ${JSON.stringify(L.map((l) => ({ who: l.who, start: l.start, end: l.end, mouth: l.mouth })))};
const DS = ${TITLE}, DE = ${dEnd};
// judul
tl.fromTo("#t-brand",{opacity:0,y:-30},{opacity:1,y:0,duration:.5,ease:"power3.out"},.1);
tl.fromTo("#t-title",{scale:1.5,opacity:0},{scale:1,opacity:1,duration:.5,ease:"power4.out"},.3);
// kartu masuk
tl.fromTo("#card-f",{x:-1200},{x:0,duration:.55,ease:"power4.out"},DS);
tl.fromTo("#card-a",{x:1200},{x:0,duration:.55,ease:"power4.out"},DS+.15);
tl.set("#card-f",{opacity:.62,scale:.96},0); tl.set("#card-a",{opacity:.62,scale:.96},0);
// subtitle
document.querySelectorAll(".sub").forEach((el,i)=>{ const id="#u"+String(i+1).padStart(2,"0"); tl.fromTo(id,{scale:.88,opacity:0,y:20},{scale:1,opacity:1,y:0,duration:.2,ease:"back.out(2)"},parseFloat(el.dataset.start)); });
// speaker, mulut, goyang kepala
const P = { F: "f", A: "a" };
L.forEach((l)=>{
  const p = P[l.who], o = p==="f"?"a":"f";
  tl.to("#card-"+p,{opacity:1,scale:1,duration:.18,ease:"power2.out"},l.start-.1);
  tl.to("#card-"+o,{opacity:.62,scale:.96,duration:.18,ease:"power2.out"},l.start-.1);
  l.mouth.forEach(([t,s])=>{ for(let k=0;k<3;k++) tl.set("#"+p+"-m"+k,{opacity:k===s?1:0},t); });
  tl.set("#"+p+"-m0",{opacity:1},l.end); tl.set("#"+p+"-m1",{opacity:0},l.end); tl.set("#"+p+"-m2",{opacity:0},l.end);
  for(let t=l.start;t<l.end-.2;t+=.32) tl.to("#"+p+"-head",{y:-6,duration:.16,yoyo:true,repeat:1,ease:"sine.inOut"},t);
});
// end card
tl.fromTo("#e-q",{y:-60,opacity:0},{y:0,opacity:1,duration:.5,ease:"power4.out"},DE+.1);
tl.fromTo("#e-stamp",{scale:3,opacity:0},{scale:1,opacity:1,duration:.18,ease:"power4.in"},DE+1.0);
tl.fromTo("#e-stamp",{x:0},{x:12,duration:.05,yoyo:true,repeat:5},DE+1.18);
tl.fromTo("#e-logo",{opacity:0},{opacity:1,duration:.6},DE+2.0);
window.__timelines["main"] = tl;`;

const html = `<!doctype html>
<html lang="id">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <title>Nobi Movie Studio — Satu Menit</title>
    <script src="assets/gsap.min.js"></script>
    <style>${css}</style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="${total}" data-width="1080" data-height="1920">
      <section id="s-title" class="scene clip" data-start="0" data-duration="${TITLE}" data-track-index="1">
        <div class="bg-spot"></div>
        <div id="t-brand" class="abs center tag" style="top:760px;">Nobi Movie Studio · Whiplash</div>
        <div id="t-title" class="abs center display" style="top:830px;font-size:300px;">Satu<br>menit</div>
      </section>
      <section id="s-dialog" class="scene clip" data-start="${TITLE}" data-duration="${+(dEnd - TITLE).toFixed(2)}" data-track-index="1">
        <div class="bg-spot"></div>
        <div id="card-f" class="card" style="top:110px;">${fletcher}<div class="name">Fletcher</div><div class="bar" style="background:#c8102e"></div></div>
        <div id="card-a" class="card" style="top:700px;">${andrew}<div class="name">Andrew</div><div class="bar" style="background:#f2a93b"></div></div>
      </section>
      <section id="s-end" class="scene clip" data-start="${dEnd}" data-duration="${END}" data-track-index="1">
        <div class="abs" style="inset:0;background:#f4ebd9;"></div>
        <div id="e-q" class="abs center display" style="top:260px;font-size:200px;color:#111;padding:0 60px;">Whiplash<br>(2014)</div>
        <div id="e-stamp" class="abs display center" style="top:820px;font-size:190px;color:#c8102e;border:14px solid #c8102e;margin:0 90px;padding:26px 0;left:0;right:0;transform:rotate(-6deg);"><div>Layak</div><div>ditonton ✔</div></div>
        <div id="e-logo" class="abs center tag" style="top:1400px;color:#111;">Nobi Movie Studio</div>
      </section>
      ${subHtml}
      ${audioHtml}
    </div>
    <script>${js}
    </script>
  </body>
</html>
`;
writeFileSync("index.html", html);
console.log(`ok · total ${total}s · ${L.filter((l) => l.has).length}/${L.length} VO ditemukan`);
