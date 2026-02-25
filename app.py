import streamlit as st
from io import BytesIO
import soundfile as sf

# Placeholder functions for translation
def translate_audio(input_audio, target_language):
    translated_audio_bytes = b"..."  # Replace with model output
    return translated_audio_bytes

def translate_video(input_video, target_language):
    translated_video_bytes = b"..."  # Replace with model output
    return translated_video_bytes

# Streamlit app with full-width UI
def main():
    st.set_page_config(page_title="Bi-lingual Translator", layout="wide")
    apply_custom_css()

    st.title("🌐 Bi-lingual Audio/Video Translator")
    st.markdown("""
        <p style="font-size: 1.1rem; color: #34495e; margin-top: -10px;">
            Translate your audio or video files effortlessly. Just upload your file, select a language, and get the translated output instantly.
        </p>
    """, unsafe_allow_html=True)
    
    # File upload option
    file_type = st.radio("Choose file type:", ('Audio', 'Video'))

    if file_type == 'Audio':
        uploaded_file = st.file_uploader("Upload an audio file:", type=["wav", "mp3", "m4a"])
    else:
        uploaded_file = st.file_uploader("Upload a video file:", type=["mp4", "mov", "avi"])

    # Language options
    st.write("Choose translation direction:")
    translation_option = st.selectbox("Translation direction:", ["Hindi to English", "English to Hindi"])

    source_language, target_language = ("Hindi", "English") if translation_option == "Hindi to English" else ("English", "Hindi")

    if uploaded_file is not None:
        # Display uploaded media
        if file_type == 'Audio':
            st.audio(uploaded_file, format="audio/wav")
        else:
            st.video(uploaded_file)

        if st.button("Translate"):
            # Translation logic
            if file_type == 'Audio':
                translated_audio_bytes = translate_audio(uploaded_file, target_language)
                st.write("### Translated Audio:")
                st.audio(BytesIO(translated_audio_bytes), format="audio/wav")
                st.download_button("Download Translated Audio", data=translated_audio_bytes, file_name="translated_audio.wav")

            else:
                translated_video_bytes = translate_video(uploaded_file, target_language)
                st.write("### Translated Video:")
                st.video(BytesIO(translated_video_bytes))
                st.download_button("Download Translated Video", data=translated_video_bytes, file_name="translated_video.mp4")

def apply_custom_css():
    st.markdown("""
        <style>
            /* Remove padding and margins for full-width experience */
            .css-18e3th9, .css-1v3fvcr {
                padding: 0 !important;
                margin: 0 !important;
                width: 100% !important;
            }
            
            /* Main title styling */
            h1 {
                color: #1a535c;
                font-family: 'Segoe UI', Tahoma, sans-serif;
                font-size: 2.75rem;
                font-weight: bold;
                margin-bottom: 15px;
                text-align: center;
            }

            /* Subtitle and instructional text */
            p {
                color: #34495e;
                font-family: 'Segoe UI', sans-serif;
                line-height: 1.5;
                text-align: center;
                margin-bottom: 1rem;
            }

            /* Radio buttons styling */
            .stRadio label, .stSelectbox label {
                font-family: 'Segoe UI', sans-serif;
                color: #2d4b7a;
                font-size: 1.05rem;
                margin: 0 0 1rem;
            }

            /* File uploader styling */
            .stFileUploader {
                background-color: #e0f7fa;
                padding: 15px;
                border: 2px solid #34b7c6;
                border-radius: 8px;
                margin-top: 10px;
                margin-bottom: 1.5rem;
                box-shadow: inset 0 0 5px rgba(52, 183, 198, 0.3);
            }

            /* Button styling */
            .stButton button {
                background-color: #ff8c42;
                color: white;
                padding: 12px 24px;
                border-radius: 6px;
                font-weight: bold;
                font-size: 1rem;
                font-family: 'Segoe UI', sans-serif;
                box-shadow: 0px 5px 15px rgba(255, 140, 66, 0.4);
                transition: all 0.3s ease;
                margin-top: 1.5rem;
            }
            .stButton button:hover {
                background-color: #e07a35;
                box-shadow: 0px 5px 20px rgba(255, 120, 66, 0.5);
            }

            /* Styling for audio and video player containers */
            .element-container {
                padding: 10px;
                border-radius: 8px;
                background-color: #eef2f7;
            }

            /* Styling for download buttons */
            .stDownloadButton button {
                background-color: #36a9e0;
                color: white;
                padding: 10px 20px;
                font-weight: bold;
                font-family: 'Segoe UI', sans-serif;
                border-radius: 6px;
                box-shadow: 0px 4px 10px rgba(54, 169, 224, 0.4);
                margin-top: 1rem;
            }
            .stDownloadButton button:hover {
                background-color: #2980b9;
                box-shadow: 0px 5px 15px rgba(41, 128, 185, 0.5);
            }
        </style>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
