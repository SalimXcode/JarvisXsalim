import streamlit as st
import time
from datetime import datetime
from style import get_css
from config import APP_NAME, VERSION
from utils import get_timestamp, simulate_typing
from agent import stream_agent_reply, reset_memory
from image_gen import generate_image, AVAILABLE_MODELS

st.set_page_config(page_title=APP_NAME, page_icon="🤖", layout="wide", initial_sidebar_state="collapsed")
st.markdown(get_css(), unsafe_allow_html=True)

# 3D grid
st.markdown('<div class="tech-grid-floor"></div>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown(
        '<div style="font-family:Orbitron;color:#00d4ff;letter-spacing:2px;padding:10px 0;'
        'border-bottom:1px solid rgba(0,212,255,0.1);">⚙️ CONTROLS</div>',
        unsafe_allow_html=True,
    )
    st.markdown("---")
    if st.button("🗑️ CLEAR CHAT", use_container_width=True):
        st.session_state.messages = [{"role": "assistant", "content": "🟢 Chat cleared. Ready."}]
        reset_memory()
        st.rerun()
    st.caption(f"🟢 Online • {get_timestamp()}")
    st.caption(f"⚡ {VERSION}")

# Hero
hero_col1, hero_col2, hero_col3 = st.columns([1, 2, 1])
with hero_col2:
    st.markdown('<div class="ai-core-wrap"><div class="ai-core"></div></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="jarvis-title">{APP_NAME}</div>', unsafe_allow_html=True)
    st.markdown('<div class="jarvis-subtitle">⚡ YOUR PERSONAL AI ASSISTANT ⚡</div>', unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align:center;margin-bottom:30px;">'
        '<span class="status-indicator"><span class="dot"></span> SYSTEM ACTIVE</span></div>',
        unsafe_allow_html=True,
    )

tab1, tab2, tab3 = st.tabs(["🤖 CHAT", "🎨 IMAGE GEN", "📁 PORTFOLIO"])

# ===== TAB 1: CHAT =====
with tab1:
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "🟢 JARVISXsalim online. How can I assist you, sir?"}
        ]

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Type your command..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            placeholder = st.empty()
            with st.spinner("⚡ Thinking..."):
                response = stream_agent_reply(prompt, placeholder)
        st.session_state.messages.append({"role": "assistant", "content": response})

# ===== TAB 2: IMAGE GEN =====
with tab2:
    st.markdown(
        '<h3 style="color:#00d4ff;font-family:Orbitron;letter-spacing:2px;">🎨 AI Image Generator</h3>'
        '<p style="color:rgba(255,255,255,0.4);">Describe your vision</p>',
        unsafe_allow_html=True,
    )
    gen_col1, gen_col2 = st.columns([3, 1])
    with gen_col1:
        img_prompt = st.text_input("", placeholder="e.g., Futuristic neon city", label_visibility="collapsed")
    with gen_col2:
        gen_btn = st.button("🚀 GENERATE", use_container_width=True)

    with st.expander("⚙️ Options"):
        opt_col1, opt_col2, opt_col3 = st.columns(3)
        with opt_col1:
            img_model = st.selectbox("Model", AVAILABLE_MODELS, index=0)
        with opt_col2:
            img_width = st.selectbox("Width", [512, 768, 1024, 1280], index=2)
        with opt_col3:
            img_height = st.selectbox("Height", [512, 768, 1024, 1280], index=2)

    if gen_btn and img_prompt:
        with st.spinner("🔄 Generating your image..."):
            try:
                image_bytes = generate_image(
                    img_prompt, width=img_width, height=img_height, model=img_model
                )
                st.image(image_bytes, caption=img_prompt, use_container_width=True)
                st.download_button(
                    "⬇️ Download",
                    data=image_bytes,
                    file_name="jarvisxsalim_image.jpg",
                    mime="image/jpeg",
                    use_container_width=True,
                )
            except Exception as e:
                st.markdown(
                    f'<div class="image-placeholder"><div class="icon">⚠️</div>'
                    f'<div class="text">Generation failed</div>'
                    f'<div class="subtext">{e}</div></div>',
                    unsafe_allow_html=True,
                )
    else:
        st.markdown(
            '<div class="image-placeholder"><div class="icon">🎨</div>'
            '<div class="text">Describe your image above</div>'
            '<div class="subtext">AI POWERED • FREE • POLLINATIONS</div></div>',
            unsafe_allow_html=True,
        )

# ===== TAB 3: PORTFOLIO =====
with tab3:
    st.markdown(
        '<h3 style="color:#00d4ff;font-family:Orbitron;letter-spacing:2px;">📁 Portfolio</h3>'
        '<p style="color:rgba(255,255,255,0.4);">Your projects showcase</p>',
        unsafe_allow_html=True,
    )
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            '<div class="portfolio-card"><span class="emoji">🤖</span>'
            '<h3>JARVISXsalim</h3><p>AI-powered personal assistant with agentic AI.</p></div>',
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            '<div class="portfolio-card"><span class="emoji">🧠</span>'
            '<h3>Agentic AI</h3><p>Custom automation and tool calling system.</p></div>',
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            '<div class="portfolio-card"><span class="emoji">🚀</span>'
            '<h3>Coming Soon</h3><p>More AI tools and integrations.</p></div>',
            unsafe_allow_html=True,
        )

# ===== FOOTER =====
st.markdown(
    f'<div style="position:fixed;bottom:0;left:0;right:0;text-align:center;padding:10px;'
    f'background:rgba(5,5,15,0.85);backdrop-filter:blur(10px);'
    f'border-top:1px solid rgba(0,212,255,0.08);z-index:10;">'
    f'<span style="color:rgba(255,255,255,0.15);font-size:0.7rem;letter-spacing:4px;">'
    f'{APP_NAME} • BUILT WITH ❤️ • AGENTIC AI</span></div>',
    unsafe_allow_html=True,
)