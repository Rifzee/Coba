import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

st.set_page_config(
    page_title="For Diva Ayu Fransisca 🌸",
    page_icon="💌",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit chrome
st.markdown("""
<style>
#MainMenu, footer, header { visibility: hidden; }
.stAppDeployButton { display: none; }
[data-testid="stToolbar"] { display: none; }
.block-container { padding-top: 0.5rem !important; max-width: 680px; }
.stButton > button {
    background: linear-gradient(135deg, #e8b4b8, #d4a5a5) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 2px !important;
    font-family: 'Jost', sans-serif !important;
    font-weight: 300 !important;
    font-size: 0.7rem !important;
    letter-spacing: 0.3em !important;
    text-transform: uppercase !important;
    padding: 0.85rem 2.5rem !important;
    box-shadow: 0 8px 24px rgba(180,120,120,0.25) !important;
    transition: all 0.3s ease !important;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #d4a5a5, #c48888) !important;
    box-shadow: 0 12px 32px rgba(180,120,120,0.35) !important;
    transform: translateY(-2px) !important;
}
[data-testid="stAppViewContainer"] { background: #fdf6f0 !important; }
[data-testid="stVerticalBlock"] { gap: 0 !important; }
</style>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;1,300;1,400&family=Jost:wght@200;300&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# ── Session state ─────────────────────────────────────────────────────────────
if "opened" not in st.session_state:
    st.session_state.opened = False

# ── Countdown helper ──────────────────────────────────────────────────────────
def get_countdown():
    target = datetime(2026, 3, 24, 19, 0, 0)
    now    = datetime.now()
    delta  = target - now
    if delta.total_seconds() <= 0:
        return 0, 0, 0, 0, True
    total   = int(delta.total_seconds())
    days    = delta.days
    hours   = (total % 86400) // 3600
    minutes = (total % 3600)  // 60
    seconds = total % 60
    return days, hours, minutes, seconds, False

# ─────────────────────────────────────────────────────────────────────────────
# PAGE A — ENVELOPE
# ─────────────────────────────────────────────────────────────────────────────
if not st.session_state.opened:

    envelope_html = """
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="UTF-8">
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@1,300&family=Jost:wght@200;300&display=swap" rel="stylesheet">
    <style>
      * { margin:0; padding:0; box-sizing:border-box; }
      body {
        background: #fdf6f0;
        font-family: 'Jost', sans-serif;
        height: 440px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        position: relative;
      }
      .petal {
        position: absolute;
        border-radius: 50% 0 50% 0;
        opacity: 0;
        animation: fall linear infinite;
        pointer-events: none;
      }
      @keyframes fall {
        0%   { transform: translateY(-10px) rotate(0deg);   opacity: 0; }
        10%  { opacity: 0.55; }
        90%  { opacity: 0.3; }
        100% { transform: translateY(460px) rotate(400deg); opacity: 0; }
      }
      .pre-title {
        font-weight: 300;
        font-size: 0.65rem;
        letter-spacing: 0.38em;
        color: #7a3a3a;
        text-transform: uppercase;
        margin-bottom: 2rem;
        animation: fadeUp 1s ease both;
      }
      @keyframes fadeUp {
        from { opacity:0; transform:translateY(12px); }
        to   { opacity:1; transform:translateY(0); }
      }
      .env-wrap {
        width: 240px;
        height: 175px;
        animation: floatEnv 3s ease-in-out infinite;
        filter: drop-shadow(0 14px 28px rgba(180,120,120,0.22));
        margin-bottom: 2rem;
      }
      @keyframes floatEnv {
        0%,100% { transform: translateY(0px); }
        50%     { transform: translateY(-10px); }
      }
      .tap-hint {
        font-weight: 300;
        font-size: 0.62rem;
        letter-spacing: 0.32em;
        color: #8a5a5a;
        text-transform: uppercase;
        animation: pulse 2s ease-in-out infinite;
        margin-bottom: 1.8rem;
      }
      @keyframes pulse {
        0%,100% { opacity:0.4; }
        50%     { opacity:1; }
      }
      /* CSS-only flap animation using SVG animate */
    </style>
    </head>
    <body>

    <script>
      const colors=['#e8b4b8','#d4a5a5','#f2c4ce','#c8a0a0'];
      for(let i=0;i<12;i++){
        const p=document.createElement('div');
        p.className='petal';
        p.style.left=Math.random()*100+'%';
        p.style.top='-10px';
        p.style.background=colors[i%4];
        p.style.animationDuration=(7+Math.random()*7)+'s';
        p.style.animationDelay=(Math.random()*6)+'s';
        const s=(4+Math.random()*5)+'px';
        p.style.width=s; p.style.height=s;
        document.body.appendChild(p);
      }
    </script>

    <p class="pre-title">✦ &nbsp; An Invitation for You &nbsp; ✦</p>

    <div class="env-wrap">
      <svg viewBox="0 0 280 200" xmlns="http://www.w3.org/2000/svg" width="100%" height="100%">
        <defs>
          <linearGradient id="envBody" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%"   stop-color="#f5d5d5"/>
            <stop offset="100%" stop-color="#e8b4b8"/>
          </linearGradient>
          <linearGradient id="envFlap" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%"   stop-color="#e0a8ac"/>
            <stop offset="100%" stop-color="#d49898"/>
          </linearGradient>
          <filter id="sh" x="-20%" y="-20%" width="150%" height="150%">
            <feDropShadow dx="0" dy="6" stdDeviation="8" flood-color="#c48888" flood-opacity="0.2"/>
          </filter>
        </defs>

        <!-- Body -->
        <rect x="10" y="60" width="260" height="130" rx="6" fill="url(#envBody)" filter="url(#sh)"/>

        <!-- Bottom fold lines -->
        <polygon points="10,190 140,125 270,190" fill="#dfa8a8" opacity="0.45"/>
        <line x1="10"  y1="190" x2="140" y2="125" stroke="#c8a0a0" stroke-width="0.8" opacity="0.5"/>
        <line x1="270" y1="190" x2="140" y2="125" stroke="#c8a0a0" stroke-width="0.8" opacity="0.5"/>

        <!-- Animated flap -->
        <g style="transform-origin:140px 60px">
          <animateTransform
            attributeName="transform" type="rotate"
            values="0 140 60; -32 140 60; -32 140 60; 0 140 60"
            keyTimes="0; 0.35; 0.65; 1"
            dur="3.5s" repeatCount="indefinite"/>
          <polygon points="10,60 270,60 140,150" fill="url(#envFlap)"/>
        </g>

        <!-- Wax seal -->
        <circle cx="140" cy="110" r="20" fill="#c48888" opacity="0.95"/>
        <circle cx="140" cy="110" r="14" fill="#b87878" opacity="0.95"/>
        <text x="140" y="116" text-anchor="middle" font-size="14" fill="#fdf6f0" font-family="serif">✦</text>

        <!-- Deco border -->
        <rect x="18" y="68" width="244" height="114" rx="3"
              fill="none" stroke="#d4a5a5" stroke-width="0.8"
              stroke-dasharray="4,3" opacity="0.45"/>
      </svg>
    </div>

    <p class="tap-hint">✦ &nbsp; click the button below to open &nbsp; ✦</p>

    </body>
    </html>
    """

    components.html(envelope_html, height=440, scrolling=False)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("💌  Open", key="open_btn", use_container_width=True):
            st.session_state.opened = True
            st.rerun()

# ─────────────────────────────────────────────────────────────────────────────
# PAGE B — INVITATION CARD
# ─────────────────────────────────────────────────────────────────────────────
else:
    days, hours, minutes, seconds, passed = get_countdown()

    invitation_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="UTF-8">
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;1,300;1,400&family=Jost:wght@200;300;400&display=swap" rel="stylesheet">
    <style>
      * {{ margin:0; padding:0; box-sizing:border-box; }}
      body {{
        background: #fdf6f0;
        font-family: 'Jost', sans-serif;
        padding: 1rem 0.5rem 1.5rem;
        position: relative;
        overflow-x: hidden;
      }}
      .petal {{
        position: fixed;
        border-radius: 50% 0 50% 0;
        opacity: 0;
        animation: fall linear infinite;
        pointer-events: none;
        z-index: 0;
      }}
      @keyframes fall {{
        0%   {{ transform:translateY(-20px) rotate(0deg); opacity:0; }}
        10%  {{ opacity:0.5; }}
        90%  {{ opacity:0.3; }}
        100% {{ transform:translateY(110vh) rotate(400deg); opacity:0; }}
      }}

      .card {{
        background: linear-gradient(160deg, #fff9f7 0%, #fff0ed 100%);
        border: 1px solid #f0d0cc;
        border-radius: 5px;
        padding: 2.2rem 1.8rem 2rem;
        position: relative;
        z-index: 1;
        box-shadow: 0 2px 8px rgba(180,120,120,0.08), 0 20px 60px rgba(180,120,120,0.13);
        animation: revealCard 1s cubic-bezier(0.22,1,0.36,1) both;
      }}
      @keyframes revealCard {{
        from {{ opacity:0; transform:translateY(36px) scale(0.97); }}
        to   {{ opacity:1; transform:translateY(0)    scale(1); }}
      }}
      .card::before {{
        content:'';
        position:absolute;
        top:0; left:0; right:0; height:3px;
        background: linear-gradient(90deg,#e8b4b8,#d4a5a5,#c48888,#d4a5a5,#e8b4b8);
        border-radius:5px 5px 0 0;
      }}

      .ornament {{
        text-align:center;
        font-weight:300;
        font-size:0.58rem;
        letter-spacing:0.7em;
        color:#8a5050;
        text-transform:uppercase;
        margin-bottom:1.6rem;
      }}
      .card-label {{
        text-align:center;
        font-weight:300;
        font-size:0.6rem;
        letter-spacing:0.38em;
        text-transform:uppercase;
        color:#6a3535;
        margin-bottom:0.45rem;
      }}
      .card-name {{
        text-align:center;
        font-family:'Cormorant Garamond',serif;
        font-style:italic;
        font-weight:400;
        font-size:2.5rem;
        color:#4a1a1a;
        line-height:1.2;
        margin-bottom:1.8rem;
      }}

      .divider {{ display:flex; align-items:center; gap:0.7rem; margin:1rem 0; }}
      .div-line {{ flex:1; height:1px; background:linear-gradient(90deg,transparent,#e8b4b8,transparent); }}
      .div-icon {{ color:#e8b4b8; font-size:0.52rem; letter-spacing:0.3em; }}

      .info-grid {{ display:grid; grid-template-columns:1fr 1fr; gap:0.8rem; margin:1.3rem 0; }}
      .info-block {{
        text-align:center;
        padding:1rem 0.7rem;
        background:rgba(255,255,255,0.65);
        border:1px solid rgba(232,180,184,0.3);
        border-radius:3px;
      }}
      .info-block.full {{ grid-column:1/-1; }}
      .info-icon {{ font-size:1rem; display:block; margin-bottom:0.3rem; }}
      .info-label {{
        font-weight:300; font-size:0.56rem;
        letter-spacing:0.35em; text-transform:uppercase;
        color:#6a3535; display:block; margin-bottom:0.2rem;
      }}
      .info-value {{
        font-family:'Cormorant Garamond',serif;
        font-weight:500; font-size:1.05rem; color:#3a1010;
        display:block; line-height:1.3;
      }}

      .countdown-section {{ margin-top:1.8rem; text-align:center; }}
      .live-badge {{
        display:inline-flex; align-items:center; gap:0.4rem;
        background:rgba(232,180,184,0.18);
        border:1px solid rgba(180,100,100,0.4);
        border-radius:20px; padding:0.28rem 0.85rem;
        font-size:0.55rem; letter-spacing:0.28em;
        text-transform:uppercase; color:#6a3535; margin-bottom:0.7rem;
        font-weight:300;
      }}
      .live-dot {{
        width:6px; height:6px; border-radius:50%;
        background:#c46060;
        animation:livePulse 1.4s ease-in-out infinite;
      }}
      @keyframes livePulse {{
        0%,100% {{ opacity:1; transform:scale(1); }}
        50%     {{ opacity:0.35; transform:scale(0.75); }}
      }}
      .countdown-title {{
        font-weight:300; font-size:0.6rem;
        letter-spacing:0.38em; text-transform:uppercase;
        color:#6a3535; margin-bottom:0.9rem;
      }}
      .cd-grid {{ display:flex; justify-content:center; gap:0.6rem; flex-wrap:wrap; }}
      .cd-block {{
        background:linear-gradient(160deg,#f2dada,#e8c8c8);
        border:1px solid #d4a0a0; border-radius:3px;
        padding:0.8rem 0.9rem; min-width:64px;
        box-shadow:0 4px 14px rgba(160,80,80,0.15);
        transition:transform 0.2s ease;
      }}
      .cd-block:hover {{ transform:translateY(-2px); }}
      .cd-num {{
        font-family:'Cormorant Garamond',serif;
        font-weight:400; font-size:1.9rem; color:#3a1010;
        display:block; line-height:1;
      }}
      .cd-unit {{
        font-weight:300; font-size:0.5rem;
        letter-spacing:0.28em; text-transform:uppercase;
        color:#6a3535; display:block; margin-top:0.22rem;
      }}

      .closing {{
        text-align:center;
        margin-top:1.8rem;
        padding-top:1.6rem;
        border-top:1px solid rgba(180,100,100,0.3);
      }}
      .closing-text {{
        font-family:'Cormorant Garamond',serif;
        font-style:italic; font-weight:400;
        font-size:1rem; color:#4a2020; line-height:1.9;
      }}
      .closing-sig {{
        margin-top:0.7rem; font-weight:300;
        font-size:0.58rem; letter-spacing:0.35em;
        color:#7a4040; text-transform:uppercase;
      }}
    </style>
    </head>
    <body>

    <script>
      // Petals
      const cols=['#e8b4b8','#d4a5a5','#f2c4ce','#c8a0a0'];
      for(let i=0;i<10;i++){{
        const p=document.createElement('div');
        p.className='petal';
        p.style.left=Math.random()*100+'vw';
        p.style.background=cols[i%4];
        p.style.animationDuration=(7+Math.random()*8)+'s';
        p.style.animationDelay=(Math.random()*6)+'s';
        const s=(4+Math.random()*5)+'px';
        p.style.width=s; p.style.height=s;
        document.body.appendChild(p);
      }}

      // Live countdown via JS (no Streamlit rerun needed)
      function pad(n){{ return String(n).padStart(2,'0'); }}
      function tick(){{
        const target=new Date('2026-03-24T19:00:00');
        const diff=target-new Date();
        if(diff<=0){{
          ['cd-days','cd-hours','cd-minutes','cd-seconds'].forEach(id=>{{
            document.getElementById(id).textContent='00';
          }});
          return;
        }}
        const t=Math.floor(diff/1000);
        document.getElementById('cd-days').textContent    = pad(Math.floor(t/86400));
        document.getElementById('cd-hours').textContent   = pad(Math.floor((t%86400)/3600));
        document.getElementById('cd-minutes').textContent = pad(Math.floor((t%3600)/60));
        document.getElementById('cd-seconds').textContent = pad(t%60);
      }}
      tick();
      setInterval(tick, 1000);
    </script>

    <div class="card">

      <p class="ornament">✦ &nbsp;&nbsp; First Meet Invitation &nbsp;&nbsp; ✦</p>

      <p class="card-label">you are sincerely invited</p>
      <h1 class="card-name">Diva Ayu Fransisca</h1>

      <div class="divider">
        <div class="div-line"></div>
        <span class="div-icon">✦ ✦ ✦</span>
        <div class="div-line"></div>
      </div>

      <div class="info-grid">
        <div class="info-block">
          <span class="info-icon">🗓️</span>
          <span class="info-label">Date</span>
          <span class="info-value">24 March 2026</span>
        </div>
        <div class="info-block">
          <span class="info-icon">🕖</span>
          <span class="info-label">Time</span>
          <span class="info-value">19.00 WIB</span>
        </div>
        <div class="info-block full">
          <span class="info-icon">🌹</span>
          <span class="info-label">Location</span>
          <span class="info-value">House of Byuss</span>
        </div>
      </div>

      <div class="divider">
        <div class="div-line"></div>
        <span class="div-icon">✦</span>
        <div class="div-line"></div>
      </div>

      <div class="countdown-section">
        <div class="live-badge">
          <div class="live-dot"></div>
          Live Countdown
        </div>
        
        <div class="cd-grid">
          <div class="cd-block">
            <span class="cd-num" id="cd-days">{days:02d}</span>
            <span class="cd-unit">Hari</span>
          </div>
          <div class="cd-block">
            <span class="cd-num" id="cd-hours">{hours:02d}</span>
            <span class="cd-unit">Jam</span>
          </div>
          <div class="cd-block">
            <span class="cd-num" id="cd-minutes">{minutes:02d}</span>
            <span class="cd-unit">Menit</span>
          </div>
          <div class="cd-block">
            <span class="cd-num" id="cd-seconds">{seconds:02d}</span>
            <span class="cd-unit">Detik</span>
          </div>
        </div>
      </div>

      <div class="closing">
        <p class="closing-text">
          "Just a random chit chat with a glass of coffee<br>
          and maybe some cakes...."
        </p>
        <p class="closing-sig">✦ &nbsp; with sincerity &nbsp; ✦</p>
      </div>

    </div>
    </body>
    </html>
    """

    components.html(invitation_html, height=800, scrolling=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("↩  Back", key="back_btn", use_container_width=True):
            st.session_state.opened = False
            st.rerun()

    st.markdown("""
    <style>
    div[data-testid="stButton"] button {
        background: transparent !important;
        color: #b8908a !important;
        border: 1px solid #e8b4b8 !important;
        box-shadow: none !important;
    }
    div[data-testid="stButton"] button:hover {
        background: rgba(232,180,184,0.1) !important;
        border-color: #d4a5a5 !important;
        transform: none !important;
    }
    </style>
    """, unsafe_allow_html=True)