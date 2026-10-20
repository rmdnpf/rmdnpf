// Audit teknis adegan 5 (hanya hal terukur): tepat satu pose terlihat tiap frame, penari tidak bergeser horizontal (tidak ada foot slide),
// dan ringkasan gerak. Tidak menilai kualitas sinematik.
import { createRequire } from "module";
import path from "path";
import { fileURLToPath } from "url";
const require = createRequire("/opt/node-tools/node_modules/");
const { chromium } = require("playwright");
const here = path.dirname(fileURLToPath(import.meta.url));
const browser = await chromium.launch({ executablePath: "/opt/pw-browsers/chromium-1194/chrome-linux/chrome" });
const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
page.on("pageerror", (e) => console.error("PAGEERR", e.message));
await page.goto("file://" + path.join(here, "..", "index.html"));
await page.waitForTimeout(1500);
const rows = await page.evaluate(() => {
  const tl = window.__timelines.dance, out = [], P = ["strut", "jump", "land", "point"];
  const g = (el, p) => +gsap.getProperty(el, p);
  for (let i = 0; i < 198; i++) {
    tl.seek(i / 30, false);
    const d = document.getElementById("dancer"), w = document.getElementById("world");
    out.push({ t: i / 30, vis: P.filter((p) => +getComputedStyle(document.getElementById("d-" + p)).opacity > 0.5), x: g(d, "x"), y: g(d, "y"), cs: g(w, "scale"), cy: g(w, "y") });
  }
  return out;
});
await browser.close();
let bad = rows.filter((r) => r.t >= 0.05 && r.t < 6.3 && r.vis.length !== 1);
const maxx = Math.max(...rows.map((r) => Math.abs(r.x)));
const sw = rows.filter((r, i) => i && r.vis[0] !== rows[i - 1].vis[0]).map((r) => r.t.toFixed(2) + "→" + r.vis[0]);
console.log(`frame dengan pose ≠1: ${bad.length} -> ${bad.length === 0 ? "LULUS" : "GAGAL"}`);
console.log(`pergeseran horizontal penari maks: ${maxx.toFixed(2)} px -> ${maxx === 0 ? "LULUS (tidak ada foot slide)" : "periksa"}`);
console.log(`pergantian pose (${sw.length}): ${sw.join(", ")}`);
console.log(`skala kamera ${Math.min(...rows.map((r) => r.cs)).toFixed(2)}–${Math.max(...rows.map((r) => r.cs)).toFixed(2)}; lompatan puncak y=${Math.min(...rows.map((r) => r.y)).toFixed(0)} px`);
