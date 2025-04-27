import streamlit as st
import requests
import sounddevice as sd
import scipy.io.wavfile as wavfile
import tempfile
import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# 🔥 Your Groq API Key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# 🛡️ Setup Groq Client
client = Groq(api_key=GROQ_API_KEY)

# 🎤 Record Audio Function
def record_audio(duration=5, fs=16000):
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    temp_wav = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    wavfile.write(temp_wav.name, fs, recording)
    return temp_wav.name

# 📝 Transcription with Groq Whisper
def transcribe_with_groq(audio_path):
    with open(audio_path, "rb") as audio_file:
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}"
        }
        response = requests.post(
            'https://api.groq.com/openai/v1/audio/transcriptions',
            headers=headers,
            files={"file": audio_file},
            data={"model": "whisper-large-v3-turbo"}
        )
    if response.status_code == 200:
        return response.json().get("text", "Transcription failed")
    else:
        return f"Error during transcription: {response.text}"

# 🧠 Llama-3.3-70B Processing
def process_with_llama(input_text):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that analyzes text. Provide a brief analysis of the user's message."},
                {"role": "user", "content": f"Analyze this text: {input_text}"}
            ],
            temperature=0.7,
            max_tokens=150,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error processing with Llama: {str(e)}"

# 💬 Sentiment Analysis with Groq
def sentiment_analysis_groq(text):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a sentiment analysis expert. Analyze the user's message and only reply with one of these words: Positive, Negative, or Neutral. Do not include any other text."},
                {"role": "user", "content": f"Analyze this message: {text}"}
            ],
            temperature=0.2,
            max_tokens=20,
        )
        sentiment = response.choices[0].message.content.strip()
        return sentiment
    except Exception as e:
        return f"Error analyzing sentiment: {str(e)}"

# 🚀 Streamlit App Layout
st.title("🎙️ Voice Sentiment Analyzer")

# --- RECORD SECTION ---
st.header("🎤 Record Your Voice")

record_col1, record_col2 = st.columns([1, 3])

with record_col1:
    record_button = st.button("🔴 Start Recording (5 sec)")

with record_col2:
    st.write("Click to record 5 seconds of audio using your microphone.")

if record_button:
    st.info("Recording audio...")
    audio_path = record_audio()
    st.success("Recording complete!")

    # Transcription with Groq Whisper
    st.info("Transcribing your voice...")
    transcription = transcribe_with_groq(audio_path)

    if transcription:
        st.subheader("📝 Transcribed Text:")
        st.success(transcription)

        # Processing Transcription with Llama Model
        st.info("Processing with Llama Model...")
        llama_output = process_with_llama(transcription)
        st.subheader("💬 Llama Model Output:")
        st.success(llama_output)

        # Sentiment Analysis with Groq
        st.info("Analyzing Sentiment...")
        sentiment = sentiment_analysis_groq(llama_output)
        
        st.subheader("💬 Sentiment:")
        st.success(sentiment)

# --- UPLOAD SECTION ---
st.header("📂 Upload Your Audio File")

upload_col1, upload_col2 = st.columns([1, 3])

with upload_col1:
    uploaded_file = st.file_uploader("Upload a WAV file", type=["wav"])

with upload_col2:
    st.write("Upload your pre-recorded WAV audio file here.")

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio_file:
        temp_audio_file.write(uploaded_file.read())
        temp_audio_path = temp_audio_file.name

    st.success("Audio file uploaded successfully!")

    # Transcription with Groq Whisper
    st.info("Transcribing uploaded audio...")
    transcription = transcribe_with_groq(temp_audio_path)

    if transcription:
        st.subheader("📝 Transcribed Text:")
        st.success(transcription)

        # Processing Transcription with Llama Model
        st.info("Processing with Llama Model...")
        llama_output = process_with_llama(transcription)
        st.subheader("💬 Llama Model Output:")
        st.success(llama_output)

        # Sentiment Analysis with Groq
        st.info("Analyzing Sentiment...")
        sentiment = sentiment_analysis_groq(llama_output)
        
        st.subheader("💬 Sentiment:")
        st.success(sentiment)

