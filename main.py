import speech_recognition as sr
import os
import pyttsx3
import webbrowser
import datetime
import openai

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Set your OpenAI API key
openai.api_key = "YOUR API KEY"

def say(text):
    engine.say(text)
    engine.runAndWait()

def ai(prompt):
    # openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.6,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    #  print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)

chatStr=""
def chat(query):
    global chatStr
    print(chatStr)
    # openai.api_key = apikey
    chatStr += f"Aayush Sir: {query}\n Jarvis: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"user said: {query}")
            return query
        except Exception as e:
            print("Some Error Occurred:", e)
            return None


if __name__ == '__main__':
    print("Initiating.... JARVIS ")
    say("Hello, I am JARVIS AI.")

    while True:
        print("Listening...!!!")
        query = takeCommand()
        if query:
            sites = [["youtube", "https://www.youtube.com"], ["google", "https://www.google.com"],
                     ["wikipedia", "https://www.wikipedia.org"]]
            for site in sites:
                if f"open {site[0]}".lower() in query.lower():
                    say(f"Opening {site[0]} Sir")
                    webbrowser.open(site[1])

            if "open music" in query:
                musicPath = r"C:\Users\Dell\Downloads\TEYA DORA - DŽANUM (JUZNI VETAR- NA GRANICI - OFFICIAL SOUNDTRACK).mp3"
                os.startfile(musicPath)

            elif "what is the time" in query:
                strfTime = datetime.datetime.now().strftime("%H:%M:%S")
                say(f"sir the time is {strfTime}")



            elif "Using artificial intelligence".lower() in query.lower():
                ai(prompt=query)

            elif "Jarvis Quit".lower() in query.lower():
                exit()

            elif "reset chat".lower() in query.lower():
                chatStr = ""

            else:
                print("Chatting...")
                chat(query)
