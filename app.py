import streamlit as st
from modules.video_analysis import analyze_video
from modules.audio_analysis import analyze_audio
from modules.piracy_check import check_piracy
from modules.certificate import generate_certificate

st.set_page_config(page_title="DeepShield AI", layout="wide")

st.title("🛡️ DeepShield AI")
st.subheader("Verify Sports Video Authenticity")

uploaded_file = st.file_uploader("Upload Sports Video", type=["mp4", "mov"])

if uploaded_file:
    st.video(uploaded_file)

    st.write("🔍 Running analysis...")

    video_score = analyze_video(uploaded_file)
    audio_score = analyze_audio(uploaded_file)
    piracy_score = check_piracy(uploaded_file)

    final_score = (video_score + audio_score + (100 - piracy_score)) / 3

    if final_score > 75:
        verdict = "✅ REAL"
    elif final_score > 50:
        verdict = "⚠️ SUSPICIOUS"
    else:
        verdict = "❌ FAKE"

    cert_id = generate_certificate(final_score, verdict)

    st.success("Analysis Complete!")

    col1, col2, col3 = st.columns(3)

    col1.metric("Video Score", f"{video_score:.2f}%")
    col2.metric("Audio Score", f"{audio_score:.2f}%")
    col3.metric("Piracy Risk", f"{piracy_score:.2f}%")

    st.subheader("Final Verdict")
    st.write(verdict)

    st.subheader("Certificate ID")
    st.code(cert_id)
