import speech_recognition as sr
import os
import pyttsx3
import webbrowser
import datetime
import openai

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Set your OpenAI API key
openai.api_key = "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"

# Initialize chatStr
chatStr = ""

def say(text):
    engine.say(text)
    engine.runAndWait()

def ai(prompt):
    try:
        text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        text += response.choices[0].text
        if not os.path.exists("Openai"):
            os.mkdir("Openai")
        with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
            f.write(text)
    except Exception as e:
        print("AI Exception:", e)

def chat(query):
    global chatStr
    try:
        chatStr += f"tony stark: {query}\n Jarvis: "
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=chatStr,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        response_text = response.choices[0].text
        say(response_text)
        chatStr += f"{response_text}\n"
        return response_text
    except Exception as e:
        print("Chat Exception:", e)
        return "I'm sorry, I encountered an issue while responding."

def takeCommand():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 0.7
            audio = r.listen(source)
            query = r.recognize_google(audio, language="en-in")
            print(f"user said: {query}")
            return query
    except Exception as e:
        print("Voice Recognition Exception:", e)
        return None

if __name__ == '__main__':
    print("Initiating.... JARVIS ")
    say("Hello, I am JARVIS AI.")

    while True:
        print("Listening...!!!")
        query = takeCommand()
        if query:
            if "open music" in query:
                musicPath = r"C:\Users\Dell\Downloads\TEYA DORA - DŽANUM.mp3"
                os.startfile(musicPath)
            elif "what is the time" in query:
                strfTime = datetime.datetime.now().strftime("%H:%M:%S")
                say(f"sir the time is {strfTime}")
            elif "using artificial intelligence" in query.lower():
                ai(prompt=query)
            elif "jarvis quit" in query.lower():
                exit()
            elif "reset chat" in query.lower():
                chatStr = ""
            else:
                print("Chatting...")
                chat(query)
