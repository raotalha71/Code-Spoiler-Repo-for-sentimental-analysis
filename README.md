# Code Spoiler Repo for sentimental analysis

Voice Sentiment Analyzer
Problem Statement
With the growing importance of voice interactions, there's a need for applications that can analyze spoken content to determine sentiment. This helps businesses understand customer feedback, assists in mental health monitoring, and improves voice assistant interactions.

Features
Voice Recording: Records user's voice for 5 seconds
Audio Upload: Supports pre-recorded WAV file uploads
Voice Transcription: Converts speech to text using advanced AI models
Sentiment Analysis: Analyzes text and classifies sentiment as Positive, Negative, or Neutral
User-friendly Interface: Clean, intuitive Streamlit interface for easy interaction
Tech Stack
Frontend: Streamlit (Python web app framework)
Audio Processing:
sounddevice (for recording audio)
scipy.io.wavfile (for wav file handling)
API Integration:
Groq API for AI processing
LLaMA-3.3-70B model for sentiment analysis
Whisper Large V3 Turbo for speech-to-text
Environment Management: python-dotenv for secure API key handling
Solution
How it Works
Recording/Uploading: Users can either record a 5-second audio clip or upload a pre-recorded WAV file
Transcription: The audio is sent to Groq's Whisper Large V3 Turbo model for accurate speech-to-text conversion
Text Processing: The transcribed text is optionally processed (currently a placeholder)
Sentiment Analysis: The LLaMA-3.3-70B model analyzes the text and classifies sentiment
Result Display: The application displays the transcribed text and sentiment classification
Setup and Installation
Clone the repository:
git clone [https://github.com/raotalha71/Code-Spoiler-Repo-for-sentimental-analysis.git
cd voice-sentiment-analyzer
Install the required packages:
pip install streamlit requests sounddevice scipy python-dotenv groq
Create a .env file in the project root with your Groq API key:
GROQ_API_KEY=your_groq_api_key_here
Run the application:
streamlit run app.py
Future Enhancements
Support for longer recordings
Multiple language support
More detailed sentiment analysis (intensity scores)
User history tracking
Export of results to CSV/PDF
Usage Notes
Ensure your microphone is properly connected for the recording feature
For best results, speak clearly and in a quiet environment
WAV file uploads should be clear audio recordings for accurate transcription
Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

License
This project is licensed under the MIT License - see the LICENSE file for details.
