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

def build_all():
    os.makedirs('assets', exist_ok=True)
    print("Encoding character assets...")
    mine_b64 = get_base64_png('assets/mine.png', 680)
    id_b64 = get_base64_png('assets/id.png', 720)

    # =========================================================================
    # 1. assets/hero.svg — Truthful Identity & Positioning
    # =========================================================================
    hero_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 940 450" width="100%" height="100%">
  <defs>
    <linearGradient id="hero-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070B16"/>
      <stop offset="50%" stop-color="#0B1325"/>
      <stop offset="100%" stop-color="#070B16"/>
    </linearGradient>
    <linearGradient id="hero-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2F86FF" stop-opacity="0.85"/>
      <stop offset="50%" stop-color="#2F86FF" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#FF3652" stop-opacity="0.65"/>
    </linearGradient>
    <linearGradient id="hero-title-blue" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#2F86FF"/>
      <stop offset="60%" stop-color="#60A5FA"/>
      <stop offset="100%" stop-color="#93C5FD"/>
    </linearGradient>
    <radialGradient id="hero-glow" cx="80%" cy="50%" r="55%">
      <stop offset="0%" stop-color="#2F86FF" stop-opacity="0.22"/>
      <stop offset="50%" stop-color="#2F86FF" stop-opacity="0.05"/>
      <stop offset="100%" stop-color="#070B16" stop-opacity="0"/>
    </radialGradient>
    <pattern id="hero-dots" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1.1" fill="#1C2B49" opacity="0.5"/>
    </pattern>
    <clipPath id="hero-portrait-clip">
      <rect x="530" y="28" width="375" height="394" rx="16"/>
    </clipPath>
  </defs>

  <style>
    @keyframes heroPulseDot {{
      0%, 100% {{ opacity: 1; transform: scale(1); }}
      50%      {{ opacity: 0.35; transform: scale(0.85); }}
    }}
    .hero-pulse {{
      animation: heroPulseDot 2.2s ease-in-out infinite;
      transform-origin: 38px 32px;
    }}
  </style>

  <!-- Container Box -->
  <rect x="0" y="0" width="940" height="450" rx="18" fill="url(#hero-bg)" stroke="url(#hero-border)" stroke-width="1.6"/>
  <rect x="0" y="0" width="940" height="450" rx="18" fill="url(#hero-dots)"/>
  <rect x="460" y="0" width="480" height="450" rx="18" fill="url(#hero-glow)"/>

  <!-- Top Metadata Bar -->
  <g transform="translate(36, 30)">
    <circle cx="6" cy="6" r="4.5" fill="#10B981" class="hero-pulse"/>
    <text x="18" y="10" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11" font-weight="800" letter-spacing="1.8" fill="#F0F6FC">ENGINEERING IDENTITY // XNACRO</text>
    <rect x="300" y="-3" width="160" height="19" rx="4" fill="#0C1B33" stroke="#2F86FF" stroke-width="0.8"/>
    <text x="310" y="10" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="9.5" font-weight="700" fill="#60A5FA">ACTIVE PRODUCTION</text>
    <text x="868" y="10" text-anchor="end" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11" font-weight="700" letter-spacing="1" fill="#8B96A8">MUZAFFARPUR, BIHAR, INDIA</text>
  </g>

  <!-- Left Content Column -->
  <g transform="translate(36, 80)">
    <!-- Eyebrow Subheading -->
    <text x="0" y="4" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="12" font-weight="800" letter-spacing="2" fill="#8B96A8">SOFTWARE ENGINEER • BUILDER</text>

    <!-- Greeting & Large Name -->
    <text x="0" y="38" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="16" font-weight="600" fill="#8B96A8">HI, I'M</text>
    <text x="0" y="94" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="58" font-weight="900" letter-spacing="-1.5" fill="#FFFFFF">PRINCE</text>
    <text x="0" y="152" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="58" font-weight="900" letter-spacing="-1.5" fill="url(#hero-title-blue)">TIWARI<tspan fill="#8B96A8" font-size="20" font-weight="500" letter-spacing="0"> (Prince Kumar)</tspan></text>

    <!-- Crimson Slash Bars + Mission Tag -->
    <g transform="translate(255, 66)">
      <rect x="0" y="0" width="4" height="24" rx="2" fill="#FF3652" transform="skewX(-20)"/>
      <rect x="9" y="0" width="4" height="24" rx="2" fill="#FF3652" transform="skewX(-20)"/>
      <rect x="18" y="0" width="4" height="24" rx="2" fill="#FF3652" transform="skewX(-20)"/>
      <text x="32" y="11" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11.5" font-weight="900" letter-spacing="1.5" fill="#FFFFFF">BUILD.</text>
      <text x="32" y="25" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11.5" font-weight="900" letter-spacing="1.5" fill="#FF3652">SURPASS.</text>
    </g>

    <!-- Clear Value Proposition -->
    <text x="0" y="196" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="15" font-weight="500" fill="#CBD5E1" line-height="24">
      <tspan x="0" dy="0">I build AI-powered products, full-stack systems,</tspan>
      <tspan x="0" dy="24">&amp; real-world spatial intelligence that actually ship.</tspan>
    </text>

    <!-- Truthful Identity Metadata Chips -->
    <g transform="translate(0, 260)">
      <rect x="0" y="0" width="85" height="28" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
      <text x="14" y="18" font-family="-apple-system, sans-serif" font-size="11.5" font-weight="700" fill="#F0F6FC">📍 INDIA</text>

      <rect x="95" y="0" width="95" height="28" rx="6" fill="#0C1527" stroke="#2F86FF" stroke-width="1.1"/>
      <text x="107" y="18" font-family="-apple-system, sans-serif" font-size="11.5" font-weight="700" fill="#60A5FA">🧠 AI / ML</text>

      <rect x="200" y="0" width="125" height="28" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
      <text x="212" y="18" font-family="-apple-system, sans-serif" font-size="11.5" font-weight="700" fill="#F0F6FC">⚡ FULL-STACK</text>

      <rect x="335" y="0" width="145" height="28" rx="6" fill="#0C1527" stroke="#FF3652" stroke-width="1.1"/>
      <text x="347" y="18" font-family="-apple-system, sans-serif" font-size="11.5" font-weight="700" fill="#FF8A9A">🚀 PRODUCT BUILDER</text>
    </g>

    <!-- Bottom Status Bar -->
    <g transform="translate(0, 304)">
      <rect x="0" y="0" width="480" height="26" rx="5" fill="#080E1C" stroke="#1E293B" stroke-width="1"/>
      <circle cx="12" cy="13" r="3.5" fill="#22C55E"/>
      <text x="22" y="17" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="10.5" font-weight="700" fill="#94A3B8">SPECIALIZATION: <tspan fill="#60A5FA">B.Tech CSE (AI &amp; ML)</tspan> • REPO: <tspan fill="#F1F5F9">github.com/xnacro</tspan></text>
    </g>
  </g>

  <!-- Right Portrait Column with Inlined Approved mine.png -->
  <g>
    <rect x="530" y="28" width="375" height="394" rx="16" fill="#0C1527" stroke="#1C2D4A" stroke-width="1.2"/>
    <g clip-path="url(#hero-portrait-clip)">
      <image href="data:image/png;base64,{mine_b64}" xlink:href="data:image/png;base64,{mine_b64}" x="525" y="16" width="385" height="415" preserveAspectRatio="xMidYMid meet"/>
    </g>
    <!-- Overlay Badge over portrait bottom -->
    <g transform="translate(675, 372)">
      <rect x="0" y="0" width="215" height="36" rx="8" fill="#0B1324" stroke="#2F86FF" stroke-width="1.3"/>
      <rect x="0" y="0" width="8" height="36" rx="4" fill="#2F86FF"/>
      <text x="18" y="16" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11" font-weight="800" fill="#FFFFFF">ENGINEER / BUILDER</text>
      <text x="18" y="29" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="9.5" font-weight="700" fill="#60A5FA">@xnacro • Muzaffarpur, India</text>
    </g>
  </g>
</svg>'''

    # =========================================================================
    # 2. assets/achievements.svg — Real Verified Credentials (Placed High!)
    # =========================================================================
    achievements_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 260" width="100%" height="100%">
  <defs>
    <linearGradient id="ach-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2F86FF" stop-opacity="0.6"/>
      <stop offset="50%" stop-color="#FF3652" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#2F86FF" stop-opacity="0.6"/>
    </linearGradient>
    <pattern id="ach-dots" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#1C2B49" opacity="0.4"/>
    </pattern>
  </defs>

  <rect x="0" y="0" width="940" height="260" rx="16" fill="#070B16" stroke="url(#ach-border)" stroke-width="1.3"/>
  <rect x="0" y="0" width="940" height="260" rx="16" fill="url(#ach-dots)"/>

  <!-- Top Section Tracker -->
  <g transform="translate(32, 22)">
    <text x="0" y="10" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="10.5" font-weight="800" letter-spacing="2" fill="#2F86FF">01 // VERIFIED RECOGNITION</text>
    <text x="0" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="20" font-weight="900" fill="#FFFFFF">PROVEN IN THE REAL WORLD<tspan fill="#FF3652">.</tspan></text>
    <text x="400" y="30" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="12" fill="#8B96A8">High-stakes national hackathons, innovation challenges &amp; active software platforms.</text>
  </g>

  <!-- 4 Visually Strong Credential Cards -->
  <g transform="translate(32, 74)">
    <!-- Card 1: Cognithon IIIT Bhagalpur -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="208" height="156" rx="10" fill="#0A1224" stroke="#2F86FF" stroke-width="1.2"/>
      <rect x="14" y="14" width="70" height="18" rx="4" fill="#12203A"/>
      <text x="22" y="27" font-family="-apple-system, sans-serif" font-size="9" font-weight="800" letter-spacing="1" fill="#60A5FA">01 / 2026</text>
      
      <text x="14" y="58" font-family="-apple-system, sans-serif" font-size="17" font-weight="900" fill="#FFFFFF">COGNITHON</text>
      <text x="14" y="74" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#8B96A8">IIIT Bhagalpur</text>

      <rect x="14" y="90" width="180" height="2" fill="#1A2D4E"/>
      
      <text x="14" y="116" font-family="-apple-system, sans-serif" font-size="20" font-weight="900" fill="#60A5FA">2ND PRIZE</text>
      <text x="14" y="136" font-family="-apple-system, sans-serif" font-size="10.5" fill="#8B96A8">National Hackathon</text>
    </g>

    <!-- Card 2: India Innovates 2026 -->
    <g transform="translate(222, 0)">
      <rect x="0" y="0" width="208" height="156" rx="10" fill="#0A1224" stroke="#FF3652" stroke-width="1.2"/>
      <rect x="14" y="14" width="70" height="18" rx="4" fill="#2A1422"/>
      <text x="22" y="27" font-family="-apple-system, sans-serif" font-size="9" font-weight="800" letter-spacing="1" fill="#FF8A9A">02 / 2026</text>
      
      <text x="14" y="58" font-family="-apple-system, sans-serif" font-size="17" font-weight="900" fill="#FFFFFF">INDIA INNOVATES</text>
      <text x="14" y="74" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#8B96A8">National Challenge</text>

      <rect x="14" y="90" width="180" height="2" fill="#3D1A2A"/>
      
      <text x="14" y="116" font-family="-apple-system, sans-serif" font-size="17" font-weight="900" fill="#FF3652">NATIONAL FINALIST</text>
      <text x="14" y="136" font-family="-apple-system, sans-serif" font-size="10.5" fill="#8B96A8">Civic &amp; Disaster Tech</text>
    </g>

    <!-- Card 3: Flipkart GRiD 2026 -->
    <g transform="translate(444, 0)">
      <rect x="0" y="0" width="208" height="156" rx="10" fill="#0A1224" stroke="#2F86FF" stroke-width="1.2"/>
      <rect x="14" y="14" width="70" height="18" rx="4" fill="#12203A"/>
      <text x="22" y="27" font-family="-apple-system, sans-serif" font-size="9" font-weight="800" letter-spacing="1" fill="#60A5FA">03 / 2026</text>
      
      <text x="14" y="58" font-family="-apple-system, sans-serif" font-size="17" font-weight="900" fill="#FFFFFF">FLIPKART GRiD</text>
      <text x="14" y="74" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#8B96A8">Engineering Track</text>

      <rect x="14" y="90" width="180" height="2" fill="#1A2D4E"/>
      
      <text x="14" y="116" font-family="-apple-system, sans-serif" font-size="17" font-weight="900" fill="#60A5FA">SEMI-FINALIST</text>
      <text x="14" y="136" font-family="-apple-system, sans-serif" font-size="10.5" fill="#8B96A8">National Flagship</text>
    </g>

    <!-- Card 4: Surakshaai.org Platform -->
    <g transform="translate(666, 0)">
      <rect x="0" y="0" width="208" height="156" rx="10" fill="#0A1224" stroke="#10B981" stroke-width="1.2"/>
      <rect x="14" y="14" width="70" height="18" rx="4" fill="#0F241F"/>
      <text x="22" y="27" font-family="-apple-system, sans-serif" font-size="9" font-weight="800" letter-spacing="1" fill="#34D399">04 / ACTIVE</text>
      
      <text x="14" y="58" font-family="-apple-system, sans-serif" font-size="17" font-weight="900" fill="#FFFFFF">SURAKSHAAI</text>
      <text x="14" y="74" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#8B96A8">surakshaai.org</text>

      <rect x="14" y="90" width="180" height="2" fill="#1A342B"/>
      
      <text x="14" y="116" font-family="-apple-system, sans-serif" font-size="17" font-weight="900" fill="#10B981">LIVE SYSTEM</text>
      <text x="14" y="136" font-family="-apple-system, sans-serif" font-size="10.5" fill="#8B96A8">Spatial AI Platform</text>
    </g>
  </g>
</svg>'''

    # =========================================================================
    # 3. assets/current-build.svg — 02 / NOW BUILDING
    # =========================================================================
    current_build_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 210" width="100%" height="100%">
  <defs>
    <linearGradient id="cb-border" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#2F86FF" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="#2F86FF" stop-opacity="0.15"/>
    </linearGradient>
    <pattern id="cb-grid" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#16223D" stroke-width="0.75" stroke-opacity="0.45"/>
    </pattern>
  </defs>

  <rect x="0" y="0" width="940" height="210" rx="14" fill="#070B16" stroke="url(#cb-border)" stroke-width="1.2"/>
  <rect x="0" y="0" width="940" height="210" rx="14" fill="url(#cb-grid)"/>

  <!-- Top bar -->
  <g transform="translate(30, 22)">
    <circle cx="5" cy="5" r="4" fill="#10B981"/>
    <text x="16" y="9" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11" font-weight="800" letter-spacing="1.8" fill="#2F86FF">02 // NOW BUILDING • ACTIVE FOCUS</text>
    <rect x="800" y="-3" width="95" height="20" rx="4" fill="#12203A"/>
    <text x="812" y="11" font-family="-apple-system, sans-serif" font-size="9.5" font-weight="800" fill="#22C55E">ACTIVE SHIP</text>
  </g>

  <!-- Left Column Card: SurakshaAI Focus -->
  <g transform="translate(30, 56)">
    <rect x="0" y="0" width="425" height="132" rx="10" fill="#0A1122" stroke="#1F2F4F" stroke-width="1"/>
    <text x="20" y="26" font-family="-apple-system, sans-serif" font-size="10" font-weight="800" letter-spacing="1" fill="#8B96A8">CURRENT PRODUCT FOCUS</text>
    <text x="20" y="52" font-family="-apple-system, sans-serif" font-size="19" font-weight="900" fill="#FFFFFF">SurakshaAI <tspan fill="#60A5FA" font-size="14" font-weight="700">• surakshaai.org</tspan></text>
    <text x="20" y="74" font-family="-apple-system, sans-serif" font-size="12.5" fill="#8B96A8">Turning real-world risk telemetry and street safety datasets into</text>
    <text x="20" y="92" font-family="-apple-system, sans-serif" font-size="12.5" fill="#8B96A8">actionable intelligence through the Dynamic Safety Index (DSI).</text>
    <g transform="translate(20, 104)">
      <rect x="0" y="0" width="85" height="18" rx="3" fill="#122442"/>
      <text x="8" y="13" font-family="-apple-system, sans-serif" font-size="9.5" font-weight="700" fill="#60A5FA">SPATIAL AI</text>
      <rect x="95" y="0" width="105" height="18" rx="3" fill="#122442"/>
      <text x="103" y="13" font-family="-apple-system, sans-serif" font-size="9.5" font-weight="700" fill="#60A5FA">MICROSERVICES</text>
    </g>
  </g>

  <!-- Right Column Card: Current Technical Sprint -->
  <g transform="translate(475, 56)">
    <rect x="0" y="0" width="435" height="132" rx="10" fill="#0A1122" stroke="#1F2F4F" stroke-width="1"/>
    <text x="20" y="26" font-family="-apple-system, sans-serif" font-size="10" font-weight="800" letter-spacing="1" fill="#8B96A8">TECHNICAL CAPABILITY SPRINT</text>
    
    <text x="20" y="54" font-family="-apple-system, sans-serif" font-size="13" font-weight="800" fill="#F5F7FA">Spatial AI Models:</text>
    <text x="145" y="54" font-family="-apple-system, sans-serif" font-size="13" fill="#8B96A8">Dynamic Safety Index, multi-tier hazard heatmaps</text>

    <text x="20" y="80" font-family="-apple-system, sans-serif" font-size="13" font-weight="800" fill="#F5F7FA">Architecture:</text>
    <text x="145" y="80" font-family="-apple-system, sans-serif" font-size="13" fill="#8B96A8">Node.js orchestrator + decoupled FastAPI ML inference</text>

    <text x="20" y="106" font-family="-apple-system, sans-serif" font-size="13" font-weight="800" fill="#F5F7FA">Availability:</text>
    <text x="145" y="106" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#22C55E">Open for AI/ML &amp; Full-Stack engineering teams</text>
  </g>
</svg>'''

    # =========================================================================
    # 4. assets/flagship.svg — 03 / FLAGSHIP SYSTEM (SurakshaAI Visual Card)
    # =========================================================================
    flagship_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 440" width="100%" height="100%">
  <defs>
    <linearGradient id="fl-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2F86FF" stop-opacity="0.85"/>
      <stop offset="50%" stop-color="#0A1224" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#FF3652" stop-opacity="0.7"/>
    </linearGradient>
    <pattern id="fl-grid" width="22" height="22" patternUnits="userSpaceOnUse">
      <path d="M 22 0 L 0 0 0 22" fill="none" stroke="#162544" stroke-width="0.8" stroke-opacity="0.6"/>
    </pattern>
  </defs>

  <rect x="0" y="0" width="940" height="440" rx="16" fill="#070B16" stroke="url(#fl-border)" stroke-width="1.5"/>
  <rect x="0" y="0" width="940" height="440" rx="16" fill="url(#fl-grid)"/>

  <!-- Top Badges -->
  <g transform="translate(32, 26)">
    <rect x="0" y="0" width="175" height="22" rx="4" fill="#14284D" stroke="#2F86FF" stroke-width="0.8"/>
    <text x="12" y="15" font-family="-apple-system, sans-serif" font-size="10" font-weight="800" fill="#60A5FA">03 // FLAGSHIP SYSTEM</text>

    <rect x="188" y="0" width="160" height="22" rx="4" fill="#2B1424" stroke="#FF3652" stroke-width="0.8"/>
    <text x="198" y="15" font-family="-apple-system, sans-serif" font-size="10" font-weight="800" fill="#FF8A9A">SPATIAL AI PLATFORM</text>

    <text x="876" y="16" text-anchor="end" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#8B96A8">STATUS: ACTIVE PRODUCTION</text>
  </g>

  <!-- Title & Real Value Proposition -->
  <g transform="translate(32, 75)">
    <text x="0" y="24" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="28" font-weight="900" fill="#FFFFFF">SurakshaAI</text>
    <text x="170" y="24" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="17" font-weight="600" fill="#8B96A8">• Real-Time Safety Intelligence Platform</text>
    
    <text x="0" y="52" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13.5" fill="#CBD5E1">
      AI-driven geospatial analytics computing a <tspan fill="#2F86FF" font-weight="700">Dynamic Safety Index (DSI)</tspan> to replace static, reactive crime tables
    </text>
    <text x="0" y="72" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13.5" fill="#CBD5E1">
      with predictive risk forecasts and hazard-aware mobility guidance across real-world streets.
    </text>
  </g>

  <!-- 4 Architectural Modules (Product Case Study Fragment) -->
  <g transform="translate(32, 178)">
    <!-- Box 1: Dynamic Heatmap -->
    <rect x="0" y="0" width="206" height="150" rx="8" fill="#0A1122" stroke="#1F2F4F" stroke-width="1"/>
    <circle cx="24" cy="24" r="10" fill="#14284D"/>
    <text x="19" y="29" font-family="-apple-system, sans-serif" font-size="13" font-weight="900" fill="#2F86FF">1</text>
    <text x="14" y="62" font-family="-apple-system, sans-serif" font-size="13.5" font-weight="800" fill="#F5F7FA">Spatial Heatmaps</text>
    <text x="14" y="82" font-family="-apple-system, sans-serif" font-size="11" fill="#8B96A8">Multi-level risk gradients</text>
    <text x="14" y="98" font-family="-apple-system, sans-serif" font-size="11" fill="#8B96A8">(District → Ward → Grid)</text>
    <rect x="14" y="118" width="120" height="20" rx="3" fill="#102038"/>
    <text x="22" y="132" font-family="-apple-system, sans-serif" font-size="9.5" font-weight="700" fill="#60A5FA">MapLibre GL • Leaflet</text>

    <!-- Box 2: ML Engine -->
    <rect x="224" y="0" width="206" height="150" rx="8" fill="#0A1122" stroke="#1F2F4F" stroke-width="1"/>
    <circle cx="24" cy="24" r="10" fill="#14284D"/>
    <text x="19" y="29" font-family="-apple-system, sans-serif" font-size="13" font-weight="900" fill="#2F86FF">2</text>
    <text x="14" y="62" font-family="-apple-system, sans-serif" font-size="13.5" font-weight="800" fill="#F5F7FA">ML Microservice</text>
    <text x="14" y="82" font-family="-apple-system, sans-serif" font-size="11" fill="#8B96A8">FastAPI endpoint,</text>
    <text x="14" y="98" font-family="-apple-system, sans-serif" font-size="11" fill="#8B96A8">RandomForest risk forecast</text>
    <rect x="14" y="118" width="130" height="20" rx="3" fill="#102038"/>
    <text x="22" y="132" font-family="-apple-system, sans-serif" font-size="9.5" font-weight="700" fill="#60A5FA">FastAPI • Scikit-learn</text>

    <!-- Box 3: NLP Signals -->
    <rect x="448" y="0" width="206" height="150" rx="8" fill="#0A1122" stroke="#1F2F4F" stroke-width="1"/>
    <circle cx="24" cy="24" r="10" fill="#2B1424"/>
    <text x="19" y="29" font-family="-apple-system, sans-serif" font-size="13" font-weight="900" fill="#FF3652">3</text>
    <text x="14" y="62" font-family="-apple-system, sans-serif" font-size="13.5" font-weight="800" fill="#F5F7FA">NLP Live Signals</text>
    <text x="14" y="82" font-family="-apple-system, sans-serif" font-size="11" fill="#8B96A8">Real-time local incident</text>
    <text x="14" y="98" font-family="-apple-system, sans-serif" font-size="11" fill="#8B96A8">geolocation &amp; severity tag</text>
    <rect x="14" y="118" width="130" height="20" rx="3" fill="#2E1624"/>
    <text x="22" y="132" font-family="-apple-system, sans-serif" font-size="9.5" font-weight="700" fill="#FF8A9A">NLP • Live Streams</text>

    <!-- Box 4: Safe Navigation -->
    <rect x="672" y="0" width="204" height="150" rx="8" fill="#0A1122" stroke="#1F2F4F" stroke-width="1"/>
    <circle cx="24" cy="24" r="10" fill="#122A22"/>
    <text x="19" y="29" font-family="-apple-system, sans-serif" font-size="13" font-weight="900" fill="#22C55E">4</text>
    <text x="14" y="62" font-family="-apple-system, sans-serif" font-size="13.5" font-weight="800" fill="#F5F7FA">Safe Navigation</text>
    <text x="14" y="82" font-family="-apple-system, sans-serif" font-size="11" fill="#8B96A8">Lowest-risk waypoint route,</text>
    <text x="14" y="98" font-family="-apple-system, sans-serif" font-size="11" fill="#8B96A8">Guardian SOS alert session</text>
    <rect x="14" y="118" width="130" height="20" rx="3" fill="#0E241B"/>
    <text x="22" y="132" font-family="-apple-system, sans-serif" font-size="9.5" font-weight="700" fill="#34D399">Node.js • Redis • SOS</text>
  </g>

  <!-- Bottom Architecture Pill Strip -->
  <g transform="translate(32, 362)">
    <rect x="0" y="0" width="876" height="50" rx="8" fill="#080E1C" stroke="#162544" stroke-width="1"/>
    <text x="18" y="29" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" fill="#8B96A8">ENGINEERING STACK:</text>
    
    <rect x="175" y="13" width="70" height="24" rx="4" fill="#12203A"/>
    <text x="184" y="29" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#F5F7FA">Node.js</text>

    <rect x="255" y="13" width="75" height="24" rx="4" fill="#12203A"/>
    <text x="264" y="29" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#F5F7FA">FastAPI</text>

    <rect x="340" y="13" width="95" height="24" rx="4" fill="#12203A"/>
    <text x="349" y="29" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#F5F7FA">Scikit-learn</text>

    <rect x="445" y="13" width="105" height="24" rx="4" fill="#12203A"/>
    <text x="454" y="29" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#F5F7FA">MapLibre GL</text>

    <rect x="560" y="13" width="75" height="24" rx="4" fill="#12203A"/>
    <text x="570" y="29" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#F5F7FA">PostGIS</text>

    <rect x="645" y="13" width="60" height="24" rx="4" fill="#12203A"/>
    <text x="655" y="29" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#F5F7FA">Redis</text>

    <rect x="715" y="13" width="145" height="24" rx="4" fill="#152F24"/>
    <text x="725" y="29" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#22C55E">&#x2714; REPO VERIFIED</text>
  </g>
</svg>'''

    # =========================================================================
    # 5. assets/selected-builds.svg — 04 / SELECTED BUILDS (No Boring Table!)
    # =========================================================================
    selected_builds_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 520" width="100%" height="100%">
  <defs>
    <linearGradient id="sb-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2F86FF" stop-opacity="0.6"/>
      <stop offset="50%" stop-color="#FF3652" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#2F86FF" stop-opacity="0.6"/>
    </linearGradient>
    <pattern id="sb-dots" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#1C2B49" opacity="0.4"/>
    </pattern>
  </defs>

  <rect x="0" y="0" width="940" height="520" rx="16" fill="#070B16" stroke="url(#sb-border)" stroke-width="1.3"/>
  <rect x="0" y="0" width="940" height="520" rx="16" fill="url(#sb-dots)"/>

  <!-- Top bar -->
  <g transform="translate(32, 24)">
    <text x="0" y="10" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="10.5" font-weight="800" letter-spacing="2" fill="#2F86FF">04 // SELECTED BUILDS • RECENT SYSTEMS</text>
    <text x="0" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="22" font-weight="900" fill="#FFFFFF">PRODUCTION SYSTEMS &amp; COMPETITIVE WORK<tspan fill="#FF3652">.</tspan></text>
    <text x="560" y="30" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11.5" fill="#8B96A8">Presented as engineered architectures, not raw tables.</text>
  </g>

  <!-- 4 Alternating Project Modules -->
  <g transform="translate(32, 78)">

    <!-- BUILD 01: RESQ -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="425" height="195" rx="10" fill="#0A1122" stroke="#1F2F4F" stroke-width="1"/>
      <text x="18" y="24" font-family="-apple-system, sans-serif" font-size="9.5" font-weight="800" letter-spacing="1" fill="#2F86FF">BUILD // 01 • INDIA INNOVATES</text>
      
      <text x="18" y="52" font-family="-apple-system, sans-serif" font-size="20" font-weight="900" fill="#FFFFFF">RESQ</text>
      <text x="75" y="52" font-family="-apple-system, sans-serif" font-size="12" font-weight="600" fill="#8B96A8">• Disaster Relief Routing Engine</text>

      <text x="18" y="78" font-family="-apple-system, sans-serif" font-size="12.5" fill="#CBD5E1">
        Damage-aware supply chain routing across natural disaster zones,
      </text>
      <text x="18" y="96" font-family="-apple-system, sans-serif" font-size="12.5" fill="#CBD5E1">
        assessing road risk surfaces via Valhalla dynamic cost-weighted routing.
      </text>

      <g transform="translate(18, 116)">
        <text x="0" y="10" font-family="-apple-system, sans-serif" font-size="10" font-weight="800" fill="#8B96A8">STACK:</text>
        <rect x="45" y="-3" width="95" height="18" rx="3" fill="#12203A"/><text x="53" y="10" font-family="-apple-system, sans-serif" font-size="9.5" font-weight="700" fill="#60A5FA">PostGIS Grids</text>
        <rect x="148" y="-3" width="75" height="18" rx="3" fill="#12203A"/><text x="156" y="10" font-family="-apple-system, sans-serif" font-size="9.5" font-weight="700" fill="#60A5FA">Valhalla</text>
        <rect x="230" y="-3" width="65" height="18" rx="3" fill="#12203A"/><text x="238" y="10" font-family="-apple-system, sans-serif" font-size="9.5" font-weight="700" fill="#60A5FA">Python</text>
      </g>

      <g transform="translate(18, 154)">
        <text x="0" y="14" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#8B96A8">SCALE: 408k cell hazard surface in PostGIS</text>
        <text x="270" y="14" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" fill="#2F86FF">VIEW REPO →</text>
      </g>
    </g>

    <!-- BUILD 02: GridShare -->
    <g transform="translate(450, 0)">
      <rect x="0" y="0" width="425" height="195" rx="10" fill="#0A1122" stroke="#1F2F4F" stroke-width="1"/>
      <text x="18" y="24" font-family="-apple-system, sans-serif" font-size="9.5" font-weight="800" letter-spacing="1" fill="#FF3652">BUILD // 02 • IIT GUWAHATI</text>
      
      <text x="18" y="52" font-family="-apple-system, sans-serif" font-size="20" font-weight="900" fill="#FFFFFF">GridShare</text>
      <text x="120" y="52" font-family="-apple-system, sans-serif" font-size="12" font-weight="600" fill="#8B96A8">• Community Microgrid</text>

      <text x="18" y="78" font-family="-apple-system, sans-serif" font-size="12.5" fill="#CBD5E1">
        Intelligent coordination layer for neighborhood solar, battery &amp;
      </text>
      <text x="18" y="96" font-family="-apple-system, sans-serif" font-size="12.5" fill="#CBD5E1">
        EV storage, optimizing decentralized P2P energy balancing in real time.
      </text>

      <g transform="translate(18, 116)">
        <text x="0" y="10" font-family="-apple-system, sans-serif" font-size="10" font-weight="800" fill="#8B96A8">STACK:</text>
        <rect x="45" y="-3" width="75" height="18" rx="3" fill="#12203A"/><text x="53" y="10" font-family="-apple-system, sans-serif" font-size="9.5" font-weight="700" fill="#60A5FA">Distributed</text>
        <rect x="128" y="-3" width="60" height="18" rx="3" fill="#12203A"/><text x="136" y="10" font-family="-apple-system, sans-serif" font-size="9.5" font-weight="700" fill="#60A5FA">Node.js</text>
        <rect x="195" y="-3" width="55" height="18" rx="3" fill="#12203A"/><text x="203" y="10" font-family="-apple-system, sans-serif" font-size="9.5" font-weight="700" fill="#60A5FA">React</text>
      </g>

      <g transform="translate(18, 154)">
        <text x="0" y="14" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#8B96A8">FLAGSHIP HACKATHON BUILD</text>
        <text x="270" y="14" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" fill="#FF3652">VIEW REPO →</text>
      </g>
    </g>

    <!-- BUILD 03: MednormAI -->
    <g transform="translate(0, 215)">
      <rect x="0" y="0" width="425" height="195" rx="10" fill="#0A1122" stroke="#1F2F4F" stroke-width="1"/>
      <text x="18" y="24" font-family="-apple-system, sans-serif" font-size="9.5" font-weight="800" letter-spacing="1" fill="#A855F7">BUILD // 03 • IIT PATNA × JILO HEALTH</text>
      
      <text x="18" y="52" font-family="-apple-system, sans-serif" font-size="20" font-weight="900" fill="#FFFFFF">MednormAI</text>
      <text x="145" y="52" font-family="-apple-system, sans-serif" font-size="12" font-weight="600" fill="#8B96A8">• Clinical Data Engine</text>

      <text x="18" y="78" font-family="-apple-system, sans-serif" font-size="12.5" fill="#CBD5E1">
        AI-powered data normalization pipeline using OCR &amp; NLP to parse
      </text>
      <text x="18" y="96" font-family="-apple-system, sans-serif" font-size="12.5" fill="#CBD5E1">
        unstructured medical PDFs and lab bills into structured health data.
      </text>

      <g transform="translate(18, 116)">
        <text x="0" y="10" font-family="-apple-system, sans-serif" font-size="10" font-weight="800" fill="#8B96A8">STACK:</text>
        <rect x="45" y="-3" width="70" height="18" rx="3" fill="#241634"/><text x="53" y="10" font-family="-apple-system, sans-serif" font-size="9.5" font-weight="700" fill="#D8B4FE">OCR • NLP</text>
        <rect x="122" y="-3" width="60" height="18" rx="3" fill="#12203A"/><text x="130" y="10" font-family="-apple-system, sans-serif" font-size="9.5" font-weight="700" fill="#60A5FA">Python</text>
        <rect x="189" y="-3" width="75" height="18" rx="3" fill="#12203A"/><text x="197" y="10" font-family="-apple-system, sans-serif" font-size="9.5" font-weight="700" fill="#60A5FA">FastAPI</text>
      </g>

      <g transform="translate(18, 154)">
        <text x="0" y="14" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#8B96A8">TRACK 2 HACKMATRIX 2.0</text>
        <text x="270" y="14" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" fill="#A855F7">VIEW REPO →</text>
      </g>
    </g>

    <!-- BUILD 04: OpenRAG -->
    <g transform="translate(450, 215)">
      <rect x="0" y="0" width="425" height="195" rx="10" fill="#0A1122" stroke="#1F2F4F" stroke-width="1"/>
      <text x="18" y="24" font-family="-apple-system, sans-serif" font-size="9.5" font-weight="800" letter-spacing="1" fill="#10B981">BUILD // 04 • AI PIPELINE</text>
      
      <text x="18" y="52" font-family="-apple-system, sans-serif" font-size="20" font-weight="900" fill="#FFFFFF">OpenRAG</text>
      <text x="115" y="52" font-family="-apple-system, sans-serif" font-size="12" font-weight="600" fill="#8B96A8">• Enterprise RAG System</text>

      <text x="18" y="78" font-family="-apple-system, sans-serif" font-size="12.5" fill="#CBD5E1">
        End-to-end Retrieval-Augmented Generation pipeline with dense
      </text>
      <text x="18" y="96" font-family="-apple-system, sans-serif" font-size="12.5" fill="#CBD5E1">
        document embeddings, vector indexing &amp; semantic hybrid retrieval.
      </text>

      <g transform="translate(18, 116)">
        <text x="0" y="10" font-family="-apple-system, sans-serif" font-size="10" font-weight="800" fill="#8B96A8">STACK:</text>
        <rect x="45" y="-3" width="60" height="18" rx="3" fill="#12203A"/><text x="53" y="10" font-family="-apple-system, sans-serif" font-size="9.5" font-weight="700" fill="#60A5FA">PyTorch</text>
        <rect x="112" y="-3" width="75" height="18" rx="3" fill="#12203A"/><text x="120" y="10" font-family="-apple-system, sans-serif" font-size="9.5" font-weight="700" fill="#60A5FA">Vector DB</text>
        <rect x="194" y="-3" width="75" height="18" rx="3" fill="#12203A"/><text x="202" y="10" font-family="-apple-system, sans-serif" font-size="9.5" font-weight="700" fill="#60A5FA">LangChain</text>
      </g>

      <g transform="translate(18, 154)">
        <text x="0" y="14" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#8B96A8">SEMANTIC RETRIEVAL PIPELINE</text>
        <text x="270" y="14" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" fill="#10B981">VIEW REPO →</text>
      </g>
    </g>

  </g>
</svg>'''

    # =========================================================================
    # 6. assets/stack.svg — 05 / ENGINE ROOM (Planetary Orbital System & AI/ML)
    # =========================================================================
    stack_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 550" width="100%" height="100%">
  <defs>
    <linearGradient id="stk-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070B16"/>
      <stop offset="60%" stop-color="#091225"/>
      <stop offset="100%" stop-color="#070B16"/>
    </linearGradient>
    <linearGradient id="stk-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2F86FF" stop-opacity="0.85"/>
      <stop offset="50%" stop-color="#A855F7" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#FF3652" stop-opacity="0.65"/>
    </linearGradient>
    <radialGradient id="sun-glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#2F86FF" stop-opacity="0.95"/>
      <stop offset="35%" stop-color="#2F86FF" stop-opacity="0.4"/>
      <stop offset="70%" stop-color="#A855F7" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#070B16" stop-opacity="0"/>
    </radialGradient>
    <pattern id="stk-dots" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1.1" fill="#1C2B49" opacity="0.45"/>
    </pattern>
  </defs>

  <style>
    @keyframes orbitPulse {{
      0%, 100% {{ transform: scale(1); filter: drop-shadow(0 0 6px rgba(47, 134, 255, 0.6)); }}
      50%      {{ transform: scale(1.05); filter: drop-shadow(0 0 16px rgba(47, 134, 255, 0.9)); }}
    }}
    .core-sun {{
      animation: orbitPulse 3.5s ease-in-out infinite;
      transform-origin: 205px 285px;
    }}
  </style>

  <rect x="0" y="0" width="940" height="550" rx="18" fill="url(#stk-bg)" stroke="url(#stk-border)" stroke-width="1.6"/>
  <rect x="0" y="0" width="940" height="550" rx="18" fill="url(#stk-dots)"/>

  <!-- Top Title Header with Sleek Modern Subheading Font -->
  <g transform="translate(36, 28)">
    <text x="0" y="10" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11" font-weight="800" letter-spacing="2" fill="#2F86FF">05 // THE ENGINE ROOM • VERIFIED TOOLCHAIN</text>
    <text x="0" y="38" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="24" font-weight="900" fill="#FFFFFF">TOOLS CHANGE. CURIOSITY DOESN'T<tspan fill="#FF3652">.</tspan></text>
    <text x="0" y="58" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11" font-weight="700" letter-spacing="1.5" fill="#60A5FA">AI &amp; MACHINE LEARNING • SPATIAL RUNTIMES • DISTRIBUTED INFRASTRUCTURE</text>
  </g>

  <!-- ================= LEFT: COMPLETE PLANETARY ORBITAL SYSTEM ================= -->
  <g transform="translate(0, 0)">
    <!-- Orbit 1: Inner Orbit (Python / AI Core) - Radius 68 -->
    <ellipse cx="205" cy="285" rx="68" ry="60" fill="none" stroke="#2F86FF" stroke-width="1.2" stroke-opacity="0.35" stroke-dasharray="4,4" transform="rotate(-15 205 285)"/>

    <!-- Orbit 2: Machine Learning Tensor Orbit - Ellipse rx=108, ry=78, deg=28 -->
    <ellipse cx="205" cy="285" rx="108" ry="78" fill="none" stroke="#A855F7" stroke-width="1.2" stroke-opacity="0.3" stroke-dasharray="5,4" transform="rotate(28 205 285)"/>

    <!-- Orbit 3: Frontend & Spatial Visualizer Orbit - Ellipse rx=142, ry=68, deg=-32 -->
    <ellipse cx="205" cy="285" rx="142" ry="68" fill="none" stroke="#2F86FF" stroke-width="1.2" stroke-opacity="0.35" stroke-dasharray="6,4" transform="rotate(-32 205 285)"/>

    <!-- Orbit 4: PostGIS & Geospatial Hazard Orbit - Ellipse rx=172, ry=92, deg=45 -->
    <ellipse cx="205" cy="285" rx="172" ry="92" fill="none" stroke="#FF3652" stroke-width="1.2" stroke-opacity="0.35" stroke-dasharray="5,5" transform="rotate(45 205 285)"/>

    <!-- Orbit 5: High-Concurrency Backend Orbit - Ellipse rx=194, ry=104, deg=-58 -->
    <ellipse cx="205" cy="285" rx="194" ry="104" fill="none" stroke="#10B981" stroke-width="1.2" stroke-opacity="0.3" stroke-dasharray="6,5" transform="rotate(-58 205 285)"/>

    <!-- Ambient Orbital Particle Stars -->
    <circle cx="150" cy="205" r="1.5" fill="#60A5FA" opacity="0.6"><animate attributeName="opacity" values="0.2;0.8;0.2" dur="2s" repeatCount="indefinite"/></circle>
    <circle cx="270" cy="355" r="1.5" fill="#A855F7" opacity="0.7"><animate attributeName="opacity" values="0.3;0.9;0.3" dur="2.7s" repeatCount="indefinite"/></circle>
    <circle cx="85" cy="295" r="1.5" fill="#FF3652" opacity="0.6"><animate attributeName="opacity" values="0.2;0.7;0.2" dur="3.2s" repeatCount="indefinite"/></circle>
    <circle cx="320" cy="235" r="1.5" fill="#10B981" opacity="0.5"><animate attributeName="opacity" values="0.1;0.8;0.1" dur="2.4s" repeatCount="indefinite"/></circle>

    <!-- CENTRAL GLOWING SUN / CORE (PT - Prince Tiwari Identity Core) -->
    <g class="core-sun">
      <!-- Outer Corona Glow -->
      <circle cx="205" cy="285" r="44" fill="url(#sun-glow)"/>
      <circle cx="205" cy="285" r="32" fill="none" stroke="#60A5FA" stroke-width="1.2" stroke-dasharray="3,3" opacity="0.7">
        <animateTransform attributeName="transform" type="rotate" from="0 205 285" to="360 205 285" dur="18s" repeatCount="indefinite"/>
      </circle>
      <!-- Sun Core Badge -->
      <rect x="180" y="260" width="50" height="50" rx="12" fill="#09142A" stroke="#2F86FF" stroke-width="2"/>
      <text x="205" y="289" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="18" font-weight="900" fill="#FFFFFF">PT</text>
      <text x="205" y="302" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="7.5" font-weight="800" fill="#60A5FA" letter-spacing="1">CORE</text>
    </g>

    <!-- PLANETARY REVOLVING BODIES -->

    <!-- PLANET 1: Python / AI (Inner Orbit - 12s Period) -->
    <g>
      <animateTransform attributeName="transform" type="rotate" from="0 205 285" to="360 205 285" dur="12s" repeatCount="indefinite"/>
      <g transform="translate(205, 221)">
        <animateTransform attributeName="transform" type="rotate" from="0 0 0" to="-360 0 0" dur="12s" repeatCount="indefinite"/>
        <circle cx="0" cy="0" r="16" fill="#08152B" stroke="#2F86FF" stroke-width="1.6"/>
        <circle cx="0" cy="0" r="19" fill="none" stroke="#2F86FF" stroke-width="0.8" stroke-opacity="0.4"/>
        <text x="0" y="4" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="9.5" font-weight="900" fill="#60A5FA">Py</text>
        <!-- Orbiting PyTorch Moon -->
        <g>
          <animateTransform attributeName="transform" type="rotate" from="0 0 0" to="360 0 0" dur="3s" repeatCount="indefinite"/>
          <circle cx="23" cy="0" r="3.5" fill="#EF4444"/>
        </g>
      </g>
    </g>

    <!-- PLANET 2: PyTorch / Machine Learning (Mid Orbit - 18s Period) -->
    <g>
      <animateTransform attributeName="transform" type="rotate" from="90 205 285" to="450 205 285" dur="18s" repeatCount="indefinite"/>
      <g transform="translate(295, 260)">
        <animateTransform attributeName="transform" type="rotate" from="0 0 0" to="-360 0 0" dur="18s" repeatCount="indefinite"/>
        <circle cx="0" cy="0" r="16" fill="#170F28" stroke="#A855F7" stroke-width="1.6"/>
        <circle cx="0" cy="0" r="19" fill="none" stroke="#A855F7" stroke-width="0.8" stroke-opacity="0.4"/>
        <text x="0" y="4" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="9.5" font-weight="900" fill="#D8B4FE">ML</text>
      </g>
    </g>

    <!-- PLANET 3: React / Frontend (Mid-Outer Orbit - 24s Period) -->
    <g>
      <animateTransform attributeName="transform" type="rotate" from="210 205 285" to="570 205 285" dur="24s" repeatCount="indefinite"/>
      <g transform="translate(90, 265)">
        <animateTransform attributeName="transform" type="rotate" from="0 0 0" to="-360 0 0" dur="24s" repeatCount="indefinite"/>
        <circle cx="0" cy="0" r="16" fill="#07152B" stroke="#2F86FF" stroke-width="1.6"/>
        <circle cx="0" cy="0" r="19" fill="none" stroke="#2F86FF" stroke-width="0.8" stroke-opacity="0.4"/>
        <text x="0" y="4" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="9.5" font-weight="900" fill="#93C5FD">Re</text>
      </g>
    </g>

    <!-- PLANET 4: PostGIS / Spatial Intelligence (Outer Orbit - 30s Counter Period) -->
    <g>
      <animateTransform attributeName="transform" type="rotate" from="360 205 285" to="0 205 285" dur="30s" repeatCount="indefinite"/>
      <g transform="translate(125, 385)">
        <animateTransform attributeName="transform" type="rotate" from="0 0 0" to="360 0 0" dur="30s" repeatCount="indefinite"/>
        <circle cx="0" cy="0" r="16" fill="#1C0E1E" stroke="#FF3652" stroke-width="1.6"/>
        <circle cx="0" cy="0" r="19" fill="none" stroke="#FF3652" stroke-width="0.8" stroke-opacity="0.4"/>
        <text x="0" y="4" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="9" font-weight="900" fill="#FFA3AF">GIS</text>
      </g>
    </g>

    <!-- PLANET 5: FastAPI / Scalable Microservices (Deep Orbit - 36s Period) -->
    <g>
      <animateTransform attributeName="transform" type="rotate" from="300 205 285" to="660 205 285" dur="36s" repeatCount="indefinite"/>
      <g transform="translate(320, 370)">
        <animateTransform attributeName="transform" type="rotate" from="0 0 0" to="-360 0 0" dur="36s" repeatCount="indefinite"/>
        <circle cx="0" cy="0" r="16" fill="#0A1D1A" stroke="#10B981" stroke-width="1.6"/>
        <circle cx="0" cy="0" r="19" fill="none" stroke="#10B981" stroke-width="0.8" stroke-opacity="0.4"/>
        <text x="0" y="4" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="9" font-weight="900" fill="#6EE7B7">API</text>
      </g>
    </g>

    <!-- Left Footnote -->
    <text x="205" y="495" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="10" font-weight="800" letter-spacing="1.5" fill="#64748B">PLANETARY RUNTIME • CONTINUOUS ORBITAL SHIP CYCLE</text>
  </g>

  <!-- ================= RIGHT: COMPLETE TECH STACK WITH DEDICATED AI/ML IDENTITY ================= -->
  <g transform="translate(425, 95)">

    <!-- Section 01: AI & Machine Learning (PROMINENT DEDICATED IDENTITY) -->
    <g transform="translate(0, 0)">
      <text x="0" y="11" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="10.5" font-weight="800" letter-spacing="1.8" fill="#C084FC">01 // AI &amp; MACHINE LEARNING SYSTEMS</text>
      <g transform="translate(0, 20)">
        <!-- Python -->
        <g transform="translate(0, 0)">
          <rect x="0" y="0" width="85" height="30" rx="6" fill="#160C26" stroke="#A855F7" stroke-width="1.2"/>
          <text x="12" y="19" font-family="-apple-system, sans-serif" font-size="11.5" font-weight="800" fill="#E9D5FF">Python</text>
        </g>
        <!-- PyTorch -->
        <g transform="translate(93, 0)">
          <rect x="0" y="0" width="85" height="30" rx="6" fill="#160C26" stroke="#A855F7" stroke-width="1.2"/>
          <text x="12" y="19" font-family="-apple-system, sans-serif" font-size="11.5" font-weight="800" fill="#E9D5FF">PyTorch</text>
        </g>
        <!-- Scikit-learn -->
        <g transform="translate(186, 0)">
          <rect x="0" y="0" width="105" height="30" rx="6" fill="#160C26" stroke="#A855F7" stroke-width="1.2"/>
          <text x="12" y="19" font-family="-apple-system, sans-serif" font-size="11.5" font-weight="800" fill="#E9D5FF">Scikit-learn</text>
        </g>
        <!-- TensorFlow -->
        <g transform="translate(299, 0)">
          <rect x="0" y="0" width="100" height="30" rx="6" fill="#160C26" stroke="#A855F7" stroke-width="1.2"/>
          <text x="12" y="19" font-family="-apple-system, sans-serif" font-size="11.5" font-weight="800" fill="#E9D5FF">TensorFlow</text>
        </g>
        <!-- OpenCV -->
        <g transform="translate(407, 0)">
          <rect x="0" y="0" width="75" height="30" rx="6" fill="#160C26" stroke="#A855F7" stroke-width="1.2"/>
          <text x="10" y="19" font-family="-apple-system, sans-serif" font-size="11.5" font-weight="800" fill="#E9D5FF">OpenCV</text>
        </g>

        <!-- Row 2 of ML: NumPy, Pandas, Transformers, LangChain, FastAPI -->
        <g transform="translate(0, 36)">
          <rect x="0" y="0" width="85" height="26" rx="5" fill="#160C26" stroke="#A855F7" stroke-width="0.8"/>
          <text x="12" y="17" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#D8B4FE">NumPy</text>

          <rect x="93" y="0" width="85" height="26" rx="5" fill="#160C26" stroke="#A855F7" stroke-width="0.8"/>
          <text x="12" y="17" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#D8B4FE">Pandas</text>

          <rect x="186" y="0" width="105" height="26" rx="5" fill="#160C26" stroke="#A855F7" stroke-width="0.8"/>
          <text x="12" y="17" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#D8B4FE">Transformers</text>

          <rect x="299" y="0" width="95" height="26" rx="5" fill="#160C26" stroke="#A855F7" stroke-width="0.8"/>
          <text x="12" y="17" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#D8B4FE">LangChain</text>

          <rect x="402" y="0" width="80" height="26" rx="5" fill="#160C26" stroke="#A855F7" stroke-width="0.8"/>
          <text x="12" y="17" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#D8B4FE">FastAPI</text>
        </g>
      </g>
    </g>

    <!-- Section 02: Core Programming Languages -->
    <g transform="translate(0, 108)">
      <text x="0" y="11" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="10.5" font-weight="800" letter-spacing="1.8" fill="#60A5FA">02 // PROGRAMMING LANGUAGES</text>
      <g transform="translate(0, 20)">
        <rect x="0" y="0" width="80" height="28" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/><text x="12" y="18" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" fill="#F1F5F9">Python</text>
        <rect x="88" y="0" width="98" height="28" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/><text x="12" y="18" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" fill="#F1F5F9">TypeScript</text>
        <rect x="194" y="0" width="98" height="28" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/><text x="12" y="18" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" fill="#F1F5F9">JavaScript</text>
        <rect x="300" y="0" width="62" height="28" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/><text x="14" y="18" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" fill="#F1F5F9">SQL</text>
        <rect x="370" y="0" width="55" height="28" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/><text x="12" y="18" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" fill="#F1F5F9">C++</text>
        <rect x="433" y="0" width="49" height="28" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/><text x="10" y="18" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" fill="#F1F5F9">Java</text>
      </g>
    </g>

    <!-- Section 03: Frontend & Spatial Runtime -->
    <g transform="translate(0, 184)">
      <text x="0" y="11" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="10.5" font-weight="800" letter-spacing="1.8" fill="#38BDF8">03 // FRONTEND &amp; SPATIAL VISUALIZATION</text>
      <g transform="translate(0, 20)">
        <rect x="0" y="0" width="70" height="28" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/><text x="12" y="18" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" fill="#F1F5F9">React</text>
        <rect x="78" y="0" width="78" height="28" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/><text x="12" y="18" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" fill="#F1F5F9">Next.js</text>
        <rect x="164" y="0" width="112" height="28" rx="6" fill="#081A33" stroke="#2F86FF" stroke-width="1.2"/><text x="12" y="18" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" fill="#60A5FA">MapLibre GL</text>
        <rect x="284" y="0" width="76" height="28" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/><text x="12" y="18" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" fill="#F1F5F9">Leaflet</text>
        <rect x="368" y="0" width="114" height="28" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/><text x="12" y="18" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" fill="#F1F5F9">Tailwind CSS</text>
      </g>
    </g>

    <!-- Section 04: Backend & Spatial Infrastructure -->
    <g transform="translate(0, 260)">
      <text x="0" y="11" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="10.5" font-weight="800" letter-spacing="1.8" fill="#34D399">04 // BACKEND &amp; SPATIAL INFRASTRUCTURE</text>
      <g transform="translate(0, 20)">
        <rect x="0" y="0" width="75" height="28" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/><text x="12" y="18" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" fill="#F1F5F9">FastAPI</text>
        <rect x="83" y="0" width="78" height="28" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/><text x="12" y="18" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" fill="#F1F5F9">Node.js</text>
        <rect x="169" y="0" width="135" height="28" rx="6" fill="#1C1022" stroke="#FF354F" stroke-width="1.2"/><text x="10" y="18" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" fill="#FF8A9A">PostgreSQL / GIS</text>
        <rect x="312" y="0" width="68" height="28" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/><text x="12" y="18" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" fill="#F1F5F9">Redis</text>
        <rect x="388" y="0" width="94" height="28" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/><text x="12" y="18" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" fill="#F1F5F9">WebSockets</text>
      </g>
    </g>

    <!-- System Flow Graphic Visual: DATA -> MODEL -> INFERENCE API -->
    <g transform="translate(0, 335)">
      <rect x="0" y="0" width="482" height="42" rx="6" fill="#080F1E" stroke="#162544" stroke-width="1"/>
      <text x="14" y="26" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="800" letter-spacing="1.2" fill="#8B96A8">SYSTEM VECTOR: <tspan fill="#60A5FA">DATA PIPELINE</tspan> → <tspan fill="#A855F7">ML MODEL</tspan> → <tspan fill="#34D399">FASTAPI INFERENCE</tspan> → <tspan fill="#F1F5F9">CLIENT UI</tspan></text>
    </g>
  </g>
</svg>'''

    # =========================================================================
    # 7. assets/id-dashboard.svg — 06 / BUILDER ID & 07 / JOURNEY
    # =========================================================================
    id_dashboard_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 940 460" width="100%" height="100%">
  <defs>
    <linearGradient id="id-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070B16"/>
      <stop offset="60%" stop-color="#0B1325"/>
      <stop offset="100%" stop-color="#070B16"/>
    </linearGradient>
    <linearGradient id="id-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2F86FF" stop-opacity="0.85"/>
      <stop offset="50%" stop-color="#2F86FF" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#FF3652" stop-opacity="0.7"/>
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

  <style>
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

  <rect x="0" y="0" width="940" height="460" rx="18" fill="url(#id-bg)" stroke="url(#id-border)" stroke-width="1.6"/>
  <rect x="0" y="0" width="940" height="460" rx="18" fill="url(#id-dots)"/>

  <!-- ================= LEFT: HANGING BUILDER PASS (Using id.png) ================= -->
  <g class="hanging-badge">
    <!-- Lanyard Strap -->
    <rect x="160" y="-10" width="30" height="55" fill="url(#id-lanyard)"/>
    <text x="175" y="25" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="7.5" font-weight="900" fill="#FFFFFF" transform="rotate(90 175 25)">BUILDER PASS</text>

    <!-- Metal Clasp & Clip -->
    <rect x="156" y="42" width="38" height="14" rx="4" fill="#94A3B8" stroke="#CBD5E1" stroke-width="1"/>
    <rect x="165" y="56" width="20" height="10" rx="2" fill="#64748B"/>

    <!-- ID Badge Body (Outer Card) -->
    <g transform="translate(62, 66)">
      <rect x="0" y="0" width="226" height="348" rx="14" fill="#0A1224" stroke="#2F86FF" stroke-width="1.6"/>

      <!-- Top Crimson Stripe with Clip Slot -->
      <rect x="0" y="0" width="226" height="26" rx="14" fill="#FF3652"/>
      <rect x="88" y="8" width="50" height="7" rx="3.5" fill="#070B16"/>

      <!-- Pass Header -->
      <g transform="translate(16, 42)">
        <text x="0" y="0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="10.5" font-weight="800" fill="#60A5FA">CREATIVE BUILDER PASS</text>
        <text x="194" y="0" text-anchor="end" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="10.5" font-weight="800" fill="#94A3B8">2026</text>
      </g>

      <!-- Portrait Box -->
      <g transform="translate(16, 54)">
        <rect x="0" y="0" width="194" height="135" rx="10" fill="#050811" stroke="#1E2F4D" stroke-width="1"/>
        <g clip-path="url(#id-badge-photo)" transform="translate(37, 8)">
          <image href="data:image/png;base64,{mine_b64}" xlink:href="data:image/png;base64,{mine_b64}" x="-15" y="-10" width="150" height="150" preserveAspectRatio="xMidYMid meet"/>
        </g>
      </g>

      <!-- Identity Details (Real, truthful info!) -->
      <g transform="translate(16, 208)">
        <text x="0" y="10" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="16" font-weight="900" fill="#FFFFFF">PRINCE TIWARI</text>
        <text x="0" y="27" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="10.5" font-weight="800" fill="#60A5FA">ENGINEER • BUILDER</text>
        <text x="0" y="43" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="10" font-weight="700" fill="#A855F7">B.Tech CSE (AI &amp; ML)</text>
        <text x="0" y="58" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="9.5" fill="#94A3B8">Muzaffarpur, Bihar, India</text>
      </g>

      <!-- Bottom Barcode -->
      <g transform="translate(16, 280)">
        <line x1="0" y1="0" x2="0" y2="28" stroke="#FFFFFF" stroke-width="2.5"/>
        <line x1="5" y1="0" x2="5" y2="28" stroke="#FFFFFF" stroke-width="1"/>
        <line x1="9" y1="0" x2="9" y2="28" stroke="#FFFFFF" stroke-width="3"/>
        <line x1="16" y1="0" x2="16" y2="28" stroke="#2F86FF" stroke-width="3.5"/>
        <line x1="24" y1="0" x2="24" y2="28" stroke="#FFFFFF" stroke-width="1"/>
        <line x1="31" y1="0" x2="31" y2="28" stroke="#FFFFFF" stroke-width="2"/>
        <line x1="38" y1="0" x2="38" y2="28" stroke="#FF3652" stroke-width="3"/>
        <line x1="46" y1="0" x2="46" y2="28" stroke="#FFFFFF" stroke-width="1.5"/>
        <line x1="54" y1="0" x2="54" y2="28" stroke="#FFFFFF" stroke-width="2.5"/>
        <line x1="62" y1="0" x2="62" y2="28" stroke="#2F86FF" stroke-width="3"/>
        <line x1="72" y1="0" x2="72" y2="28" stroke="#FFFFFF" stroke-width="1"/>
        <line x1="80" y1="0" x2="80" y2="28" stroke="#FFFFFF" stroke-width="3.5"/>
        <line x1="90" y1="0" x2="90" y2="28" stroke="#FFFFFF" stroke-width="1"/>
        <line x1="98" y1="0" x2="98" y2="28" stroke="#2F86FF" stroke-width="2"/>
        <line x1="108" y1="0" x2="108" y2="28" stroke="#FFFFFF" stroke-width="4"/>
        <line x1="118" y1="0" x2="118" y2="28" stroke="#FFFFFF" stroke-width="1.5"/>
        <line x1="126" y1="0" x2="126" y2="28" stroke="#FF3652" stroke-width="2.5"/>
        <line x1="134" y1="0" x2="134" y2="28" stroke="#FFFFFF" stroke-width="3"/>
        <line x1="144" y1="0" x2="144" y2="28" stroke="#FFFFFF" stroke-width="1"/>
        <line x1="152" y1="0" x2="152" y2="28" stroke="#FFFFFF" stroke-width="2"/>
        <line x1="162" y1="0" x2="162" y2="28" stroke="#2F86FF" stroke-width="3"/>
        <line x1="172" y1="0" x2="172" y2="28" stroke="#FFFFFF" stroke-width="1.5"/>
        <line x1="184" y1="0" x2="184" y2="28" stroke="#FFFFFF" stroke-width="3"/>
        <text x="97" y="42" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="8.5" font-weight="700" fill="#94A3B8">XNACRO-2026-IN-VERIFIED</text>
      </g>
    </g>
  </g>

  <!-- ================= RIGHT: 07 // CHRONOLOGICAL JOURNEY & TIMELINE ================= -->
  <g transform="translate(345, 30)">
    <text x="0" y="10" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11" font-weight="800" letter-spacing="2" fill="#2F86FF">06 // ENGINEERING TRAJECTORY • TIMELINE</text>
    <text x="0" y="38" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="26" font-weight="900" fill="#FFFFFF">THE JOURNEY SO FAR<tspan fill="#FF3652">.</tspan></text>
    <text x="0" y="58" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11.5" fill="#8B96A8">From core software foundations to national competition wins and production spatial AI.</text>

    <!-- Timeline Horizontal Progression -->
    <g transform="translate(0, 95)">
      <!-- Line -->
      <line x1="30" y1="20" x2="520" y2="20" stroke="#1F2F4F" stroke-width="2"/>

      <!-- Node 1: 2024 -->
      <g transform="translate(30, 0)">
        <circle cx="0" cy="20" r="7" fill="#0C1527" stroke="#2F86FF" stroke-width="2.5"/>
        <text x="-16" y="0" font-family="-apple-system, sans-serif" font-size="13" font-weight="900" fill="#60A5FA">2024</text>
        <text x="-25" y="48" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" fill="#F5F7FA">Full-Stack Foundations</text>
        <text x="-25" y="66" font-family="-apple-system, sans-serif" font-size="10.5" fill="#8B96A8">MERN stack, REST APIs,</text>
        <text x="-25" y="80" font-family="-apple-system, sans-serif" font-size="10.5" fill="#8B96A8">relational schemas &amp; CS logic.</text>
      </g>

      <!-- Node 2: 2025 -->
      <g transform="translate(195, 0)">
        <circle cx="0" cy="20" r="7" fill="#0C1527" stroke="#2F86FF" stroke-width="2.5"/>
        <text x="-16" y="0" font-family="-apple-system, sans-serif" font-size="13" font-weight="900" fill="#60A5FA">2025</text>
        <text x="-25" y="48" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" fill="#F5F7FA">Applied AI &amp; Hackathons</text>
        <text x="-25" y="66" font-family="-apple-system, sans-serif" font-size="10.5" fill="#8B96A8">ML models, Scikit-learn,</text>
        <text x="-25" y="80" font-family="-apple-system, sans-serif" font-size="10.5" fill="#8B96A8">NLP news extraction &amp; APIs.</text>
      </g>

      <!-- Node 3: 2026 -->
      <g transform="translate(365, 0)">
        <circle cx="0" cy="20" r="7" fill="#0C1527" stroke="#FF3652" stroke-width="2.5"/>
        <text x="-16" y="0" font-family="-apple-system, sans-serif" font-size="13" font-weight="900" fill="#FF8A9A">2026</text>
        <text x="-25" y="48" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" fill="#F5F7FA">National Recognition</text>
        <text x="-25" y="66" font-family="-apple-system, sans-serif" font-size="10.5" fill="#8B96A8">Cognithon 2nd, India Innovates,</text>
        <text x="-25" y="80" font-family="-apple-system, sans-serif" font-size="10.5" fill="#8B96A8">Flipkart GRiD Semi-Finalist.</text>
      </g>

      <!-- Node 4: NOW -->
      <g transform="translate(505, 0)">
        <circle cx="0" cy="20" r="8" fill="#10B981"/>
        <text x="-14" y="0" font-family="-apple-system, sans-serif" font-size="13" font-weight="900" fill="#22C55E">NOW</text>
        <text x="-35" y="48" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" fill="#F5F7FA">Active Production</text>
        <text x="-35" y="66" font-family="-apple-system, sans-serif" font-size="10.5" fill="#8B96A8">Shipping SurakshaAI &amp;</text>
        <text x="-35" y="80" font-family="-apple-system, sans-serif" font-size="10.5" fill="#8B96A8">real-world spatial models.</text>
      </g>
    </g>

    <!-- Proof of Work Callout Panel -->
    <g transform="translate(0, 240)">
      <rect x="0" y="0" width="555" height="142" rx="10" fill="#080E1C" stroke="#162544" stroke-width="1.2"/>
      <text x="20" y="26" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="800" letter-spacing="1.5" fill="#60A5FA">PROOF OF WORK • AUTHENTIC VERIFICATION</text>
      <text x="20" y="52" font-family="-apple-system, sans-serif" font-size="14.5" font-weight="900" fill="#FFFFFF">Real builds. Real problem spaces. Tested in competitive arenas.</text>
      <text x="20" y="74" font-family="-apple-system, sans-serif" font-size="12" fill="#8B96A8">
        Every system represented on this profile is backed by genuine repositories, verifiable
      </text>
      <text x="20" y="92" font-family="-apple-system, sans-serif" font-size="12" fill="#8B96A8">
        hackathon submissions across IIIT Bhagalpur, IIT Guwahati, IIT Patna, and production code.
      </text>
      <rect x="20" y="106" width="130" height="22" rx="4" fill="#14284D"/>
      <text x="28" y="121" font-family="-apple-system, sans-serif" font-size="9.5" font-weight="800" fill="#60A5FA">OPEN-SOURCE PROOF</text>
    </g>
  </g>
</svg>'''

    # =========================================================================
    # 8. assets/connect.svg — 07 / INITIATE TRANSMISSION (Pointing id.png)
    # =========================================================================
    connect_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 940 450" width="100%" height="100%">
  <defs>
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
      <rect x="0" y="0" width="420" height="430"/>
    </clipPath>
  </defs>

  <style>
    @keyframes arrowNudge {{
      0%, 100% {{ transform: translateX(0); }}
      50%      {{ transform: translateX(6px); }}
    }}
    .nudge-arrow {{
      animation: arrowNudge 1.8s ease-in-out infinite;
    }}
  </style>

  <rect x="0" y="0" width="940" height="450" rx="18" fill="url(#cn-bg)" stroke="url(#cn-border)" stroke-width="1.6"/>
  <rect x="0" y="0" width="940" height="450" rx="18" fill="url(#cn-dots)"/>

  <!-- Left Pointing Character id.png guiding attention right -->
  <g transform="translate(10, 20)">
    <ellipse cx="225" cy="225" rx="175" ry="175" fill="#2F86FF" fill-opacity="0.12"/>
    <g clip-path="url(#cn-character-clip)">
      <image href="data:image/png;base64,{id_b64}" xlink:href="data:image/png;base64,{id_b64}" x="-10" y="10" width="440" height="400" preserveAspectRatio="xMidYMid meet"/>
    </g>
  </g>

  <!-- Right Headline & Social Channels -->
  <g transform="translate(435, 36)">
    <text x="0" y="10" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11" font-weight="800" letter-spacing="2" fill="#2F86FF">07 // TRANSMISSION PROTOCOL</text>
    <text x="0" y="42" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="34" font-weight="900" fill="#FFFFFF">LET'S BUILD SOMETHING<tspan fill="#FF3652">.</tspan></text>
    <text x="0" y="65" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13.5" fill="#8B96A8">
      Open for AI/ML architecture, geospatial systems &amp; high-impact products.
    </text>

    <!-- 4 Direct Channels Cards -->
    <g transform="translate(0, 88)">
      <!-- Card 1: GitHub -->
      <g transform="translate(0, 0)">
        <rect x="0" y="0" width="460" height="52" rx="8" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
        <rect x="12" y="12" width="28" height="28" rx="6" fill="#14243F"/>
        <text x="21" y="31" font-family="sans-serif" font-size="15" fill="#FFFFFF">&#x2325;</text>
        <text x="50" y="24" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13" font-weight="800" fill="#FFFFFF">GitHub</text>
        <text x="50" y="40" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11" font-weight="600" fill="#60A5FA">github.com/xnacro • Repositories &amp; Core Code</text>
        <g class="nudge-arrow">
          <text x="425" y="32" font-family="-apple-system, sans-serif" font-size="16" font-weight="900" fill="#2F86FF">→</text>
        </g>
      </g>

      <!-- Card 2: LinkedIn -->
      <g transform="translate(0, 62)">
        <rect x="0" y="0" width="460" height="52" rx="8" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
        <rect x="12" y="12" width="28" height="28" rx="6" fill="#0A2540"/>
        <text x="20" y="31" font-family="sans-serif" font-size="14" font-weight="900" fill="#0A66C2">in</text>
        <text x="50" y="24" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13" font-weight="800" fill="#FFFFFF">LinkedIn</text>
        <text x="50" y="40" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11" font-weight="600" fill="#60A5FA">linkedin.com/in/prince-tiwari-727375328</text>
        <g class="nudge-arrow">
          <text x="425" y="32" font-family="-apple-system, sans-serif" font-size="16" font-weight="900" fill="#2F86FF">→</text>
        </g>
      </g>

      <!-- Card 3: Instagram -->
      <g transform="translate(0, 124)">
        <rect x="0" y="0" width="460" height="52" rx="8" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
        <rect x="12" y="12" width="28" height="28" rx="6" fill="#2A1224"/>
        <text x="20" y="31" font-family="sans-serif" font-size="14" fill="#FF3652">&#x1F4F8;</text>
        <text x="50" y="24" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13" font-weight="800" fill="#FFFFFF">Instagram</text>
        <text x="50" y="40" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11" font-weight="600" fill="#FF7088">@am_princetiwari • Engineering &amp; Life</text>
        <g class="nudge-arrow">
          <text x="425" y="32" font-family="-apple-system, sans-serif" font-size="16" font-weight="900" fill="#FF3652">→</text>
        </g>
      </g>

      <!-- Card 4: Email -->
      <g transform="translate(0, 186)">
        <rect x="0" y="0" width="460" height="52" rx="8" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
        <rect x="12" y="12" width="28" height="28" rx="6" fill="#14243F"/>
        <text x="20" y="31" font-family="sans-serif" font-size="14" fill="#EA4335">&#x2709;</text>
        <text x="50" y="24" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13" font-weight="800" fill="#FFFFFF">Direct Electronic Comms</text>
        <text x="50" y="40" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11" font-weight="600" fill="#60A5FA">businessofficialtech@gmail.com</text>
        <g class="nudge-arrow">
          <text x="425" y="32" font-family="-apple-system, sans-serif" font-size="16" font-weight="900" fill="#2F86FF">→</text>
        </g>
      </g>
    </g>

    <!-- Bottom Guidance -->
    <text x="0" y="360" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="10" font-weight="800" letter-spacing="1.5" fill="#64748B">CLICKABLE LINKS WIRED IN REPOSITORY DOCUMENT BELOW</text>
  </g>
</svg>'''

    files = {
        'assets/hero.svg': hero_svg,
        'assets/achievements.svg': achievements_svg,
        'assets/current-build.svg': current_build_svg,
        'assets/flagship.svg': flagship_svg,
        'assets/selected-builds.svg': selected_builds_svg,
        'assets/stack.svg': stack_svg,
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
