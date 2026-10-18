// Audit gerak deterministik: seek timeline per frame (30 fps), baca transform kamera & posisi kaki dalam koordinat dunia.
// Pakai: node scripts/motion_audit.mjs [--dump]
import { createRequire } from "module";
import path from "path";
import { fileURLToPath } from "url";
const require = createRequire("/opt/node-tools/node_modules/");
const { chromium } = require("playwright");
const here = path.dirname(fileURLToPath(import.meta.url));
const browser = await chromium.launch({ executablePath: "/opt/pw-browsers/chromium-1194/chrome-linux/chrome" }).catch(() => chromium.launch());
const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
page.on("pageerror", (e) => console.error("PAGEERR", e.message)); page.on("console", (m) => { if (m.type() === "error") console.error("CONSOLE", m.text()); });
await page.goto("file://" + path.join(here, "..", "index.html"));
await page.waitForTimeout(1500);
await page.waitForTimeout(500);
const FPS = 30, N = Math.round(9.5 * FPS);
const rows = await page.evaluate(({ FPS, N }) => {
  const tl = window.__timelines.evr, out = [];
  const g = (el, p) => +gsap.getProperty(el, p);
  for (let i = 0; i < N; i++) {
    tl.seek(i / FPS, false);
    const r = { f: i, t: i / FPS };
    for (const k of ["L", "R"]) {
      const w = document.getElementById(k + "-world");
      r[k + "w"] = [g(w, "scaleX"), g(w, "scaleY"), g(w, "x"), g(w, "y")];
      r[k + "bg"] = [g(document.getElementById(k + "-bg"), "scaleX"), g(document.getElementById(k + "-bg"), "x")];
      for (const n of ["tom", "sum-lean", "sum-twirl"]) {
        const el = document.getElementById(k + "-" + n);
        // posisi kaki dalam koordinat dunia: tengah-bawah elemen + translasi GSAP (pivot di kaki, rotasi tidak menggeser kaki)
        r[k + n] = { op: +getComputedStyle(el).opacity, fx: el.offsetLeft + el.offsetWidth / 2 + g(el, "x"), fy: el.offsetTop + el.offsetHeight + g(el, "y"), rot: g(el, "rotation") };
      }
    }
    out.push(r);
  }
  return out;
}, { FPS, N });
await browser.close();
const cuts = [6, 57, 117, 177, 225]; // frame potongan keras (0.2,1.9,3.9,5.9,7.5 s)
let fail = [], report = [];
// 1) kamera sama di dua panel (relatif terhadap pusat tampilan; panel R sebelum 9.0 s bergeser +540 px)
let maxCam = 0;
for (const r of rows) {
  const a = r.Lw, b = r.Rw;
  const dx = Math.abs((b[2] - (r.t >= 9.0 ? 0 : 540)) - a[2]);
  const d = Math.max(Math.abs(a[0] - b[0]), dx / 540, Math.abs(a[3] - b[3]) / 1920);
  if (r.t < 8.99) maxCam = Math.max(maxCam, dx, Math.abs(a[3] - b[3]), Math.abs(a[0] - b[0]) * 100);
}
report.push(`kamera L vs R: selisih maks ${maxCam.toFixed(3)} px / ${(maxCam).toFixed(3)} (batas 1) -> ${maxCam <= 1 ? "LULUS" : "GAGAL"}`);
// 2) gerak kamera per shot: skala awal/akhir
const shots = [["A", 6, 56], ["B", 57, 116], ["C", 117, 176], ["D", 177, 224], ["E", 225, 280]];
for (const [n, a, b] of shots) {
  const s0 = rows[a].Lw[0], s1 = rows[b].Lw[0];
  report.push(`shot ${n}: skala ${s0.toFixed(2)} -> ${s1.toFixed(2)}, pusat dunia x ${((270 - rows[a].Lw[2]) / s0).toFixed(0)} -> ${((270 - rows[b].Lw[2]) / s1).toFixed(0)}`);
}
// 3) jendela statis > 0.5 s (kamera DAN figur diam)
let still = 0, maxStill = 0;
for (let i = 1; i < rows.length; i++) {
  const p = rows[i - 1], c = rows[i];
  const mv = Math.abs(c.Lw[0] - p.Lw[0]) * 1000 + Math.abs(c.Lw[2] - p.Lw[2]) + Math.abs(c.Lw[3] - p.Lw[3]) +
    Math.abs(c.Ltom.fx - p.Ltom.fx) + Math.abs(c.Ltom.rot - p.Ltom.rot) * 5;
  still = mv < 0.02 ? still + 1 : 0; maxStill = Math.max(maxStill, still);
}
report.push(`jendela statis terpanjang: ${(maxStill / FPS).toFixed(2)} s (batas 0.5) -> ${maxStill / FPS <= 0.5 ? "LULUS" : "GAGAL"}`);
// 4) kaki Summer/Tom berdiri: drift kaki dalam ruang dunia per 0.5 s di luar potongan/busur
function world(r, k, n) { return rows.length && r[k + n].fx; }
const drift = [];
for (const k of ["L", "R"]) for (const n of ["tom", "sum-lean", "sum-twirl"]) {
  let worst = 0, at = 0;
  for (let i = 15; i < rows.length - 15; i++) {
    const a = rows[i], b = rows[i + 15];
    if (a[k + n].op < 0.9 || b[k + n].op < 0.9) continue;
    if (cuts.some((c) => c > i - 1 && c <= i + 15)) continue;           // melewati potongan keras
    if (a.t >= 5.9 && a.t < 7.6) continue;                              // sisipan tangan
    const d = Math.abs(world(b, k, n) - world(a, k, n));
    if (d > worst) { worst = d; at = a.t; }
  }
  drift.push([k + " " + n, worst, at]);
}
for (const [id, d, t] of drift) report.push(`drift kaki ${id}: ${d.toFixed(1)} px dunia/0.5 s (maks, mulai t=${t.toFixed(2)}) ${d <= 4 ? "ok" : "BERGERAK (dikomentari di README: langkah/busur disengaja)"}`);
console.log(report.join("\n"));
if (process.argv.includes("--dump")) console.log(JSON.stringify(rows.filter((_, i) => i % 15 === 0).map((r) => ({ t: r.t, cam: r.Lw, tom: r.Ltom, lean: r.Llean, R: r.Rw }))));
