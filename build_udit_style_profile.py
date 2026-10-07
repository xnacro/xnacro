import os
import io
import base64
import xml.etree.ElementTree as ET
from PIL import Image

def get_base64_png(path, max_width=750):
    im = Image.open(path)
    if im.width > max_width:
        ratio = max_width / im.width
        new_size = (max_width, int(im.height * ratio))
        im = im.resize(new_size, Image.Resampling.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, format='PNG', optimize=True)
    return base64.b64encode(buf.getvalue()).decode('ascii')

# =========================================================================
# COMMON SVG DEFS & BRAND ICONS (100% Self-Contained, No External Runtime)
# =========================================================================
COMMON_STYLE = '''
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@600;700;800;900&amp;family=Plus+Jakarta+Sans:wght@400;500;600;700;800&amp;display=swap');
    .font-display { font-family: 'Outfit', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
    .font-sans { font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
'''

TECH_ICONS_DEFS = '''
    <!-- Technology Brand SVG Marks (ViewBox 0 0 16 16) -->
    <g id="icon-python" viewBox="0 0 16 16">
      <path d="M7.9 1C4.4 1 4.2 2.5 4.2 2.5l.01 1.6h3.8v.5H3.1S1.5 4.4 1.5 7.9s1.4 3.5 1.4 3.5h.9v-1.2s-.04-1.4 1.4-1.4h3.7s1.3.02 1.3-1.3V2.4S10.3 1 7.9 1zm-1.1 1.1a.6.6 0 1 1 0 1.2.6.6 0 0 1 0-1.2z" fill="#387EB8"/>
      <path d="M8.1 15c3.5 0 3.7-1.5 3.7-1.5l-.01-1.6H8v-.5h4.9s1.6-.2 1.6-3.7-1.4-3.5-1.4-3.5h-.9v1.2s.04 1.4-1.4 1.4H7.1s-1.3-.02-1.3 1.3v5.1s-.2 1.4 2.3 1.4zm1.1-1.1a.6.6 0 1 1 0-1.2.6.6 0 0 1 0 1.2z" fill="#FFE052"/>
    </g>
    <g id="icon-pytorch" viewBox="0 0 16 16">
      <path d="M8.8 2.2a5.5 5.5 0 0 0-3.9 9.4l1.5-1.5a3.4 3.4 0 0 1 2.4-5.8V2.2z" fill="#EE4C2C"/>
      <circle cx="10.5" cy="3" r="1.2" fill="#EE4C2C"/>
    </g>
    <g id="icon-scikit" viewBox="0 0 16 16">
      <circle cx="4.5" cy="4.5" r="2.8" fill="#F89939"/>
      <circle cx="11.5" cy="5.5" r="2.5" fill="#3499CD"/>
      <circle cx="8" cy="11.5" r="2.2" fill="#F89939"/>
      <line x1="4.5" y1="4.5" x2="11.5" y2="5.5" stroke="#94A3B8" stroke-width="1.2"/>
      <line x1="4.5" y1="4.5" x2="8" y2="11.5" stroke="#94A3B8" stroke-width="1.2"/>
      <line x1="11.5" y1="5.5" x2="8" y2="11.5" stroke="#94A3B8" stroke-width="1.2"/>
    </g>
    <g id="icon-tensorflow" viewBox="0 0 16 16">
      <path d="M8 1.5l-6 3.4v2.6l6-3.4v10.5l3.5-2V7.1l3.5 2V6.5L8 1.5z" fill="#FF6F00"/>
      <path d="M8 4.1L4.5 6.1v2.6l3.5-2v7.9l-2.4 1.4V10L3.5 8.7v5.8l4.5 2.6 4.5-2.6V8.7l-2.1 1.3v4.2l-2.4-1.4V4.1z" fill="#FFA800"/>
    </g>
    <g id="icon-opencv" viewBox="0 0 16 16">
      <circle cx="8" cy="4" r="2.5" fill="#EA3829"/>
      <circle cx="4" cy="11" r="2.5" fill="#4B9626"/>
      <circle cx="12" cy="11" r="2.5" fill="#0E58A8"/>
    </g>
    <g id="icon-numpy" viewBox="0 0 16 16">
      <rect x="2" y="2" width="12" height="12" rx="2.5" fill="#4DABCF"/>
      <path d="M4.5 11.5V4.5l5.5 7V4.5" stroke="#013243" stroke-width="1.4" fill="none"/>
    </g>
    <g id="icon-pandas" viewBox="0 0 16 16">
      <rect x="3" y="2.5" width="2.2" height="11" rx="0.5" fill="#130654"/>
      <rect x="6.9" y="5" width="2.2" height="8.5" rx="0.5" fill="#FFD43B"/>
      <rect x="10.8" y="3.5" width="2.2" height="7.5" rx="0.5" fill="#E70488"/>
    </g>
    <g id="icon-transformers" viewBox="0 0 16 16">
      <circle cx="8" cy="8" r="6" fill="#FFD21E"/>
      <circle cx="5.8" cy="6.8" r="1.3" fill="#1E293B"/>
      <circle cx="10.2" cy="6.8" r="1.3" fill="#1E293B"/>
      <path d="M5.5 10.2c1.2 1.2 3.8 1.2 5 0" stroke="#1E293B" stroke-width="1.3" stroke-linecap="round" fill="none"/>
    </g>
    <g id="icon-langchain" viewBox="0 0 16 16">
      <rect x="2" y="5" width="4.5" height="4.5" rx="1.5" fill="#00A67E"/>
      <rect x="9.5" y="5" width="4.5" height="4.5" rx="1.5" fill="#1C3C3C"/>
      <line x1="6.5" y1="7.25" x2="9.5" y2="7.25" stroke="#00A67E" stroke-width="2"/>
    </g>
    <g id="icon-fastapi" viewBox="0 0 16 16">
      <circle cx="8" cy="8" r="7" fill="#05998B"/>
      <path d="M8.5 2.8L4.5 8.5h3.5l-.8 4.7 4.8-5.7H8z" fill="#FFFFFF"/>
    </g>
    <g id="icon-typescript" viewBox="0 0 16 16">
      <rect x="1" y="1" width="14" height="14" rx="2.5" fill="#3178C6"/>
      <text x="3.5" y="11" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" font-weight="900" fill="#FFF">TS</text>
    </g>
    <g id="icon-javascript" viewBox="0 0 16 16">
      <rect x="1" y="1" width="14" height="14" rx="2.5" fill="#F7DF1E"/>
      <text x="3.5" y="11" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" font-weight="900" fill="#000">JS</text>
    </g>
    <g id="icon-sql" viewBox="0 0 16 16">
      <ellipse cx="8" cy="4" rx="6" ry="2.2" fill="#336791"/>
      <path d="M2 4v4c0 1.2 2.7 2.2 6 2.2s6-1 6-2.2V4" fill="none" stroke="#336791" stroke-width="1.4"/>
      <path d="M2 8v4c0 1.2 2.7 2.2 6 2.2s6-1 6-2.2V8" fill="none" stroke="#336791" stroke-width="1.4"/>
    </g>
    <g id="icon-cpp" viewBox="0 0 16 16">
      <path d="M8 1.2l6 3.5v7l-6 3.5-6-3.5v-7L8 1.2z" fill="#00599C"/>
      <text x="4.2" y="10.8" font-family="'Plus Jakarta Sans', sans-serif" font-size="7" font-weight="900" fill="#FFF">C+</text>
    </g>
    <g id="icon-java" viewBox="0 0 16 16">
      <path d="M5.2 12.2c2.2.4 5.2.4 6.8-.5M4.5 13.8c2.8.6 6.2.6 8.5-.5M6.8 9.8c1.7.3 3.9.3 5-.4" stroke="#EA2D2E" stroke-width="1.3" stroke-linecap="round" fill="none"/>
      <path d="M9.2 2.5c.6 1.2-1.2 2.3-1.2 3.5s1.7 1.7 1.2 2.8" stroke="#5382A1" stroke-width="1.3" stroke-linecap="round" fill="none"/>
    </g>
    <g id="icon-react" viewBox="0 0 16 16">
      <ellipse cx="8" cy="8" rx="7" ry="2.6" fill="none" stroke="#61DAFB" stroke-width="1.2"/>
      <ellipse cx="8" cy="8" rx="7" ry="2.6" fill="none" stroke="#61DAFB" stroke-width="1.2" transform="rotate(60 8 8)"/>
      <ellipse cx="8" cy="8" rx="7" ry="2.6" fill="none" stroke="#61DAFB" stroke-width="1.2" transform="rotate(120 8 8)"/>
      <circle cx="8" cy="8" r="1.5" fill="#61DAFB"/>
    </g>
    <g id="icon-nextjs" viewBox="0 0 16 16">
      <circle cx="8" cy="8" r="7" fill="#000" stroke="#334155" stroke-width="0.8"/>
      <path d="M5 5v6M11 5v6M5 5l6 6" stroke="#FFF" stroke-width="1.3"/>
    </g>
    <g id="icon-maplibre" viewBox="0 0 16 16">
      <path d="M2.5 4l3.8-1.8L9.8 4 13.5 2.2V12l-3.7 1.8L6.3 12 2.5 13.8V4z" fill="#396BFE" opacity="0.9"/>
      <path d="M6.3 2.2V12M9.8 4v9.8" stroke="#FFFFFF" stroke-width="1"/>
    </g>
    <g id="icon-leaflet" viewBox="0 0 16 16">
      <path d="M13 2.5C8.5 2.5 3.5 7 3.5 11.5c0 1.8.6 2.5 1.8 2.5 4.5 0 7.7-6.5 7.7-11.5z" fill="#199900"/>
      <path d="M5.2 13.8c1.8-3 4-6 7.8-11.3" stroke="#FFFFFF" stroke-width="1" stroke-linecap="round" fill="none"/>
    </g>
    <g id="icon-tailwind" viewBox="0 0 16 16">
      <path d="M4 6.2c.9-1.8 2.5-2.2 4-1.2 1.4.9 2 2.4 3.1 2.6 1.2.3 2.3-.4 3.2-1.4-.9 1.8-2.5 2.2-4 1.2-1.4-.9-2-2.4-3.1-2.6-1.2-.3-2.3.4-3.2 1.4zm-2.3 4.6c.9-1.8 2.5-2.2 4-1.2 1.4.9 2 2.4 3.1 2.6 1.2.3 2.3-.4 3.2-1.4-.9 1.8-2.5 2.2-4 1.2-1.4-.9-2-2.4-3.1-2.6-1.2-.3-2.3.4-3.2 1.4z" fill="#06B6D4"/>
    </g>
    <g id="icon-nodejs" viewBox="0 0 16 16">
      <path d="M8 1.2l6 3.5v7l-6 3.5-6-3.5v-7L8 1.2z" fill="#339933"/>
      <text x="5" y="10.8" font-family="'Plus Jakarta Sans', sans-serif" font-size="7.5" font-weight="900" fill="#FFF">N</text>
    </g>
    <g id="icon-postgres" viewBox="0 0 16 16">
      <path d="M8 2a6 6 0 0 0-6 6c0 3.3 2.7 6 6 6s6-2.7 6-6a6 6 0 0 0-6-6zm-1.2 9.5c-.7 0-1.2-.5-1.2-1.2s.5-1.2 1.2-1.2 1.2.5 1.2 1.2-.5 1.2-1.2 1.2zm2.4-3.6H5.6V6.6h3.6v1.3z" fill="#4169E1"/>
    </g>
    <g id="icon-redis" viewBox="0 0 16 16">
      <path d="M8 2.2L2.5 5.5l5.5 3.3 5.5-3.3L8 2.2zm-5.5 5.5l5.5 3.3 5.5-3.3v2.2L8 13.2l-5.5-3.3V7.7zm0 4.4l5.5 3.3 5.5-3.3v2.2L8 17.6l-5.5-3.3v-2.2z" fill="#DC382D"/>
    </g>
    <g id="icon-websockets" viewBox="0 0 16 16">
      <circle cx="4.5" cy="8" r="3" fill="#2F86FF"/>
      <circle cx="11.5" cy="8" r="3" fill="#FF3652"/>
      <path d="M6 6.5l4 3M10 6.5l-4 3" stroke="#FFFFFF" stroke-width="1.1"/>
    </g>
'''

def build_all():
    os.makedirs('assets', exist_ok=True)
    print("Encoding character assets...")
    mine_b64 = get_base64_png('assets/mine.png', 680)
    id_b64 = get_base64_png('assets/id.png', 720)

    # =========================================================================
    # 1. assets/hero.svg — Clean Identity & Positioning (No Resume Chips, Exactly 2 Fonts)
    # =========================================================================
    hero_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 940 430" width="100%" height="100%">
  <defs>
    <style>{COMMON_STYLE}
      @keyframes heroPulseDot {{
        0%, 100% {{ opacity: 1; transform: scale(1); }}
        50%      {{ opacity: 0.35; transform: scale(0.85); }}
      }}
      .hero-pulse {{
        animation: heroPulseDot 2.2s ease-in-out infinite;
        transform-origin: 38px 30px;
      }}
    </style>
    <linearGradient id="hero-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070B16"/>
      <stop offset="50%" stop-color="#0B1325"/>
      <stop offset="100%" stop-color="#070B16"/>
    </linearGradient>
    <linearGradient id="hero-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2F86FF" stop-opacity="0.85"/>
      <stop offset="50%" stop-color="#2F86FF" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#FF3652" stop-opacity="0.6"/>
    </linearGradient>
    <linearGradient id="hero-title-blue" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#2F86FF"/>
      <stop offset="60%" stop-color="#60A5FA"/>
      <stop offset="100%" stop-color="#93C5FD"/>
    </linearGradient>
    <radialGradient id="hero-glow" cx="80%" cy="50%" r="55%">
      <stop offset="0%" stop-color="#2F86FF" stop-opacity="0.2"/>
      <stop offset="50%" stop-color="#2F86FF" stop-opacity="0.04"/>
      <stop offset="100%" stop-color="#070B16" stop-opacity="0"/>
    </radialGradient>
    <pattern id="hero-dots" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1.1" fill="#1C2B49" opacity="0.45"/>
    </pattern>
    <clipPath id="hero-portrait-clip">
      <rect x="540" y="24" width="365" height="382" rx="16"/>
    </clipPath>
  </defs>

  <!-- Container Box -->
  <rect x="0" y="0" width="940" height="430" rx="18" fill="url(#hero-bg)" stroke="url(#hero-border)" stroke-width="1.6"/>
  <rect x="0" y="0" width="940" height="430" rx="18" fill="url(#hero-dots)"/>
  <rect x="460" y="0" width="480" height="430" rx="18" fill="url(#hero-glow)"/>

  <!-- Top Metadata Bar -->
  <g transform="translate(36, 28)">
    <circle cx="6" cy="6" r="4.5" fill="#2F86FF" class="hero-pulse"/>
    <text x="18" y="10" class="font-sans" font-size="11" font-weight="700" letter-spacing="1.5" fill="#F0F6FC">PRINCE TIWARI</text>
    <text x="868" y="10" text-anchor="end" class="font-sans" font-size="11" font-weight="600" letter-spacing="1" fill="#8B96A8">MUZAFFARPUR, BIHAR, INDIA</text>
  </g>

  <!-- Left Content Column -->
  <g transform="translate(36, 75)">
    <!-- Eyebrow Subheading -->
    <text x="0" y="4" class="font-sans" font-size="11.5" font-weight="700" letter-spacing="2" fill="#8B96A8">SOFTWARE ENGINEER • BUILDER</text>

    <!-- Greeting & Large Name Display (Display Font) -->
    <text x="0" y="38" class="font-sans" font-size="16" font-weight="600" fill="#8B96A8">HI, I'M</text>
    <text x="0" y="96" class="font-display" font-size="62" font-weight="900" letter-spacing="-1.5" fill="#FFFFFF">PRINCE</text>
    <text x="0" y="156" class="font-display" font-size="62" font-weight="900" letter-spacing="-1.5" fill="url(#hero-title-blue)">TIWARI</text>

    <!-- Crimson Slash Bars -->
    <g transform="translate(255, 68)">
      <rect x="0" y="0" width="4" height="24" rx="2" fill="#FF3652" transform="skewX(-20)"/>
      <rect x="9" y="0" width="4" height="24" rx="2" fill="#FF3652" transform="skewX(-20)"/>
      <rect x="18" y="0" width="4" height="24" rx="2" fill="#FF3652" transform="skewX(-20)"/>
    </g>

    <!-- Short, Confident Positioning Statement (1-2 lines) -->
    <text x="0" y="202" class="font-sans" font-size="15" font-weight="500" fill="#CBD5E1">
      <tspan x="0" dy="0">I build AI-powered products, full-stack systems,</tspan>
      <tspan x="0" dy="24">&amp; real-world spatial intelligence.</tspan>
    </text>

    <!-- Compact Truthful Metadata Line (Whitespace instead of chip clutter) -->
    <g transform="translate(0, 275)">
      <text x="0" y="14" class="font-sans" font-size="12" font-weight="700" letter-spacing="1.2" fill="#60A5FA">
        INDIA  •  B.TECH CSE (AI &amp; ML)  •  OPEN TO COLLABORATE
      </text>
    </g>
  </g>

  <!-- Right Portrait Column with Inlined Approved mine.png -->
  <g>
    <rect x="540" y="24" width="365" height="382" rx="16" fill="#0C1527" stroke="#1C2D4A" stroke-width="1.2"/>
    <g clip-path="url(#hero-portrait-clip)">
      <image href="data:image/png;base64,{mine_b64}" xlink:href="data:image/png;base64,{mine_b64}" x="535" y="12" width="375" height="402" preserveAspectRatio="xMidYMid meet"/>
    </g>
  </g>
</svg>'''

    # =========================================================================
    # 2. assets/achievements.svg — 02 / VERIFIED RECOGNITION (Near Top!)
    # =========================================================================
    achievements_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 240" width="100%" height="100%">
  <defs>
    <style>{COMMON_STYLE}</style>
    <linearGradient id="ach-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2F86FF" stop-opacity="0.6"/>
      <stop offset="50%" stop-color="#FF3652" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#2F86FF" stop-opacity="0.6"/>
    </linearGradient>
    <pattern id="ach-dots" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#1C2B49" opacity="0.4"/>
    </pattern>
  </defs>

  <rect x="0" y="0" width="940" height="240" rx="16" fill="#070B16" stroke="url(#ach-border)" stroke-width="1.3"/>
  <rect x="0" y="0" width="940" height="240" rx="16" fill="url(#ach-dots)"/>

  <!-- Top Section Tracker -->
  <g transform="translate(32, 22)">
    <text x="0" y="10" class="font-sans" font-size="10.5" font-weight="700" letter-spacing="2" fill="#2F86FF">02 // VERIFIED RECOGNITION</text>
    <text x="0" y="32" class="font-display" font-size="20" font-weight="900" fill="#FFFFFF">PROVEN IN THE REAL WORLD<tspan fill="#FF3652">.</tspan></text>
    <text x="400" y="30" class="font-sans" font-size="12" fill="#8B96A8">National hackathon wins, engineering challenges &amp; active software systems.</text>
  </g>

  <!-- 4 Refined Credential Cards (Year • Achievement • Organization • Result) -->
  <g transform="translate(32, 70)">
    <!-- Card 1: Cognithon IIIT Bhagalpur -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="208" height="142" rx="10" fill="#0A1224" stroke="#2F86FF" stroke-width="1.2"/>
      <rect x="14" y="14" width="60" height="18" rx="4" fill="#12203A"/>
      <text x="20" y="27" class="font-display" font-size="10" font-weight="800" letter-spacing="1" fill="#60A5FA">2026</text>
      
      <text x="14" y="56" class="font-display" font-size="17" font-weight="900" fill="#FFFFFF">COGNITHON</text>
      <text x="14" y="72" class="font-sans" font-size="11" font-weight="600" fill="#8B96A8">IIIT Bhagalpur</text>

      <rect x="14" y="86" width="180" height="1" fill="#1A2D4E"/>
      
      <text x="14" y="112" class="font-display" font-size="18" font-weight="900" fill="#60A5FA">2ND PRIZE</text>
      <text x="14" y="128" class="font-sans" font-size="10" fill="#8B96A8">National Hackathon</text>
    </g>

    <!-- Card 2: India Innovates 2026 -->
    <g transform="translate(222, 0)">
      <rect x="0" y="0" width="208" height="142" rx="10" fill="#0A1224" stroke="#FF3652" stroke-width="1.2"/>
      <rect x="14" y="14" width="60" height="18" rx="4" fill="#2A1422"/>
      <text x="20" y="27" class="font-display" font-size="10" font-weight="800" letter-spacing="1" fill="#FF8A9A">2026</text>
      
      <text x="14" y="56" class="font-display" font-size="17" font-weight="900" fill="#FFFFFF">INDIA INNOVATES</text>
      <text x="14" y="72" class="font-sans" font-size="11" font-weight="600" fill="#8B96A8">Civic Innovation</text>

      <rect x="14" y="86" width="180" height="1" fill="#3D1A2A"/>
      
      <text x="14" y="112" class="font-display" font-size="16" font-weight="900" fill="#FF3652">NATIONAL FINALIST</text>
      <text x="14" y="128" class="font-sans" font-size="10" fill="#8B96A8">Disaster Relief Tech</text>
    </g>

    <!-- Card 3: Flipkart GRiD 2026 -->
    <g transform="translate(444, 0)">
      <rect x="0" y="0" width="208" height="142" rx="10" fill="#0A1224" stroke="#2F86FF" stroke-width="1.2"/>
      <rect x="14" y="14" width="60" height="18" rx="4" fill="#12203A"/>
      <text x="20" y="27" class="font-display" font-size="10" font-weight="800" letter-spacing="1" fill="#60A5FA">2026</text>
      
      <text x="14" y="56" class="font-display" font-size="17" font-weight="900" fill="#FFFFFF">FLIPKART GRiD</text>
      <text x="14" y="72" class="font-sans" font-size="11" font-weight="600" fill="#8B96A8">Engineering Track</text>

      <rect x="14" y="86" width="180" height="1" fill="#1A2D4E"/>
      
      <text x="14" y="112" class="font-display" font-size="16" font-weight="900" fill="#60A5FA">SEMI-FINALIST</text>
      <text x="14" y="128" class="font-sans" font-size="10" fill="#8B96A8">Campus Tech Flagship</text>
    </g>

    <!-- Card 4: Surakshaai.org Platform -->
    <g transform="translate(666, 0)">
      <rect x="0" y="0" width="208" height="142" rx="10" fill="#0A1224" stroke="#2F86FF" stroke-width="1.2"/>
      <rect x="14" y="14" width="60" height="18" rx="4" fill="#102544"/>
      <text x="20" y="27" class="font-display" font-size="10" font-weight="800" letter-spacing="1" fill="#93C5FD">2026</text>
      
      <text x="14" y="56" class="font-display" font-size="17" font-weight="900" fill="#FFFFFF">SURAKSHAAI</text>
      <text x="14" y="72" class="font-sans" font-size="11" font-weight="600" fill="#8B96A8">surakshaai.org</text>

      <rect x="14" y="86" width="180" height="1" fill="#1E3354"/>
      
      <text x="14" y="112" class="font-display" font-size="15" font-weight="900" fill="#60A5FA">FOUNDER &amp; ARCHITECT</text>
      <text x="14" y="128" class="font-sans" font-size="10" fill="#8B96A8">Spatial AI Platform</text>
    </g>
  </g>
</svg>'''

    # =========================================================================
    # 3. assets/current-build.svg — 03 / NOW BUILDING
    # =========================================================================
    current_build_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 190" width="100%" height="100%">
  <defs>
    <style>{COMMON_STYLE}</style>
    <linearGradient id="cb-border" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#2F86FF" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="#2F86FF" stop-opacity="0.15"/>
    </linearGradient>
    <pattern id="cb-grid" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#16223D" stroke-width="0.75" stroke-opacity="0.45"/>
    </pattern>
  </defs>

  <rect x="0" y="0" width="940" height="190" rx="14" fill="#070B16" stroke="url(#cb-border)" stroke-width="1.2"/>
  <rect x="0" y="0" width="940" height="190" rx="14" fill="url(#cb-grid)"/>

  <!-- Top bar -->
  <g transform="translate(30, 20)">
    <circle cx="5" cy="5" r="4" fill="#2F86FF"/>
    <text x="16" y="9" class="font-sans" font-size="11" font-weight="700" letter-spacing="1.8" fill="#2F86FF">03 // NOW BUILDING</text>
  </g>

  <!-- Left Column Card: SurakshaAI Focus -->
  <g transform="translate(30, 48)">
    <rect x="0" y="0" width="425" height="122" rx="10" fill="#0A1122" stroke="#1F2F4F" stroke-width="1"/>
    <text x="20" y="24" class="font-sans" font-size="10" font-weight="700" letter-spacing="1" fill="#8B96A8">CURRENT PRODUCT FOCUS</text>
    <text x="20" y="48" class="font-display" font-size="18" font-weight="900" fill="#FFFFFF">SurakshaAI <tspan fill="#60A5FA" font-size="13" font-weight="700">• surakshaai.org</tspan></text>
    <text x="20" y="70" class="font-sans" font-size="12" fill="#8B96A8">Turning real-world risk telemetry and street safety datasets into</text>
    <text x="20" y="88" class="font-sans" font-size="12" fill="#8B96A8">predictive intelligence through the Dynamic Safety Index (DSI).</text>
    <g transform="translate(20, 96)">
      <text x="0" y="12" class="font-sans" font-size="10" font-weight="700" fill="#60A5FA">SPATIAL AI  •  MICROSERVICES  •  GEOGRAPHIC RISK</text>
    </g>
  </g>

  <!-- Right Column Card: Current Technical Sprint -->
  <g transform="translate(475, 48)">
    <rect x="0" y="0" width="435" height="122" rx="10" fill="#0A1122" stroke="#1F2F4F" stroke-width="1"/>
    <text x="20" y="24" class="font-sans" font-size="10" font-weight="700" letter-spacing="1" fill="#8B96A8">ACTIVE SPRINT</text>
    
    <text x="20" y="50" class="font-sans" font-size="12.5" font-weight="700" fill="#F5F7FA">Spatial AI Models:</text>
    <text x="140" y="50" class="font-sans" font-size="12" fill="#8B96A8">Dynamic Safety Index &amp; multi-tier risk heatmaps</text>

    <text x="20" y="74" class="font-sans" font-size="12.5" font-weight="700" fill="#F5F7FA">Architecture:</text>
    <text x="140" y="74" class="font-sans" font-size="12" fill="#8B96A8">Node.js orchestrator + decoupled FastAPI ML inference</text>

    <text x="20" y="98" class="font-sans" font-size="12.5" font-weight="700" fill="#F5F7FA">Focus:</text>
    <text x="140" y="98" class="font-sans" font-size="12" fill="#60A5FA">Product engineering &amp; high-concurrency systems</text>
  </g>
</svg>'''

    # =========================================================================
    # 4. assets/flagship.svg — 04 // FLAGSHIP SYSTEM (SurakshaAI Product Visual)
    # =========================================================================
    flagship_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 370" width="100%" height="100%">
  <defs>
    <style>{COMMON_STYLE}</style>
    <linearGradient id="fl-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2F86FF" stop-opacity="0.85"/>
      <stop offset="50%" stop-color="#0A1224" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#FF3652" stop-opacity="0.7"/>
    </linearGradient>
    <pattern id="fl-grid" width="22" height="22" patternUnits="userSpaceOnUse">
      <path d="M 22 0 L 0 0 0 22" fill="none" stroke="#162544" stroke-width="0.8" stroke-opacity="0.6"/>
    </pattern>
  </defs>

  <rect x="0" y="0" width="940" height="370" rx="16" fill="#070B16" stroke="url(#fl-border)" stroke-width="1.5"/>
  <rect x="0" y="0" width="940" height="370" rx="16" fill="url(#fl-grid)"/>

  <!-- Top Badges -->
  <g transform="translate(32, 24)">
    <rect x="0" y="0" width="170" height="22" rx="4" fill="#14284D" stroke="#2F86FF" stroke-width="0.8"/>
    <text x="12" y="15" class="font-sans" font-size="10" font-weight="700" fill="#60A5FA">04 // FLAGSHIP SYSTEM</text>

    <rect x="182" y="0" width="160" height="22" rx="4" fill="#2B1424" stroke="#FF3652" stroke-width="0.8"/>
    <text x="192" y="15" class="font-sans" font-size="10" font-weight="700" fill="#FF8A9A">SPATIAL AI PLATFORM</text>
  </g>

  <!-- Title & Narrative -->
  <g transform="translate(32, 68)">
    <text x="0" y="24" class="font-display" font-size="30" font-weight="900" fill="#FFFFFF">SURAKSHAAI</text>
    <text x="200" y="22" class="font-sans" font-size="15" font-weight="600" fill="#8B96A8">• Real-Time Geospatial Safety Intelligence Platform</text>
    
    <text x="0" y="52" class="font-sans" font-size="13" fill="#CBD5E1">
      AI-driven geospatial analytics computing a <tspan fill="#2F86FF" font-weight="700">Dynamic Safety Index (DSI)</tspan> to replace static crime tables
    </text>
    <text x="0" y="70" class="font-sans" font-size="13" fill="#CBD5E1">
      with predictive risk forecasts and hazard-aware mobility guidance across real-world streets.
    </text>
  </g>

  <!-- 3 Spacious Core Capabilities (No dashboard overlap!) -->
  <g transform="translate(32, 162)">
    <!-- Capability 1 -->
    <rect x="0" y="0" width="276" height="122" rx="8" fill="#0A1122" stroke="#1F2F4F" stroke-width="1"/>
    <text x="16" y="26" class="font-display" font-size="14" font-weight="800" fill="#F5F7FA">Dynamic Safety Index</text>
    <text x="16" y="48" class="font-sans" font-size="11.5" fill="#8B96A8">Algorithmic spatial risk scoring</text>
    <text x="16" y="64" class="font-sans" font-size="11.5" fill="#8B96A8">evaluated across geographic micro-grids.</text>
    <rect x="16" y="86" width="130" height="20" rx="3" fill="#102038"/>
    <text x="24" y="100" class="font-sans" font-size="9.5" font-weight="700" fill="#60A5FA">MapLibre GL • Leaflet</text>

    <!-- Capability 2 -->
    <rect x="300" y="0" width="276" height="122" rx="8" fill="#0A1122" stroke="#1F2F4F" stroke-width="1"/>
    <text x="16" y="26" class="font-display" font-size="14" font-weight="800" fill="#F5F7FA">Predictive ML Inference</text>
    <text x="16" y="48" class="font-sans" font-size="11.5" fill="#8B96A8">Decoupled FastAPI microservice</text>
    <text x="16" y="64" class="font-sans" font-size="11.5" fill="#8B96A8">forecasting real-time incident likelihood.</text>
    <rect x="16" y="86" width="140" height="20" rx="3" fill="#102038"/>
    <text x="24" y="100" class="font-sans" font-size="9.5" font-weight="700" fill="#60A5FA">FastAPI • Scikit-learn</text>

    <!-- Capability 3 -->
    <rect x="600" y="0" width="276" height="122" rx="8" fill="#0A1122" stroke="#1F2F4F" stroke-width="1"/>
    <text x="16" y="26" class="font-display" font-size="14" font-weight="800" fill="#F5F7FA">Safe-Path Guidance</text>
    <text x="16" y="48" class="font-sans" font-size="11.5" fill="#8B96A8">Lowest-risk waypoint routing</text>
    <text x="16" y="64" class="font-sans" font-size="11.5" fill="#8B96A8">with real-time guardian telemetry sessions.</text>
    <rect x="16" y="86" width="140" height="20" rx="3" fill="#182A45"/>
    <text x="24" y="100" class="font-sans" font-size="9.5" font-weight="700" fill="#93C5FD">Node.js • PostGIS • Redis</text>
  </g>

  <!-- Bottom Architecture Strip -->
  <g transform="translate(32, 305)">
    <rect x="0" y="0" width="876" height="42" rx="6" fill="#080E1C" stroke="#162544" stroke-width="1"/>
    <text x="16" y="25" class="font-sans" font-size="11" font-weight="700" fill="#8B96A8">STACK: <tspan fill="#F5F7FA">Python • FastAPI • Scikit-learn • MapLibre GL • PostgreSQL / PostGIS • Redis</tspan></text>
    <text x="760" y="25" class="font-sans" font-size="11" font-weight="800" fill="#2F86FF">VIEW PROJECT →</text>
  </g>
</svg>'''

    # =========================================================================
    # 5. assets/stack.svg — 05 // THE ENGINE ROOM (Real Planetary Orbits & Full Stack)
    # =========================================================================
    stack_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 520" width="100%" height="100%">
  <defs>
    <style>{COMMON_STYLE}
      @keyframes orbitPulse {{
        0%, 100% {{ transform: scale(1); filter: drop-shadow(0 0 6px rgba(47, 134, 255, 0.6)); }}
        50%      {{ transform: scale(1.05); filter: drop-shadow(0 0 14px rgba(47, 134, 255, 0.9)); }}
      }}
      .core-sun {{
        animation: orbitPulse 3.5s ease-in-out infinite;
        transform-origin: 205px 275px;
      }}
    </style>
    {TECH_ICONS_DEFS}
    <linearGradient id="stk-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070B16"/>
      <stop offset="60%" stop-color="#091225"/>
      <stop offset="100%" stop-color="#070B16"/>
    </linearGradient>
    <linearGradient id="stk-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2F86FF" stop-opacity="0.85"/>
      <stop offset="50%" stop-color="#2F86FF" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#FF3652" stop-opacity="0.6"/>
    </linearGradient>
    <radialGradient id="sun-glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#2F86FF" stop-opacity="0.95"/>
      <stop offset="35%" stop-color="#2F86FF" stop-opacity="0.4"/>
      <stop offset="70%" stop-color="#60A5FA" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#070B16" stop-opacity="0"/>
    </radialGradient>
    <pattern id="stk-dots" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1.1" fill="#1C2B49" opacity="0.45"/>
    </pattern>
  </defs>

  <rect x="0" y="0" width="940" height="520" rx="18" fill="url(#stk-bg)" stroke="url(#stk-border)" stroke-width="1.6"/>
  <rect x="0" y="0" width="940" height="520" rx="18" fill="url(#stk-dots)"/>

  <!-- Top Title Header -->
  <g transform="translate(36, 26)">
    <text x="0" y="10" class="font-sans" font-size="11" font-weight="700" letter-spacing="2" fill="#2F86FF">05 // THE ENGINE ROOM</text>
    <text x="0" y="36" class="font-display" font-size="24" font-weight="900" fill="#FFFFFF">TOOLS CHANGE. CURIOSITY DOESN'T<tspan fill="#FF3652">.</tspan></text>
    <text x="0" y="56" class="font-sans" font-size="11.5" font-weight="600" fill="#8B96A8">AI &amp; MACHINE LEARNING • SPATIAL RUNTIMES • DISTRIBUTED SYSTEMS</text>
  </g>

  <!-- ================= LEFT: REAL ORBITAL PLANETARY SYSTEM ================= -->
  <g transform="translate(0, 10)">
    <!-- Orbit 1: Inner Orbit (Python / AI Core) - 18s -->
    <ellipse cx="205" cy="275" rx="68" ry="60" fill="none" stroke="#2F86FF" stroke-width="1.2" stroke-opacity="0.35" stroke-dasharray="4,4" transform="rotate(-15 205 275)"/>

    <!-- Orbit 2: Mid Orbit (FastAPI / Backend) - 24s -->
    <ellipse cx="205" cy="275" rx="112" ry="76" fill="none" stroke="#60A5FA" stroke-width="1.2" stroke-opacity="0.3" stroke-dasharray="5,4" transform="rotate(25 205 275)"/>

    <!-- Orbit 3: Outer Orbit (React / Frontend) - 30s -->
    <ellipse cx="205" cy="275" rx="148" ry="74" fill="none" stroke="#2F86FF" stroke-width="1.2" stroke-opacity="0.35" stroke-dasharray="6,4" transform="rotate(-30 205 275)"/>

    <!-- Orbit 4: Deep Orbit (PostGIS / Spatial) - 36s -->
    <ellipse cx="205" cy="275" rx="180" ry="96" fill="none" stroke="#FF3652" stroke-width="1.2" stroke-opacity="0.35" stroke-dasharray="5,5" transform="rotate(45 205 275)"/>

    <!-- Ambient Orbital Particle Stars with independent twinkle -->
    <circle cx="150" cy="195" r="1.5" fill="#60A5FA" opacity="0.6"><animate attributeName="opacity" values="0.2;0.8;0.2" dur="2s" repeatCount="indefinite"/></circle>
    <circle cx="270" cy="345" r="1.5" fill="#60A5FA" opacity="0.7"><animate attributeName="opacity" values="0.3;0.9;0.3" dur="2.7s" repeatCount="indefinite"/></circle>
    <circle cx="85" cy="285" r="1.5" fill="#FF3652" opacity="0.6"><animate attributeName="opacity" values="0.2;0.7;0.2" dur="3.2s" repeatCount="indefinite"/></circle>
    <circle cx="320" cy="225" r="1.5" fill="#60A5FA" opacity="0.5"><animate attributeName="opacity" values="0.1;0.8;0.1" dur="2.4s" repeatCount="indefinite"/></circle>

    <!-- CENTRAL GLOWING SUN / PT CORE -->
    <g class="core-sun">
      <circle cx="205" cy="275" r="44" fill="url(#sun-glow)"/>
      <circle cx="205" cy="275" r="32" fill="none" stroke="#60A5FA" stroke-width="1.2" stroke-dasharray="3,3" opacity="0.7">
        <animateTransform attributeName="transform" type="rotate" from="0 205 275" to="360 205 275" dur="18s" repeatCount="indefinite"/>
      </circle>
      <rect x="180" y="250" width="50" height="50" rx="12" fill="#09142A" stroke="#2F86FF" stroke-width="2"/>
      <text x="205" y="279" text-anchor="middle" class="font-display" font-size="18" font-weight="900" fill="#FFFFFF">PT</text>
      <text x="205" y="292" text-anchor="middle" class="font-sans" font-size="7.5" font-weight="800" fill="#60A5FA" letter-spacing="1">CORE</text>
    </g>

    <!-- REVOLVING PLANETARY NODES (Layered linear speeds, counter-rotated with REAL brand marks) -->

    <!-- Planet 1: Python / AI Core (18s) with PyTorch Moon -->
    <g>
      <animateTransform attributeName="transform" type="rotate" from="0 205 275" to="360 205 275" dur="18s" repeatCount="indefinite"/>
      <g transform="translate(205, 215)">
        <animateTransform attributeName="transform" type="rotate" from="0 0 0" to="-360 0 0" dur="18s" repeatCount="indefinite"/>
        <circle cx="0" cy="0" r="17" fill="#08152B" stroke="#2F86FF" stroke-width="1.6"/>
        <g transform="translate(-8, -8)">
          <use href="#icon-python" width="16" height="16"/>
        </g>
        <!-- Orbiting PyTorch Moon -->
        <g>
          <animateTransform attributeName="transform" type="rotate" from="0 0 0" to="360 0 0" dur="4s" repeatCount="indefinite"/>
          <g transform="translate(24, 0)">
            <circle cx="0" cy="0" r="6" fill="#1A0C16" stroke="#EE4C2C" stroke-width="1"/>
            <g transform="translate(-4, -4)"><use href="#icon-pytorch" width="8" height="8"/></g>
          </g>
        </g>
      </g>
    </g>

    <!-- Planet 2: FastAPI / Backend (24s) -->
    <g>
      <animateTransform attributeName="transform" type="rotate" from="90 205 275" to="450 205 275" dur="24s" repeatCount="indefinite"/>
      <g transform="translate(300, 255)">
        <animateTransform attributeName="transform" type="rotate" from="0 0 0" to="-360 0 0" dur="24s" repeatCount="indefinite"/>
        <circle cx="0" cy="0" r="16" fill="#07152B" stroke="#05998B" stroke-width="1.6"/>
        <g transform="translate(-7, -7)">
          <use href="#icon-fastapi" width="14" height="14"/>
        </g>
      </g>
    </g>

    <!-- Planet 3: React / Frontend (30s) -->
    <g>
      <animateTransform attributeName="transform" type="rotate" from="210 205 275" to="570 205 275" dur="30s" repeatCount="indefinite"/>
      <g transform="translate(90, 255)">
        <animateTransform attributeName="transform" type="rotate" from="0 0 0" to="-360 0 0" dur="30s" repeatCount="indefinite"/>
        <circle cx="0" cy="0" r="16" fill="#061226" stroke="#61DAFB" stroke-width="1.6"/>
        <g transform="translate(-7, -7)">
          <use href="#icon-react" width="14" height="14"/>
        </g>
      </g>
    </g>

    <!-- Planet 4: PostGIS / Spatial (36s Counter) -->
    <g>
      <animateTransform attributeName="transform" type="rotate" from="360 205 275" to="0 205 275" dur="36s" repeatCount="indefinite"/>
      <g transform="translate(125, 380)">
        <animateTransform attributeName="transform" type="rotate" from="0 0 0" to="360 0 0" dur="36s" repeatCount="indefinite"/>
        <circle cx="0" cy="0" r="16" fill="#1C0E1E" stroke="#FF3652" stroke-width="1.6"/>
        <g transform="translate(-7, -7)">
          <use href="#icon-postgres" width="14" height="14"/>
        </g>
      </g>
    </g>

    <!-- Left Footnote -->
    <text x="205" y="480" text-anchor="middle" class="font-sans" font-size="10" font-weight="700" letter-spacing="1.5" fill="#64748B">PLANETARY RUNTIME • CONTINUOUS ORBITAL SHIP CYCLE</text>
  </g>

  <!-- ================= RIGHT: COMPLETE REAL TECH STACK (Zero Empty Boxes, Brand Icons!) ================= -->
  <g transform="translate(425, 90)">

    <!-- 01 // AI & MACHINE LEARNING -->
    <g transform="translate(0, 0)">
      <text x="0" y="11" class="font-sans" font-size="11" font-weight="700" letter-spacing="1.5" fill="#60A5FA">01 // AI &amp; MACHINE LEARNING</text>
      <!-- Row 1 -->
      <g transform="translate(0, 20)">
        <g transform="translate(0, 0)">
          <rect x="0" y="0" width="85" height="28" rx="6" fill="#0C1527" stroke="#2F86FF" stroke-width="1.1"/>
          <g transform="translate(8, 6)"><use href="#icon-python" width="16" height="16"/></g>
          <text x="28" y="18" class="font-sans" font-size="11" font-weight="700" fill="#F1F5F9">Python</text>
        </g>
        <g transform="translate(93, 0)">
          <rect x="0" y="0" width="90" height="28" rx="6" fill="#0C1527" stroke="#2F86FF" stroke-width="1.1"/>
          <g transform="translate(8, 6)"><use href="#icon-pytorch" width="16" height="16"/></g>
          <text x="28" y="18" class="font-sans" font-size="11" font-weight="700" fill="#F1F5F9">PyTorch</text>
        </g>
        <g transform="translate(191, 0)">
          <rect x="0" y="0" width="105" height="28" rx="6" fill="#0C1527" stroke="#2F86FF" stroke-width="1.1"/>
          <g transform="translate(8, 6)"><use href="#icon-scikit" width="16" height="16"/></g>
          <text x="28" y="18" class="font-sans" font-size="11" font-weight="700" fill="#F1F5F9">Scikit-learn</text>
        </g>
        <g transform="translate(304, 0)">
          <rect x="0" y="0" width="105" height="28" rx="6" fill="#0C1527" stroke="#2F86FF" stroke-width="1.1"/>
          <g transform="translate(8, 6)"><use href="#icon-tensorflow" width="16" height="16"/></g>
          <text x="28" y="18" class="font-sans" font-size="11" font-weight="700" fill="#F1F5F9">TensorFlow</text>
        </g>
        <g transform="translate(417, 0)">
          <rect x="0" y="0" width="80" height="28" rx="6" fill="#0C1527" stroke="#2F86FF" stroke-width="1.1"/>
          <g transform="translate(8, 6)"><use href="#icon-opencv" width="16" height="16"/></g>
          <text x="28" y="18" class="font-sans" font-size="11" font-weight="700" fill="#F1F5F9">OpenCV</text>
        </g>
      </g>

      <!-- Row 2 -->
      <g transform="translate(0, 56)">
        <g transform="translate(0, 0)">
          <rect x="0" y="0" width="85" height="26" rx="5" fill="#0C1527" stroke="#1E2F4D" stroke-width="0.9"/>
          <g transform="translate(8, 5)"><use href="#icon-numpy" width="15" height="15"/></g>
          <text x="28" y="17" class="font-sans" font-size="10.5" font-weight="600" fill="#CBD5E1">NumPy</text>
        </g>
        <g transform="translate(93, 0)">
          <rect x="0" y="0" width="85" height="26" rx="5" fill="#0C1527" stroke="#1E2F4D" stroke-width="0.9"/>
          <g transform="translate(8, 5)"><use href="#icon-pandas" width="15" height="15"/></g>
          <text x="28" y="17" class="font-sans" font-size="10.5" font-weight="600" fill="#CBD5E1">Pandas</text>
        </g>
        <g transform="translate(186, 0)">
          <rect x="0" y="0" width="112" height="26" rx="5" fill="#0C1527" stroke="#1E2F4D" stroke-width="0.9"/>
          <g transform="translate(8, 5)"><use href="#icon-transformers" width="15" height="15"/></g>
          <text x="28" y="17" class="font-sans" font-size="10.5" font-weight="600" fill="#CBD5E1">Transformers</text>
        </g>
        <g transform="translate(306, 0)">
          <rect x="0" y="0" width="100" height="26" rx="5" fill="#0C1527" stroke="#1E2F4D" stroke-width="0.9"/>
          <g transform="translate(8, 5)"><use href="#icon-langchain" width="15" height="15"/></g>
          <text x="28" y="17" class="font-sans" font-size="10.5" font-weight="600" fill="#CBD5E1">LangChain</text>
        </g>
        <g transform="translate(414, 0)">
          <rect x="0" y="0" width="83" height="26" rx="5" fill="#0C1527" stroke="#1E2F4D" stroke-width="0.9"/>
          <g transform="translate(8, 5)"><use href="#icon-fastapi" width="15" height="15"/></g>
          <text x="28" y="17" class="font-sans" font-size="10.5" font-weight="600" fill="#CBD5E1">FastAPI</text>
        </g>
      </g>
    </g>

    <!-- 02 // LANGUAGES -->
    <g transform="translate(0, 114)">
      <text x="0" y="11" class="font-sans" font-size="11" font-weight="700" letter-spacing="1.5" fill="#60A5FA">02 // PROGRAMMING LANGUAGES</text>
      <g transform="translate(0, 20)">
        <g transform="translate(0, 0)">
          <rect x="0" y="0" width="80" height="28" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
          <g transform="translate(8, 6)"><use href="#icon-python" width="16" height="16"/></g>
          <text x="28" y="18" class="font-sans" font-size="11" font-weight="700" fill="#F1F5F9">Python</text>
        </g>
        <g transform="translate(88, 0)">
          <rect x="0" y="0" width="102" height="28" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
          <g transform="translate(8, 6)"><use href="#icon-typescript" width="16" height="16"/></g>
          <text x="28" y="18" class="font-sans" font-size="11" font-weight="700" fill="#F1F5F9">TypeScript</text>
        </g>
        <g transform="translate(198, 0)">
          <rect x="0" y="0" width="100" height="28" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
          <g transform="translate(8, 6)"><use href="#icon-javascript" width="16" height="16"/></g>
          <text x="28" y="18" class="font-sans" font-size="11" font-weight="700" fill="#F1F5F9">JavaScript</text>
        </g>
        <g transform="translate(306, 0)">
          <rect x="0" y="0" width="65" height="28" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
          <g transform="translate(8, 6)"><use href="#icon-sql" width="16" height="16"/></g>
          <text x="28" y="18" class="font-sans" font-size="11" font-weight="700" fill="#F1F5F9">SQL</text>
        </g>
        <g transform="translate(379, 0)">
          <rect x="0" y="0" width="58" height="28" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
          <g transform="translate(8, 6)"><use href="#icon-cpp" width="16" height="16"/></g>
          <text x="27" y="18" class="font-sans" font-size="11" font-weight="700" fill="#F1F5F9">C++</text>
        </g>
        <g transform="translate(445, 0)">
          <rect x="0" y="0" width="55" height="28" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
          <g transform="translate(8, 6)"><use href="#icon-java" width="16" height="16"/></g>
          <text x="26" y="18" class="font-sans" font-size="11" font-weight="700" fill="#F1F5F9">Java</text>
        </g>
      </g>
    </g>

    <!-- 03 // FRONTEND & SPATIAL -->
    <g transform="translate(0, 194)">
      <text x="0" y="11" class="font-sans" font-size="11" font-weight="700" letter-spacing="1.5" fill="#60A5FA">03 // FRONTEND &amp; SPATIAL VISUALIZATION</text>
      <g transform="translate(0, 20)">
        <g transform="translate(0, 0)">
          <rect x="0" y="0" width="76" height="28" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
          <g transform="translate(8, 6)"><use href="#icon-react" width="16" height="16"/></g>
          <text x="28" y="18" class="font-sans" font-size="11" font-weight="700" fill="#F1F5F9">React</text>
        </g>
        <g transform="translate(84, 0)">
          <rect x="0" y="0" width="82" height="28" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
          <g transform="translate(8, 6)"><use href="#icon-nextjs" width="16" height="16"/></g>
          <text x="28" y="18" class="font-sans" font-size="11" font-weight="700" fill="#F1F5F9">Next.js</text>
        </g>
        <g transform="translate(174, 0)">
          <rect x="0" y="0" width="118" height="28" rx="6" fill="#081A33" stroke="#2F86FF" stroke-width="1.2"/>
          <g transform="translate(8, 6)"><use href="#icon-maplibre" width="16" height="16"/></g>
          <text x="28" y="18" class="font-sans" font-size="11" font-weight="700" fill="#60A5FA">MapLibre GL</text>
        </g>
        <g transform="translate(300, 0)">
          <rect x="0" y="0" width="82" height="28" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
          <g transform="translate(8, 6)"><use href="#icon-leaflet" width="16" height="16"/></g>
          <text x="28" y="18" class="font-sans" font-size="11" font-weight="700" fill="#F1F5F9">Leaflet</text>
        </g>
        <g transform="translate(390, 0)">
          <rect x="0" y="0" width="110" height="28" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
          <g transform="translate(8, 6)"><use href="#icon-tailwind" width="16" height="16"/></g>
          <text x="28" y="18" class="font-sans" font-size="11" font-weight="700" fill="#F1F5F9">Tailwind CSS</text>
        </g>
      </g>
    </g>

    <!-- 04 // BACKEND & DATABASES -->
    <g transform="translate(0, 274)">
      <text x="0" y="11" class="font-sans" font-size="11" font-weight="700" letter-spacing="1.5" fill="#60A5FA">04 // BACKEND &amp; SPATIAL INFRASTRUCTURE</text>
      <g transform="translate(0, 20)">
        <g transform="translate(0, 0)">
          <rect x="0" y="0" width="84" height="28" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
          <g transform="translate(8, 6)"><use href="#icon-fastapi" width="16" height="16"/></g>
          <text x="28" y="18" class="font-sans" font-size="11" font-weight="700" fill="#F1F5F9">FastAPI</text>
        </g>
        <g transform="translate(92, 0)">
          <rect x="0" y="0" width="86" height="28" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
          <g transform="translate(8, 6)"><use href="#icon-nodejs" width="16" height="16"/></g>
          <text x="28" y="18" class="font-sans" font-size="11" font-weight="700" fill="#F1F5F9">Node.js</text>
        </g>
        <g transform="translate(186, 0)">
          <rect x="0" y="0" width="138" height="28" rx="6" fill="#1C1022" stroke="#FF3652" stroke-width="1.2"/>
          <g transform="translate(8, 6)"><use href="#icon-postgres" width="16" height="16"/></g>
          <text x="28" y="18" class="font-sans" font-size="11" font-weight="700" fill="#FF8A9A">PostgreSQL / GIS</text>
        </g>
        <g transform="translate(332, 0)">
          <rect x="0" y="0" width="75" height="28" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
          <g transform="translate(8, 6)"><use href="#icon-redis" width="16" height="16"/></g>
          <text x="28" y="18" class="font-sans" font-size="11" font-weight="700" fill="#F1F5F9">Redis</text>
        </g>
        <g transform="translate(415, 0)">
          <rect x="0" y="0" width="85" height="28" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
          <g transform="translate(8, 6)"><use href="#icon-websockets" width="16" height="16"/></g>
          <text x="28" y="18" class="font-sans" font-size="10.5" font-weight="700" fill="#F1F5F9">WebSockets</text>
        </g>
      </g>
    </g>

  </g>
</svg>'''

    # =========================================================================
    # 6. assets/selected-builds.svg — 06 // SELECTED BUILDS (Alternating Layouts)
    # =========================================================================
    selected_builds_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 680" width="100%" height="100%">
  <defs>
    <style>{COMMON_STYLE}</style>
    <linearGradient id="sb-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2F86FF" stop-opacity="0.6"/>
      <stop offset="50%" stop-color="#FF3652" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#2F86FF" stop-opacity="0.6"/>
    </linearGradient>
    <pattern id="sb-dots" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#1C2B49" opacity="0.4"/>
    </pattern>
    <linearGradient id="danger-poly" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FF3652" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#FF3652" stop-opacity="0.05"/>
    </linearGradient>
  </defs>

  <rect x="0" y="0" width="940" height="680" rx="16" fill="#070B16" stroke="url(#sb-border)" stroke-width="1.3"/>
  <rect x="0" y="0" width="940" height="680" rx="16" fill="url(#sb-dots)"/>

  <!-- Top bar -->
  <g transform="translate(32, 22)">
    <text x="0" y="10" class="font-sans" font-size="10.5" font-weight="700" letter-spacing="2" fill="#2F86FF">06 // SELECTED BUILDS</text>
    <text x="0" y="34" class="font-display" font-size="22" font-weight="900" fill="#FFFFFF">ENGINEERED SYSTEMS<tspan fill="#FF3652">.</tspan></text>
    <text x="560" y="32" class="font-sans" font-size="11.5" fill="#8B96A8">High-impact projects with verified architectural depth.</text>
  </g>

  <!-- 4 Alternating Project Modules -->
  <g transform="translate(32, 70)">

    <!-- ================= BUILD 01: RESQ (Content Left, Technical Visual Right) ================= -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="876" height="150" rx="10" fill="#0A1122" stroke="#1F2F4F" stroke-width="1"/>
      <!-- Content Left -->
      <g transform="translate(24, 18)">
        <text x="0" y="10" class="font-sans" font-size="9.5" font-weight="700" letter-spacing="1.5" fill="#60A5FA">01 // ROUTING &amp; DISASTER INTELLIGENCE</text>
        <text x="0" y="32" class="font-display" font-size="20" font-weight="900" fill="#FFFFFF">RESQ</text>
        <text x="0" y="48" class="font-sans" font-size="11.5" font-weight="700" fill="#2F86FF">Disaster Relief Routing Engine</text>

        <text x="0" y="72" class="font-sans" font-size="12" fill="#CBD5E1">
          Damage-aware supply chain routing across natural disaster zones, assessing road risk
        </text>
        <text x="0" y="88" class="font-sans" font-size="12" fill="#CBD5E1">
          surfaces via Valhalla dynamic cost-weighted routing &amp; PostGIS hazard geometries.
        </text>

        <g transform="translate(0, 108)">
          <text x="0" y="10" class="font-sans" font-size="10.5" font-weight="700" fill="#8B96A8">STACK: <tspan fill="#60A5FA">PostGIS • Valhalla Routing • Python • GeoJSON</tspan></text>
          <text x="380" y="10" class="font-sans" font-size="10.5" font-weight="700" fill="#FF8A9A">NATIONAL FINALIST</text>
        </g>
      </g>

      <!-- Technical Visual Right: Dynamic Hazard Bypass Diagram -->
      <g transform="translate(580, 15)">
        <rect x="0" y="0" width="276" height="120" rx="8" fill="#070E1A" stroke="#162544" stroke-width="1"/>
        <!-- Hazard Polygon -->
        <polygon points="70,25 150,15 190,65 120,95 60,60" fill="url(#danger-poly)" stroke="#FF3652" stroke-width="1" stroke-dasharray="3,3"/>
        <text x="110" y="55" class="font-sans" font-size="9" font-weight="700" fill="#FF8A9A" text-anchor="middle">FLOOD / HAZARD ZONE</text>
        <!-- Rerouted Path (Cost-weighted bypass) -->
        <path d="M 25 100 Q 40 40 70 20 T 150 15 T 220 30 T 255 75" fill="none" stroke="#2F86FF" stroke-width="2.5"/>
        <circle cx="25" cy="100" r="4.5" fill="#2F86FF"/>
        <text x="25" y="114" class="font-sans" font-size="8" font-weight="700" fill="#8B96A8" text-anchor="middle">ORIGIN</text>
        <circle cx="255" cy="75" r="4.5" fill="#10B981"/>
        <text x="255" y="90" class="font-sans" font-size="8" font-weight="700" fill="#10B981" text-anchor="middle">RELIEF HUB</text>
      </g>
    </g>

    <!-- ================= BUILD 02: GridShare (Visual Left, Content Right) ================= -->
    <g transform="translate(0, 165)">
      <rect x="0" y="0" width="876" height="150" rx="10" fill="#0A1122" stroke="#1F2F4F" stroke-width="1"/>
      <!-- Technical Visual Left: Microgrid P2P Power Flow Diagram -->
      <g transform="translate(20, 15)">
        <rect x="0" y="0" width="276" height="120" rx="8" fill="#070E1A" stroke="#162544" stroke-width="1"/>
        <!-- Node 1: Solar -->
        <circle cx="50" cy="40" r="16" fill="#1F1D0E" stroke="#EAB308" stroke-width="1.2"/>
        <text x="50" y="44" class="font-sans" font-size="8.5" font-weight="800" fill="#FDE047" text-anchor="middle">SOLAR</text>
        <!-- Node 2: Battery ESS -->
        <circle cx="140" cy="85" r="18" fill="#0E1D2A" stroke="#2F86FF" stroke-width="1.4"/>
        <text x="140" y="88" class="font-sans" font-size="8.5" font-weight="800" fill="#60A5FA" text-anchor="middle">STORAGE</text>
        <!-- Node 3: EV / Home Load -->
        <circle cx="225" cy="40" r="16" fill="#1E0E1B" stroke="#FF3652" stroke-width="1.2"/>
        <text x="225" y="44" class="font-sans" font-size="8.5" font-weight="800" fill="#FFA3AF" text-anchor="middle">EV LOAD</text>
        <!-- Interconnection Energy Flow -->
        <line x1="65" y1="48" x2="124" y2="78" stroke="#60A5FA" stroke-width="1.8" stroke-dasharray="4,3"/>
        <line x1="156" y1="78" x2="210" y2="48" stroke="#FF3652" stroke-width="1.8" stroke-dasharray="4,3"/>
        <text x="140" y="24" class="font-sans" font-size="8" font-weight="700" fill="#8B96A8" text-anchor="middle">P2P BALANCING PROTOCOL</text>
      </g>

      <!-- Content Right -->
      <g transform="translate(320, 18)">
        <text x="0" y="10" class="font-sans" font-size="9.5" font-weight="700" letter-spacing="1.5" fill="#FF8A9A">02 // DISTRIBUTED ENERGY &amp; P2P TRADING</text>
        <text x="0" y="32" class="font-display" font-size="20" font-weight="900" fill="#FFFFFF">GridShare</text>
        <text x="0" y="48" class="font-sans" font-size="11.5" font-weight="700" fill="#FF3652">Community Microgrid Coordinator</text>

        <text x="0" y="72" class="font-sans" font-size="12" fill="#CBD5E1">
          Intelligent coordination layer for neighborhood solar, battery &amp; EV storage, optimizing
        </text>
        <text x="0" y="88" class="font-sans" font-size="12" fill="#CBD5E1">
          decentralized peer-to-peer energy balancing and consumption peaks in real time.
        </text>

        <g transform="translate(0, 108)">
          <text x="0" y="10" class="font-sans" font-size="10.5" font-weight="700" fill="#8B96A8">STACK: <tspan fill="#60A5FA">Distributed Node.js • React • Telemetry Streaming</tspan></text>
          <text x="370" y="10" class="font-sans" font-size="10.5" font-weight="700" fill="#60A5FA">IIT GUWAHATI FLAGSHIP</text>
        </g>
      </g>
    </g>

    <!-- ================= BUILD 03: MednormAI (Content Left, Visual Right) ================= -->
    <g transform="translate(0, 330)">
      <rect x="0" y="0" width="876" height="150" rx="10" fill="#0A1122" stroke="#1F2F4F" stroke-width="1"/>
      <!-- Content Left -->
      <g transform="translate(24, 18)">
        <text x="0" y="10" class="font-sans" font-size="9.5" font-weight="700" letter-spacing="1.5" fill="#60A5FA">03 // CLINICAL DATA EXTRACTION &amp; NLP</text>
        <text x="0" y="32" class="font-display" font-size="20" font-weight="900" fill="#FFFFFF">MednormAI</text>
        <text x="0" y="48" class="font-sans" font-size="11.5" font-weight="700" fill="#2F86FF">Clinical Data Normalization Engine</text>

        <text x="0" y="72" class="font-sans" font-size="12" fill="#CBD5E1">
          AI data normalization pipeline using optical character recognition &amp; NLP pipelines
        </text>
        <text x="0" y="88" class="font-sans" font-size="12" fill="#CBD5E1">
          to parse unstructured clinical PDFs and medical bills into normalized records.
        </text>

        <g transform="translate(0, 108)">
          <text x="0" y="10" class="font-sans" font-size="10.5" font-weight="700" fill="#8B96A8">STACK: <tspan fill="#60A5FA">OCR Pipeline • NLP • Python • FastAPI • Regex Heuristics</tspan></text>
          <text x="380" y="10" class="font-sans" font-size="10.5" font-weight="700" fill="#8B96A8">HACKMATRIX 2.0</text>
        </g>
      </g>

      <!-- Technical Visual Right: Document Parsing Flow -->
      <g transform="translate(580, 15)">
        <rect x="0" y="0" width="276" height="120" rx="8" fill="#070E1A" stroke="#162544" stroke-width="1"/>
        <!-- Step 1: Raw Medical PDF -->
        <rect x="20" y="25" width="55" height="70" rx="4" fill="#0F172A" stroke="#334155" stroke-width="1"/>
        <line x1="28" y1="38" x2="65" y2="38" stroke="#64748B" stroke-width="1.5"/>
        <line x1="28" y1="48" x2="58" y2="48" stroke="#64748B" stroke-width="1.5"/>
        <line x1="28" y1="58" x2="62" y2="58" stroke="#64748B" stroke-width="1.5"/>
        <text x="47" y="85" class="font-sans" font-size="7.5" font-weight="700" fill="#94A3B8" text-anchor="middle">RAW PDF</text>
        <!-- Arrow -->
        <path d="M 85 60 L 115 60" stroke="#2F86FF" stroke-width="1.5" marker-end="url(#arrow)"/>
        <!-- Step 2: NLP Parser -->
        <rect x="125" y="35" width="50" height="50" rx="6" fill="#12203A" stroke="#2F86FF" stroke-width="1.2"/>
        <text x="150" y="58" class="font-sans" font-size="8.5" font-weight="800" fill="#60A5FA" text-anchor="middle">OCR + NLP</text>
        <text x="150" y="70" class="font-sans" font-size="7.5" fill="#8B96A8" text-anchor="middle">MODEL</text>
        <!-- Arrow -->
        <path d="M 185 60 L 205 60" stroke="#2F86FF" stroke-width="1.5"/>
        <!-- Step 3: Structured JSON Tree -->
        <rect x="215" y="25" width="45" height="70" rx="4" fill="#0F241F" stroke="#10B981" stroke-width="1"/>
        <text x="237" y="52" class="font-sans" font-size="8" font-weight="800" fill="#34D399" text-anchor="middle">{{ JSON }}</text>
        <text x="237" y="80" class="font-sans" font-size="7" fill="#6EE7B7" text-anchor="middle">CLEAN</text>
      </g>
    </g>

    <!-- ================= BUILD 04: OpenRAG (Compact Horizontal Full-Width Bar) ================= -->
    <g transform="translate(0, 495)">
      <rect x="0" y="0" width="876" height="75" rx="10" fill="#0A1122" stroke="#1F2F4F" stroke-width="1"/>
      <g transform="translate(24, 18)">
        <!-- Left: Index + Title -->
        <text x="0" y="10" class="font-sans" font-size="9" font-weight="700" letter-spacing="1.5" fill="#60A5FA">04 // SEMANTIC RETRIEVAL</text>
        <text x="0" y="32" class="font-display" font-size="18" font-weight="900" fill="#FFFFFF">OpenRAG</text>
        <text x="100" y="32" class="font-sans" font-size="12" font-weight="700" fill="#60A5FA">• Enterprise RAG Pipeline</text>

        <!-- Middle: Description -->
        <text x="320" y="18" class="font-sans" font-size="11.5" fill="#CBD5E1">Dense document embeddings, vector indexing &amp; semantic hybrid search.</text>
        <text x="320" y="34" class="font-sans" font-size="10" font-weight="700" fill="#8B96A8">STACK: <tspan fill="#60A5FA">PyTorch • Transformers • Vector DB • LangChain</tspan></text>

        <!-- Right: CTA Link -->
        <text x="825" y="28" class="font-sans" font-size="11" font-weight="800" fill="#2F86FF" text-anchor="end">VIEW REPOSITORY →</text>
      </g>
    </g>

  </g>
</svg>'''

    # =========================================================================
    # 7. assets/id-dashboard.svg — 07 // BUILDER ID & MILESTONES (Clean & Spaced)
    # =========================================================================
    id_dashboard_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 940 440" width="100%" height="100%">
  <defs>
    <style>{COMMON_STYLE}
      @keyframes subtlePendulum {{
        0%   {{ transform: rotate(-0.8deg); }}
        50%  {{ transform: rotate(0.8deg); }}
        100% {{ transform: rotate(-0.8deg); }}
      }}
      .hanging-badge {{
        animation: subtlePendulum 5.5s ease-in-out infinite;
        transform-origin: 175px 35px;
      }}
    </style>
    <linearGradient id="id-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070B16"/>
      <stop offset="60%" stop-color="#0B1325"/>
      <stop offset="100%" stop-color="#070B16"/>
    </linearGradient>
    <linearGradient id="id-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2F86FF" stop-opacity="0.85"/>
      <stop offset="50%" stop-color="#2F86FF" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#FF3652" stop-opacity="0.6"/>
    </linearGradient>
    <linearGradient id="id-lanyard" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1848A0"/>
      <stop offset="50%" stop-color="#2F86FF"/>
      <stop offset="100%" stop-color="#1848A0"/>
    </linearGradient>
    <pattern id="id-dots" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1.1" fill="#1C2B49" opacity="0.45"/>
    </pattern>
    <clipPath id="id-badge-photo">
      <rect x="0" y="0" width="120" height="120" rx="10"/>
    </clipPath>
  </defs>

  <rect x="0" y="0" width="940" height="440" rx="18" fill="url(#id-bg)" stroke="url(#id-border)" stroke-width="1.6"/>
  <rect x="0" y="0" width="940" height="440" rx="18" fill="url(#id-dots)"/>

  <!-- ================= LEFT: HANGING BUILDER PASS ================= -->
  <g class="hanging-badge">
    <rect x="160" y="-10" width="30" height="55" fill="url(#id-lanyard)"/>
    <text x="175" y="25" text-anchor="middle" class="font-sans" font-size="7.5" font-weight="900" fill="#FFFFFF" transform="rotate(90 175 25)">BUILDER PASS</text>

    <!-- Metal Clasp -->
    <rect x="156" y="42" width="38" height="14" rx="4" fill="#94A3B8" stroke="#CBD5E1" stroke-width="1"/>
    <rect x="165" y="56" width="20" height="10" rx="2" fill="#64748B"/>

    <!-- ID Badge Body -->
    <g transform="translate(62, 66)">
      <rect x="0" y="0" width="226" height="336" rx="14" fill="#0A1224" stroke="#2F86FF" stroke-width="1.6"/>
      <rect x="0" y="0" width="226" height="26" rx="14" fill="#FF3652"/>
      <rect x="88" y="8" width="50" height="7" rx="3.5" fill="#070B16"/>

      <!-- Pass Header -->
      <g transform="translate(16, 42)">
        <text x="0" y="0" class="font-sans" font-size="10.5" font-weight="700" fill="#60A5FA">BUILDER PASS</text>
        <text x="194" y="0" text-anchor="end" class="font-sans" font-size="10.5" font-weight="700" fill="#94A3B8">2026</text>
      </g>

      <!-- Portrait Box -->
      <g transform="translate(16, 54)">
        <rect x="0" y="0" width="194" height="130" rx="10" fill="#050811" stroke="#1E2F4D" stroke-width="1"/>
        <g clip-path="url(#id-badge-photo)" transform="translate(37, 5)">
          <image href="data:image/png;base64,{mine_b64}" xlink:href="data:image/png;base64,{mine_b64}" x="-15" y="-10" width="150" height="150" preserveAspectRatio="xMidYMid meet"/>
        </g>
      </g>

      <!-- Identity Details -->
      <g transform="translate(16, 202)">
        <text x="0" y="10" class="font-display" font-size="16" font-weight="900" fill="#FFFFFF">PRINCE TIWARI</text>
        <text x="0" y="27" class="font-sans" font-size="10.5" font-weight="700" fill="#60A5FA">SOFTWARE ENGINEER • BUILDER</text>
        <text x="0" y="43" class="font-sans" font-size="10" font-weight="600" fill="#A855F7">AI / ML • FULL-STACK • SPATIAL</text>
        <text x="0" y="58" class="font-sans" font-size="9.5" fill="#94A3B8">Muzaffarpur, Bihar, India</text>
      </g>

      <!-- Barcode -->
      <g transform="translate(16, 272)">
        <line x1="0" y1="0" x2="0" y2="26" stroke="#FFFFFF" stroke-width="2.5"/>
        <line x1="5" y1="0" x2="5" y2="26" stroke="#FFFFFF" stroke-width="1"/>
        <line x1="9" y1="0" x2="9" y2="26" stroke="#FFFFFF" stroke-width="3"/>
        <line x1="16" y1="0" x2="16" y2="26" stroke="#2F86FF" stroke-width="3.5"/>
        <line x1="24" y1="0" x2="24" y2="26" stroke="#FFFFFF" stroke-width="1"/>
        <line x1="31" y1="0" x2="31" y2="26" stroke="#FFFFFF" stroke-width="2"/>
        <line x1="38" y1="0" x2="38" y2="26" stroke="#FF3652" stroke-width="3"/>
        <line x1="46" y1="0" x2="46" y2="26" stroke="#FFFFFF" stroke-width="1.5"/>
        <line x1="54" y1="0" x2="54" y2="26" stroke="#FFFFFF" stroke-width="2.5"/>
        <line x1="62" y1="0" x2="62" y2="26" stroke="#2F86FF" stroke-width="3"/>
        <line x1="72" y1="0" x2="72" y2="26" stroke="#FFFFFF" stroke-width="1"/>
        <line x1="80" y1="0" x2="80" y2="26" stroke="#FFFFFF" stroke-width="3.5"/>
        <line x1="90" y1="0" x2="90" y2="26" stroke="#FFFFFF" stroke-width="1"/>
        <line x1="98" y1="0" x2="98" y2="26" stroke="#2F86FF" stroke-width="2"/>
        <line x1="108" y1="0" x2="108" y2="26" stroke="#FFFFFF" stroke-width="4"/>
        <line x1="118" y1="0" x2="118" y2="26" stroke="#FFFFFF" stroke-width="1.5"/>
        <line x1="126" y1="0" x2="126" y2="26" stroke="#FF3652" stroke-width="2.5"/>
        <line x1="134" y1="0" x2="134" y2="26" stroke="#FFFFFF" stroke-width="3"/>
        <line x1="144" y1="0" x2="144" y2="26" stroke="#FFFFFF" stroke-width="1"/>
        <line x1="152" y1="0" x2="152" y2="26" stroke="#FFFFFF" stroke-width="2"/>
        <line x1="162" y1="0" x2="162" y2="26" stroke="#2F86FF" stroke-width="3"/>
        <line x1="172" y1="0" x2="172" y2="26" stroke="#FFFFFF" stroke-width="1.5"/>
        <line x1="184" y1="0" x2="184" y2="26" stroke="#FFFFFF" stroke-width="3"/>
        <text x="97" y="38" text-anchor="middle" class="font-sans" font-size="8.5" font-weight="700" fill="#94A3B8">PT-2026-IN</text>
      </g>
    </g>
  </g>

  <!-- ================= RIGHT: 07 // CHRONOLOGICAL MILESTONES ================= -->
  <g transform="translate(345, 26)">
    <text x="0" y="10" class="font-sans" font-size="11" font-weight="700" letter-spacing="2" fill="#2F86FF">07 // CHRONOLOGICAL MILESTONES</text>
    <text x="0" y="36" class="font-display" font-size="24" font-weight="900" fill="#FFFFFF">THE JOURNEY SO FAR<tspan fill="#FF3652">.</tspan></text>
    <text x="0" y="56" class="font-sans" font-size="11.5" fill="#8B96A8">Foundations, competitive hackathons, and spatial AI.</text>

    <!-- Timeline Progression -->
    <g transform="translate(0, 88)">
      <line x1="30" y1="20" x2="520" y2="20" stroke="#1F2F4F" stroke-width="2"/>

      <!-- Node 1: 2024 -->
      <g transform="translate(30, 0)">
        <circle cx="0" cy="20" r="7" fill="#0C1527" stroke="#2F86FF" stroke-width="2.5"/>
        <text x="-16" y="0" class="font-display" font-size="13" font-weight="900" fill="#60A5FA">2024</text>
        <text x="-25" y="46" class="font-sans" font-size="12" font-weight="700" fill="#F5F7FA">Full-Stack Foundations</text>
        <text x="-25" y="64" class="font-sans" font-size="10.5" fill="#8B96A8">MERN stack, REST APIs,</text>
        <text x="-25" y="78" class="font-sans" font-size="10.5" fill="#8B96A8">relational schemas &amp; CS logic.</text>
      </g>

      <!-- Node 2: 2025 -->
      <g transform="translate(195, 0)">
        <circle cx="0" cy="20" r="7" fill="#0C1527" stroke="#2F86FF" stroke-width="2.5"/>
        <text x="-16" y="0" class="font-display" font-size="13" font-weight="900" fill="#60A5FA">2025</text>
        <text x="-25" y="46" class="font-sans" font-size="12" font-weight="700" fill="#F5F7FA">Applied AI &amp; Hackathons</text>
        <text x="-25" y="64" class="font-sans" font-size="10.5" fill="#8B96A8">ML models, Scikit-learn,</text>
        <text x="-25" y="78" class="font-sans" font-size="10.5" fill="#8B96A8">NLP news extraction &amp; APIs.</text>
      </g>

      <!-- Node 3: 2026 -->
      <g transform="translate(365, 0)">
        <circle cx="0" cy="20" r="7" fill="#0C1527" stroke="#FF3652" stroke-width="2.5"/>
        <text x="-16" y="0" class="font-display" font-size="13" font-weight="900" fill="#FF8A9A">2026</text>
        <text x="-25" y="46" class="font-sans" font-size="12" font-weight="700" fill="#F5F7FA">National Recognition</text>
        <text x="-25" y="64" class="font-sans" font-size="10.5" fill="#8B96A8">Cognithon 2nd, India Innovates,</text>
        <text x="-25" y="78" class="font-sans" font-size="10.5" fill="#8B96A8">Flipkart GRiD Semi-Finalist.</text>
      </g>

      <!-- Node 4: NOW -->
      <g transform="translate(505, 0)">
        <circle cx="0" cy="20" r="8" fill="#2F86FF"/>
        <text x="-14" y="0" class="font-display" font-size="13" font-weight="900" fill="#60A5FA">NOW</text>
        <text x="-35" y="46" class="font-sans" font-size="12" font-weight="700" fill="#F5F7FA">Shipping Builds</text>
        <text x="-35" y="66" class="font-sans" font-size="10.5" fill="#8B96A8">SurakshaAI platform &amp;</text>
        <text x="-35" y="80" class="font-sans" font-size="10.5" fill="#8B96A8">real-world spatial models.</text>
      </g>
    </g>

    <!-- Proof of Work Callout Panel -->
    <g transform="translate(0, 230)">
      <rect x="0" y="0" width="555" height="135" rx="10" fill="#080E1C" stroke="#162544" stroke-width="1.2"/>
      <text x="20" y="25" class="font-sans" font-size="10.5" font-weight="700" letter-spacing="1.5" fill="#60A5FA">PROOF OF WORK • AUTHENTIC VERIFICATION</text>
      <text x="20" y="50" class="font-display" font-size="14.5" font-weight="800" fill="#FFFFFF">Real builds. Real problem spaces. Tested in competitive arenas.</text>
      <text x="20" y="72" class="font-sans" font-size="12" fill="#8B96A8">
        Every system represented on this profile is backed by genuine repositories, verifiable
      </text>
      <text x="20" y="90" class="font-sans" font-size="12" fill="#8B96A8">
        hackathon submissions across IIIT Bhagalpur, IIT Guwahati, IIT Patna, and production code.
      </text>
      <rect x="20" y="104" width="140" height="20" rx="4" fill="#14284D"/>
      <text x="28" y="118" class="font-sans" font-size="9.5" font-weight="700" fill="#60A5FA">OPEN-SOURCE PROOF</text>
    </g>
  </g>
</svg>'''

    # =========================================================================
    # 8. assets/connect.svg — 08 // INITIATE TRANSMISSION (Pointing id.png)
    # =========================================================================
    connect_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 940 420" width="100%" height="100%">
  <defs>
    <style>{COMMON_STYLE}
      @keyframes arrowNudge {{
        0%, 100% {{ transform: translateX(0); }}
        50%      {{ transform: translateX(6px); }}
      }}
      .nudge-arrow {{
        animation: arrowNudge 1.8s ease-in-out infinite;
      }}
    </style>
    <linearGradient id="cn-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070B16"/>
      <stop offset="60%" stop-color="#0A1224"/>
      <stop offset="100%" stop-color="#070B16"/>
    </linearGradient>
    <linearGradient id="cn-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2F86FF" stop-opacity="0.85"/>
      <stop offset="50%" stop-color="#FF3652" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#2F86FF" stop-opacity="0.85"/>
    </linearGradient>
    <pattern id="cn-dots" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1.1" fill="#1E293B" opacity="0.45"/>
    </pattern>
    <clipPath id="cn-character-clip">
      <rect x="0" y="0" width="420" height="400"/>
    </clipPath>
  </defs>

  <rect x="0" y="0" width="940" height="420" rx="18" fill="url(#cn-bg)" stroke="url(#cn-border)" stroke-width="1.6"/>
  <rect x="0" y="0" width="940" height="420" rx="18" fill="url(#cn-dots)"/>

  <!-- Left Pointing Character id.png guiding attention right -->
  <g transform="translate(10, 10)">
    <ellipse cx="225" cy="210" rx="175" ry="175" fill="#2F86FF" fill-opacity="0.12"/>
    <g clip-path="url(#cn-character-clip)">
      <image href="data:image/png;base64,{id_b64}" xlink:href="data:image/png;base64,{id_b64}" x="-10" y="0" width="440" height="400" preserveAspectRatio="xMidYMid meet"/>
    </g>
  </g>

  <!-- Right Headline & Social Channels -->
  <g transform="translate(435, 30)">
    <text x="0" y="10" class="font-sans" font-size="11" font-weight="700" letter-spacing="2" fill="#2F86FF">08 // TRANSMISSION</text>
    <text x="0" y="42" class="font-display" font-size="34" font-weight="900" fill="#FFFFFF">LET'S BUILD SOMETHING<tspan fill="#FF3652">.</tspan></text>
    <text x="0" y="65" class="font-sans" font-size="13.5" fill="#8B96A8">
      Open for AI/ML architecture, geospatial systems &amp; high-impact products.
    </text>

    <!-- 4 Direct Channels Cards -->
    <g transform="translate(0, 84)">
      <!-- Card 1: GitHub -->
      <g transform="translate(0, 0)">
        <rect x="0" y="0" width="460" height="50" rx="8" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
        <text x="18" y="30" class="font-sans" font-size="15" fill="#FFFFFF">&#x2325;</text>
        <text x="44" y="23" class="font-display" font-size="13" font-weight="800" fill="#FFFFFF">GitHub</text>
        <text x="44" y="39" class="font-sans" font-size="11" font-weight="600" fill="#60A5FA">github.com/xnacro • Repositories &amp; Core Code</text>
        <g class="nudge-arrow"><text x="425" y="31" class="font-display" font-size="16" font-weight="900" fill="#2F86FF">→</text></g>
      </g>

      <!-- Card 2: LinkedIn -->
      <g transform="translate(0, 58)">
        <rect x="0" y="0" width="460" height="50" rx="8" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
        <text x="18" y="30" class="font-sans" font-size="14" font-weight="900" fill="#0A66C2">in</text>
        <text x="44" y="23" class="font-display" font-size="13" font-weight="800" fill="#FFFFFF">LinkedIn</text>
        <text x="44" y="39" class="font-sans" font-size="11" font-weight="600" fill="#60A5FA">linkedin.com/in/prince-tiwari-727375328</text>
        <g class="nudge-arrow"><text x="425" y="31" class="font-display" font-size="16" font-weight="900" fill="#2F86FF">→</text></g>
      </g>

      <!-- Card 3: Instagram -->
      <g transform="translate(0, 116)">
        <rect x="0" y="0" width="460" height="50" rx="8" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
        <text x="18" y="30" class="font-sans" font-size="14" fill="#FF3652">&#x1F4F8;</text>
        <text x="44" y="23" class="font-display" font-size="13" font-weight="800" fill="#FFFFFF">Instagram</text>
        <text x="44" y="39" class="font-sans" font-size="11" font-weight="600" fill="#FF7088">@am_princetiwari • Engineering &amp; Life</text>
        <g class="nudge-arrow"><text x="425" y="31" class="font-display" font-size="16" font-weight="900" fill="#FF3652">→</text></g>
      </g>

      <!-- Card 4: Email -->
      <g transform="translate(0, 174)">
        <rect x="0" y="0" width="460" height="50" rx="8" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
        <text x="18" y="30" class="font-sans" font-size="14" fill="#EA4335">&#x2709;</text>
        <text x="44" y="23" class="font-display" font-size="13" font-weight="800" fill="#FFFFFF">Direct Electronic Comms</text>
        <text x="44" y="39" class="font-sans" font-size="11" font-weight="600" fill="#60A5FA">businessofficialtech@gmail.com</text>
        <g class="nudge-arrow"><text x="425" y="31" class="font-display" font-size="16" font-weight="900" fill="#2F86FF">→</text></g>
      </g>
    </g>

    <!-- Bottom Guidance -->
    <text x="0" y="342" class="font-sans" font-size="10" font-weight="700" letter-spacing="1.5" fill="#64748B">CLICKABLE LINKS WIRED IN REPOSITORY DOCUMENT BELOW</text>
  </g>
</svg>'''

    files = {
        'assets/hero.svg': hero_svg,
        'assets/achievements.svg': achievements_svg,
        'assets/current-build.svg': current_build_svg,
        'assets/flagship.svg': flagship_svg,
        'assets/stack.svg': stack_svg,
        'assets/selected-builds.svg': selected_builds_svg,
        'assets/id-dashboard.svg': id_dashboard_svg,
        'assets/connect.svg': connect_svg,
    }

    for path, content in files.items():
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        # Validate XML
        try:
            ET.fromstring(content)
            print(f"Verified XML: {path} (OK)")
        except Exception as e:
            print(f"ERROR in {path}: {e}")

if __name__ == '__main__':
    build_all()
