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
    # 1. assets/hero.svg
    # =========================================================================
    hero_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 920 460" width="100%" height="100%">
  <defs>
    <linearGradient id="hero-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070B16"/>
      <stop offset="60%" stop-color="#0A1122"/>
      <stop offset="100%" stop-color="#070B16"/>
    </linearGradient>
    <linearGradient id="hero-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247BFF" stop-opacity="0.7"/>
      <stop offset="50%" stop-color="#247BFF" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#FF354F" stop-opacity="0.6"/>
    </linearGradient>
    <linearGradient id="hero-title-blue" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#247BFF"/>
      <stop offset="100%" stop-color="#60A5FA"/>
    </linearGradient>
    <radialGradient id="hero-glow" cx="80%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#247BFF" stop-opacity="0.25"/>
      <stop offset="60%" stop-color="#247BFF" stop-opacity="0.05"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
    </radialGradient>
    <pattern id="hero-dots" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#1C2B49" opacity="0.45"/>
    </pattern>
    <clipPath id="hero-portrait-clip">
      <rect x="520" y="30" width="370" height="390" rx="16"/>
    </clipPath>
  </defs>

  <style>
    @keyframes heroCycleRole {{
      0%, 20%   {{ opacity: 1; transform: translateY(0); }}
      22%, 25%  {{ opacity: 0; transform: translateY(-8px); }}
      26%, 45%  {{ opacity: 0; transform: translateY(8px); }}
      47%, 70%  {{ opacity: 1; transform: translateY(0); }}
      72%, 75%  {{ opacity: 0; transform: translateY(-8px); }}
      76%, 95%  {{ opacity: 0; transform: translateY(8px); }}
      97%, 100% {{ opacity: 1; transform: translateY(0); }}
    }}
    @keyframes heroPulseDot {{
      0%, 100% {{ opacity: 1; transform: scale(1); }}
      50%      {{ opacity: 0.4; transform: scale(0.85); }}
    }}
    .hero-role-text {{
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      font-size: 14px;
      font-weight: 700;
      letter-spacing: 0.5px;
      fill: #247BFF;
    }}
    .hero-pulse {{
      animation: heroPulseDot 2.4s ease-in-out infinite;
      transform-origin: 34px 34px;
    }}
  </style>

  <!-- Container -->
  <rect x="0" y="0" width="920" height="460" rx="16" fill="url(#hero-bg)" stroke="url(#hero-border)" stroke-width="1.5"/>
  <rect x="0" y="0" width="920" height="460" rx="16" fill="url(#hero-dots)"/>
  <rect x="450" y="0" width="470" height="460" rx="16" fill="url(#hero-glow)"/>

  <!-- Top Metadata Bar -->
  <g transform="translate(34, 30)">
    <circle cx="6" cy="6" r="4.5" fill="#247BFF" class="hero-pulse"/>
    <text x="18" y="10" font-family="'JetBrains Mono', 'Fira Code', monospace" font-size="11" font-weight="700" letter-spacing="1.5" fill="#F0F6FC">SOFTWARE ENGINEER</text>
    <text x="840" y="10" text-anchor="end" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="600" letter-spacing="1" fill="#8B96A8">INDIA // OPEN TO COLLAB</text>
  </g>

  <!-- Left Content Column -->
  <g transform="translate(34, 85)">
    <!-- Sub-greeting -->
    <text x="0" y="0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="16" font-weight="600" fill="#8B96A8">Hi, I'm</text>

    <!-- Large Name Display -->
    <text x="0" y="52" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="56" font-weight="900" letter-spacing="-1.5" fill="#FFFFFF">PRINCE</text>
    <text x="0" y="112" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="56" font-weight="900" letter-spacing="-1.5" fill="url(#hero-title-blue)">TIWARI</text>

    <!-- Crimson Slash Bars + Mission -->
    <g transform="translate(260, 68)">
      <rect x="0" y="0" width="4" height="24" rx="2" fill="#FF354F" transform="skewX(-20)"/>
      <rect x="9" y="0" width="4" height="24" rx="2" fill="#FF354F" transform="skewX(-20)"/>
      <rect x="18" y="0" width="4" height="24" rx="2" fill="#FF354F" transform="skewX(-20)"/>
      <text x="32" y="12" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13" font-weight="800" letter-spacing="1.5" fill="#FFFFFF">BUILD.</text>
      <text x="32" y="27" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13" font-weight="800" letter-spacing="1.5" fill="#FF354F">BEYOND.</text>
    </g>

    <!-- Dynamic Role Tag -->
    <g transform="translate(0, 140)">
      <rect x="0" y="0" width="280" height="28" rx="6" fill="#0D172E" stroke="#247BFF" stroke-width="1" stroke-opacity="0.5"/>
      <text x="14" y="19" class="hero-role-text">Team Leader @ Legacy Coderz</text>
    </g>

    <!-- One-Line Pitch -->
    <text x="0" y="200" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14.5" fill="#C9D1D9" line-height="22">
      <tspan x="0" dy="0">Building real-time geospatial safety intelligence systems</tspan>
      <tspan x="0" dy="22">&amp; predictive AI platforms that actually ship.</tspan>
    </text>

    <!-- Location & Telemetry Strip -->
    <g transform="translate(0, 252)">
      <!-- Chip 1 -->
      <rect x="0" y="0" width="105" height="26" rx="5" fill="#0C1426" stroke="#1E2F4D" stroke-width="1"/>
      <text x="12" y="17" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#F0F6FC">📍 India</text>

      <!-- Chip 2 -->
      <rect x="115" y="0" width="145" height="26" rx="5" fill="#0C1426" stroke="#1E2F4D" stroke-width="1"/>
      <text x="127" y="17" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#247BFF">⚡ Legacy Coderz</text>

      <!-- Chip 3 -->
      <rect x="270" y="0" width="155" height="26" rx="5" fill="#0C1426" stroke="#1E2F4D" stroke-width="1"/>
      <text x="282" y="17" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#FF354F">🗺️ 408k Grid Cells</text>
    </g>
  </g>

  <!-- Right Portrait Column with Inlined PNG -->
  <g>
    <!-- Background Frame glow -->
    <rect x="520" y="38" width="365" height="385" rx="16" fill="#0C1527" stroke="#1C2D4A" stroke-width="1"/>
    
    <!-- Inlined Portrait Image -->
    <g clip-path="url(#hero-portrait-clip)">
      <image href="data:image/png;base64,{mine_b64}" xlink:href="data:image/png;base64,{mine_b64}" x="515" y="20" width="380" height="405" preserveAspectRatio="xMidYMid meet"/>
    </g>

    <!-- Overlay Badge over portrait bottom -->
    <g transform="translate(680, 375)">
      <rect x="0" y="0" width="185" height="34" rx="8" fill="#0B1324" stroke="#247BFF" stroke-width="1.2"/>
      <rect x="0" y="0" width="10" height="34" rx="4" fill="#247BFF"/>
      <text x="20" y="16" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="10.5" font-weight="800" fill="#FFFFFF">ENGINEER / BUILDER</text>
      <text x="20" y="27" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="600" fill="#60A5FA">@xnacro</text>
    </g>
  </g>
</svg>'''

    # =========================================================================
    # 2. assets/about-life.svg
    # =========================================================================
    about_life_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 920 440" width="100%" height="100%">
  <defs>
    <linearGradient id="ab-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247BFF" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="#247BFF" stop-opacity="0.1"/>
    </linearGradient>
    <linearGradient id="ab-card-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0A1122"/>
      <stop offset="100%" stop-color="#060A14"/>
    </linearGradient>
    <pattern id="ab-dots" width="18" height="18" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="0.9" fill="#1C2B49" opacity="0.4"/>
    </pattern>
    <clipPath id="ab-avatar-clip">
      <rect x="0" y="0" width="140" height="140" rx="12"/>
    </clipPath>
  </defs>

  <style>
    @keyframes progressRun {{
      0%   {{ width: 0; }}
      100% {{ width: 80px; }}
    }}
    .progress-bar-active {{
      animation: progressRun 4s linear infinite;
    }}
  </style>

  <rect x="0" y="0" width="920" height="440" rx="16" fill="#070B16"/>
  <rect x="0" y="0" width="920" height="440" rx="16" fill="url(#ab-dots)"/>

  <!-- ================= CARD 1: FROM THOUGHT TO THING ================= -->
  <g transform="translate(18, 18)">
    <rect x="0" y="0" width="434" height="404" rx="14" fill="url(#ab-card-bg)" stroke="url(#ab-border)" stroke-width="1.2"/>

    <g transform="translate(24, 24)">
      <!-- Eyebrow & Title -->
      <text x="0" y="10" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" letter-spacing="1.5" fill="#8B96A8">01 / FROM THOUGHT TO THING</text>
      <text x="0" y="36" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="22" font-weight="900" fill="#FFFFFF">IDEAS. BUILT DIFFERENT.</text>

      <!-- Terminal Window Simulation -->
      <g transform="translate(0, 56)">
        <rect x="0" y="0" width="386" height="100" rx="8" fill="#050811" stroke="#16233B" stroke-width="1"/>
        
        <!-- Terminal Header -->
        <circle cx="16" cy="14" r="3.5" fill="#FF5F56"/>
        <circle cx="28" cy="14" r="3.5" fill="#FFBD2E"/>
        <circle cx="40" cy="14" r="3.5" fill="#27C93F"/>
        <text x="60" y="17" font-family="'JetBrains Mono', monospace" font-size="10" fill="#6B7A94">github.com/xnacro/build</text>

        <!-- Command Prompt -->
        <text x="16" y="44" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="600" fill="#247BFF">&gt; turn_curiosity_into_impact()</text>

        <!-- 3 Step Pills: Ideate -> Engineer -> Ship -->
        <g transform="translate(16, 58)">
          <!-- 01 Ideate -->
          <rect x="0" y="0" width="70" height="26" rx="4" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
          <text x="10" y="17" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#8B96A8">01 IDEATE</text>

          <text x="78" y="17" font-family="sans-serif" font-size="11" fill="#4B5E80">→</text>

          <!-- 02 Engineer -->
          <rect x="94" y="0" width="85" height="26" rx="4" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
          <text x="102" y="17" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#8B96A8">02 ENGINEER</text>

          <text x="187" y="17" font-family="sans-serif" font-size="11" fill="#4B5E80">→</text>

          <!-- 03 Ship -->
          <rect x="203" y="0" width="70" height="26" rx="4" fill="#14284D" stroke="#247BFF" stroke-width="1.2"/>
          <text x="217" y="17" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="800" fill="#60A5FA">03 SHIP</text>
        </g>
      </g>

      <!-- 3 Capabilities Rows -->
      <g transform="translate(0, 180)">
        <!-- Row 1 -->
        <g transform="translate(0, 0)">
          <text x="0" y="14" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="700" fill="#247BFF">&lt;&gt;</text>
          <text x="24" y="14" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13.5" font-weight="800" fill="#F0F6FC">Modern Web &amp; App Dev</text>
          <text x="24" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="12" fill="#8B96A8">From first interaction to production-scale platforms.</text>
        </g>

        <!-- Row 2 -->
        <g transform="translate(0, 52)">
          <text x="0" y="14" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="700" fill="#FF354F">☁</text>
          <text x="24" y="14" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13.5" font-weight="800" fill="#F0F6FC">AI &amp; Spatial Integration</text>
          <text x="24" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="12" fill="#8B96A8">Scalable systems, risk modeling &amp; real-world data.</text>
        </g>

        <!-- Row 3 -->
        <g transform="translate(0, 104)">
          <text x="0" y="14" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="700" fill="#22C55E">👥</text>
          <text x="24" y="14" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13.5" font-weight="800" fill="#F0F6FC">Team Leadership &amp; Hackathons</text>
          <text x="24" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="12" fill="#8B96A8">Leading Legacy Coderz in national civic innovation.</text>
        </g>
      </g>
    </g>
  </g>

  <!-- ================= CARD 2: LIFE OUTSIDE THE COMMIT ================= -->
  <g transform="translate(468, 18)">
    <rect x="0" y="0" width="434" height="404" rx="14" fill="url(#ab-card-bg)" stroke="url(#ab-border)" stroke-width="1.2"/>

    <g transform="translate(24, 24)">
      <!-- Eyebrow & Title -->
      <text x="0" y="10" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" letter-spacing="1.5" fill="#8B96A8">02 / LIFE OUTSIDE THE COMMIT</text>
      <text x="0" y="36" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="22" font-weight="900" fill="#FFFFFF">MORE THAN A JOB TITLE.</text>

      <!-- Carousel Progress Indicators -->
      <g transform="translate(0, 52)">
        <!-- Seg 1 -->
        <rect x="0" y="0" width="80" height="3" rx="1.5" fill="#1C2D4A"/>
        <rect x="0" y="0" width="80" height="3" rx="1.5" fill="#247BFF" class="progress-bar-active"/>

        <!-- Seg 2 -->
        <rect x="90" y="0" width="80" height="3" rx="1.5" fill="#1C2D4A"/>
        
        <!-- Seg 3 -->
        <rect x="180" y="0" width="80" height="3" rx="1.5" fill="#1C2D4A"/>
      </g>

      <!-- Featured Interests Slide Content -->
      <g transform="translate(0, 75)">
        <!-- Portrait Box -->
        <g transform="translate(0, 10)">
          <rect x="0" y="0" width="140" height="140" rx="12" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
          <g clip-path="url(#ab-avatar-clip)">
            <image href="data:image/png;base64,{mine_b64}" xlink:href="data:image/png;base64,{mine_b64}" x="-10" y="-10" width="160" height="160" preserveAspectRatio="xMidYMid meet"/>
          </g>
          <rect x="10" y="112" width="120" height="20" rx="4" fill="#0B1324" stroke="#247BFF" stroke-width="0.8"/>
          <text x="18" y="126" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="700" fill="#60A5FA">PRINCE / YOUR BUILDER</text>
        </g>

        <!-- Right Side Principles -->
        <g transform="translate(160, 20)">
          <g transform="translate(0, 0)">
            <text x="0" y="14" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="800" fill="#FF354F">01</text>
            <text x="24" y="14" font-family="-apple-system, sans-serif" font-size="12.5" font-weight="800" fill="#F0F6FC">FIND THE GAP</text>
          </g>
          <g transform="translate(0, 42)">
            <text x="0" y="14" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="800" fill="#247BFF">02</text>
            <text x="24" y="14" font-family="-apple-system, sans-serif" font-size="12.5" font-weight="800" fill="#F0F6FC">BUILD YOUR PLAN</text>
          </g>
          <g transform="translate(0, 84)">
            <text x="0" y="14" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="800" fill="#22C55E">03</text>
            <text x="24" y="14" font-family="-apple-system, sans-serif" font-size="12.5" font-weight="800" fill="#F0F6FC">TAKE THE LEAP</text>
          </g>
        </g>
      </g>

      <!-- Bottom Mentorship / Collaboration Callout -->
      <g transform="translate(0, 260)">
        <rect x="0" y="0" width="386" height="85" rx="8" fill="#060C18" stroke="#16233B" stroke-width="1"/>
        <text x="18" y="24" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="700" letter-spacing="1" fill="#8B96A8">ENGINEERING PERSPECTIVE</text>
        <text x="18" y="48" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="15" font-weight="800" fill="#FFFFFF">System Architecture &amp; Collaboration</text>
        <text x="18" y="68" font-family="-apple-system, sans-serif" font-size="12" fill="#8B96A8">A clearer roadmap. A stronger, more resilient system.</text>
      </g>
    </g>
  </g>
</svg>'''

    # =========================================================================
    # 3. assets/stack.svg
    # =========================================================================
    stack_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 920 460" width="100%" height="100%">
  <defs>
    <linearGradient id="stk-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070B16"/>
      <stop offset="100%" stop-color="#0A1122"/>
    </linearGradient>
    <linearGradient id="stk-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247BFF" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#FF354F" stop-opacity="0.4"/>
    </linearGradient>
    <pattern id="stk-dots" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#1C2B49" opacity="0.4"/>
    </pattern>
  </defs>

  <style>
    @keyframes orbitPulse {{
      0%, 100% {{ transform: scale(1); opacity: 0.9; }}
      50%      {{ transform: scale(1.08); opacity: 1; }}
    }}
    .core-cube {{
      animation: orbitPulse 3s ease-in-out infinite;
      transform-origin: 200px 245px;
    }}
  </style>

  <rect x="0" y="0" width="920" height="460" rx="16" fill="url(#stk-bg)" stroke="url(#stk-border)" stroke-width="1.5"/>
  <rect x="0" y="0" width="920" height="460" rx="16" fill="url(#stk-dots)"/>

  <!-- Top Title Header -->
  <g transform="translate(34, 30)">
    <text x="0" y="10" font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="700" letter-spacing="1.5" fill="#8B96A8">03 / MY ENGINE ROOM</text>
    <text x="0" y="38" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="26" font-weight="900" fill="#FFFFFF">TOOLS CHANGE. CURIOSITY DOESN'T.</text>
    <text x="0" y="58" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="600" letter-spacing="1" fill="#247BFF">LANGUAGES / SYSTEMS / INTELLIGENCE</text>
  </g>

  <!-- ================= LEFT: 3 TILTED ELLIPTICAL ORBITS ================= -->
  <g transform="translate(0, 0)">
    <!-- Orbit 1 (Large Outer) -->
    <ellipse cx="200" cy="245" rx="160" ry="60" fill="none" stroke="#247BFF" stroke-width="1.2" stroke-opacity="0.4" stroke-dasharray="6,4" transform="rotate(-25 200 245)"/>

    <!-- Orbit 2 (Middle) -->
    <ellipse cx="200" cy="245" rx="130" ry="75" fill="none" stroke="#60A5FA" stroke-width="1.2" stroke-opacity="0.35" transform="rotate(35 200 245)"/>

    <!-- Orbit 3 (Inner) -->
    <ellipse cx="200" cy="245" rx="95" ry="45" fill="none" stroke="#FF354F" stroke-width="1.2" stroke-opacity="0.4" transform="rotate(-65 200 245)"/>

    <!-- Central Glowing Core Cube -->
    <g class="core-cube">
      <rect x="175" y="220" width="50" height="50" rx="10" fill="#0D1A38" stroke="#247BFF" stroke-width="2"/>
      <text x="200" y="252" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="18" font-weight="900" fill="#FFFFFF">PT</text>
    </g>

    <!-- Revolving Node 1: Python -->
    <g transform="translate(90, 180)">
      <circle cx="15" cy="15" r="16" fill="#0C1527" stroke="#247BFF" stroke-width="1.2"/>
      <text x="15" y="19" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="800" fill="#60A5FA">Py</text>
    </g>

    <!-- Revolving Node 2: React -->
    <g transform="translate(290, 175)">
      <circle cx="15" cy="15" r="16" fill="#0C1527" stroke="#247BFF" stroke-width="1.2"/>
      <text x="15" y="19" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="800" fill="#60A5FA">Re</text>
    </g>

    <!-- Revolving Node 3: Node.js -->
    <g transform="translate(190, 320)">
      <circle cx="15" cy="15" r="16" fill="#0C1527" stroke="#22C55E" stroke-width="1.2"/>
      <text x="15" y="19" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="800" fill="#22C55E">Nd</text>
    </g>

    <!-- Revolving Node 4: PostGIS -->
    <g transform="translate(275, 290)">
      <circle cx="15" cy="15" r="16" fill="#0C1527" stroke="#FF354F" stroke-width="1.2"/>
      <text x="15" y="19" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="800" fill="#FF354F">GIS</text>
    </g>

    <!-- Revolving Node 5: FastAPI -->
    <g transform="translate(65, 280)">
      <circle cx="15" cy="15" r="16" fill="#0C1527" stroke="#247BFF" stroke-width="1.2"/>
      <text x="15" y="19" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="800" fill="#60A5FA">API</text>
    </g>

    <!-- Left Footnote -->
    <text x="200" y="415" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" letter-spacing="1" fill="#8B96A8">CODE IS THE TOOL. IMPACT IS THE POINT.</text>
  </g>

  <!-- ================= RIGHT: GROUPED STACK CHIPS ================= -->
  <g transform="translate(430, 105)">
    <!-- Section 01: Languages -->
    <g transform="translate(0, 0)">
      <text x="0" y="12" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#8B96A8">01 / LANGUAGES</text>
      <g transform="translate(0, 22)">
        <rect x="0" y="0" width="105" height="34" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
        <text x="14" y="21" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#F0F6FC">TypeScript</text>

        <rect x="115" y="0" width="95" height="34" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
        <text x="129" y="21" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#F0F6FC">Python</text>

        <rect x="220" y="0" width="110" height="34" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
        <text x="234" y="21" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#F0F6FC">JavaScript</text>

        <rect x="340" y="0" width="85" height="34" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
        <text x="354" y="21" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#F0F6FC">SQL</text>
      </g>
    </g>

    <!-- Section 02: Frontend & Spatial -->
    <g transform="translate(0, 85)">
      <text x="0" y="12" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#8B96A8">02 / FRONTEND &amp; SPATIAL RUNTIME</text>
      <g transform="translate(0, 22)">
        <rect x="0" y="0" width="85" height="34" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
        <text x="14" y="21" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#F0F6FC">React</text>

        <rect x="95" y="0" width="90" height="34" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
        <text x="109" y="21" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#F0F6FC">Next.js</text>

        <rect x="195" y="0" width="125" height="34" rx="6" fill="#0C1F2E" stroke="#247BFF" stroke-width="1.2"/>
        <text x="207" y="21" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#60A5FA">MapLibre GL</text>

        <rect x="330" y="0" width="95" height="34" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
        <text x="344" y="21" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#F0F6FC">Leaflet</text>
      </g>
    </g>

    <!-- Section 03: Backend, Cloud & AI -->
    <g transform="translate(0, 170)">
      <text x="0" y="12" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#8B96A8">03 / BACKEND, CLOUD &amp; AI INTELLIGENCE</text>
      <g transform="translate(0, 22)">
        <rect x="0" y="0" width="95" height="34" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
        <text x="14" y="21" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#F0F6FC">Node.js</text>

        <rect x="105" y="0" width="95" height="34" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
        <text x="119" y="21" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#F0F6FC">FastAPI</text>

        <rect x="210" y="0" width="130" height="34" rx="6" fill="#1C1022" stroke="#FF354F" stroke-width="1.2"/>
        <text x="222" y="21" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#FF8A9A">PostgreSQL / GIS</text>

        <rect x="350" y="0" width="75" height="34" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
        <text x="362" y="21" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#F0F6FC">Redis</text>
      </g>
    </g>

    <!-- Right Footnote -->
    <g transform="translate(0, 275)">
      <text x="0" y="12" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" letter-spacing="1.5" fill="#247BFF">BUILD / EXPERIMENT / SHIP / REPEAT</text>
    </g>
  </g>
</svg>'''

    # =========================================================================
    # 4. assets/id-dashboard.svg
    # =========================================================================
    id_dashboard_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 920 460" width="100%" height="100%">
  <defs>
    <linearGradient id="id-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070B16"/>
      <stop offset="100%" stop-color="#0B1224"/>
    </linearGradient>
    <linearGradient id="id-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247BFF" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#FF354F" stop-opacity="0.6"/>
    </linearGradient>
    <linearGradient id="id-lanyard" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1848A0"/>
      <stop offset="50%" stop-color="#247BFF"/>
      <stop offset="100%" stop-color="#1848A0"/>
    </linearGradient>
    <pattern id="id-dots" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#1C2B49" opacity="0.4"/>
    </pattern>
    <clipPath id="id-badge-photo">
      <rect x="0" y="0" width="110" height="110" rx="8"/>
    </clipPath>
  </defs>

  <style>
    @keyframes pendulumSwing {{
      0%   {{ transform: rotate(-1.7deg); }}
      50%  {{ transform: rotate(1.7deg); }}
      100% {{ transform: rotate(-1.7deg); }}
    }}
    .hanging-badge {{
      animation: pendulumSwing 4.5s ease-in-out infinite;
      transform-origin: 175px 40px;
    }}
  </style>

  <rect x="0" y="0" width="920" height="460" rx="16" fill="url(#id-bg)" stroke="url(#id-border)" stroke-width="1.5"/>
  <rect x="0" y="0" width="920" height="460" rx="16" fill="url(#id-dots)"/>

  <!-- ================= LEFT: HANGING LANYARD ID BADGE ================= -->
  <g class="hanging-badge">
    <!-- Lanyard Strap from Top -->
    <rect x="160" y="-10" width="30" height="55" fill="url(#id-lanyard)"/>
    <text x="175" y="25" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="7" font-weight="900" fill="#FFFFFF" transform="rotate(90 175 25)">LEGACY CODERZ</text>

    <!-- Metal Clasp & Clip -->
    <rect x="156" y="42" width="38" height="14" rx="4" fill="#A0AEC0" stroke="#CBD5E1" stroke-width="1"/>
    <rect x="165" y="56" width="20" height="10" rx="2" fill="#718096"/>

    <!-- ID Badge Body (Outer Card) -->
    <g transform="translate(65, 66)">
      <rect x="0" y="0" width="220" height="340" rx="12" fill="#0C1426" stroke="#247BFF" stroke-width="1.6"/>
      
      <!-- Top Red Stripe with Clip Slot -->
      <rect x="0" y="0" width="220" height="26" rx="12" fill="#FF354F"/>
      <rect x="85" y="8" width="50" height="7" rx="3.5" fill="#070B16"/>

      <!-- Pass Header -->
      <g transform="translate(16, 42)">
        <text x="0" y="0" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="800" fill="#60A5FA">XN / BUILDER PASS</text>
        <text x="188" y="0" text-anchor="end" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="800" fill="#8B96A8">0510</text>
      </g>

      <!-- Portrait Box -->
      <g transform="translate(16, 56)">
        <rect x="0" y="0" width="188" height="135" rx="8" fill="#060A14" stroke="#1E2F4D" stroke-width="1"/>
        <g clip-path="url(#id-badge-photo)" transform="translate(39, 12)">
          <image href="data:image/png;base64,{mine_b64}" xlink:href="data:image/png;base64,{mine_b64}" x="-15" y="-10" width="140" height="140" preserveAspectRatio="xMidYMid meet"/>
        </g>
      </g>

      <!-- Identity Details -->
      <g transform="translate(16, 210)">
        <text x="0" y="10" font-family="-apple-system, sans-serif" font-size="15" font-weight="900" fill="#FFFFFF">PRINCE TIWARI</text>
        <text x="0" y="26" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#247BFF">TEAM LEADER @ LEGACY CODERZ</text>
        <text x="0" y="42" font-family="-apple-system, sans-serif" font-size="10.5" fill="#8B96A8">Full-Stack &amp; AI Systems Engineer</text>
      </g>

      <!-- Bottom Barcode -->
      <g transform="translate(16, 275)">
        <line x1="0" y1="0" x2="0" y2="30" stroke="#FFFFFF" stroke-width="2.5"/>
        <line x1="5" y1="0" x2="5" y2="30" stroke="#FFFFFF" stroke-width="1"/>
        <line x1="9" y1="0" x2="9" y2="30" stroke="#FFFFFF" stroke-width="3"/>
        <line x1="15" y1="0" x2="15" y2="30" stroke="#FFFFFF" stroke-width="1.5"/>
        <line x1="20" y1="0" x2="20" y2="30" stroke="#247BFF" stroke-width="3.5"/>
        <line x1="27" y1="0" x2="27" y2="30" stroke="#FFFFFF" stroke-width="1"/>
        <line x1="33" y1="0" x2="33" y2="30" stroke="#FFFFFF" stroke-width="2"/>
        <line x1="39" y1="0" x2="39" y2="30" stroke="#FF354F" stroke-width="3"/>
        <line x1="46" y1="0" x2="46" y2="30" stroke="#FFFFFF" stroke-width="1"/>
        <line x1="52" y1="0" x2="52" y2="30" stroke="#FFFFFF" stroke-width="2.5"/>
        <line x1="60" y1="0" x2="60" y2="30" stroke="#FFFFFF" stroke-width="1"/>
        <line x1="66" y1="0" x2="66" y2="30" stroke="#247BFF" stroke-width="3"/>
        <line x1="74" y1="0" x2="74" y2="30" stroke="#FFFFFF" stroke-width="1"/>
        <line x1="80" y1="0" x2="80" y2="30" stroke="#FFFFFF" stroke-width="2"/>
        <line x1="88" y1="0" x2="88" y2="30" stroke="#FFFFFF" stroke-width="3.5"/>
        <line x1="96" y1="0" x2="96" y2="30" stroke="#FFFFFF" stroke-width="1"/>
        <line x1="102" y1="0" x2="102" y2="30" stroke="#247BFF" stroke-width="2"/>
        <line x1="110" y1="0" x2="110" y2="30" stroke="#FFFFFF" stroke-width="4"/>
        <line x1="120" y1="0" x2="120" y2="30" stroke="#FFFFFF" stroke-width="1.5"/>
        <line x1="128" y1="0" x2="128" y2="30" stroke="#FF354F" stroke-width="2.5"/>
        <line x1="136" y1="0" x2="136" y2="30" stroke="#FFFFFF" stroke-width="3"/>
        <line x1="145" y1="0" x2="145" y2="30" stroke="#FFFFFF" stroke-width="1"/>
        <line x1="152" y1="0" x2="152" y2="30" stroke="#FFFFFF" stroke-width="2"/>
        <line x1="160" y1="0" x2="160" y2="30" stroke="#247BFF" stroke-width="3"/>
        <line x1="170" y1="0" x2="170" y2="30" stroke="#FFFFFF" stroke-width="1.5"/>
        <line x1="180" y1="0" x2="180" y2="30" stroke="#FFFFFF" stroke-width="3"/>
        <text x="94" y="44" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="8.5" fill="#8B96A8">XNACRO-2026-IN</text>
      </g>
    </g>
  </g>

  <!-- ================= RIGHT: CREDENTIAL METRICS & EVIDENCE ================= -->
  <g transform="translate(340, 40)">
    <!-- Header -->
    <text x="0" y="10" font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="700" letter-spacing="1.5" fill="#8B96A8">04 / BUILDER CREDENTIALS</text>
    <text x="0" y="38" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="28" font-weight="900" fill="#FFFFFF">REAL WORK. REAL IMPACT.</text>
    <text x="0" y="58" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="600" letter-spacing="1" fill="#FF354F">PUBLIC SNAPSHOT // 2026</text>

    <!-- 3 Big Metric Cards -->
    <g transform="translate(0, 80)">
      <!-- Metric 1: Grid cells -->
      <rect x="0" y="0" width="170" height="95" rx="10" fill="#0A1122" stroke="#247BFF" stroke-width="1.2"/>
      <text x="18" y="24" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="700" fill="#8B96A8">RESQ / IIT GUWAHATI</text>
      <text x="18" y="60" font-family="-apple-system, sans-serif" font-size="28" font-weight="900" fill="#247BFF">408k</text>
      <text x="18" y="80" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#F0F6FC">Hazard Grid Cells</text>

      <!-- Metric 2: Team Lead -->
      <rect x="185" y="0" width="170" height="95" rx="10" fill="#0A1122" stroke="#FF354F" stroke-width="1.2"/>
      <text x="203" y="24" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="700" fill="#8B96A8">NATIONAL CHALLENGE</text>
      <text x="203" y="60" font-family="-apple-system, sans-serif" font-size="24" font-weight="900" fill="#FF354F">LEAD</text>
      <text x="203" y="80" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#F0F6FC">Team Legacy Coderz</text>

      <!-- Metric 3: Experience -->
      <rect x="370" y="0" width="170" height="95" rx="10" fill="#0A1122" stroke="#22C55E" stroke-width="1.2"/>
      <text x="388" y="24" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="700" fill="#8B96A8">SYSTEM MATURITY</text>
      <text x="388" y="60" font-family="-apple-system, sans-serif" font-size="28" font-weight="900" fill="#22C55E">2+ Yrs</text>
      <text x="388" y="80" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#F0F6FC">Full-Stack &amp; AI</text>
    </g>

    <!-- Flagship Systems Summary Panel -->
    <g transform="translate(0, 200)">
      <rect x="0" y="0" width="540" height="150" rx="10" fill="#080E1C" stroke="#16233B" stroke-width="1"/>
      <text x="20" y="26" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#8B96A8">FLAGSHIP SYSTEMS ARCHITECTURE</text>

      <!-- System 1 -->
      <g transform="translate(20, 42)">
        <circle cx="5" cy="5" r="4" fill="#247BFF"/>
        <text x="18" y="9" font-family="-apple-system, sans-serif" font-size="13" font-weight="800" fill="#F0F6FC">SurakshaAI — Real-Time Safety Platform</text>
        <text x="18" y="25" font-family="-apple-system, sans-serif" font-size="11" fill="#8B96A8">FastAPI ML inference microservice, dynamic risk index, Mapbox heatmaps &amp; guardian tracking.</text>
      </g>

      <!-- System 2 -->
      <g transform="translate(20, 85)">
        <circle cx="5" cy="5" r="4" fill="#FF354F"/>
        <text x="18" y="9" font-family="-apple-system, sans-serif" font-size="13" font-weight="800" fill="#F0F6FC">RESQ — Damage-Aware Relief Routing</text>
        <text x="18" y="25" font-family="-apple-system, sans-serif" font-size="11" fill="#8B96A8">408,986 cell hazard surface in PostGIS, Valhalla dynamic cost-weighted convoy routing engine.</text>
      </g>
    </g>
  </g>
</svg>'''

    # =========================================================================
    # 5. assets/connect.svg
    # =========================================================================
    connect_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 920 440" width="100%" height="100%">
  <defs>
    <linearGradient id="cn-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070B16"/>
      <stop offset="100%" stop-color="#0A1122"/>
    </linearGradient>
    <linearGradient id="cn-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247BFF" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#FF354F" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#247BFF" stop-opacity="0.8"/>
    </linearGradient>
    <pattern id="cn-dots" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#1C2B49" opacity="0.4"/>
    </pattern>
    <clipPath id="cn-character-clip">
      <rect x="0" y="0" width="410" height="420"/>
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

  <rect x="0" y="0" width="920" height="440" rx="16" fill="url(#cn-bg)" stroke="url(#cn-border)" stroke-width="1.5"/>
  <rect x="0" y="0" width="920" height="440" rx="16" fill="url(#cn-dots)"/>

  <!-- ================= LEFT: POINTING CHARACTER (id.png) ================= -->
  <g transform="translate(10, 20)">
    <!-- Ambient glow behind character pointing right -->
    <ellipse cx="220" cy="220" rx="170" ry="170" fill="#247BFF" fill-opacity="0.12"/>
    <g clip-path="url(#cn-character-clip)">
      <image href="data:image/png;base64,{id_b64}" xlink:href="data:image/png;base64,{id_b64}" x="-10" y="10" width="430" height="390" preserveAspectRatio="xMidYMid meet"/>
    </g>
  </g>

  <!-- ================= RIGHT: HEADLINE & SOCIAL CHANNELS ================= -->
  <g transform="translate(430, 36)">
    <!-- Eyebrow & Headline -->
    <text x="0" y="10" font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="700" letter-spacing="1.5" fill="#247BFF">05 // TRANSMISSION</text>
    <text x="0" y="42" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="34" font-weight="900" fill="#FFFFFF">LET'S BUILD SOMETHING<tspan fill="#FF354F">.</tspan></text>
    <text x="0" y="64" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13" fill="#8B96A8">
      Open for system architecture, spatial intelligence &amp; high-impact roles.
    </text>

    <!-- 4 Social Cards with Nudging Arrows -->
    <g transform="translate(0, 85)">
      <!-- Card 1: GitHub -->
      <g transform="translate(0, 0)">
        <rect x="0" y="0" width="450" height="52" rx="8" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
        <rect x="12" y="12" width="28" height="28" rx="6" fill="#14243F"/>
        <text x="21" y="31" font-family="sans-serif" font-size="15" fill="#FFFFFF">⌥</text>
        <text x="50" y="24" font-family="-apple-system, sans-serif" font-size="13" font-weight="800" fill="#FFFFFF">GitHub</text>
        <text x="50" y="40" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#60A5FA">github.com/xnacro</text>
        <g class="nudge-arrow">
          <text x="415" y="32" font-family="-apple-system, sans-serif" font-size="16" font-weight="900" fill="#247BFF">→</text>
        </g>
      </g>

      <!-- Card 2: LinkedIn -->
      <g transform="translate(0, 62)">
        <rect x="0" y="0" width="450" height="52" rx="8" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
        <rect x="12" y="12" width="28" height="28" rx="6" fill="#0A2540"/>
        <text x="20" y="31" font-family="sans-serif" font-size="14" font-weight="900" fill="#0A66C2">in</text>
        <text x="50" y="24" font-family="-apple-system, sans-serif" font-size="13" font-weight="800" fill="#FFFFFF">LinkedIn</text>
        <text x="50" y="40" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#60A5FA">in/prince-tiwari-727375328</text>
        <g class="nudge-arrow">
          <text x="415" y="32" font-family="-apple-system, sans-serif" font-size="16" font-weight="900" fill="#247BFF">→</text>
        </g>
      </g>

      <!-- Card 3: Instagram -->
      <g transform="translate(0, 124)">
        <rect x="0" y="0" width="450" height="52" rx="8" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
        <rect x="12" y="12" width="28" height="28" rx="6" fill="#2A1224"/>
        <text x="20" y="31" font-family="sans-serif" font-size="14" fill="#E4405F">📸</text>
        <text x="50" y="24" font-family="-apple-system, sans-serif" font-size="13" font-weight="800" fill="#FFFFFF">Instagram</text>
        <text x="50" y="40" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#FF7088">@am_princetiwari</text>
        <g class="nudge-arrow">
          <text x="415" y="32" font-family="-apple-system, sans-serif" font-size="16" font-weight="900" fill="#FF354F">→</text>
        </g>
      </g>

      <!-- Card 4: Email -->
      <g transform="translate(0, 186)">
        <rect x="0" y="0" width="450" height="52" rx="8" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
        <rect x="12" y="12" width="28" height="28" rx="6" fill="#14243F"/>
        <text x="20" y="31" font-family="sans-serif" font-size="14" fill="#EA4335">✉</text>
        <text x="50" y="24" font-family="-apple-system, sans-serif" font-size="13" font-weight="800" fill="#FFFFFF">Direct Comms</text>
        <text x="50" y="40" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#60A5FA">businessofficialtech@gmail.com</text>
        <g class="nudge-arrow">
          <text x="415" y="32" font-family="-apple-system, sans-serif" font-size="16" font-weight="900" fill="#247BFF">→</text>
        </g>
      </g>
    </g>

    <!-- Bottom Guidance -->
    <text x="0" y="355" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" letter-spacing="1" fill="#8B96A8">CLICKABLE LINKS WIRED IN README BELOW</text>
  </g>
</svg>'''

    files = {
        'assets/hero.svg': hero_svg,
        'assets/about-life.svg': about_life_svg,
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
