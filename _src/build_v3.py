#!/usr/bin/env python3
# v3 (Strogatz homage) — multi-page, bilingual (JP/EN) site generator.
# 中身は梅田栄作の実コンテンツ verbatim。EN は本人 JP 文の翻訳 (draft)。
# JP は root (/) に、EN は /en/ サブフォルダに出力。design は stevenstrogatz.com への homage。
import os

OUT = "/tmp/eumeda-hub/_version3"
os.makedirs(OUT, exist_ok=True)
os.makedirs(os.path.join(OUT, "en"), exist_ok=True)
BASE = "https://www.eisaku-umeda.com"
LANGS = ("ja", "en")
# bump on style.css changes → cache-busts the stylesheet link so browsers
# (and Cloudflare edge) fetch the new CSS instead of a stale 4h-cached copy.
CSS_VER = "20260614b"

NAV = [
    ("home",     "home",     "index.html"),
    ("research", "research", "research.html"),
    ("works",    "works",    "works.html"),
    ("creative", "creative", "creative.html"),
    ("homage",   "homage",   "homage.html"),
    ("contact",  "contact",  "contact.html"),
]

def clean_link(href):
    return "/" if href == "index.html" else "/" + href[:-5]

def page_url(href, lang):
    """Root-absolute clean URL for a page in a given locale.
    ja: /, /research ...  |  en: /en/, /en/research ..."""
    base = clean_link(href)
    if lang == "ja":
        return base
    return "/en/" if href == "index.html" else "/en" + base

FAVICON = ("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'>"
           "<rect width='64' height='64' rx='12' fill='%232D5016'/>"
           "<text x='32' y='45' font-family='Georgia,serif' font-size='40' fill='%23ffffff' text-anchor='middle'>E</text></svg>")

def photo_fig(lang):
    alt = ("梅田栄作 (Eisaku Umeda) — 東京都立大学 理学研究科" if lang == "ja"
           else "Eisaku Umeda — Graduate School of Science, Tokyo Metropolitan University")
    return f"""<figure class="portrait">
  <img src="/eisaku.png" alt="{alt}" width="440" height="440">
  <figcaption class="cap">Photo Credit: Ann Umeda</figcaption>
</figure>"""

# Works / Highlights のピクセルサムネ (HL でのみ使用)
THUMBS = {}
THUMBS.update({
 'px_research': '<svg viewBox="0 0 120 78" shape-rendering="crispEdges" role="img" aria-label="research"><rect x="73" y="24" width="5" height="5" fill="#9a7b3f"/><rect x="78" y="24" width="5" height="5" fill="#9a7b3f"/><rect x="53" y="29" width="5" height="5" fill="#2D5016"/><rect x="58" y="29" width="5" height="5" fill="#2D5016"/><rect x="73" y="29" width="5" height="5" fill="#9a7b3f"/><rect x="78" y="29" width="5" height="5" fill="#9a7b3f"/><rect x="53" y="34" width="5" height="5" fill="#2D5016"/><rect x="58" y="34" width="5" height="5" fill="#2D5016"/><rect x="73" y="34" width="5" height="5" fill="#9a7b3f"/><rect x="78" y="34" width="5" height="5" fill="#9a7b3f"/><rect x="33" y="39" width="5" height="5" fill="#2D5016"/><rect x="38" y="39" width="5" height="5" fill="#2D5016"/><rect x="53" y="39" width="5" height="5" fill="#2D5016"/><rect x="58" y="39" width="5" height="5" fill="#2D5016"/><rect x="73" y="39" width="5" height="5" fill="#9a7b3f"/><rect x="78" y="39" width="5" height="5" fill="#9a7b3f"/><rect x="33" y="44" width="5" height="5" fill="#2D5016"/><rect x="38" y="44" width="5" height="5" fill="#2D5016"/><rect x="53" y="44" width="5" height="5" fill="#2D5016"/><rect x="58" y="44" width="5" height="5" fill="#2D5016"/><rect x="73" y="44" width="5" height="5" fill="#9a7b3f"/><rect x="78" y="44" width="5" height="5" fill="#9a7b3f"/><rect x="33" y="49" width="5" height="5" fill="#2D5016"/><rect x="38" y="49" width="5" height="5" fill="#2D5016"/><rect x="53" y="49" width="5" height="5" fill="#2D5016"/><rect x="58" y="49" width="5" height="5" fill="#2D5016"/><rect x="73" y="49" width="5" height="5" fill="#9a7b3f"/><rect x="78" y="49" width="5" height="5" fill="#9a7b3f"/><rect x="33" y="54" width="5" height="5" fill="#2D5016"/><rect x="38" y="54" width="5" height="5" fill="#2D5016"/><rect x="43" y="54" width="5" height="5" fill="#2D5016"/><rect x="48" y="54" width="5" height="5" fill="#2D5016"/><rect x="53" y="54" width="5" height="5" fill="#2D5016"/><rect x="58" y="54" width="5" height="5" fill="#2D5016"/><rect x="63" y="54" width="5" height="5" fill="#2D5016"/><rect x="68" y="54" width="5" height="5" fill="#2D5016"/><rect x="73" y="54" width="5" height="5" fill="#2D5016"/><rect x="78" y="54" width="5" height="5" fill="#2D5016"/><rect x="83" y="54" width="5" height="5" fill="#2D5016"/></svg>',
 'px_works': '<svg viewBox="0 0 120 78" shape-rendering="crispEdges" role="img" aria-label="works"><rect x="33" y="19" width="5" height="5" fill="#2D5016"/><rect x="38" y="19" width="5" height="5" fill="#2D5016"/><rect x="43" y="19" width="5" height="5" fill="#2D5016"/><rect x="48" y="19" width="5" height="5" fill="#2D5016"/><rect x="53" y="19" width="5" height="5" fill="#2D5016"/><rect x="58" y="19" width="5" height="5" fill="#2D5016"/><rect x="63" y="19" width="5" height="5" fill="#2D5016"/><rect x="68" y="19" width="5" height="5" fill="#2D5016"/><rect x="73" y="19" width="5" height="5" fill="#2D5016"/><rect x="78" y="19" width="5" height="5" fill="#2D5016"/><rect x="83" y="19" width="5" height="5" fill="#2D5016"/><rect x="33" y="24" width="5" height="5" fill="#2D5016"/><rect x="83" y="24" width="5" height="5" fill="#2D5016"/><rect x="33" y="29" width="5" height="5" fill="#2D5016"/><rect x="43" y="29" width="5" height="5" fill="#9a7b3f"/><rect x="48" y="29" width="5" height="5" fill="#9a7b3f"/><rect x="53" y="29" width="5" height="5" fill="#9a7b3f"/><rect x="58" y="29" width="5" height="5" fill="#9a7b3f"/><rect x="63" y="29" width="5" height="5" fill="#9a7b3f"/><rect x="83" y="29" width="5" height="5" fill="#2D5016"/><rect x="33" y="34" width="5" height="5" fill="#2D5016"/><rect x="83" y="34" width="5" height="5" fill="#2D5016"/><rect x="33" y="39" width="5" height="5" fill="#2D5016"/><rect x="43" y="39" width="5" height="5" fill="#4f7a2e"/><rect x="48" y="39" width="5" height="5" fill="#4f7a2e"/><rect x="53" y="39" width="5" height="5" fill="#4f7a2e"/><rect x="58" y="39" width="5" height="5" fill="#4f7a2e"/><rect x="63" y="39" width="5" height="5" fill="#4f7a2e"/><rect x="68" y="39" width="5" height="5" fill="#4f7a2e"/><rect x="73" y="39" width="5" height="5" fill="#4f7a2e"/><rect x="83" y="39" width="5" height="5" fill="#2D5016"/><rect x="33" y="44" width="5" height="5" fill="#2D5016"/><rect x="43" y="44" width="5" height="5" fill="#4f7a2e"/><rect x="48" y="44" width="5" height="5" fill="#4f7a2e"/><rect x="53" y="44" width="5" height="5" fill="#4f7a2e"/><rect x="63" y="44" width="5" height="5" fill="#4f7a2e"/><rect x="68" y="44" width="5" height="5" fill="#4f7a2e"/><rect x="73" y="44" width="5" height="5" fill="#4f7a2e"/><rect x="83" y="44" width="5" height="5" fill="#2D5016"/><rect x="33" y="49" width="5" height="5" fill="#2D5016"/><rect x="38" y="49" width="5" height="5" fill="#2D5016"/><rect x="43" y="49" width="5" height="5" fill="#2D5016"/><rect x="48" y="49" width="5" height="5" fill="#2D5016"/><rect x="53" y="49" width="5" height="5" fill="#2D5016"/><rect x="58" y="49" width="5" height="5" fill="#2D5016"/><rect x="63" y="49" width="5" height="5" fill="#2D5016"/><rect x="68" y="49" width="5" height="5" fill="#2D5016"/><rect x="73" y="49" width="5" height="5" fill="#2D5016"/><rect x="78" y="49" width="5" height="5" fill="#2D5016"/><rect x="83" y="49" width="5" height="5" fill="#2D5016"/><rect x="53" y="54" width="5" height="5" fill="#2D5016"/><rect x="58" y="54" width="5" height="5" fill="#2D5016"/><rect x="63" y="54" width="5" height="5" fill="#2D5016"/><rect x="43" y="59" width="5" height="5" fill="#2D5016"/><rect x="48" y="59" width="5" height="5" fill="#2D5016"/><rect x="53" y="59" width="5" height="5" fill="#2D5016"/><rect x="58" y="59" width="5" height="5" fill="#2D5016"/><rect x="63" y="59" width="5" height="5" fill="#2D5016"/><rect x="68" y="59" width="5" height="5" fill="#2D5016"/><rect x="73" y="59" width="5" height="5" fill="#2D5016"/></svg>',
 'px_creative': '<svg viewBox="0 0 120 78" shape-rendering="crispEdges" role="img" aria-label="pen"><rect x="76" y="15" width="4" height="4" fill="#2D5016"/><rect x="80" y="15" width="4" height="4" fill="#2D5016"/><rect x="72" y="19" width="4" height="4" fill="#2D5016"/><rect x="76" y="19" width="4" height="4" fill="#2D5016"/><rect x="80" y="19" width="4" height="4" fill="#2D5016"/><rect x="68" y="23" width="4" height="4" fill="#2D5016"/><rect x="72" y="23" width="4" height="4" fill="#2D5016"/><rect x="76" y="23" width="4" height="4" fill="#2D5016"/><rect x="64" y="27" width="4" height="4" fill="#2D5016"/><rect x="68" y="27" width="4" height="4" fill="#2D5016"/><rect x="72" y="27" width="4" height="4" fill="#2D5016"/><rect x="60" y="31" width="4" height="4" fill="#2D5016"/><rect x="64" y="31" width="4" height="4" fill="#2D5016"/><rect x="68" y="31" width="4" height="4" fill="#2D5016"/><rect x="56" y="35" width="4" height="4" fill="#2D5016"/><rect x="60" y="35" width="4" height="4" fill="#2D5016"/><rect x="64" y="35" width="4" height="4" fill="#2D5016"/><rect x="52" y="39" width="4" height="4" fill="#9a7b3f"/><rect x="56" y="39" width="4" height="4" fill="#9a7b3f"/><rect x="60" y="39" width="4" height="4" fill="#9a7b3f"/><rect x="48" y="43" width="4" height="4" fill="#9a7b3f"/><rect x="52" y="43" width="4" height="4" fill="#9a7b3f"/><rect x="56" y="43" width="4" height="4" fill="#9a7b3f"/><rect x="60" y="43" width="4" height="4" fill="#9a7b3f"/><rect x="44" y="47" width="4" height="4" fill="#9a7b3f"/><rect x="48" y="47" width="4" height="4" fill="#9a7b3f"/><rect x="52" y="47" width="4" height="4" fill="#1b330d"/><rect x="56" y="47" width="4" height="4" fill="#9a7b3f"/><rect x="60" y="47" width="4" height="4" fill="#9a7b3f"/><rect x="40" y="51" width="4" height="4" fill="#9a7b3f"/><rect x="44" y="51" width="4" height="4" fill="#9a7b3f"/><rect x="48" y="51" width="4" height="4" fill="#1b330d"/><rect x="52" y="51" width="4" height="4" fill="#9a7b3f"/><rect x="40" y="55" width="4" height="4" fill="#9a7b3f"/><rect x="44" y="55" width="4" height="4" fill="#9a7b3f"/><rect x="36" y="59" width="4" height="4" fill="#9a7b3f"/><rect x="40" y="59" width="4" height="4" fill="#9a7b3f"/><rect x="36" y="63" width="4" height="4" fill="#9a7b3f"/></svg>',
})

# ── highlights (home) — internal links are locale-aware ──
def HL(lang):
    return f"""<div class="highlights">
  <a class="hcard" href="{page_url('research.html', lang)}">
    <div class="thumb">{THUMBS['px_research']}</div>
    <h3>research</h3>
  </a>
  <a class="hcard" href="{page_url('works.html', lang)}">
    <div class="thumb">{THUMBS['px_works']}</div>
    <h3>works</h3>
  </a>
  <a class="hcard" href="{page_url('creative.html', lang)}">
    <div class="thumb">{THUMBS['px_creative']}</div>
    <h3>creative</h3>
  </a>
</div>"""

# Featured paper — citation, language-neutral (shared)
FEATURE = """<div class="feature">
  <div class="cover" aria-hidden="true"><span class="j">Plant<br>Species<br>Biology</span><span class="y">2026</span></div>
  <div>
    <span class="authors">Tachiki, Y., &amp; Umeda, E. (2026).</span>
    <a class="ttl" href="https://doi.org/10.1111/1442-1984.70039">Asymmetric competitions between seedling and clonal ramet promote the evolution of extraordinary long flowering time in monocarpic perennial plants.</a>
    <span class="venue">Plant Species Biology, 41(1), e70039.</span>
    <a class="more" href="https://doi.org/10.1111/1442-1984.70039">read the paper</a>
  </div>
</div>"""

# elsewhere — labels already English (shared)
ELSEWHERE = """<h3>elsewhere</h3>
<ul class="affil links">
  <li><a href="https://x.com/EIUmeda">X / @EIUmeda</a></li>
  <li><a href="https://researchmap.jp/eisaku_umeda">researchmap</a></li>
  <li><a href="https://orcid.org/0009-0001-8731-0583">ORCID</a></li>
  <li><a href="https://github.com/eUmeda">github / @eUmeda</a></li>
</ul>"""

# ── tagline (home heading): (primary, sub) ──
TAGLINE = {
 "ja": ("生命の進化を数理で解く", "Solving the evolution of life through mathematics."),
 "en": ("Solving the evolution of life through mathematics.", "生命の進化を数理で解く"),
}

BIO_BODY = {
 "ja": """<div class="bio">
          <p>梅田栄作（Eisaku Umeda）は個体群動態と進化の相互作用を研究しています。専門は数理生物学・進化生態学・植物生態学。東京都立大学 理学研究科 数理計算生物学研究室に所属しています。</p>
        </div>""",
 "en": """<div class="bio">
          <p>Eisaku Umeda studies the interplay between population dynamics and evolution. His fields are mathematical biology, evolutionary ecology, and plant ecology. He belongs to the Mathematical and Computational Biology Laboratory, Graduate School of Science, Tokyo Metropolitan University.</p>
        </div>""",
}

CAREER_SECTION = {
 "ja": """<section class="sec"><h2>経歴</h2>
        <ul class="timeline wide">
          <li><span class="when">高校</span><span class="what">福岡県立福岡高校　図書委員会／文芸部 出身</span></li>
          <li><span class="when">2019.4 – 2023.3</span><span class="what">東京都立大学 理学部 生命科学</span></li>
          <li><span class="when">2023.4 – 2025.3</span><span class="what">東京都立大学大学院 理学研究科 生命科学専攻　修士課程</span></li>
          <li><span class="when">2025.4 –</span><span class="what">東京都立大学大学院 理学研究科 生命科学専攻　博士課程</span></li>
        </ul>
      </section>""",
 "en": """<section class="sec"><h2>Education</h2>
        <ul class="timeline wide">
          <li><span class="when">High school</span><span class="what">Fukuoka Prefectural Fukuoka High School — Library Committee / Literature Club</span></li>
          <li><span class="when">2019.4 – 2023.3</span><span class="what">B.S. in Biological Sciences, Tokyo Metropolitan University</span></li>
          <li><span class="when">2023.4 – 2025.3</span><span class="what">M.S. course, Biological Sciences, Graduate School of Science, Tokyo Metropolitan University</span></li>
          <li><span class="when">2025.4 –</span><span class="what">Ph.D. course, Biological Sciences, Graduate School of Science, Tokyo Metropolitan University</span></li>
        </ul>
      </section>""",
}

RECENTLY = {
 "ja": """<h3>recently</h3>
      <ul class="timeline">
        <li><span class="when">2026 · paper</span><span class="what">Tachiki &amp; Umeda (2026), <i>Plant Species Biology</i>.</span></li>
        <li><span class="when">2025.4 –</span><span class="what">東京都立大学大学院 博士課程に進学。</span></li>
      </ul>""",
 "en": """<h3>recently</h3>
      <ul class="timeline">
        <li><span class="when">2026 · paper</span><span class="what">Tachiki &amp; Umeda (2026), <i>Plant Species Biology</i>.</span></li>
        <li><span class="when">2025.4 –</span><span class="what">Began the Ph.D. course at Tokyo Metropolitan University.</span></li>
      </ul>""",
}

# ───────────────────────────── per-page content ─────────────────────────────
TITLES = {
 "home": {
   "ja": "梅田栄作 (Eisaku Umeda) — 数理生物学・進化生態学・植物生態学 | 東京都立大学",
   "en": "Eisaku Umeda (梅田栄作) — Mathematical Biology, Evolutionary Ecology, Plant Ecology | Tokyo Metropolitan University"},
 "research": {
   "ja": "Research — 梅田栄作 (Eisaku Umeda) | 数理生物学・進化生態学・植物生態学",
   "en": "Research — Eisaku Umeda | Mathematical Biology, Evolutionary Ecology, Plant Ecology"},
 "works": {
   "ja": "Works — 梅田栄作 (Eisaku Umeda) | 研究・教育デモ・可視化・Web制作",
   "en": "Works — Eisaku Umeda | Research & Teaching Demos, Visualization, Web"},
 "creative": {
   "ja": "Creative — 犬井作 (Tsukuru Inui) | 梅田栄作 (Eisaku Umeda)",
   "en": "Creative — Tsukuru Inui | Eisaku Umeda"},
 "homage": {
   "ja": "Homage — Steven Strogatz への敬意 | 梅田栄作 (Eisaku Umeda)",
   "en": "Homage — A Tribute to Steven Strogatz | Eisaku Umeda"},
 "contact": {
   "ja": "Contact — 梅田栄作 (Eisaku Umeda) | 東京都立大学",
   "en": "Contact — Eisaku Umeda | Tokyo Metropolitan University"},
}

DESCS = {
 "home": {
   "ja": "梅田栄作 (Eisaku Umeda)。東京都立大学 理学研究科 博士課程。数理生物学・進化生態学・植物生態学。個体ベースシミュレーションでササタケ類の個体群動態と進化を研究。犬井作 (Tsukuru Inui) 名義で創作活動。",
   "en": "Eisaku Umeda — doctoral student at the Graduate School of Science, Tokyo Metropolitan University. Mathematical biology, evolutionary ecology, and plant ecology. Studies the population dynamics and evolution of bamboos using individual-based simulation. Also writes fiction under the pen name Tsukuru Inui."},
 "research": {
   "ja": "梅田栄作の研究紹介。生活史戦略の進化に関心。最長120年待って一斉開花するササタケ類の開花時間の進化を、個体ベースシミュレーションと一方向的競争の明示化から研究。査読論文 Tachiki and Umeda (2026, Plant Species Biology)。",
   "en": "Eisaku Umeda's research. Interested in the evolution of life-history strategies. Studies the evolution of flowering time in bamboos — which can wait up to 120 years before flowering en masse — through individual-based simulation and the explicit treatment of asymmetric competition. Peer-reviewed paper: Tachiki and Umeda (2026, Plant Species Biology)."},
 "works": {
   "ja": "梅田栄作の成果物。研究・教育デモ集、サラブレッド系統年表、論文カード生成パイプライン、研究室サイト制作。Web とコードでつくる作品。",
   "en": "Eisaku Umeda's works: research and teaching demos, a thoroughbred sire-line chronicle, a paper-card generation pipeline, and laboratory websites. Things built with the web and code."},
 "creative": {
   "ja": "梅田栄作は犬井作（Tsukuru Inui）名義で創作活動をしています。これまでの作品と今後の活動を集約予定。",
   "en": "Eisaku Umeda creates under the pen name Tsukuru Inui. Past works and future activities will be gathered here."},
 "homage": {
   "ja": "このサイトは数学者 Steven Strogatz の個人サイト stevenstrogatz.com へのオマージュ（パロディ）です。著書 SYNC（早川書房）・Nonlinear Dynamics and Chaos、ポッドキャスト The Joy of Why、本家サイトへのリンク。",
   "en": "This site is an homage (a parody) of mathematician Steven Strogatz's personal site, stevenstrogatz.com. Links to his books SYNC and Nonlinear Dynamics and Chaos, his podcast The Joy of Why, and the original site."},
 "contact": {
   "ja": "梅田栄作 (Eisaku Umeda) への連絡先。X (@EIUmeda)・researchmap・GitHub。東京都立大学 理学研究科 生命科学専攻。",
   "en": "How to reach Eisaku Umeda: X (@EIUmeda), researchmap, and GitHub. Department of Biological Sciences, Graduate School of Science, Tokyo Metropolitan University."},
}

def home_main(lang):
    tag_main, tag_sub = TAGLINE[lang]
    latest = "Latest Work"
    highlights = "Highlights"
    return f"""
      <div class="home-heading">
        <p class="tagline">{tag_main}
          <span class="en">{tag_sub}</span></p>
      </div>
      <section class="hero bio-hero">
        {photo_fig(lang)}
        {BIO_BODY[lang]}
      </section>
      <hr class="div">
      {CAREER_SECTION[lang]}
      <hr class="div">
      <section class="sec"><h2>{latest}</h2>{FEATURE}</section>
      <hr class="div">
      <section class="sec"><h2>{highlights}</h2>{HL(lang)}</section>
"""

# research narrative (本人 JP 文 verbatim / EN は draft 翻訳)
RESEARCH_BODY = {
 "ja": """
        <h3 class="sub-h">1. 私の研究のはじまりと最初に出版された論文</h3>
        <div class="rbody">
          <p>私の興味は「生活史戦略（life history strategy）の進化」にあります。生活史戦略とは、生物が特定の環境で適応度を最大化するために採る、繁殖と生存の行動の組み合わせを指します（Buss &amp; Schmitt, 2019）。たとえば植物がいつ、生涯で何回花を咲かせるか、といった特徴です。サクラは毎年花咲きますが、竹林へ行ってもほとんど花を咲かせていることはありませんよね。このような、生き物がいつ育ち、いつ繁殖するかといった特徴が、大小・種類を問わず、どのように多様になったかに興味があります。</p>
          <p>きっかけは偶然読んだ指導教官の論文で、ササタケ類が開花まで待つ年数が、地下茎が長いほど長くなることを示した理論研究でした。ササタケ類は「一回繁殖型・多年生」という生活史を示します。種子から発芽した後、何十年もの間、地下に枝を伸ばしてクローン（いわゆる「タケノコ」です）を生産し、やがて一斉に開花・枯死するのです。この発芽から開花までかかる時間は種特異的であり、3年から120年まで幅があり、アジアでは熱帯から温帯に向かって長くなる緯度的勾配が見られます。この緯度的勾配を生み出すのが地下茎構造の違いではないか、というのがこの論文の主張でした。</p>
          <p>実は、日本や中国、韓国といった東アジアの国々では竹林があるのに、インドネシアやインド、スリランカでは竹林はみられません。熱帯アジアに分布するササタケは、クローンを親のそばに生産・配置します。これは地下茎構造の違いに由来します。温帯型のササタケ類は細く長い地下茎を、熱帯型は太く短い地下茎を種特異的に有するのです。Tachiki et al. 2015 J. Ecol. は、開花周期に見られる緯度的勾配は、地下茎構造の熱帯から温帯にかけた違いと同様の傾向を示しているだけでなく、その地下茎構造の違いが緯度的勾配の創出要因ではないかと示したのです。</p>
          <p>この論文は私が初めて読んだ数理生物学の研究論文であり、それまでの私の世界にはないものでした。地下茎が長いとクローン間の距離が離れる。そのため開花まで待つ期間に生じるクローン間の競争が緩和される。結果、クローナル成長効率が改善され、より開花が遅延する。高校時代は文芸部に所属しており、伊藤計劃や円城塔のSF小説に憧れて、自分でも思弁的な（つもりの）空想小説を書いていた私にとって、その営みは非常に刺激的でした。数理という道具を使えば、まるでSF小説の登場人物のように、真理を探求できる。そういう手応えが、Tachiki et al. 2015 J. Ecol. からは感じ取れました。本気でこれをやりたい！ そう思いました。</p>
          <p>当初は先行研究の結果をどうしても再現できず、原因を探るうちに、鍵が一方向的競争にあると分かってきました。光をめぐる競争では、背の高い個体が光を独占し、低い個体を被陰します。優位が一方向にしか働かないこの非対称性は、先行研究では暗黙に仮定されていましたが、私のモデルでは明示的に組み込む必要がありました。この仮定を正面から扱って解析した結果をまとめたのが、立木先生との共著 Tachiki &amp; Umeda（2026）です。種子由来の子孫と、地下茎を介してクローナルに生産された子孫のあいだの非対称な競争が、一回繁殖型の多年生植物における異常に長い開花時間の進化を促しうることを示しました。</p>
          <p>現在は、2報目の研究に取り組んでいます。</p>
          <figure class="gabstract">
            <img class="gabstract-img" src="/fig1.png" alt="一方向的競争のイメージ">
            <figcaption>一方向的競争のイメージ</figcaption>
          </figure>
        </div>""",
 "en": """
        <h3 class="sub-h">1. How my research began, and my first published paper</h3>
        <div class="rbody">
          <p>My interest lies in the evolution of life-history strategies. A life-history strategy is the combination of reproductive and survival behaviors that an organism adopts to maximize its fitness in a particular environment (Buss &amp; Schmitt, 2019) — for instance, when, and how many times in its life, a plant flowers. Cherry trees bloom every year, yet when you step into a bamboo grove you almost never find one in flower. I am fascinated by how such traits — when an organism grows and when it reproduces — came to be so diverse across living things, whatever their size or kind.</p>
          <p>It began with a paper by my advisor that I happened to read: a theoretical study showing that the number of years bamboos wait before flowering grows longer as their rhizomes grow longer. Bamboos follow a monocarpic, perennial life history. After germinating from seed, they spend decades extending underground branches to produce clones (the shoots we call <i>takenoko</i>), until at last they flower and die all at once. This time from germination to flowering is species-specific, ranging from 3 to 120 years, and across Asia it shows a latitudinal gradient, lengthening from the tropics toward the temperate zone. The paper argued that this gradient might be generated by differences in rhizome structure.</p>
          <p>In fact, while East Asian countries such as Japan, China, and Korea have bamboo groves, Indonesia, India, and Sri Lanka do not. The bamboos of tropical Asia produce and place their clones close to the parent — a consequence of rhizome structure. Temperate bamboos have, species by species, thin and long rhizomes, while tropical ones have thick and short rhizomes. Tachiki et al. (2015, J. Ecol.) showed not only that the latitudinal gradient in flowering cycles parallels the tropical-to-temperate change in rhizome structure, but that this difference in rhizome structure may itself be what creates the gradient.</p>
          <p>This was the first mathematical-biology paper I had ever read, and it was unlike anything in my world until then. When the rhizome is long, the distance between clones grows; the competition among clones during the waiting period before flowering is eased; and so clonal growth becomes more efficient and flowering is delayed even further. In high school I belonged to the literature club, and — admiring the science fiction of Project Itoh and Toh EnJoe — I wrote my own (would-be) speculative stories; to me, this endeavor was electrifying. With the tool of mathematics, one could pursue truth like a character in a science-fiction novel. That was the conviction I drew from Tachiki et al. (2015, J. Ecol.). I want to do this for real! — that is what I thought.</p>
          <p>At first I simply could not reproduce the earlier study's results, and as I searched for the cause I came to see that the key lay in asymmetric competition. In competition for light, taller individuals monopolize the light and shade out shorter ones. This asymmetry — where the advantage runs in only one direction — had been assumed implicitly in the earlier work, but in my model it had to be built in explicitly. The analysis that confronts this assumption head-on is the paper I co-authored with Prof. Tachiki, Tachiki &amp; Umeda (2026). We showed that asymmetric competition between seed-derived offspring and offspring produced clonally through rhizomes can drive the evolution of extraordinarily long flowering times in monocarpic perennial plants.</p>
          <p>I am now working on my second study.</p>
          <figure class="gabstract">
            <img class="gabstract-img" src="/fig1.png" alt="An illustration of asymmetric competition">
            <figcaption>An illustration of asymmetric competition</figcaption>
          </figure>
        </div>""",
}

REFERENCES = """
      <section class="sec"><h2>References</h2>
        <ol class="refs">
          <li>Buss, D., &amp; Schmitt, D. (2019). Mate preferences and their behavioral manifestations. Annual Review of Psychology, 70(1), 77–110.</li>
          <li>Tachiki, Y., Makita, A., Suyama, Y., &amp; Satake, A. (2015). A spatially explicit model for flowering time in bamboos: long rhizomes drive the evolution of delayed flowering. Journal of Ecology, 103(3), 585–593.</li>
          <li>Tachiki, Y., &amp; Umeda, E. (2026). Asymmetric competitions between seedling and clonal ramet promote the evolution of extraordinary long flowering time in monocarpic perennial plants. Plant Species Biology, 41(1), e70039. <a href="https://doi.org/10.1111/1442-1984.70039">doi:10.1111/1442-1984.70039</a></li>
        </ol>
      </section>"""

def research_main(lang):
    head = "Research"
    return f"""
      <section class="sec"><h2>{head}</h2>{RESEARCH_BODY[lang]}
      </section>{REFERENCES}
"""

# Works cards — (url, thumb-key[unused in list], {ja,en title}, {ja,en desc})
WORK_ITEMS = [
 ("https://eumeda.github.io/Claude-public/", "demos",
  {"ja":"研究・教育デモ集", "en":"Research &amp; Teaching Demos"},
  {"ja":"非線形力学系（Strogatz）の分岐・カオス、数理生物モデル、データ可視化のインタラクティブ実装集。",
   "en":"An interactive collection of nonlinear-dynamics (Strogatz) bifurcations and chaos, mathematical-biology models, and data visualizations."}),
 ("https://eumeda.github.io/sire-line-fromEclipse-toSundaySilence/", "sire",
  {"ja":"サラブレッド系統年表", "en":"Thoroughbred Sire-Line Chronicle"},
  {"ja":"Darley Arabian から Equinox までの父系（sire-line）の流れを辿る年表型ビジュアライゼーション。",
   "en":"A timeline visualization tracing the sire-line from the Darley Arabian to Equinox."}),
 ("https://github.com/eUmeda/Claude-papercards", "cards",
  {"ja":"論文カード生成", "en":"Paper Card Generator"},
  {"ja":"論文 PDF から A5 要約カード＋対訳 IMRAD PDF を生成するパイプライン（docling + LLM）。",
   "en":"A pipeline that turns a paper PDF into an A5 summary card plus a bilingual IMRAD PDF (docling + LLM)."}),
 ("https://mcb.fpark.tmu.ac.jp/", "mcb",
  {"ja":"数理計算生物学研究室", "en":"Mathematical &amp; Computational Biology Lab"},
  {"ja":"立木（Tachiki）グループ公式サイト — Web 制作協力。",
   "en":"Official site of the Tachiki group — web development support."}),
 ("https://biol.fpark.tmu.ac.jp/plantecol/", "leaf",
  {"ja":"植物生態学研究室", "en":"Plant Ecology Laboratory"},
  {"ja":"東京都立大学 — Web 制作協力。",
   "en":"Tokyo Metropolitan University — web development support."}),
]
SKILL_ITEMS = [
 ("https://github.com/eUmeda/pdf-metadata-filler", "meta",
  {"ja":"PDF メタデータ補完", "en":"PDF Metadata Filler"},
  {"ja":"論文 PDF の Title/Author/DOI を OpenAlex・CrossRef・CiNii・OCR・LLM の多段で自動補完する Claude Code skill。",
   "en":"A Claude Code skill that auto-fills a paper PDF's Title/Author/DOI through a multi-stage pipeline of OpenAlex, CrossRef, CiNii, OCR, and LLM."}),
 ("https://github.com/eUmeda/session-resume", "resume",
  {"ja":"セッション再開プロンプト生成", "en":"Session-Resume Prompt Generator"},
  {"ja":"作業を中断する際、次回再開用の構造化プロンプトを LLM ベストプラクティスに沿って生成する Claude Code skill。",
   "en":"A Claude Code skill that, when you pause your work, generates a structured prompt for resuming next time, following LLM best practices."}),
 ("https://github.com/eUmeda/LLM-prompting-bestpractice", "prompt",
  {"ja":"プロンプト設計ベストプラクティス", "en":"Prompt-Design Best Practices"},
  {"ja":"Anthropic・OpenAI・Edison の 3 ベンダー統合の作法で外部 LLM 用プロンプトを設計・レビューする Claude Code skill。",
   "en":"A Claude Code skill for designing and reviewing prompts for external LLMs, combining the practices of three vendors — Anthropic, OpenAI, and Edison."}),
]

def work_list(items, lang):
    return "\n".join(
      f'''          <li>
            <a class="t" href="{u}">{title[lang]}</a>
            <div class="d">{desc[lang]}</div>
          </li>'''
      for (u, t, title, desc) in items)

def works_main(lang):
    return f"""
      <section class="sec"><h2>Works</h2>
        <h3 class="sub-h">Publications</h3>
        {FEATURE}
        <h3 class="sub-h">Made for Fun</h3>
        <ul class="worklist">
{work_list(WORK_ITEMS[:3], lang)}
        </ul>
        <h3 class="sub-h">Claude Code Skills</h3>
        <ul class="worklist">
{work_list(SKILL_ITEMS, lang)}
        </ul>
        <h3 class="sub-h">Made for Work</h3>
        <ul class="worklist">
{work_list(WORK_ITEMS[3:], lang)}
        </ul>
      </section>
"""

CREATIVE_MAIN = {
 "ja": """
      <section class="sec"><h2>Creative</h2>
        <p class="lead">梅田栄作は、<b>犬井作（Tsukuru Inui）</b>名義で創作活動をしています。</p>
        <ul class="worklist">
          <li>
            <a class="t" href="/inui">犬井作 / Tsukuru Inui</a><span class="wip">工事中</span>
            <div class="d">犬井作名義の創作活動をまとめるページ。これまでの作品と今後の活動を集約予定。</div>
          </li>
        </ul>
        <p class="note">創作のページは現在準備中です。完成までしばらくお待ちください。</p>
      </section>
""",
 "en": """
      <section class="sec"><h2>Creative</h2>
        <p class="lead">Eisaku Umeda creates under the pen name <b>Tsukuru Inui (犬井作)</b>.</p>
        <ul class="worklist">
          <li>
            <a class="t" href="/inui">Tsukuru Inui / 犬井作</a><span class="wip">under construction</span>
            <div class="d">A page gathering creative work under the Tsukuru Inui name. Past works and future activities will be collected here.</div>
          </li>
        </ul>
        <p class="note">The creative page is currently in preparation. Please bear with me until it is complete.</p>
      </section>
""",
}

BOOK_URL = "https://www.stevenstrogatz.com/books/nonlinear-dynamics-and-chaos-with-applications-to-physics-biology-chemistry-and-engineering"
ROUTLEDGE_URL = "https://www.routledge.com/Nonlinear-Dynamics-and-Chaos-With-Applications-to-Physics-Biology-Chemistry-and-Engineering/Strogatz/p/book/9780367026509"
JOYWHY_URL = "https://www.quantamagazine.org/tag/the-joy-of-why/"
JOYWHY_APPLE = "https://podcasts.apple.com/us/podcast/the-joy-of-why/id1608948873"
STROGATZ_URL = "https://www.stevenstrogatz.com/"
SYNC_URL = "https://www.amazon.co.jp/dp/4150504032"

HOMAGE_MAIN = {
 "ja": f"""
      <section class="sec"><h2>An Homage to Steven Strogatz</h2>
        <p class="manifesto">このサイトは数学者 Steven Strogatz の個人サイト stevenstrogatz.com のデザインをできるだけコピーしています。作家・奈須きのこが講談社BOXを愛するあまりそのデザインを完全コピーした同人誌を発行したエピソードがあります。それと同じことをしました。氏の著作の邦訳は、学部生時代の私を大いに刺激しました。私は彼を尊敬しています</p>
        <p class="lead">そして本家はこちら。</p>
        <a class="visit-original" href="{STROGATZ_URL}">stevenstrogatz.com →</a>
      </section>
      <hr class="div">
      <section class="sec"><h2>悩んだらこの一冊</h2>
        <h3 class="sub-h">一般書</h3>
        <div class="tribute">
          <div>
            <span class="authors">スティーヴン・ストロガッツ（蔵本由紀 監修・長尾力 訳）</span>
            <a class="ttl" href="{SYNC_URL}">SYNC なぜ自然はシンクロしたがるのか</a>
            <span class="venue">ハヤカワ文庫 NF 403 〈数理を愉しむ〉シリーズ・早川書房</span>
            <p class="d">数理を用いて生命現象を解き明かす面白さ、研究者としてのスタンスがぎゅっと詰まった一冊です。Kindleで現在も販売しています。</p>
            <a class="more" href="{SYNC_URL}">Kindleで読む（Amazon）</a>
          </div>
        </div>
        <h3 class="sub-h">教科書</h3>
        <div class="tribute">
          <div>
            <span class="authors">Steven H. Strogatz</span>
            <a class="ttl" href="{BOOK_URL}">Nonlinear Dynamics and Chaos</a>
            <span class="venue">With Applications to Physics, Biology, Chemistry, and Engineering — 3rd ed., CRC Press (2024)</span>
            <p class="d">非線形力学系とカオスの定番教科書。分岐・アトラクター・カオスを、数式と図と直観で読ませる名著です。</p>
            <a class="more" href="{BOOK_URL}">strogatz.com</a>
            <a class="more" href="{ROUTLEDGE_URL}">publisher</a>
          </div>
        </div>
      </section>
      <hr class="div">
      <section class="sec"><h2>His Podcast</h2>
        <ul class="worklist">
          <li>
            <a class="t" href="{JOYWHY_URL}">The Joy of Why</a>
            <div class="d">Strogatz が第一線の科学者・数学者に「大きな問い」を尋ねる、Quanta Magazine のポッドキャスト。<a href="{JOYWHY_APPLE}">Apple&nbsp;Podcasts</a> ほか各所で配信。</div>
          </li>
        </ul>
      </section>
""",
 "en": f"""
      <section class="sec"><h2>An Homage to Steven Strogatz</h2>
        <p class="manifesto">This site copies, as closely as it can, the design of mathematician Steven Strogatz's personal site, stevenstrogatz.com. There is a story about the novelist Kinoko Nasu, who loved Kodansha BOX so much that he published a <i>doujinshi</i> (a self-made book) that completely copied its design. I have done the same thing. The Japanese translations of Strogatz's books inspired me greatly in my undergraduate years. I admire him.</p>
        <p class="lead">And here is the original.</p>
        <a class="visit-original" href="{STROGATZ_URL}">stevenstrogatz.com →</a>
      </section>
      <hr class="div">
      <section class="sec"><h2>When in doubt, read this</h2>
        <h3 class="sub-h">For general readers</h3>
        <div class="tribute">
          <div>
            <span class="authors">Steven Strogatz (Japanese edition: supervised by Yoshiki Kuramoto, translated by Tsutomu Nagao)</span>
            <a class="ttl" href="{SYNC_URL}">SYNC: The Emerging Science of Spontaneous Order</a>
            <span class="venue">Japanese edition: Hayakawa Bunko NF 403, the “Enjoying Mathematics” series — Hayakawa Publishing</span>
            <p class="d">A single volume brimming with the delight of using mathematics to unravel the phenomena of life, and with a researcher's stance toward the world. The Japanese edition is still on sale for Kindle.</p>
            <a class="more" href="{SYNC_URL}">Read on Kindle (Amazon.co.jp)</a>
          </div>
        </div>
        <h3 class="sub-h">Textbook</h3>
        <div class="tribute">
          <div>
            <span class="authors">Steven H. Strogatz</span>
            <a class="ttl" href="{BOOK_URL}">Nonlinear Dynamics and Chaos</a>
            <span class="venue">With Applications to Physics, Biology, Chemistry, and Engineering — 3rd ed., CRC Press (2024)</span>
            <p class="d">The standard textbook on nonlinear dynamics and chaos. A classic that conveys bifurcations, attractors, and chaos through equations, figures, and intuition.</p>
            <a class="more" href="{BOOK_URL}">strogatz.com</a>
            <a class="more" href="{ROUTLEDGE_URL}">publisher</a>
          </div>
        </div>
      </section>
      <hr class="div">
      <section class="sec"><h2>His Podcast</h2>
        <ul class="worklist">
          <li>
            <a class="t" href="{JOYWHY_URL}">The Joy of Why</a>
            <div class="d">A Quanta Magazine podcast in which Strogatz asks leading scientists and mathematicians the big questions. Available on <a href="{JOYWHY_APPLE}">Apple&nbsp;Podcasts</a> and elsewhere.</div>
          </li>
        </ul>
      </section>
""",
}

CONTACT_MAIN = {
 "ja": """
      <section class="sec"><h2>Contact</h2>
        <p class="lead">ご連絡は以下のいずれかからどうぞ。</p>
        <ul class="worklist">
          <li><a class="t" href="https://x.com/EIUmeda">X / @EIUmeda</a><div class="d">日々の研究・創作の発信。DM でのご連絡も。</div></li>
          <li><a class="t" href="https://researchmap.jp/eisaku_umeda">researchmap</a><div class="d">研究業績・プロフィール。</div></li>
          <li><a class="t" href="https://github.com/eUmeda">github / @eUmeda</a><div class="d">コード・成果物のリポジトリ。</div></li>
        </ul>
        <p class="note">所属: 東京都立大学 理学研究科 生命科学専攻（南大沢キャンパス）。</p>
      </section>
""",
 "en": """
      <section class="sec"><h2>Contact</h2>
        <p class="lead">Feel free to reach me through any of the following.</p>
        <ul class="worklist">
          <li><a class="t" href="https://x.com/EIUmeda">X / @EIUmeda</a><div class="d">Daily updates on research and creative work. Direct messages welcome.</div></li>
          <li><a class="t" href="https://researchmap.jp/eisaku_umeda">researchmap</a><div class="d">Research output and profile.</div></li>
          <li><a class="t" href="https://github.com/eUmeda">github / @eUmeda</a><div class="d">Repositories of code and works.</div></li>
        </ul>
        <p class="note">Affiliation: Department of Biological Sciences, Graduate School of Science, Tokyo Metropolitan University (Minami-Osawa campus).</p>
      </section>
""",
}

# assemble PAGES[key][lang] = dict(title, desc, ld, main)
MAINS = {
 "home":     {l: home_main(l)     for l in LANGS},
 "research": {l: research_main(l) for l in LANGS},
 "works":    {l: works_main(l)    for l in LANGS},
 "creative": CREATIVE_MAIN,
 "homage":   HOMAGE_MAIN,
 "contact":  CONTACT_MAIN,
}
LD_PAGES = {"home"}

PAGES = {}
for _k in ("home", "research", "works", "creative", "homage", "contact"):
    PAGES[_k] = {
        l: dict(title=TITLES[_k][l], desc=DESCS[_k][l], ld=(_k in LD_PAGES), main=MAINS[_k][l])
        for l in LANGS
    }

# ───────────────────────────── template ─────────────────────────────
LD_JSON = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "@id": "https://www.eisaku-umeda.com/#person",
  "name": "梅田栄作",
  "alternateName": ["Eisaku Umeda", "犬井作", "Tsukuru Inui"],
  "givenName": "栄作", "familyName": "梅田",
  "url": "https://www.eisaku-umeda.com/",
  "image": "https://www.eisaku-umeda.com/eisaku.png",
  "jobTitle": "博士課程学生 (Doctoral Student)",
  "affiliation": { "@type": "CollegeOrUniversity", "name": "東京都立大学 理学研究科 生命科学専攻", "url": "https://www.tmu.ac.jp/" },
  "alumniOf": { "@type": "CollegeOrUniversity", "name": "東京都立大学", "url": "https://www.tmu.ac.jp/" },
  "knowsAbout": ["Mathematical Biology","Evolutionary Ecology","Plant Ecology","Population Dynamics","数理生物学","進化生態学","植物生態学","個体群動態"],
  "memberOf": [
    { "@type": "Organization", "name": "日本生態学会" },
    { "@type": "Organization", "name": "個体群生態学会" },
    { "@type": "Organization", "name": "日本数理生物学会" }
  ],
  "sameAs": ["https://x.com/EIUmeda","https://researchmap.jp/eisaku_umeda","https://github.com/eUmeda","https://orcid.org/0009-0001-8731-0583","https://jglobal.jst.go.jp/detail?JGLOBAL_ID=202601009337600570"]
}
</script>"""

def nav_html(active, lang):
    items = "\n".join(
        f'        <li><a href="{page_url(href, lang)}"{" class=\"active\"" if k==active else ""}>{label}</a></li>'
        for (k,label,href) in NAV)
    return f"""      <nav class="vnav" aria-label="Site">
      <ul>
{items}
      </ul>
      </nav>"""

def rail_html(active, lang):
    recently = RECENTLY[lang] if active == "home" else ""
    return f"""    <aside class="rail">
{nav_html(active, lang)}
      {recently}
      {ELSEWHERE}
    </aside>"""

def foot_nav(lang):
    return "\n".join(f'      <li><a href="{page_url(href, lang)}">{label}</a></li>' for (k,label,href) in NAV)

def render(active, lang):
    p = PAGES[active][lang]
    ld = ("\n" + LD_JSON) if p.get("ld") else ""
    href = {k:h for k,_l,h in NAV if "#" not in h}[active]
    ja_url = BASE + page_url(href, "ja")
    en_url = BASE + page_url(href, "en")
    url = en_url if lang == "en" else ja_url
    home_u = page_url("index.html", lang)
    h1 = p["title"].split("|")[0].strip()
    og_locale = "en_US" if lang == "en" else "ja_JP"
    og_alt = "ja_JP" if lang == "en" else "en_US"
    hreflang = (f'<link rel="alternate" hreflang="ja" href="{ja_url}">\n'
                f'<link rel="alternate" hreflang="en" href="{en_url}">\n'
                f'<link rel="alternate" hreflang="x-default" href="{ja_url}">')
    ja_rel = page_url(href, "ja")
    en_rel = page_url(href, "en")
    if lang == "en":
        toggle = (f'<div class="lang-toggle" aria-label="Language">'
                  f'<a href="{ja_rel}" hreflang="ja" lang="ja">JP</a>'
                  f'<span class="lang-current">EN</span></div>')
    else:
        toggle = (f'<div class="lang-toggle" aria-label="Language">'
                  f'<span class="lang-current">JP</span>'
                  f'<a href="{en_rel}" hreflang="en" lang="en">EN</a></div>')
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<script>if(location.hostname.endsWith("pages.dev"))location.replace("https://www.eisaku-umeda.com"+location.pathname+location.search+location.hash);</script>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="index,follow">
<title>{p['title']}</title>
<meta name="description" content="{p['desc']}">
<meta name="author" content="梅田栄作 / Eisaku Umeda">
<link rel="canonical" href="{url}">
{hreflang}
<meta name="theme-color" content="#dedede">
<meta property="og:type" content="profile">
<meta property="og:title" content="{p['title']}">
<meta property="og:description" content="{p['desc']}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/eisaku.png">
<meta property="og:image:width" content="1432">
<meta property="og:image:height" content="1233">
<meta property="og:locale" content="{og_locale}">
<meta property="og:locale:alternate" content="{og_alt}">
<meta property="og:site_name" content="Eisaku Umeda">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{p['title']}">
<meta name="twitter:description" content="{p['desc']}">
<meta name="twitter:site" content="@EIUmeda">
<meta name="twitter:image" content="{BASE}/eisaku.png">
<link rel="icon" href="{FAVICON}">{ld}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=PT+Serif:ital,wght@0,400;0,700;1,400;1,700&family=Mulish:ital,wght@0,200;0,300;0,400;0,600;0,700;1,400&family=Noto+Sans+JP:wght@400;500;700&family=Noto+Serif+JP:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/style.css?v={CSS_VER}">
</head>
<body>

<div class="banner">
  <div class="banner-inner">
    <div class="site-title"><a href="{home_u}">Eisaku&nbsp;Umeda</a></div>
    <svg class="culm-logo" viewBox="0 0 246 66" role="img" aria-label="Culm">
      <line x1="18" y1="14" x2="227.2" y2="14" stroke="#c8a85c" stroke-width="1.2"/>
      <text x="122.6" y="50" text-anchor="middle" font-family="Georgia, 'Times New Roman', serif" font-size="40" fill="#c8a85c"><tspan>C</tspan><tspan dx="23">U</tspan><tspan dx="23">L</tspan><tspan dx="23">M</tspan></text>
      <line x1="18" y1="60" x2="227.2" y2="60" stroke="#c8a85c" stroke-width="1.2"/>
    </svg>
  </div>
</div>

<div class="shell">
  <div class="layout">
    <main class="main">
      <h1 class="vh">{h1}</h1>
{p['main']}
    </main>
{rail_html(active, lang)}
  </div>
</div>

{toggle}

<footer>
  <div class="foot-inner">
    <ul class="foot-nav">
{foot_nav(lang)}
    </ul>
    <div class="foot-meta">
      <span>© 2026 梅田栄作 · Eisaku Umeda</span>
      <span class="cc">⚒ <b>Generated with Claude Code</b></span>
      <span><a href="https://github.com/eUmeda">github.com/eUmeda</a></span>
    </div>
    <p class="colophon">design lovingly modeled after <a href="https://www.stevenstrogatz.com/">stevenstrogatz.com</a> — with admiration.</p>
  </div>
</footer>

</body>
</html>
"""

# clean a stale page if present (both locales)
for stale in ("about" + ".html",):
    for d in (OUT, os.path.join(OUT, "en")):
        sp = os.path.join(d, stale)
        if os.path.exists(sp):
            os.remove(sp)

# write JP (root) + EN (en/) pages
for (k,_,href) in NAV:
    if k not in PAGES:
        continue
    with open(os.path.join(OUT, href), "w", encoding="utf-8") as f:
        f.write(render(k, "ja"))
    with open(os.path.join(OUT, "en", href), "w", encoding="utf-8") as f:
        f.write(render(k, "en"))
    print("wrote", href, "+ en/" + href)

# robots.txt (unchanged)
open(os.path.join(OUT,"robots.txt"),"w",encoding="utf-8").write(
    "User-agent: *\nAllow: /\n\nUser-agent: GPTBot\nAllow: /\nUser-agent: ClaudeBot\nAllow: /\nUser-agent: Claude-Web\nAllow: /\nUser-agent: PerplexityBot\nAllow: /\nUser-agent: Google-Extended\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % BASE)

# sitemap.xml — bilingual: JP + EN url per page, each with reciprocal xhtml:link alternates.
LASTMOD = "2026-06-14"
_bilingual = [h for k,_l,h in NAV if "#" not in h]  # the 6 generated pages
_blocks = []
for href in _bilingual:
    ja = BASE + page_url(href, "ja")
    en = BASE + page_url(href, "en")
    alts = ('<xhtml:link rel="alternate" hreflang="ja" href="%s"/>'
            '<xhtml:link rel="alternate" hreflang="en" href="%s"/>'
            '<xhtml:link rel="alternate" hreflang="x-default" href="%s"/>') % (ja, en, ja)
    _blocks.append('  <url><loc>%s</loc><lastmod>%s</lastmod>%s</url>' % (ja, LASTMOD, alts))
    _blocks.append('  <url><loc>%s</loc><lastmod>%s</lastmod>%s</url>' % (en, LASTMOD, alts))
# inui — JP-only placeholder (noindex), no alternates
_blocks.append('  <url><loc>%s/inui</loc><lastmod>%s</lastmod></url>' % (BASE, LASTMOD))
_locs = "\n".join(_blocks)
open(os.path.join(OUT,"sitemap.xml"),"w",encoding="utf-8").write(
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
    'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n%s\n</urlset>\n' % _locs)
print("wrote robots.txt + sitemap.xml")
print("done")
