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
    hero_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 940 470" width="100%" height="100%">
  <defs>
    <linearGradient id="hero-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#060913"/>
      <stop offset="50%" stop-color="#0A1224"/>
      <stop offset="100%" stop-color="#060913"/>
    </linearGradient>
    <linearGradient id="hero-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247BFF" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#8B5CF6" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#FF354F" stop-opacity="0.7"/>
    </linearGradient>
    <linearGradient id="hero-title-blue" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#247BFF"/>
      <stop offset="50%" stop-color="#60A5FA"/>
      <stop offset="100%" stop-color="#38BDF8"/>
    </linearGradient>
    <radialGradient id="hero-glow" cx="80%" cy="50%" r="55%">
      <stop offset="0%" stop-color="#247BFF" stop-opacity="0.25"/>
      <stop offset="50%" stop-color="#8B5CF6" stop-opacity="0.1"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
    </radialGradient>
    <pattern id="hero-dots" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1.1" fill="#1E293B" opacity="0.6"/>
    </pattern>
    <clipPath id="hero-portrait-clip">
      <rect x="530" y="32" width="380" height="406" rx="16"/>
    </clipPath>
  </defs>

  <style>
    @keyframes heroPulseDot {{
      0%, 100% {{ opacity: 1; transform: scale(1); }}
      50%      {{ opacity: 0.35; transform: scale(0.85); }}
    }}
    @keyframes heroBadgeGlow {{
      0%, 100% {{ filter: drop-shadow(0 0 4px rgba(36, 123, 255, 0.4)); }}
      50%      {{ filter: drop-shadow(0 0 10px rgba(56, 189, 248, 0.8)); }}
    }}
    .hero-pulse {{
      animation: heroPulseDot 2.2s ease-in-out infinite;
      transform-origin: 38px 34px;
    }}
    .hero-glow-box {{
      animation: heroBadgeGlow 3s ease-in-out infinite;
    }}
  </style>

  <!-- Container Box -->
  <rect x="0" y="0" width="940" height="470" rx="18" fill="url(#hero-bg)" stroke="url(#hero-border)" stroke-width="1.6"/>
  <rect x="0" y="0" width="940" height="470" rx="18" fill="url(#hero-dots)"/>
  <rect x="460" y="0" width="480" height="470" rx="18" fill="url(#hero-glow)"/>

  <!-- Top Metadata Bar -->
  <g transform="translate(36, 32)">
    <circle cx="6" cy="6" r="4.5" fill="#10B981" class="hero-pulse"/>
    <text x="18" y="10" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', sans-serif" font-size="11" font-weight="800" letter-spacing="1.8" fill="#F0F6FC">PRINCE TIWARI // FULL-STACK &amp; AI/ML SYSTEMS</text>
    <rect x="370" y="-2" width="180" height="18" rx="4" fill="#0C1B33" stroke="#247BFF" stroke-width="0.8"/>
    <text x="378" y="10" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', sans-serif" font-size="9.5" font-weight="700" fill="#38BDF8">BUILDING SURAKSHAAI.ORG</text>
    <text x="868" y="10" text-anchor="end" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', sans-serif" font-size="11" font-weight="700" letter-spacing="1" fill="#8B96A8">MUZAFFARPUR, BIHAR, INDIA</text>
  </g>

  <!-- Left Content Column -->
  <g transform="translate(36, 82)">
    <!-- Eyebrow Subheading -->
    <text x="0" y="4" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', sans-serif" font-size="12" font-weight="800" letter-spacing="2" fill="#818CF8">AI/ML ENGINEER • SYSTEM ARCHITECT • NATIONAL FINALIST</text>

    <!-- Large Name Display -->
    <text x="0" y="58" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', sans-serif" font-size="58" font-weight="900" letter-spacing="-1.5" fill="#FFFFFF">PRINCE</text>
    <text x="0" y="118" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', sans-serif" font-size="58" font-weight="900" letter-spacing="-1.5" fill="url(#hero-title-blue)">TIWARI<tspan fill="#8B96A8" font-size="22" font-weight="600" letter-spacing="0"> (Prince Kumar)</tspan></text>

    <!-- Crimson Slash Bars + Mission Tag -->
    <g transform="translate(255, 28)">
      <rect x="0" y="0" width="4" height="24" rx="2" fill="#FF354F" transform="skewX(-20)"/>
      <rect x="9" y="0" width="4" height="24" rx="2" fill="#FF354F" transform="skewX(-20)"/>
      <rect x="18" y="0" width="4" height="24" rx="2" fill="#FF354F" transform="skewX(-20)"/>
      <text x="32" y="11" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', sans-serif" font-size="11.5" font-weight="900" letter-spacing="1.5" fill="#FFFFFF">BUILD.</text>
      <text x="32" y="25" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', sans-serif" font-size="11.5" font-weight="900" letter-spacing="1.5" fill="#FF354F">SURPASS.</text>
    </g>

    <!-- Dynamic Academic & Role Tag -->
    <g transform="translate(0, 142)">
      <rect x="0" y="0" width="375" height="30" rx="7" fill="#0E1A33" stroke="#247BFF" stroke-width="1.2" class="hero-glow-box"/>
      <circle cx="14" cy="15" r="4" fill="#38BDF8"/>
      <text x="26" y="19" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', sans-serif" font-size="12" font-weight="800" fill="#E2E8F0">B.Tech CSE (AI &amp; ML) • Team Leader @ Legacy Coderz</text>
    </g>

    <!-- Pitch Statement -->
    <text x="0" y="202" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', sans-serif" font-size="14.5" fill="#CBD5E1" line-height="23">
      <tspan x="0" dy="0">Engineering real-time spatial safety AI platforms, predictive risk models,</tspan>
      <tspan x="0" dy="22">and high-concurrency production architectures that make a tangible difference.</tspan>
    </text>

    <!-- Verified National Honors & Credentials Badges Strip -->
    <g transform="translate(0, 252)">
      <!-- Badge 1: Cognithon 2nd -->
      <g transform="translate(0, 0)">
        <rect x="0" y="0" width="225" height="28" rx="6" fill="#131B2E" stroke="#F59E0B" stroke-width="1.1"/>
        <text x="10" y="18" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11.5" font-weight="800" fill="#FBBF24">🏆 2nd @ Cognithon IIIT Bhagalpur</text>
      </g>

      <!-- Badge 2: India Innovates -->
      <g transform="translate(235, 0)">
        <rect x="0" y="0" width="235" height="28" rx="6" fill="#131B2E" stroke="#FF354F" stroke-width="1.1"/>
        <text x="10" y="18" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11.5" font-weight="800" fill="#FF8A9A">🇮🇳 National Finalist India Innovates '26</text>
      </g>
    </g>

    <!-- Strip 2: Flipkart GRiD & Location -->
    <g transform="translate(0, 290)">
      <!-- Badge 3: Flipkart GRiD -->
      <g transform="translate(0, 0)">
        <rect x="0" y="0" width="240" height="28" rx="6" fill="#131B2E" stroke="#247BFF" stroke-width="1.1"/>
        <text x="10" y="18" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11.5" font-weight="800" fill="#60A5FA">⚡ Flipkart GRiD '26 Semi-Finalist</text>
      </g>

      <!-- Badge 4: Location -->
      <g transform="translate(250, 0)">
        <rect x="0" y="0" width="220" height="28" rx="6" fill="#131B2E" stroke="#10B981" stroke-width="1.1"/>
        <text x="10" y="18" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11.5" font-weight="800" fill="#34D399">📍 Muzaffarpur, Bihar, India</text>
      </g>
    </g>

    <!-- Bottom Status Bar -->
    <g transform="translate(0, 335)">
      <rect x="0" y="0" width="470" height="28" rx="6" fill="#080E1C" stroke="#1E293B" stroke-width="1"/>
      <circle cx="14" cy="14" r="3.5" fill="#10B981"/>
      <text x="25" y="18" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', sans-serif" font-size="10.5" font-weight="700" fill="#94A3B8">STATUS: <tspan fill="#38BDF8">ACTIVE SHIPPING</tspan> • REPO: <tspan fill="#F1F5F9">github.com/xnacro</tspan></text>
    </g>
  </g>

  <!-- Right Portrait Column with Inlined PNG -->
  <g>
    <rect x="530" y="32" width="380" height="406" rx="16" fill="#0C1527" stroke="#1C2D4A" stroke-width="1.2"/>
    <g clip-path="url(#hero-portrait-clip)">
      <image href="data:image/png;base64,{mine_b64}" xlink:href="data:image/png;base64,{mine_b64}" x="525" y="24" width="390" height="420" preserveAspectRatio="xMidYMid meet"/>
    </g>
    <!-- Overlay Badge over portrait bottom -->
    <g transform="translate(685, 386)">
      <rect x="0" y="0" width="205" height="36" rx="8" fill="#0B1324" stroke="#247BFF" stroke-width="1.3"/>
      <rect x="0" y="0" width="8" height="36" rx="4" fill="#247BFF"/>
      <text x="18" y="16" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11" font-weight="800" fill="#FFFFFF">AI &amp; SYSTEMS ARCHITECT</text>
      <text x="18" y="29" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="9.5" font-weight="700" fill="#38BDF8">@xnacro • Legacy Coderz</text>
    </g>
  </g>
</svg>'''

    # =========================================================================
    # 2. assets/about-life.svg
    # =========================================================================
    about_life_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 940 450" width="100%" height="100%">
  <defs>
    <linearGradient id="ab-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247BFF" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#8B5CF6" stop-opacity="0.3"/>
    </linearGradient>
    <linearGradient id="ab-card-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0A1224"/>
      <stop offset="100%" stop-color="#060913"/>
    </linearGradient>
    <pattern id="ab-dots" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#1E293B" opacity="0.45"/>
    </pattern>
    <clipPath id="ab-avatar-clip">
      <rect x="0" y="0" width="145" height="145" rx="14"/>
    </clipPath>
  </defs>

  <rect x="0" y="0" width="940" height="450" rx="18" fill="#060913"/>
  <rect x="0" y="0" width="940" height="450" rx="18" fill="url(#ab-dots)"/>

  <!-- ================= CARD 1: FROM THOUGHT TO PRODUCTION ================= -->
  <g transform="translate(20, 20)">
    <rect x="0" y="0" width="440" height="410" rx="16" fill="url(#ab-card-bg)" stroke="url(#ab-border)" stroke-width="1.3"/>

    <g transform="translate(24, 24)">
      <!-- Eyebrow Subheading -->
      <text x="0" y="10" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', sans-serif" font-size="10.5" font-weight="800" letter-spacing="2" fill="#60A5FA">01 // FROM RESEARCH TO RUNTIME</text>
      <text x="0" y="36" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', sans-serif" font-size="22" font-weight="900" fill="#FFFFFF">ENGINEERED FOR IMPACT<tspan fill="#FF354F">.</tspan></text>

      <!-- Terminal Window Simulation -->
      <g transform="translate(0, 56)">
        <rect x="0" y="0" width="392" height="96" rx="8" fill="#040711" stroke="#16233B" stroke-width="1"/>
        <circle cx="16" cy="14" r="3.5" fill="#EF4444"/>
        <circle cx="28" cy="14" r="3.5" fill="#F59E0B"/>
        <circle cx="40" cy="14" r="3.5" fill="#10B981"/>
        <text x="58" y="17" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="10" font-weight="700" fill="#64748B">surakshaai.org/core/runtime</text>

        <text x="16" y="44" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', monospace" font-size="11.5" font-weight="700" fill="#38BDF8">&gt; surakshaai.deploy_intelligence(mode="real_time")</text>

        <!-- 3 Step Pills: Ideate -> Engineer -> Ship -->
        <g transform="translate(16, 56)">
          <rect x="0" y="0" width="76" height="26" rx="5" fill="#0E1A33" stroke="#1E2F4D" stroke-width="1"/>
          <text x="12" y="17" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="10" font-weight="800" fill="#94A3B8">01 IDEATE</text>

          <text x="84" y="17" font-family="sans-serif" font-size="11" fill="#475569">→</text>

          <rect x="98" y="0" width="94" height="26" rx="5" fill="#0E1A33" stroke="#1E2F4D" stroke-width="1"/>
          <text x="10" y="17" transform="translate(98, 0)" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="10" font-weight="800" fill="#94A3B8">02 ARCHITECT</text>

          <text x="200" y="17" font-family="sans-serif" font-size="11" fill="#475569">→</text>

          <rect x="214" y="0" width="80" height="26" rx="5" fill="#152B52" stroke="#247BFF" stroke-width="1.2"/>
          <text x="12" y="17" transform="translate(214, 0)" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="10" font-weight="900" fill="#38BDF8">03 SHIP</text>
        </g>
      </g>

      <!-- 3 Capabilities Rows with clean modern fonts -->
      <g transform="translate(0, 176)">
        <g transform="translate(0, 0)">
          <circle cx="8" cy="10" r="5" fill="#38BDF8"/>
          <text x="22" y="14" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', sans-serif" font-size="13.5" font-weight="800" fill="#F8FAFC">AI &amp; Machine Learning Pipelines</text>
          <text x="22" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="12" fill="#94A3B8">PyTorch, anomaly detection, CV models &amp; RAG vector retrieval.</text>
        </g>

        <g transform="translate(0, 52)">
          <circle cx="8" cy="10" r="5" fill="#FF354F"/>
          <text x="22" y="14" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', sans-serif" font-size="13.5" font-weight="800" fill="#F8FAFC">Geospatial Risk Modeling &amp; PostGIS</text>
          <text x="22" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="12" fill="#94A3B8">408,986 hazard cells, Valhalla routing &amp; Dynamic Safety Index.</text>
        </g>

        <g transform="translate(0, 104)">
          <circle cx="8" cy="10" r="5" fill="#10B981"/>
          <text x="22" y="14" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', sans-serif" font-size="13.5" font-weight="800" fill="#F8FAFC">Full-Stack Production Platforms</text>
          <text x="22" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="12" fill="#94A3B8">High-concurrency FastAPI microservices, React, Next.js &amp; WebSockets.</text>
        </g>
      </g>
    </g>
  </g>

  <!-- ================= CARD 2: NATIONAL HONORS & LEADERSHIP ================= -->
  <g transform="translate(480, 20)">
    <rect x="0" y="0" width="440" height="410" rx="16" fill="url(#ab-card-bg)" stroke="url(#ab-border)" stroke-width="1.3"/>

    <g transform="translate(24, 24)">
      <!-- Eyebrow Subheading -->
      <text x="0" y="10" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', sans-serif" font-size="10.5" font-weight="800" letter-spacing="2" fill="#A855F7">02 // COMPETITIVE TRAJECTORY &amp; HONORS</text>
      <text x="0" y="36" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', sans-serif" font-size="22" font-weight="900" fill="#FFFFFF">PROVEN ON THE NATIONAL STAGE<tspan fill="#F59E0B">.</tspan></text>

      <!-- Content Split: Photo + Highlights -->
      <g transform="translate(0, 60)">
        <!-- Portrait Box -->
        <g transform="translate(0, 0)">
          <rect x="0" y="0" width="135" height="135" rx="12" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
          <g clip-path="url(#ab-avatar-clip)">
            <image href="data:image/png;base64,{mine_b64}" xlink:href="data:image/png;base64,{mine_b64}" x="-10" y="-10" width="155" height="155" preserveAspectRatio="xMidYMid meet"/>
          </g>
          <rect x="8" y="106" width="119" height="22" rx="4" fill="#0B1324" stroke="#247BFF" stroke-width="0.8"/>
          <text x="14" y="121" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="8.5" font-weight="800" fill="#60A5FA">PRINCE TIWARI • CSE (AI&amp;ML)</text>
        </g>

        <!-- Right Side Principles & Milestones -->
        <g transform="translate(150, 6)">
          <g transform="translate(0, 0)">
            <rect x="0" y="0" width="235" height="34" rx="6" fill="#131F33" stroke="#F59E0B" stroke-width="0.8"/>
            <text x="10" y="15" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="10.5" font-weight="900" fill="#FBBF24">🏆 2nd @ COGNITHON</text>
            <text x="10" y="27" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="9" fill="#CBD5E1">IIIT Bhagalpur National Hackathon</text>
          </g>

          <g transform="translate(0, 42)">
            <rect x="0" y="0" width="235" height="34" rx="6" fill="#131F33" stroke="#FF354F" stroke-width="0.8"/>
            <text x="10" y="15" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="10.5" font-weight="900" fill="#FF8A9A">🇮🇳 INDIA INNOVATES 2026</text>
            <text x="10" y="27" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="9" fill="#CBD5E1">National Finalist</text>
          </g>

          <g transform="translate(0, 84)">
            <rect x="0" y="0" width="235" height="34" rx="6" fill="#131F33" stroke="#247BFF" stroke-width="0.8"/>
            <text x="10" y="15" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="10.5" font-weight="900" fill="#60A5FA">⚡ FLIPKART GRiD 2026</text>
            <text x="10" y="27" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="9" fill="#CBD5E1">National Semi-Finalist</text>
          </g>
        </g>
      </g>

      <!-- Bottom Leadership Card -->
      <g transform="translate(0, 222)">
        <rect x="0" y="0" width="392" height="110" rx="10" fill="#080E1C" stroke="#16233B" stroke-width="1"/>
        <text x="16" y="24" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', sans-serif" font-size="10" font-weight="800" letter-spacing="1.5" fill="#38BDF8">LEADERSHIP • COLLABORATION</text>
        <text x="16" y="48" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="15" font-weight="900" fill="#FFFFFF">Team Leader @ Legacy Coderz</text>
        <text x="16" y="68" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="12" fill="#94A3B8">
          Leading multi-disciplinary engineering squads under high-pressure competitive
        </text>
        <text x="16" y="86" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="12" fill="#94A3B8">
          deadlines, architecting end-to-end solutions that solve acute real-world challenges.
        </text>
      </g>
    </g>
  </g>
</svg>'''

    # =========================================================================
    # 3. assets/stack.svg (PLANETARY ORBITAL ANIMATION + ALL ML SKILLS)
    # =========================================================================
    stack_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 940 500" width="100%" height="100%">
  <defs>
    <linearGradient id="stk-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#060913"/>
      <stop offset="60%" stop-color="#091224"/>
      <stop offset="100%" stop-color="#060913"/>
    </linearGradient>
    <linearGradient id="stk-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247BFF" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#8B5CF6" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="#FF354F" stop-opacity="0.5"/>
    </linearGradient>
    <radialGradient id="sun-glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.9"/>
      <stop offset="35%" stop-color="#247BFF" stop-opacity="0.4"/>
      <stop offset="70%" stop-color="#8B5CF6" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#060913" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="planet-glow-cyan" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#0369A1" stop-opacity="0.2"/>
    </radialGradient>
    <pattern id="stk-dots" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1.1" fill="#1E293B" opacity="0.45"/>
    </pattern>
  </defs>

  <style>
    @keyframes orbitPulse {{
      0%, 100% {{ transform: scale(1); filter: drop-shadow(0 0 8px rgba(56, 189, 248, 0.6)); }}
      50%      {{ transform: scale(1.06); filter: drop-shadow(0 0 18px rgba(36, 123, 255, 0.9)); }}
    }}
    @keyframes orbitSpinCW {{
      from {{ transform: rotate(0deg); }}
      to   {{ transform: rotate(360deg); }}
    }}
    @keyframes orbitSpinCCW {{
      from {{ transform: rotate(0deg); }}
      to   {{ transform: rotate(-360deg); }}
    }}
    .core-sun {{
      animation: orbitPulse 3.5s ease-in-out infinite;
      transform-origin: 205px 260px;
    }}
  </style>

  <rect x="0" y="0" width="940" height="500" rx="18" fill="url(#stk-bg)" stroke="url(#stk-border)" stroke-width="1.6"/>
  <rect x="0" y="0" width="940" height="500" rx="18" fill="url(#stk-dots)"/>

  <!-- Top Title Header with Sleek Modern Subheading Font -->
  <g transform="translate(36, 28)">
    <text x="0" y="10" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', sans-serif" font-size="11" font-weight="800" letter-spacing="2.2" fill="#60A5FA">03 // MY ENGINE ROOM</text>
    <text x="0" y="38" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', sans-serif" font-size="26" font-weight="900" fill="#FFFFFF">TOOLS CHANGE. CURIOSITY DOESN'T<tspan fill="#FF354F">.</tspan></text>
    <text x="0" y="58" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', sans-serif" font-size="11" font-weight="700" letter-spacing="1.5" fill="#38BDF8">AI &amp; DEEP LEARNING • SPATIAL INTELLIGENCE • PRODUCTION RUNTIMES</text>
  </g>

  <!-- ================= LEFT: COMPLETE PLANETARY ORBITAL SYSTEM ================= -->
  <g transform="translate(0, 0)">
    <!-- Orbit 1: Inner Orbit (Python / Core AI) - Radius 68 -->
    <ellipse cx="205" cy="260" rx="68" ry="60" fill="none" stroke="#38BDF8" stroke-width="1.2" stroke-opacity="0.35" stroke-dasharray="4,4" transform="rotate(-15 205 260)"/>

    <!-- Orbit 2: Machine Learning Tensor Orbit - Ellipse rx=108, ry=78, deg=28 -->
    <ellipse cx="205" cy="260" rx="108" ry="78" fill="none" stroke="#A855F7" stroke-width="1.2" stroke-opacity="0.3" stroke-dasharray="5,4" transform="rotate(28 205 260)"/>

    <!-- Orbit 3: Frontend & Spatial Visualizer Orbit - Ellipse rx=142, ry=68, deg=-32 -->
    <ellipse cx="205" cy="260" rx="142" ry="68" fill="none" stroke="#247BFF" stroke-width="1.2" stroke-opacity="0.35" stroke-dasharray="6,4" transform="rotate(-32 205 260)"/>

    <!-- Orbit 4: PostGIS & Geospatial Hazard Orbit - Ellipse rx=172, ry=92, deg=45 -->
    <ellipse cx="205" cy="260" rx="172" ry="92" fill="none" stroke="#FF354F" stroke-width="1.2" stroke-opacity="0.35" stroke-dasharray="5,5" transform="rotate(45 205 260)"/>

    <!-- Orbit 5: High-Concurrency Backend Orbit - Ellipse rx=194, ry=104, deg=-58 -->
    <ellipse cx="205" cy="260" rx="194" ry="104" fill="none" stroke="#10B981" stroke-width="1.2" stroke-opacity="0.3" stroke-dasharray="6,5" transform="rotate(-58 205 260)"/>

    <!-- Ambient Orbital Particle Stars -->
    <circle cx="150" cy="180" r="1.5" fill="#38BDF8" opacity="0.6">
      <animate attributeName="opacity" values="0.2;0.8;0.2" dur="2s" repeatCount="indefinite"/>
    </circle>
    <circle cx="270" cy="330" r="1.5" fill="#A855F7" opacity="0.7">
      <animate attributeName="opacity" values="0.3;0.9;0.3" dur="2.7s" repeatCount="indefinite"/>
    </circle>
    <circle cx="85" cy="270" r="1.5" fill="#FF354F" opacity="0.6">
      <animate attributeName="opacity" values="0.2;0.7;0.2" dur="3.2s" repeatCount="indefinite"/>
    </circle>
    <circle cx="320" cy="210" r="1.5" fill="#10B981" opacity="0.5">
      <animate attributeName="opacity" values="0.1;0.8;0.1" dur="2.4s" repeatCount="indefinite"/>
    </circle>

    <!-- CENTRAL GLOWING SUN / CORE (PT - Prince Tiwari) -->
    <g class="core-sun">
      <!-- Outer Corona Glow -->
      <circle cx="205" cy="260" r="44" fill="url(#sun-glow)"/>
      <circle cx="205" cy="260" r="32" fill="none" stroke="#38BDF8" stroke-width="1.2" stroke-dasharray="3,3" opacity="0.7">
        <animateTransform attributeName="transform" type="rotate" from="0 205 260" to="360 205 260" dur="15s" repeatCount="indefinite"/>
      </circle>
      <!-- Sun Core Badge -->
      <rect x="180" y="235" width="50" height="50" rx="12" fill="#09142A" stroke="#247BFF" stroke-width="2"/>
      <text x="205" y="264" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="18" font-weight="900" fill="#FFFFFF">PT</text>
      <text x="205" y="277" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="7.5" font-weight="800" fill="#38BDF8" letter-spacing="1">CORE</text>
    </g>

    <!-- ================= PLANETARY REVOLVING BODIES ================= -->

    <!-- PLANET 1: Python / AI (Inner Orbit - 12s Period) -->
    <g>
      <animateTransform attributeName="transform" type="rotate" from="0 205 260" to="360 205 260" dur="12s" repeatCount="indefinite"/>
      <g transform="translate(205, 196)">
        <!-- Counter-rotate so text stays upright -->
        <animateTransform attributeName="transform" type="rotate" from="0 0 0" to="-360 0 0" dur="12s" repeatCount="indefinite"/>
        <circle cx="0" cy="0" r="16" fill="#08152B" stroke="#38BDF8" stroke-width="1.6"/>
        <circle cx="0" cy="0" r="19" fill="none" stroke="#38BDF8" stroke-width="0.8" stroke-opacity="0.4"/>
        <text x="0" y="4" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="9.5" font-weight="900" fill="#38BDF8">Py</text>
        <!-- Mini Orbiting Moon: PyTorch -->
        <g>
          <animateTransform attributeName="transform" type="rotate" from="0 0 0" to="360 0 0" dur="3s" repeatCount="indefinite"/>
          <circle cx="23" cy="0" r="3.5" fill="#EF4444"/>
        </g>
      </g>
    </g>

    <!-- PLANET 2: PyTorch / Machine Learning (Mid Orbit - 18s Period) -->
    <g>
      <animateTransform attributeName="transform" type="rotate" from="90 205 260" to="450 205 260" dur="18s" repeatCount="indefinite"/>
      <g transform="translate(295, 235)">
        <animateTransform attributeName="transform" type="rotate" from="0 0 0" to="-360 0 0" dur="18s" repeatCount="indefinite"/>
        <circle cx="0" cy="0" r="16" fill="#170F28" stroke="#A855F7" stroke-width="1.6"/>
        <circle cx="0" cy="0" r="19" fill="none" stroke="#A855F7" stroke-width="0.8" stroke-opacity="0.4"/>
        <text x="0" y="4" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="9.5" font-weight="900" fill="#D8B4FE">ML</text>
      </g>
    </g>

    <!-- PLANET 3: React / Frontend (Mid-Outer Orbit - 24s Period) -->
    <g>
      <animateTransform attributeName="transform" type="rotate" from="210 205 260" to="570 205 260" dur="24s" repeatCount="indefinite"/>
      <g transform="translate(90, 240)">
        <animateTransform attributeName="transform" type="rotate" from="0 0 0" to="-360 0 0" dur="24s" repeatCount="indefinite"/>
        <circle cx="0" cy="0" r="16" fill="#07152B" stroke="#247BFF" stroke-width="1.6"/>
        <circle cx="0" cy="0" r="19" fill="none" stroke="#247BFF" stroke-width="0.8" stroke-opacity="0.4"/>
        <text x="0" y="4" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="9.5" font-weight="900" fill="#93C5FD">Re</text>
      </g>
    </g>

    <!-- PLANET 4: PostGIS / Spatial Intelligence (Outer Orbit - 30s Counter Period) -->
    <g>
      <animateTransform attributeName="transform" type="rotate" from="360 205 260" to="0 205 260" dur="30s" repeatCount="indefinite"/>
      <g transform="translate(125, 360)">
        <animateTransform attributeName="transform" type="rotate" from="0 0 0" to="360 0 0" dur="30s" repeatCount="indefinite"/>
        <circle cx="0" cy="0" r="16" fill="#1C0E1E" stroke="#FF354F" stroke-width="1.6"/>
        <circle cx="0" cy="0" r="19" fill="none" stroke="#FF354F" stroke-width="0.8" stroke-opacity="0.4"/>
        <text x="0" y="4" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="9" font-weight="900" fill="#FFA3AF">GIS</text>
      </g>
    </g>

    <!-- PLANET 5: FastAPI / Scalable Microservices (Deep Orbit - 36s Period) -->
    <g>
      <animateTransform attributeName="transform" type="rotate" from="300 205 260" to="660 205 260" dur="36s" repeatCount="indefinite"/>
      <g transform="translate(320, 345)">
        <animateTransform attributeName="transform" type="rotate" from="0 0 0" to="-360 0 0" dur="36s" repeatCount="indefinite"/>
        <circle cx="0" cy="0" r="16" fill="#0A1D1A" stroke="#10B981" stroke-width="1.6"/>
        <circle cx="0" cy="0" r="19" fill="none" stroke="#10B981" stroke-width="0.8" stroke-opacity="0.4"/>
        <text x="0" y="4" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="9" font-weight="900" fill="#6EE7B7">API</text>
      </g>
    </g>

    <!-- Left Footnote -->
    <text x="205" y="458" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', sans-serif" font-size="10" font-weight="800" letter-spacing="1.5" fill="#64748B">PLANETARY RUNTIME • CONTINUOUS ORBITAL SHIP CYCLE</text>
  </g>

  <!-- ================= RIGHT: COMPLETE STACK WITH FULL AI & ML SPECIALIZATION ================= -->
  <g transform="translate(425, 100)">

    <!-- Section 01: AI & Machine Learning (CORE SPECIALIZATION) -->
    <g transform="translate(0, 0)">
      <text x="0" y="11" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', sans-serif" font-size="10.5" font-weight="800" letter-spacing="1.8" fill="#C084FC">01 // AI &amp; MACHINE LEARNING (CORE)</text>
      <g transform="translate(0, 20)">
        <!-- PyTorch -->
        <rect x="0" y="0" width="85" height="30" rx="6" fill="#160C26" stroke="#A855F7" stroke-width="1.2"/>
        <text x="12" y="19" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11.5" font-weight="800" fill="#E9D5FF">PyTorch</text>

        <!-- TensorFlow -->
        <rect x="93" y="0" width="105" height="30" rx="6" fill="#160C26" stroke="#A855F7" stroke-width="1.2"/>
        <text x="105" y="19" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11.5" font-weight="800" fill="#E9D5FF">TensorFlow</text>

        <!-- Scikit-Learn -->
        <rect x="206" y="0" width="102" height="30" rx="6" fill="#160C26" stroke="#A855F7" stroke-width="1.2"/>
        <text x="218" y="19" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11.5" font-weight="800" fill="#E9D5FF">Scikit-Learn</text>

        <!-- OpenCV -->
        <rect x="316" y="0" width="82" height="30" rx="6" fill="#160C26" stroke="#A855F7" stroke-width="1.2"/>
        <text x="328" y="19" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11.5" font-weight="800" fill="#E9D5FF">OpenCV</text>

        <!-- LangChain / RAG -->
        <rect x="406" y="0" width="76" height="30" rx="6" fill="#160C26" stroke="#A855F7" stroke-width="1.2"/>
        <text x="416" y="19" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11" font-weight="800" fill="#E9D5FF">LangChain</text>
      </g>
    </g>

    <!-- Section 02: Core Programming Languages -->
    <g transform="translate(0, 78)">
      <text x="0" y="11" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', sans-serif" font-size="10.5" font-weight="800" letter-spacing="1.8" fill="#60A5FA">02 // PROGRAMMING LANGUAGES</text>
      <g transform="translate(0, 20)">
        <rect x="0" y="0" width="80" height="30" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
        <text x="14" y="19" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11.5" font-weight="800" fill="#F1F5F9">Python</text>

        <rect x="88" y="0" width="98" height="30" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
        <text x="100" y="19" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11.5" font-weight="800" fill="#F1F5F9">TypeScript</text>

        <rect x="194" y="0" width="98" height="30" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
        <text x="206" y="19" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11.5" font-weight="800" fill="#F1F5F9">JavaScript</text>

        <rect x="300" y="0" width="62" height="30" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
        <text x="312" y="19" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11.5" font-weight="800" fill="#F1F5F9">SQL</text>

        <rect x="370" y="0" width="58" height="30" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
        <text x="382" y="19" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11.5" font-weight="800" fill="#F1F5F9">C++</text>

        <rect x="436" y="0" width="46" height="30" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
        <text x="444" y="19" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11.5" font-weight="800" fill="#F1F5F9">Java</text>
      </g>
    </g>

    <!-- Section 03: Frontend & Spatial Runtime -->
    <g transform="translate(0, 156)">
      <text x="0" y="11" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', sans-serif" font-size="10.5" font-weight="800" letter-spacing="1.8" fill="#38BDF8">03 // FRONTEND &amp; SPATIAL VISUALIZATION</text>
      <g transform="translate(0, 20)">
        <rect x="0" y="0" width="72" height="30" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
        <text x="14" y="19" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11.5" font-weight="800" fill="#F1F5F9">React</text>

        <rect x="80" y="0" width="78" height="30" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
        <text x="92" y="19" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11.5" font-weight="800" fill="#F1F5F9">Next.js</text>

        <rect x="166" y="0" width="115" height="30" rx="6" fill="#081A33" stroke="#247BFF" stroke-width="1.2"/>
        <text x="178" y="19" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11.5" font-weight="800" fill="#60A5FA">MapLibre GL</text>

        <rect x="289" y="0" width="76" height="30" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
        <text x="301" y="19" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11.5" font-weight="800" fill="#F1F5F9">Leaflet</text>

        <rect x="373" y="0" width="109" height="30" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
        <text x="383" y="19" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11.5" font-weight="800" fill="#F1F5F9">Tailwind CSS</text>
      </g>
    </g>

    <!-- Section 04: Backend, Database & Cloud Systems -->
    <g transform="translate(0, 234)">
      <text x="0" y="11" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', sans-serif" font-size="10.5" font-weight="800" letter-spacing="1.8" fill="#34D399">04 // BACKEND &amp; SPATIAL INFRASTRUCTURE</text>
      <g transform="translate(0, 20)">
        <rect x="0" y="0" width="82" height="30" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
        <text x="14" y="19" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11.5" font-weight="800" fill="#F1F5F9">FastAPI</text>

        <rect x="90" y="0" width="82" height="30" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
        <text x="102" y="19" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11.5" font-weight="800" fill="#F1F5F9">Node.js</text>

        <rect x="180" y="0" width="138" height="30" rx="6" fill="#1C1022" stroke="#FF354F" stroke-width="1.2"/>
        <text x="190" y="19" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11.5" font-weight="800" fill="#FF8A9A">PostgreSQL / GIS</text>

        <rect x="326" y="0" width="70" height="30" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
        <text x="338" y="19" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11.5" font-weight="800" fill="#F1F5F9">Redis</text>

        <rect x="404" y="0" width="78" height="30" rx="6" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
        <text x="416" y="19" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11.5" font-weight="800" fill="#F1F5F9">Docker</text>
      </g>
    </g>

    <!-- Right Footnote Guidance -->
    <g transform="translate(0, 316)">
      <rect x="0" y="0" width="482" height="26" rx="5" fill="#080F1E" stroke="#16233B" stroke-width="0.8"/>
      <text x="14" y="17" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', sans-serif" font-size="10" font-weight="800" letter-spacing="1.5" fill="#38BDF8">EXPLORE • ARCHITECT • REPEAT • ZERO DRIFT</text>
    </g>
  </g>
</svg>'''

    # =========================================================================
    # 4. assets/id-dashboard.svg (NATIONAL HONORS & CREDENTIALS DASHBOARD)
    # =========================================================================
    id_dashboard_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 940 480" width="100%" height="100%">
  <defs>
    <linearGradient id="id-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#060913"/>
      <stop offset="60%" stop-color="#0B1324"/>
      <stop offset="100%" stop-color="#060913"/>
    </linearGradient>
    <linearGradient id="id-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247BFF" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#F59E0B" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="#FF354F" stop-opacity="0.7"/>
    </linearGradient>
    <linearGradient id="id-lanyard" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1848A0"/>
      <stop offset="50%" stop-color="#247BFF"/>
      <stop offset="100%" stop-color="#1848A0"/>
    </linearGradient>
    <pattern id="id-dots" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1.1" fill="#1E293B" opacity="0.45"/>
    </pattern>
    <clipPath id="id-badge-photo">
      <rect x="0" y="0" width="120" height="120" rx="10"/>
    </clipPath>
  </defs>

  <style>
    @keyframes pendulumSwing {{
      0%   {{ transform: rotate(-1.5deg); }}
      50%  {{ transform: rotate(1.5deg); }}
      100% {{ transform: rotate(-1.5deg); }}
    }}
    .hanging-badge {{
      animation: pendulumSwing 4.5s ease-in-out infinite;
      transform-origin: 175px 35px;
    }}
  </style>

  <rect x="0" y="0" width="940" height="480" rx="18" fill="url(#id-bg)" stroke="url(#id-border)" stroke-width="1.6"/>
  <rect x="0" y="0" width="940" height="480" rx="18" fill="url(#id-dots)"/>

  <!-- ================= LEFT: HANGING LANYARD ID BADGE ================= -->
  <g class="hanging-badge">
    <!-- Lanyard Strap -->
    <rect x="160" y="-10" width="30" height="55" fill="url(#id-lanyard)"/>
    <text x="175" y="25" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="7.5" font-weight="900" fill="#FFFFFF" transform="rotate(90 175 25)">LEGACY CODERZ</text>

    <!-- Metal Clasp & Clip -->
    <rect x="156" y="42" width="38" height="14" rx="4" fill="#94A3B8" stroke="#CBD5E1" stroke-width="1"/>
    <rect x="165" y="56" width="20" height="10" rx="2" fill="#64748B"/>

    <!-- ID Badge Body (Outer Card) -->
    <g transform="translate(62, 66)">
      <rect x="0" y="0" width="226" height="360" rx="14" fill="#0A1224" stroke="#247BFF" stroke-width="1.6"/>

      <!-- Top Red Stripe with Clip Slot -->
      <rect x="0" y="0" width="226" height="28" rx="14" fill="#FF354F"/>
      <rect x="88" y="9" width="50" height="7" rx="3.5" fill="#060913"/>

      <!-- Pass Header -->
      <g transform="translate(16, 44)">
        <text x="0" y="0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="10.5" font-weight="800" fill="#60A5FA">OFFICIAL BUILDER PASS</text>
        <text x="194" y="0" text-anchor="end" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="10.5" font-weight="800" fill="#94A3B8">2026</text>
      </g>

      <!-- Portrait Box -->
      <g transform="translate(16, 56)">
        <rect x="0" y="0" width="194" height="140" rx="10" fill="#050811" stroke="#1E2F4D" stroke-width="1"/>
        <g clip-path="url(#id-badge-photo)" transform="translate(37, 10)">
          <image href="data:image/png;base64,{mine_b64}" xlink:href="data:image/png;base64,{mine_b64}" x="-15" y="-10" width="150" height="150" preserveAspectRatio="xMidYMid meet"/>
        </g>
      </g>

      <!-- Identity Details -->
      <g transform="translate(16, 216)">
        <text x="0" y="10" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="16" font-weight="900" fill="#FFFFFF">PRINCE TIWARI</text>
        <text x="0" y="27" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="10" font-weight="800" fill="#38BDF8">FOUNDER @ SURAKSHAAI.ORG</text>
        <text x="0" y="43" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="10" font-weight="700" fill="#A855F7">B.Tech CSE (AI &amp; ML)</text>
        <text x="0" y="58" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="9.5" fill="#94A3B8">Muzaffarpur, Bihar, India</text>
      </g>

      <!-- Bottom Barcode -->
      <g transform="translate(16, 292)">
        <line x1="0" y1="0" x2="0" y2="30" stroke="#FFFFFF" stroke-width="2.5"/>
        <line x1="5" y1="0" x2="5" y2="30" stroke="#FFFFFF" stroke-width="1"/>
        <line x1="9" y1="0" x2="9" y2="30" stroke="#FFFFFF" stroke-width="3"/>
        <line x1="16" y1="0" x2="16" y2="30" stroke="#247BFF" stroke-width="3.5"/>
        <line x1="24" y1="0" x2="24" y2="30" stroke="#FFFFFF" stroke-width="1"/>
        <line x1="31" y1="0" x2="31" y2="30" stroke="#FFFFFF" stroke-width="2"/>
        <line x1="38" y1="0" x2="38" y2="30" stroke="#FF354F" stroke-width="3"/>
        <line x1="46" y1="0" x2="46" y2="30" stroke="#FFFFFF" stroke-width="1.5"/>
        <line x1="54" y1="0" x2="54" y2="30" stroke="#FFFFFF" stroke-width="2.5"/>
        <line x1="62" y1="0" x2="62" y2="30" stroke="#247BFF" stroke-width="3"/>
        <line x1="72" y1="0" x2="72" y2="30" stroke="#FFFFFF" stroke-width="1"/>
        <line x1="80" y1="0" x2="80" y2="30" stroke="#FFFFFF" stroke-width="3.5"/>
        <line x1="90" y1="0" x2="90" y2="30" stroke="#FFFFFF" stroke-width="1"/>
        <line x1="98" y1="0" x2="98" y2="30" stroke="#247BFF" stroke-width="2"/>
        <line x1="108" y1="0" x2="108" y2="30" stroke="#FFFFFF" stroke-width="4"/>
        <line x1="118" y1="0" x2="118" y2="30" stroke="#FFFFFF" stroke-width="1.5"/>
        <line x1="126" y1="0" x2="126" y2="30" stroke="#FF354F" stroke-width="2.5"/>
        <line x1="134" y1="0" x2="134" y2="30" stroke="#FFFFFF" stroke-width="3"/>
        <line x1="144" y1="0" x2="144" y2="30" stroke="#FFFFFF" stroke-width="1"/>
        <line x1="152" y1="0" x2="152" y2="30" stroke="#FFFFFF" stroke-width="2"/>
        <line x1="162" y1="0" x2="162" y2="30" stroke="#247BFF" stroke-width="3"/>
        <line x1="172" y1="0" x2="172" y2="30" stroke="#FFFFFF" stroke-width="1.5"/>
        <line x1="184" y1="0" x2="184" y2="30" stroke="#FFFFFF" stroke-width="3"/>
        <text x="97" y="44" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="8.5" font-weight="700" fill="#94A3B8">XNACRO-2026-IN-VERIFIED</text>
      </g>
    </g>
  </g>

  <!-- ================= RIGHT: CREDENTIAL METRICS & NATIONAL HONORS ================= -->
  <g transform="translate(345, 30)">
    <!-- Header with Sleek Modern Subheading Font -->
    <text x="0" y="10" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', sans-serif" font-size="11" font-weight="800" letter-spacing="2" fill="#60A5FA">04 // VERIFIED NATIONAL HONORS &amp; EVIDENCE</text>
    <text x="0" y="38" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', sans-serif" font-size="28" font-weight="900" fill="#FFFFFF">PROVEN RECORD. VERIFIED IMPACT<tspan fill="#F59E0B">.</tspan></text>
    <text x="0" y="58" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', sans-serif" font-size="11" font-weight="700" letter-spacing="1.2" fill="#F59E0B">PUBLIC ARCHITECTURAL &amp; COMPETITIVE RECORD // 2026</text>

    <!-- 3 Big Verified Achievement Cards from Image 2 -->
    <g transform="translate(0, 78)">
      <!-- Metric 1: Cognithon 2nd Prize -->
      <g transform="translate(0, 0)">
        <rect x="0" y="0" width="176" height="105" rx="10" fill="#0A1224" stroke="#F59E0B" stroke-width="1.4"/>
        <text x="16" y="24" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="9.5" font-weight="800" fill="#FBBF24">🏆 IIIT BHAGALPUR</text>
        <text x="16" y="62" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="28" font-weight="900" fill="#FBBF24">2nd</text>
        <text x="16" y="82" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="12" font-weight="800" fill="#F8FAFC">Cognithon Hackathon</text>
        <text x="16" y="96" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="9" fill="#94A3B8">National Contest Winner</text>
      </g>

      <!-- Metric 2: India Innovates National Finalist -->
      <g transform="translate(190, 0)">
        <rect x="0" y="0" width="176" height="105" rx="10" fill="#0A1224" stroke="#FF354F" stroke-width="1.4"/>
        <text x="16" y="24" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="9.5" font-weight="800" fill="#FF8A9A">🇮🇳 INDIA INNOVATES '26</text>
        <text x="16" y="62" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="24" font-weight="900" fill="#FF354F">FINALIST</text>
        <text x="16" y="82" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="12" font-weight="800" fill="#F8FAFC">National Finalist</text>
        <text x="16" y="96" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="9" fill="#94A3B8">Pan-India Innovation</text>
      </g>

      <!-- Metric 3: Flipkart GRiD 2026 -->
      <g transform="translate(380, 0)">
        <rect x="0" y="0" width="180" height="105" rx="10" fill="#0A1224" stroke="#247BFF" stroke-width="1.4"/>
        <text x="16" y="24" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="9.5" font-weight="800" fill="#60A5FA">⚡ FLIPKART GRiD 2026</text>
        <text x="16" y="62" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="22" font-weight="900" fill="#247BFF">SEMI-FIN</text>
        <text x="16" y="82" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="12" font-weight="800" fill="#F8FAFC">National Semi-Finalist</text>
        <text x="16" y="96" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="9" fill="#94A3B8">Engineering Flagship Track</text>
      </g>
    </g>

    <!-- Flagship Systems Summary Panel with All Key Builds -->
    <g transform="translate(0, 202)">
      <rect x="0" y="0" width="560" height="218" rx="12" fill="#080E1C" stroke="#16233B" stroke-width="1.2"/>
      <text x="20" y="24" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', sans-serif" font-size="10.5" font-weight="800" letter-spacing="1.5" fill="#38BDF8">FLAGSHIP PLATFORMS &amp; SYSTEMS ARCHITECTURE</text>

      <!-- System 1: SurakshaAI -->
      <g transform="translate(20, 38)">
        <circle cx="5" cy="7" r="4.5" fill="#247BFF"/>
        <text x="18" y="11" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13" font-weight="800" fill="#F8FAFC">Surakshaai.org — AI Geospatial Safety Analytics Engine</text>
        <text x="18" y="26" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11" fill="#94A3B8">FastAPI ML inference, Dynamic Safety Index (DSI), real-time heatmaps &amp; guardian telemetry.</text>
      </g>

      <!-- System 2: RESQ -->
      <g transform="translate(20, 78)">
        <circle cx="5" cy="7" r="4.5" fill="#FF354F"/>
        <text x="18" y="11" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13" font-weight="800" fill="#F8FAFC">RESQ — Damage-Aware Disaster Relief Routing Engine</text>
        <text x="18" y="26" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11" fill="#94A3B8">408,986 hazard surface grid cells in PostGIS with Valhalla dynamic cost-weighted routing.</text>
      </g>

      <!-- System 3: GridShare -->
      <g transform="translate(20, 118)">
        <circle cx="5" cy="7" r="4.5" fill="#10B981"/>
        <text x="18" y="11" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13" font-weight="800" fill="#F8FAFC">GridShare — Community Microgrid Energy Optimization (IIT Guwahati)</text>
        <text x="18" y="26" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11" fill="#94A3B8">Real-time solar, battery &amp; EV surplus balancing with localized P2P decentralized trade mechanism.</text>
      </g>

      <!-- System 4: MednormAI -->
      <g transform="translate(20, 158)">
        <circle cx="5" cy="7" r="4.5" fill="#A855F7"/>
        <text x="18" y="11" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13" font-weight="800" fill="#F8FAFC">MednormAI — Clinical Data Normalization Engine (IIT Patna x Jilo Health)</text>
        <text x="18" y="26" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11" fill="#94A3B8">OCR &amp; NLP pipeline converting unstructured medical PDFs and lab bills into structured health data.</text>
      </g>
    </g>
  </g>
</svg>'''

    # =========================================================================
    # 5. assets/connect.svg
    # =========================================================================
    connect_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 940 450" width="100%" height="100%">
  <defs>
    <linearGradient id="cn-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#060913"/>
      <stop offset="60%" stop-color="#0A1224"/>
      <stop offset="100%" stop-color="#060913"/>
    </linearGradient>
    <linearGradient id="cn-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247BFF" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#8B5CF6" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="#FF354F" stop-opacity="0.8"/>
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

  <!-- Left Pointing Character -->
  <g transform="translate(10, 20)">
    <ellipse cx="225" cy="225" rx="175" ry="175" fill="#247BFF" fill-opacity="0.12"/>
    <g clip-path="url(#cn-character-clip)">
      <image href="data:image/png;base64,{id_b64}" xlink:href="data:image/png;base64,{id_b64}" x="-10" y="10" width="440" height="400" preserveAspectRatio="xMidYMid meet"/>
    </g>
  </g>

  <!-- Right Headline & Social Channels -->
  <g transform="translate(435, 36)">
    <!-- Sleek Modern Subheading Font -->
    <text x="0" y="10" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', sans-serif" font-size="11" font-weight="800" letter-spacing="2" fill="#38BDF8">05 // TRANSMISSION PROTOCOL</text>
    <text x="0" y="42" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', sans-serif" font-size="34" font-weight="900" fill="#FFFFFF">LET'S BUILD SOMETHING<tspan fill="#FF354F">.</tspan></text>
    <text x="0" y="65" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13.5" fill="#94A3B8">
      Open for AI/ML architecture, geospatial engineering &amp; high-impact roles.
    </text>

    <!-- 4 Social Cards with modern layout -->
    <g transform="translate(0, 88)">
      <!-- Card 1: GitHub -->
      <g transform="translate(0, 0)">
        <rect x="0" y="0" width="460" height="52" rx="8" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
        <rect x="12" y="12" width="28" height="28" rx="6" fill="#14243F"/>
        <text x="21" y="31" font-family="sans-serif" font-size="15" fill="#FFFFFF">⌥</text>
        <text x="50" y="24" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13" font-weight="800" fill="#FFFFFF">GitHub Profile</text>
        <text x="50" y="40" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11" font-weight="600" fill="#60A5FA">github.com/xnacro • 10+ Repositories &amp; Sandboxes</text>
        <g class="nudge-arrow">
          <text x="425" y="32" font-family="-apple-system, sans-serif" font-size="16" font-weight="900" fill="#247BFF">→</text>
        </g>
      </g>

      <!-- Card 2: LinkedIn -->
      <g transform="translate(0, 62)">
        <rect x="0" y="0" width="460" height="52" rx="8" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
        <rect x="12" y="12" width="28" height="28" rx="6" fill="#0A2540"/>
        <text x="20" y="31" font-family="sans-serif" font-size="14" font-weight="900" fill="#0A66C2">in</text>
        <text x="50" y="24" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13" font-weight="800" fill="#FFFFFF">LinkedIn Network</text>
        <text x="50" y="40" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11" font-weight="600" fill="#60A5FA">linkedin.com/in/prince-tiwari-727375328</text>
        <g class="nudge-arrow">
          <text x="425" y="32" font-family="-apple-system, sans-serif" font-size="16" font-weight="900" fill="#247BFF">→</text>
        </g>
      </g>

      <!-- Card 3: Instagram -->
      <g transform="translate(0, 124)">
        <rect x="0" y="0" width="460" height="52" rx="8" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
        <rect x="12" y="12" width="28" height="28" rx="6" fill="#2A1224"/>
        <text x="20" y="31" font-family="sans-serif" font-size="14" fill="#E4405F">📸</text>
        <text x="50" y="24" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13" font-weight="800" fill="#FFFFFF">Instagram</text>
        <text x="50" y="40" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11" font-weight="600" fill="#FF7088">@am_princetiwari • Engineering &amp; Life</text>
        <g class="nudge-arrow">
          <text x="425" y="32" font-family="-apple-system, sans-serif" font-size="16" font-weight="900" fill="#FF354F">→</text>
        </g>
      </g>

      <!-- Card 4: Email -->
      <g transform="translate(0, 186)">
        <rect x="0" y="0" width="460" height="52" rx="8" fill="#0C1527" stroke="#1E2F4D" stroke-width="1"/>
        <rect x="12" y="12" width="28" height="28" rx="6" fill="#14243F"/>
        <text x="20" y="31" font-family="sans-serif" font-size="14" fill="#EA4335">✉</text>
        <text x="50" y="24" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13" font-weight="800" fill="#FFFFFF">Direct Electronic Transmission</text>
        <text x="50" y="40" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11" font-weight="600" fill="#38BDF8">businessofficialtech@gmail.com</text>
        <g class="nudge-arrow">
          <text x="425" y="32" font-family="-apple-system, sans-serif" font-size="16" font-weight="900" fill="#247BFF">→</text>
        </g>
      </g>
    </g>

    <!-- Bottom Guidance -->
    <text x="0" y="360" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', sans-serif" font-size="10" font-weight="800" letter-spacing="1.5" fill="#64748B">CLICKABLE PROTOCOLS ACTIVE IN REPOSITORY DOCUMENT BELOW</text>
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
