def get_css():
    return """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;400;600;700&family=Share+Tech+Mono&display=swap');

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    * { box-sizing: border-box; }

    .stApp {
        background: #020617;
        font-family: 'Rajdhani', sans-serif;
        perspective: 1200px;
    }

    /* ---------- Ambient holo glow ---------- */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background:
            radial-gradient(ellipse at 15% 40%, rgba(0,255,242,0.10) 0%, transparent 55%),
            radial-gradient(ellipse at 85% 15%, rgba(255,47,208,0.10) 0%, transparent 50%),
            radial-gradient(ellipse at 50% 90%, rgba(0,255,242,0.06) 0%, transparent 50%),
            #020617;
        z-index: -4;
        animation: bgPulse 7s ease-in-out infinite;
    }
    @keyframes bgPulse { 0%,100% { opacity: 0.85; } 50% { opacity: 1; } }

    /* ---------- Scanlines overlay ---------- */
    .stApp::after {
        content: '';
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background: repeating-linear-gradient(
            to bottom,
            rgba(0,255,242,0.025) 0px,
            rgba(0,255,242,0.025) 1px,
            transparent 2px,
            transparent 4px
        );
        z-index: -1;
        animation: scanDrift 9s linear infinite;
        pointer-events: none;
    }
    @keyframes scanDrift { 0% { background-position: 0 0; } 100% { background-position: 0 40px; } }

    /* ---------- 3D perspective hex-grid floor ---------- */
    .tech-grid-floor {
        position: fixed;
        bottom: 0; left: 0; width: 100%; height: 45vh;
        z-index: -2;
        pointer-events: none;
        background-image:
            linear-gradient(rgba(0,255,242,0.16) 1px, transparent 1px),
            linear-gradient(90deg, rgba(255,47,208,0.14) 1px, transparent 1px);
        background-size: 44px 44px;
        transform: perspective(500px) rotateX(72deg) translateY(40%);
        transform-origin: bottom;
        -webkit-mask-image: linear-gradient(to top, rgba(0,0,0,0.95), transparent 90%);
        mask-image: linear-gradient(to top, rgba(0,0,0,0.95), transparent 90%);
        animation: gridDrift 5s linear infinite;
    }
    @keyframes gridDrift {
        0% { background-position: 0 0, 0 0; }
        100% { background-position: 0 44px, 44px 0; }
    }

    /* ---------- AI Core: rotating hexagon reactor ---------- */
    .ai-core-wrap {
        display: flex; justify-content: center; align-items: center;
        margin: 4px auto 12px auto; height: 150px;
    }
    .ai-core {
        position: relative;
        width: 90px; height: 90px;
        background: conic-gradient(from 0deg, #00fff2, #ff2fd0, #00fff2);
        clip-path: polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%);
        box-shadow: 0 0 35px rgba(0,255,242,0.55), 0 0 70px rgba(255,47,208,0.3);
        animation: coreSpin 6s linear infinite, coreBreathe 2.6s ease-in-out infinite;
    }
    .ai-core::before {
        content: '';
        position: absolute; inset: 10px;
        background: #020617;
        clip-path: polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%);
    }
    .ai-core::after {
        content: '';
        position: absolute;
        top: 50%; left: 50%;
        width: 140px; height: 140px;
        transform: translate(-50%,-50%);
        border: 1.5px dashed rgba(0,255,242,0.35);
        border-radius: 50%;
        animation: ringSpin 8s linear infinite reverse;
    }
    @keyframes coreSpin { 0% { filter: hue-rotate(0deg); } 100% { filter: hue-rotate(360deg); } }
    @keyframes coreBreathe { 0%,100% { transform: scale(1); } 50% { transform: scale(1.08); } }
    @keyframes ringSpin { 0% { transform: translate(-50%,-50%) rotate(0deg); } 100% { transform: translate(-50%,-50%) rotate(360deg); } }

    /* ---------- Title: holographic glitch shimmer ---------- */
    .jarvis-title {
        font-family: 'Orbitron', sans-serif;
        font-weight: 900;
        font-size: 3.5rem;
        text-align: center;
        padding: 20px 0 0 0;
        letter-spacing: 3px;
        background: linear-gradient(100deg, #00fff2 20%, #ff2fd0 50%, #00fff2 80%);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: holoShift 4s linear infinite, glitchFlicker 6s ease-in-out infinite;
    }
    @keyframes holoShift { 0% { background-position: 0% 50%; } 100% { background-position: 200% 50%; } }
    @keyframes glitchFlicker {
        0%, 92%, 100% { filter: drop-shadow(0 0 18px rgba(0,255,242,0.4)); opacity: 1; }
        93% { filter: drop-shadow(2px 0 6px rgba(255,47,208,0.7)); opacity: 0.85; transform: translateX(1px); }
        94% { filter: drop-shadow(-2px 0 6px rgba(0,255,242,0.7)); opacity: 1; transform: translateX(-1px); }
        95% { transform: translateX(0); }
    }

    .jarvis-subtitle {
        text-align: center;
        color: rgba(0,255,242,0.55);
        font-family: 'Share Tech Mono', monospace;
        font-weight: 400;
        font-size: 1rem;
        letter-spacing: 8px;
        margin-top: -10px;
        margin-bottom: 30px;
        text-transform: uppercase;
    }

    /* ---------- Tabs: hex-cut holo panels ---------- */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: rgba(0,255,242,0.03);
        border-radius: 4px;
        padding: 8px;
        backdrop-filter: blur(12px);
        border: 1px solid rgba(0,255,242,0.15);
        box-shadow: 0 8px 30px rgba(0,0,0,0.4);
        margin-bottom: 30px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px; padding: 0 30px; border-radius: 2px;
        font-weight: 600; font-size: 0.95rem; letter-spacing: 3px;
        color: rgba(255,255,255,0.45);
        transition: all 0.3s ease; background: transparent; border: none;
        clip-path: polygon(6% 0, 100% 0, 94% 100%, 0 100%);
    }
    .stTabs [data-baseweb="tab"]:hover {
        color: #00fff2;
        background: rgba(0,255,242,0.06);
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, rgba(0,255,242,0.18), rgba(255,47,208,0.18)) !important;
        color: #00fff2 !important;
        box-shadow: 0 0 30px rgba(0,255,242,0.2), inset 0 0 15px rgba(0,255,242,0.1);
        border: 1px solid rgba(0,255,242,0.3);
    }

    /* ---------- Chat input ---------- */
    .stChatInput textarea,
    .stChatInput [data-testid="stChatInputTextArea"] {
        background: rgba(0,255,242,0.04) !important;
        border: 1px solid rgba(0,255,242,0.3) !important;
        border-radius: 4px !important;
        color: #e8fffe !important;
        font-family: 'Share Tech Mono', monospace !important;
        font-size: 0.95rem !important;
        padding: 12px 20px !important;
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
    }
    .stChatInput textarea:focus,
    .stChatInput [data-testid="stChatInputTextArea"]:focus {
        border-color: #00fff2 !important;
        box-shadow: 0 0 30px rgba(0,255,242,0.25) !important;
        background: rgba(0,255,242,0.07) !important;
    }
    .stChatInput textarea::placeholder { color: rgba(0,255,242,0.3); }

    /* ---------- Chat messages: corner-cut holo cards ---------- */
    .stChatMessage,
    [data-testid="stChatMessage"] {
        background: rgba(0,255,242,0.03) !important;
        border: 1px solid rgba(0,255,242,0.12) !important;
        border-radius: 6px !important;
        padding: 16px !important;
        margin: 8px 0 !important;
        backdrop-filter: blur(8px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
        clip-path: polygon(0 0, 100% 0, 100% 92%, 97% 100%, 0 100%);
        animation: msgSlide 0.45s ease;
    }
    @keyframes msgSlide { 0% { opacity: 0; transform: translateY(20px); } 100% { opacity: 1; transform: translateY(0); } }

    [data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) {
        background: linear-gradient(135deg, rgba(0,255,242,0.14), rgba(255,47,208,0.1)) !important;
        border-left: 3px solid #00fff2 !important;
    }
    [data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarAssistant"]) {
        background: rgba(255,47,208,0.04) !important;
        border-left: 3px solid #ff2fd0 !important;
    }

    /* ---------- Buttons: neon sweep ---------- */
    .stButton button {
        position: relative;
        overflow: hidden;
        background: rgba(0,255,242,0.06) !important;
        border: 1px solid rgba(0,255,242,0.35) !important;
        border-radius: 4px !important;
        color: #00fff2 !important;
        font-weight: 600 !important;
        letter-spacing: 1px;
        padding: 10px 24px !important;
        transition: all 0.25s ease !important;
        backdrop-filter: blur(10px);
    }
    .stButton button::before {
        content: '';
        position: absolute; top: 0; left: -75%;
        width: 50%; height: 100%;
        background: linear-gradient(120deg, transparent, rgba(0,255,242,0.4), transparent);
        transform: skewX(-20deg);
        transition: left 0.5s ease;
    }
    .stButton button:hover::before { left: 125%; }
    .stButton button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 40px rgba(0,255,242,0.25) !important;
        border-color: #00fff2 !important;
        color: #ffffff !important;
    }
    .stButton button:active { transform: translateY(-1px) scale(0.99); }

    /* ---------- Image placeholder ---------- */
    .image-placeholder {
        background: rgba(0,255,242,0.03);
        border: 2px dashed rgba(0,255,242,0.25);
        border-radius: 8px;
        padding: 60px 20px;
        text-align: center;
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
        min-height: 350px;
        display: flex; flex-direction: column; align-items: center; justify-content: center;
    }
    .image-placeholder:hover {
        border-color: #00fff2;
        background: rgba(0,255,242,0.05);
        box-shadow: 0 0 60px rgba(0,255,242,0.12);
        transform: translateY(-4px);
    }
    .image-placeholder .icon { font-size: 4rem; margin-bottom: 20px; opacity: 0.4; filter: drop-shadow(0 0 15px rgba(0,255,242,0.5)); }
    .image-placeholder .text { color: rgba(255,255,255,0.4); font-size: 1.1rem; font-weight: 300; letter-spacing: 2px; }
    .image-placeholder .subtext { color: rgba(0,255,242,0.35); font-size: 0.8rem; margin-top: 10px; letter-spacing: 4px; font-family: 'Share Tech Mono', monospace; }

    /* ---------- Portfolio: holo hex cards with 3D tilt ---------- */
    .portfolio-card {
        position: relative;
        background: rgba(0,255,242,0.03);
        border: 1px solid rgba(0,255,242,0.18);
        border-radius: 6px;
        padding: 30px;
        transition: transform 0.35s ease, box-shadow 0.35s ease, border-color 0.35s ease;
        backdrop-filter: blur(8px);
        text-align: center;
        height: 100%;
        transform-style: preserve-3d;
        clip-path: polygon(0 0, 100% 0, 100% 94%, 94% 100%, 0 100%);
    }
    .portfolio-card:hover {
        transform: perspective(700px) rotateX(6deg) rotateY(-6deg) translateY(-8px) translateZ(10px);
        border-color: #00fff2;
        box-shadow: 0 20px 50px rgba(0,0,0,0.5), 0 0 45px rgba(0,255,242,0.18);
        background: rgba(0,255,242,0.05);
    }
    .portfolio-card .emoji { font-size: 3rem; margin-bottom: 15px; display: block; filter: drop-shadow(0 0 12px rgba(0,255,242,0.4)); }
    .portfolio-card h3 { color: #00fff2; font-family: 'Orbitron', sans-serif; font-size: 1.05rem; letter-spacing: 2px; margin-bottom: 10px; }
    .portfolio-card p { color: rgba(255,255,255,0.5); font-size: 0.9rem; font-weight: 300; line-height: 1.6; }

    /* ---------- Status indicator ---------- */
    .status-indicator {
        display: inline-flex; align-items: center; gap: 8px;
        padding: 6px 16px; border-radius: 3px;
        background: rgba(0,255,242,0.06);
        border: 1px solid rgba(0,255,242,0.25);
        font-size: 0.78rem; color: #00fff2; letter-spacing: 2px;
        font-family: 'Share Tech Mono', monospace;
    }
    .status-indicator .dot {
        width: 8px; height: 8px; border-radius: 50%;
        background: #00fff2; box-shadow: 0 0 10px #00fff2;
        animation: dotPulse 1.4s ease-in-out infinite;
    }
    @keyframes dotPulse { 0%,100% { opacity: 1; transform: scale(1); } 50% { opacity: 0.3; transform: scale(0.7); } }

    /* ---------- Scrollbar ---------- */
    ::-webkit-scrollbar { width: 6px; height: 6px; }
    ::-webkit-scrollbar-track { background: rgba(0,255,242,0.03); border-radius: 10px; }
    ::-webkit-scrollbar-thumb { background: linear-gradient(135deg, #00fff2, #ff2fd0); border-radius: 10px; }
    ::-webkit-scrollbar-thumb:hover { background: linear-gradient(135deg, #ff2fd0, #00fff2); }

    @media (max-width: 768px) {
        .jarvis-title { font-size: 2.2rem; letter-spacing: 1px; }
        .jarvis-subtitle { font-size: 0.75rem; letter-spacing: 4px; }
        .stTabs [data-baseweb="tab"] { padding: 0 15px; font-size: 0.75rem; height: 40px; }
        .ai-core { width: 65px; height: 65px; }
        .ai-core::after { width: 100px; height: 100px; }
        .ai-core-wrap { height: 110px; }
    }
    </style>
    """