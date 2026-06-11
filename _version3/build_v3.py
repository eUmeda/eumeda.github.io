#!/usr/bin/env python3
# v3 (Strogatz homage) — multi-page site generator.
# 中身は梅田栄作の実コンテンツ verbatim。タグラインのみオリジナル。design は stevenstrogatz.com への homage (colophon で明示)。
import os

OUT = "/tmp/eumeda-hub/_version3"
os.makedirs(OUT, exist_ok=True)

NAV = [
    ("home",     "home",     "index.html"),
    ("research", "research", "research.html"),
    ("works",    "works",    "works.html"),
    ("creative", "creative", "creative.html"),
    ("homage",   "homage",   "homage.html"),
    ("contact",  "contact",  "contact.html"),
]

FAVICON = ("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'>"
           "<rect width='64' height='64' rx='12' fill='%232D5016'/>"
           "<text x='32' y='45' font-family='Georgia,serif' font-size='40' fill='%23ffffff' text-anchor='middle'>E</text></svg>")

SOCIAL_X = ('<a href="https://x.com/EIUmeda" aria-label="X" title="X / @EIUmeda">'
            '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg></a>')
SOCIAL_RM = ('<a class="rm" href="https://researchmap.jp/eisaku_umeda" aria-label="researchmap" title="researchmap">'
             '<img src="researchmap.gif" alt="researchmap" width="187" height="23"></a>')
SOCIAL_GH = ('<a href="https://github.com/eUmeda" aria-label="GitHub" title="GitHub / @eUmeda">'
             '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23A11.5 11.5 0 0112 5.803c1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.91 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222 0 1.606-.015 2.898-.015 3.293 0 .322.218.694.825.576C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg></a>')

# ヒーローの本人写真 (Strogatz 本家のポートレート位置)。eisaku.jpg を _version3/ に置く。
PHOTO_FIG = """<figure class="portrait">
  <img src="eisaku.png" alt="梅田栄作 (Eisaku Umeda) — 東京都立大学 理学研究科" width="440" height="440">
  <figcaption class="cap">梅田栄作 · Eisaku&nbsp;Umeda</figcaption>
</figure>"""

PORTRAIT_SVG = """<svg viewBox="0 0 200 240" role="img" aria-label="位相図（減衰振動子の相図）">
  <rect width="200" height="240" fill="#fbfbfa"/>
  <line x1="20" y1="120" x2="184" y2="120" stroke="#cfcfcf" stroke-width="1"/>
  <line x1="100" y1="20" x2="100" y2="220" stroke="#cfcfcf" stroke-width="1"/>
  <g stroke="#c9c9c9" stroke-width="1">
    <line x1="46" y1="60" x2="58" y2="66"/><line x1="140" y1="60" x2="152" y2="70"/>
    <line x1="46" y1="180" x2="58" y2="174"/><line x1="140" y1="180" x2="152" y2="170"/>
    <line x1="70" y1="40" x2="84" y2="44"/><line x1="116" y1="196" x2="130" y2="200"/>
  </g>
  <path d="M178 36 C 120 6, 36 30, 30 96 C 26 156, 96 196, 150 176 C 188 162, 188 118, 150 108 C 118 100, 86 120, 92 146 C 96 166, 124 168, 132 150" fill="none" stroke="#2D5016" stroke-width="2.1"/>
  <path d="M26 196 C 70 214, 150 206, 174 150" fill="none" stroke="#ea7d07" stroke-width="1.7"/>
  <circle cx="116" cy="138" r="4.4" fill="#2D5016"/>
  <circle cx="100" cy="120" r="4" fill="#fff" stroke="#333" stroke-width="1.6"/>
  <path d="M150 176 l -9 -1 l 5 7 z" fill="#2D5016"/>
  <path d="M174 150 l -2 -9 l -7 6 z" fill="#ea7d07"/>
</svg>"""

# Works のサムネ (5 種, 各々モチーフ違い)
THUMBS = {
 "demos": '<svg viewBox="0 0 120 78"><line x1="10" y1="68" x2="110" y2="68" stroke="#cfcfcf"/><line x1="10" y1="10" x2="10" y2="68" stroke="#cfcfcf"/><path d="M12 66 C 40 64, 52 18, 70 18 C 88 18, 100 60, 112 40" fill="none" stroke="#2D5016" stroke-width="2"/><circle cx="70" cy="18" r="3" fill="#9a7b3f"/></svg>',
 "sire":  '<svg viewBox="0 0 120 78"><line x1="20" y1="39" x2="48" y2="39" stroke="#2D5016" stroke-width="2"/><line x1="48" y1="39" x2="72" y2="22" stroke="#2D5016" stroke-width="2"/><line x1="48" y1="39" x2="72" y2="56" stroke="#2D5016" stroke-width="2"/><line x1="72" y1="22" x2="100" y2="14" stroke="#cfcfcf" stroke-width="2"/><line x1="72" y1="22" x2="100" y2="30" stroke="#cfcfcf" stroke-width="2"/><line x1="72" y1="56" x2="100" y2="48" stroke="#cfcfcf" stroke-width="2"/><line x1="72" y1="56" x2="100" y2="64" stroke="#cfcfcf" stroke-width="2"/><circle cx="20" cy="39" r="3.4" fill="#9a7b3f"/></svg>',
 "cards": '<svg viewBox="0 0 120 78"><rect x="30" y="20" width="44" height="40" fill="#fff" stroke="#cfcfcf"/><rect x="40" y="16" width="44" height="40" fill="#fff" stroke="#2D5016"/><line x1="46" y1="26" x2="78" y2="26" stroke="#9a7b3f" stroke-width="2"/><line x1="46" y1="34" x2="78" y2="34" stroke="#cfcfcf"/><line x1="46" y1="40" x2="72" y2="40" stroke="#cfcfcf"/></svg>',
 "mcb":   '<svg viewBox="0 0 120 78"><line x1="60" y1="39" x2="30" y2="20" stroke="#cfcfcf"/><line x1="60" y1="39" x2="92" y2="24" stroke="#cfcfcf"/><line x1="60" y1="39" x2="34" y2="58" stroke="#cfcfcf"/><line x1="60" y1="39" x2="88" y2="58" stroke="#cfcfcf"/><circle cx="60" cy="39" r="5" fill="#2D5016"/><circle cx="30" cy="20" r="3.4" fill="#9a7b3f"/><circle cx="92" cy="24" r="3.4" fill="#2D5016"/><circle cx="34" cy="58" r="3.4" fill="#2D5016"/><circle cx="88" cy="58" r="3.4" fill="#2D5016"/></svg>',
 "leaf":  '<svg viewBox="0 0 120 78"><path d="M60 12 C 38 30, 38 50, 60 66 C 82 50, 82 30, 60 12 Z" fill="none" stroke="#2D5016" stroke-width="2"/><path d="M60 12 C 60 30, 60 50, 60 66" stroke="#cfcfcf"/><path d="M60 30 L 49 26 M60 38 L 71 34 M60 46 L 49 42" stroke="#cfcfcf"/><circle cx="60" cy="39" r="3" fill="#9a7b3f"/></svg>',
}

# ── highlights (home) ──
HL = """<div class="highlights">
  <a class="hcard" href="research.html">
    <div class="thumb">%(demos)s</div>
    <h3>research</h3>
    <p>数理生物学・進化生態学・植物生態学。個体群ベースシミュレーションで、ササタケ類の個体群動態と進化の相互作用を研究。</p>
  </a>
  <a class="hcard" href="works.html">
    <div class="thumb">%(cards)s</div>
    <h3>works</h3>
    <p>研究・教育デモ集、系統年表、論文カード生成、研究室サイト制作。Web とコードでつくる成果物。</p>
  </a>
  <a class="hcard" href="creative.html">
    <div class="thumb">%(leaf)s</div>
    <h3>creative</h3>
    <p>犬井作（Tsukuru Inui）名義の創作活動。これまでの作品と今後の活動を集約予定。</p>
  </a>
</div>""" % THUMBS

FEATURE = """<div class="feature">
  <div class="cover" aria-hidden="true"><span class="j">Plant<br>Species<br>Biology</span><span class="y">2026</span></div>
  <div>
    <span class="authors">Tachiki, Y., &amp; Umeda, E. (2026).</span>
    <a class="ttl" href="https://doi.org/10.1111/1442-1984.70039">Asymmetric competitions between seedling and clonal ramet promote the evolution of extraordinary long flowering time in monocarpic perennial plants.</a>
    <span class="venue">Plant Species Biology, 41(1), e70039.</span>
    <a class="more" href="https://doi.org/10.1111/1442-1984.70039">read the paper</a>
  </div>
</div>"""

ELSEWHERE = """<h3>elsewhere</h3>
<ul class="affil links">
  <li><a href="https://x.com/EIUmeda">X / @EIUmeda</a></li>
  <li><a href="https://researchmap.jp/eisaku_umeda">researchmap</a></li>
  <li><a href="https://github.com/eUmeda">github / @eUmeda</a></li>
</ul>"""

BIO_BODY = """<div class="bio">
          <p>梅田栄作（Eisaku Umeda）は個体群動態と進化の相互作用を研究しています。専門は数理生物学・進化生態学・植物生態学。東京都立大学 理学研究科 数理計算生物学研究室に所属しています。</p>
        </div>"""

CAREER_SECTION = """<section class="sec"><h2>経歴</h2>
        <ul class="timeline wide">
          <li><span class="when">高校</span><span class="what">福岡県立福岡高校　図書委員会／文芸部 出身</span></li>
          <li><span class="when">2019.4 – 2023.3</span><span class="what">東京都立大学 理学部 生命科学</span></li>
          <li><span class="when">2023.4 – 2025.3</span><span class="what">東京都立大学大学院 理学研究科 生命科学専攻　修士課程</span></li>
          <li><span class="when">2025.4 –</span><span class="what">東京都立大学大学院 理学研究科 生命科学専攻　博士課程</span></li>
        </ul>
      </section>"""

SOCIETIES_SECTION = """<section class="sec"><h2>所属学会</h2>
        <ul class="affil body-list">
          <li>日本生態学会</li>
          <li>個体群生態学会</li>
          <li>数理生物学会</li>
        </ul>
      </section>"""

RECENTLY = """<h3>recently</h3>
      <ul class="timeline">
        <li><span class="when">2026 · paper</span><span class="what">Tachiki &amp; Umeda (2026), <i>Plant Species Biology</i>.</span></li>
        <li><span class="when">2025.4 –</span><span class="what">東京都立大学大学院 博士課程に進学。</span></li>
      </ul>"""

# ───────────────────────────── per-page content ─────────────────────────────
PAGES = {}

PAGES["home"] = dict(
  title="梅田栄作 (Eisaku Umeda) — 数理生物学・進化生態学・植物生態学 | 東京都立大学",
  desc="梅田栄作 (Eisaku Umeda)。東京都立大学 理学研究科 博士課程。数理生物学・進化生態学・植物生態学。個体群ベースシミュレーションでササタケ類の個体群動態と進化を研究。犬井作 (Tsukuru Inui) 名義で創作活動。",
  ld=True,
  main=f"""
      <div class="home-heading">
        <p class="tagline">生命の進化を数理で解く
          <span class="en">Solving the evolution of life through mathematics.</span></p>
      </div>
      <section class="hero bio-hero">
        {PHOTO_FIG}
        {BIO_BODY}
      </section>
      <hr class="div">
      {CAREER_SECTION}
      <hr class="div">
      <section class="sec"><h2>Latest Work</h2>{FEATURE}</section>
      <hr class="div">
      <section class="sec"><h2>Highlights</h2>{HL}</section>
""",
  side=None)

PAGES["research"] = dict(
  title="Research — 梅田栄作 (Eisaku Umeda) | 数理生物学・進化生態学・植物生態学",
  desc="梅田栄作の研究。数理生物学・進化生態学・植物生態学。個体群ベースシミュレーションでササタケ類（タケ・ササ）の個体群動態と進化の相互作用を研究。査読論文一覧。",
  ld=False,
  main="""
      <section class="sec"><h2>Research</h2>
        <p class="lead">研究紹介は現在準備中です。</p>
      </section>
""",
  side=None)

# Works cards
WORK_ITEMS = [
 ("https://eumeda.github.io/Claude-public/", "demos", "研究・教育デモ集",
  "非線形力学系（Strogatz）の分岐・カオス、数理生物モデル、データ可視化のインタラクティブ実装集。"),
 ("https://eumeda.github.io/sire-line-fromEclipse-toSundaySilence/", "sire", "サラブレッド系統年表",
  "Darley Arabian から Equinox までの父系（sire-line）の流れを辿る年表型ビジュアライゼーション。"),
 ("https://github.com/eUmeda/Claude-papercards", "cards", "論文カード生成",
  "論文 PDF から A5 要約カード＋対訳 IMRAD PDF を生成するパイプライン（docling + LLM）。"),
 ("https://mcb.fpark.tmu.ac.jp/", "mcb", "数理計算生物学研究室",
  "立木（Tachiki）グループ公式サイト — Web 制作協力。"),
 ("https://biol.fpark.tmu.ac.jp/plantecol/", "leaf", "植物生態学研究室",
  "東京都立大学 — Web 制作協力。"),
]
WORK_LIST_FUN = "\n".join(
  f'''          <li>
            <a class="t" href="{u}">{title}</a>
            <div class="d">{desc}</div>
          </li>'''
  for (u,t,title,desc) in WORK_ITEMS[:3])

WORK_LIST_WORK = "\n".join(
  f'''          <li>
            <a class="t" href="{u}">{title}</a>
            <div class="d">{desc}</div>
          </li>'''
  for (u,t,title,desc) in WORK_ITEMS[3:])

PAGES["works"] = dict(
  title="Works — 梅田栄作 (Eisaku Umeda) | 研究・教育デモ・可視化・Web制作",
  desc="梅田栄作の成果物。研究・教育デモ集、サラブレッド系統年表、論文カード生成パイプライン、研究室サイト制作。Web とコードでつくる作品。",
  ld=False,
  main=f"""
      <section class="sec"><h2>Works</h2>
        <h3 class="sub-h">Publications</h3>
        {FEATURE}
        <h3 class="sub-h">Made for Fun</h3>
        <ul class="worklist">
{WORK_LIST_FUN}
        </ul>
        <h3 class="sub-h">Made for Work</h3>
        <ul class="worklist">
{WORK_LIST_WORK}
        </ul>
      </section>
""",
  side=None)

PAGES["creative"] = dict(
  title="Creative — 犬井作 (Tsukuru Inui) | 梅田栄作 (Eisaku Umeda)",
  desc="梅田栄作は犬井作（Tsukuru Inui）名義で創作活動をしています。これまでの作品と今後の活動を集約予定。",
  ld=False,
  main=f"""
      <section class="sec"><h2>Creative</h2>
        <p class="lead">梅田栄作は、<b>犬井作（Tsukuru Inui）</b>名義で創作活動をしています。</p>
        <ul class="worklist">
          <li>
            <a class="t" href="/inui.html">犬井作 / Tsukuru Inui</a><span class="wip">工事中</span>
            <div class="d">犬井作名義の創作活動をまとめるページ。これまでの作品と今後の活動を集約予定。</div>
          </li>
        </ul>
        <p class="note">創作のページは現在準備中です。完成までしばらくお待ちください。</p>
      </section>
""",
  side=None)

BOOK_URL = "https://www.stevenstrogatz.com/books/nonlinear-dynamics-and-chaos-with-applications-to-physics-biology-chemistry-and-engineering"
ROUTLEDGE_URL = "https://www.routledge.com/Nonlinear-Dynamics-and-Chaos-With-Applications-to-Physics-Biology-Chemistry-and-Engineering/Strogatz/p/book/9780367026509"
JOYWHY_URL = "https://www.quantamagazine.org/tag/the-joy-of-why/"
JOYWHY_APPLE = "https://podcasts.apple.com/us/podcast/the-joy-of-why/id1608948873"
STROGATZ_URL = "https://www.stevenstrogatz.com/"

# 書影の代替: 本家カバーの複製ではなく、位相図モチーフのオリジナル tribute 図
COVER_ART = """<svg viewBox="0 0 120 120" role="img" aria-label="位相図モチーフ">
  <g stroke="#a9d49a" stroke-width="1.4" fill="none">
    <path d="M60 18 C 26 22, 16 60, 40 84 C 64 108, 104 92, 100 62 C 97 38, 70 34, 62 54 C 56 70, 76 78, 84 66"/>
  </g>
  <path d="M30 96 C 60 110, 100 96, 104 64" fill="none" stroke="#c8a85c" stroke-width="1.3"/>
  <circle cx="73" cy="59" r="3.4" fill="#c8a85c"/>
  <circle cx="60" cy="54" r="3" fill="#fff" stroke="#1b330d" stroke-width="1.2"/>
</svg>"""

PAGES["homage"] = dict(
  title="Homage — Steven Strogatz への敬意 | 梅田栄作 (Eisaku Umeda)",
  desc="このサイトは数学者 Steven Strogatz の個人サイト stevenstrogatz.com へのオマージュ（パロディ）です。著書 Nonlinear Dynamics and Chaos、ポッドキャスト The Joy of Why、本家サイトへのリンク。",
  ld=False,
  main=f"""
      <section class="sec"><h2>An Homage to Steven Strogatz</h2>
        <p class="manifesto">このサイトは数学者 Steven Strogatz の個人サイト stevenstrogatz.com のデザインをできるだけコピーしています。作家・奈須きのこが講談社BOXを愛するあまりそのデザインを完全コピーした同人誌を発行したエピソードがあります。それと同じことをしました。氏の著作の邦訳は、学部生時代の私を大いに刺激しました。私は彼を尊敬しています</p>
        <p class="lead">そして本家はこちら。</p>
        <a class="visit-original" href="{STROGATZ_URL}">stevenstrogatz.com →</a>
      </section>
      <hr class="div">
      <section class="sec"><h2>The Book That Started It</h2>
        <div class="tribute">
          <div class="bookcover" aria-hidden="true">
            <div><div class="bt">Nonlinear Dynamics and Chaos</div><div class="bsub">With Applications to Physics, Biology, Chemistry, and Engineering</div></div>
            <div class="bart">{COVER_ART}</div>
            <div class="bau">Steven H. Strogatz</div>
          </div>
          <div>
            <span class="authors">Steven H. Strogatz</span>
            <a class="ttl" href="{BOOK_URL}">Nonlinear Dynamics and Chaos</a>
            <span class="venue">With Applications to Physics, Biology, Chemistry, and Engineering — 3rd ed., CRC Press (2024)</span>
            <p class="d">非線形力学系とカオスの定番教科書。分岐・アトラクター・カオスを、数式と図と直観で読ませる名著です。</p>
            <a class="more" href="{BOOK_URL}">strogatz.com</a>
            <a class="more" href="{ROUTLEDGE_URL}">publisher</a>
          </div>
        </div>
        <p class="note">※ 上の書影は本家カバーの複製ではなく、敬意をこめて描いた位相図モチーフのオリジナル代替図です。実物のカバー・購入は上記リンクから。</p>
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
  side=None)

PAGES["contact"] = dict(
  title="Contact — 梅田栄作 (Eisaku Umeda) | 東京都立大学",
  desc="梅田栄作 (Eisaku Umeda) への連絡先。X (@EIUmeda)・researchmap・GitHub。東京都立大学 理学研究科 生命科学専攻。",
  ld=False,
  main="""
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
  side=None)

# ───────────────────────────── template ─────────────────────────────
LD_JSON = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "@id": "https://eumeda.github.io/#person",
  "name": "梅田栄作",
  "alternateName": ["Eisaku Umeda", "犬井作", "Tsukuru Inui"],
  "givenName": "栄作", "familyName": "梅田",
  "url": "https://eumeda.github.io/",
  "jobTitle": "博士課程学生 (Doctoral Student)",
  "affiliation": { "@type": "CollegeOrUniversity", "name": "東京都立大学 理学研究科 生命科学専攻", "url": "https://www.tmu.ac.jp/" },
  "alumniOf": { "@type": "CollegeOrUniversity", "name": "東京都立大学", "url": "https://www.tmu.ac.jp/" },
  "knowsAbout": ["Mathematical Biology","Evolutionary Ecology","Plant Ecology","Population Dynamics","数理生物学","進化生態学","植物生態学","個体群動態"],
  "memberOf": [
    { "@type": "Organization", "name": "日本生態学会" },
    { "@type": "Organization", "name": "個体群生態学会" },
    { "@type": "Organization", "name": "日本数理生物学会" }
  ],
  "sameAs": ["https://x.com/EIUmeda","https://researchmap.jp/eisaku_umeda","https://github.com/eUmeda"]
}
</script>"""

def nav_html(active):
    items = "\n".join(
        f'        <li><a href="{href}"{" class=\"active\"" if k==active else ""}>{label}</a></li>'
        for (k,label,href) in NAV)
    return f"""      <nav class="vnav" aria-label="Site">
      <ul>
{items}
      </ul>
      </nav>"""

def rail_html(active):
    recently = RECENTLY if active == "home" else ""
    return f"""    <aside class="rail">
{nav_html(active)}
      {recently}
      {ELSEWHERE}
    </aside>"""

def foot_nav():
    return "\n".join(f'      <li><a href="{href}">{label}</a></li>' for (k,label,href) in NAV)

def render(active):
    p = PAGES[active]
    ld = ("\n" + LD_JSON) if p.get("ld") else ""
    cmp_links = ('  <a href="/_version1">v1 · Forge</a>\n'
                 '  <a href="/_version2">v2 · Reading</a>\n'
                 '  <a href="/_version3/" class="here">v3 · Strogatz</a>')
    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex,follow"><!-- TEMP 比較ページ -->
<title>{p['title']}</title>
<meta name="description" content="{p['desc']}">
<meta name="author" content="梅田栄作 / Eisaku Umeda">
<link rel="canonical" href="https://eumeda.github.io/">
<meta name="theme-color" content="#dedede">
<meta property="og:type" content="profile">
<meta property="og:title" content="{p['title']}">
<meta property="og:description" content="{p['desc']}">
<meta property="og:url" content="https://eumeda.github.io/">
<meta property="og:locale" content="ja_JP">
<meta property="og:site_name" content="Eisaku Umeda">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{p['title']}">
<meta name="twitter:description" content="{p['desc']}">
<meta name="twitter:site" content="@EIUmeda">
<link rel="icon" href="{FAVICON}">{ld}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=PT+Serif:ital,wght@0,400;0,700;1,400;1,700&family=Mulish:ital,wght@0,200;0,300;0,400;0,600;0,700;1,400&family=Noto+Sans+JP:wght@400;500;700&family=Noto+Serif+JP:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>

<div class="cmpbar">
  <b>compare</b>
{cmp_links}
  <span class="sp"></span>
  <a href="/">現行 live</a>
</div>

<div class="banner">
  <div class="banner-inner">
    <div class="site-title"><a href="index.html">Eisaku&nbsp;Umeda</a></div>
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
{p['main']}
    </main>
{rail_html(active)}
  </div>
</div>

<footer>
  <div class="foot-inner">
    <ul class="foot-nav">
{foot_nav()}
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

for stale in ("about" + ".html",):
    stale_path = os.path.join(OUT, stale)
    if os.path.exists(stale_path):
        os.remove(stale_path)

for (k,_,href) in NAV:
    if k not in PAGES:
        continue
    with open(os.path.join(OUT, href), "w", encoding="utf-8") as f:
        f.write(render(k))
    print("wrote", href)
print("done")
