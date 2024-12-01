# **JARVIS AI Assistant** 🤖

**JARVIS AI** is a powerful virtual assistant built using Python, integrating state-of-the-art technologies to offer seamless, real-time interactions. With its integration of OpenAI's ChatGPT API, speech recognition, and text-to-speech capabilities, JARVIS enables conversational AI, web browsing, time-based queries, and media control.

---

## **Features** ✨

1. **Conversational AI**  
   - Powered by OpenAI's ChatGPT for intelligent, context-aware conversations.  
   - Provides accurate and meaningful responses to user queries.  

2. **Speech Recognition**  
   - Uses Python's `speech_recognition` library for converting speech to text.  
   - Allows hands-free, real-time interaction.  

3. **Text-to-Speech (TTS)**  
   - Converts JARVIS's textual responses to speech for an immersive experience.  
   - Supports multiple voices and languages (customizable).  

4. **Web Browsing** 🌐  
   - Automatically opens and navigates to websites based on user commands.  
   - Example: "Open YouTube," "Search for Python tutorials."  

5. **Time Queries** ⏰  
   - Responds to time-based commands like "What time is it?" or "Set a reminder."  

6. **Media Control** 🎵  
   - Control playback of media such as music or videos.  
   - Example: "Play my favorite playlist," "Pause the music."  

7. **Custom API Integration**  
   - Uses OpenAI's GPT API for scalable and efficient conversational AI.

8. **Extensibility**  
   - Modular design for easy addition of new features and commands.  
   - Example: Add integrations for smart home devices or additional APIs.

---

## **Tech Stack** 🛠️

- **Programming Language**: Python  
- **APIs**: OpenAI's GPT (ChatGPT API)  
- **Libraries Used**:
  - `speech_recognition`: For speech input.
  - `pyttsx3`: For text-to-speech output.
  - `openai`: To access the ChatGPT API.
  - `webbrowser`: To facilitate web browsing.
  - `datetime`: For handling time-related queries.
  - `os`: To interact with the operating system (e.g., opening files or media).

---

## **Installation Guide** 🚀

Follow these steps to set up and run the JARVIS AI Assistant on your system:

### **Follow these steps**  
```bash
git clone https://github.com/your-username/jarvis-ai.git
cd jarvis-ai

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt

OPENAI_API_KEY=your-api-key-here

python jarvis.py

