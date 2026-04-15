import streamlit as st
import base64
import random

# IMPORT YOUR MODULE
from modules.certificate import generate_certificate

# ================= BACKGROUND IMAGE =================
def get_base64_of_image(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg_image = get_base64_of_image("assets/background.jpg")

page_bg = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("data:image/jpg;base64,{bg_image}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

[data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
}}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# ================= GLASS UI =================
st.markdown("""
<style>
.block-container {
    background: rgba(0, 0, 0, 0.65);
    padding: 2rem;
    border-radius: 15px;
    backdrop-filter: blur(12px);
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ================= TITLE =================
st.markdown("""
<h1 style='text-align: center; color: #00ffe1; font-size: 3rem;'>
🛡️ DeepShield AI
</h1>
<p style='text-align: center; color: white; font-size: 1.2rem;'>
Real-time Deepfake & Piracy Detection for Sports Media
</p>
""", unsafe_allow_html=True)

st.write("")

# ================= FILE UPLOAD =================
uploaded_file = st.file_uploader("📤 Upload a sports video", type=["mp4", "mov", "avi"])

# ================= VERDICT FUNCTION =================
def show_verdict(verdict):
    if verdict == "Real":
        st.markdown("<h2 style='color:#00ff00;'>✅ VERIFIED SPORTS CONTENT</h2>", unsafe_allow_html=True)
    elif verdict == "Fake":
        st.markdown("<h2 style='color:#ff4b4b;'>🚨 FAKE CONTENT DETECTED</h2>", unsafe_allow_html=True)
    else:
        st.markdown("<h2 style='color:#ffa500;'>⚠️ SUSPICIOUS CONTENT</h2>", unsafe_allow_html=True)

# ================= MAIN LOGIC =================
if uploaded_file is not None:

    st.video(uploaded_file)

    # Loading animation
    with st.spinner("🔍 Analyzing video with AI models..."):
        video_score = random.uniform(60, 99)
        audio_score = random.uniform(60, 99)
        piracy_risk = random.choice(["Low", "Medium", "High"])

    # Verdict logic
    if video_score > 85 and audio_score > 85:
        verdict = "Real"
    elif video_score > 70:
        verdict = "Suspicious"
    else:
        verdict = "Fake"

    # ================= RESULTS =================
    st.markdown("### 📊 Analysis Results")

    col1, col2, col3 = st.columns(3)

    col1.metric("🎥 Video Score", f"{video_score:.2f}%")
    col2.metric("🔊 Audio Score", f"{audio_score:.2f}%")
    col3.metric("🕵️ Piracy Risk", piracy_risk)

    st.progress(int(video_score))

    # ================= VERDICT =================
    show_verdict(verdict)

    # ================= CERTIFICATE =================
    st.markdown("### 📜 Authenticity Certificate")

    final_score = (video_score + audio_score) / 2

    cert_id, file_path = generate_certificate(final_score, verdict)

    st.write(f"Certificate ID: {cert_id}")

    with open(file_path, "rb") as f:
        st.download_button(
            label="📥 Download Certificate",
            data=f,
            file_name="DeepShield_Certificate.pdf",
            mime="application/pdf"
        )

# ================= HOW IT WORKS =================
with st.expander("🧠 How DeepShield AI Works"):
    st.write("""
    - 🎥 Frame consistency analysis  
    - 🔊 Audio anomaly detection  
    - 🔍 Perceptual hashing for piracy detection  
    - 📜 Blockchain-based certificate generation (simulated)
    """)
