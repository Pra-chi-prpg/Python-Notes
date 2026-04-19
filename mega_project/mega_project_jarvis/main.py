import speech_recognition as sr
import pyttsx3
import webbrowser
import client
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = ""
def speak(text):
    engine.say(text)
    engine.runAndWait()

def speak_new(text):
    tts = gTTS(text)
    tts.save("temp")
    # initialize pygame mixer
    pygame.mixer.init()
    # load the mp3 file
    pygame.mixer.music.load("temp.mp3")
    # play the mp3 file
    pygame.mixer.music.play()

#  keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove("temp.mp3")




def aiProcess(command):
    client = OpenAI(
    # api_key= "",
)
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are Jarvis, a smart assistant  named Jarvis Skilled in general tasks like Alexa and Google Cloud.Give short responses"},
            {"role": "user", "content": command}
        ]
    )

    return completion.choices[0].message.content




def aiProcess(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com") 
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link =musicLibrary.music[song]  
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
             # parse the JSON response
            data = r.json()
             # Extract the article
            articles = data.get('articles',[])
            # Print the headlines
            for article in articles:
                speak(article['title'])
    else:
        # lets openAi handle the request
        output = aiProcess(c)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Jarvis.....")
    while True:
        # listen for the wake word "jarvis"
        # obtain audio from the miccrophone
        r = sr.Recognizer()
        print("recognizing...")
        #  recognize speech using google
        try:
            with sr.Microphone() as source:
                print("Listening..")
                audio = r.listen(source,timeout=2 ,phrase_time_limit=1)
            word=r.recognize_google(audio)
            if (word.lower() == "Jarvis"):
                speak("Ya")
            # listen for command

            with sr.Microphone() as source:
                print("Jarvis active...")
                audio = r.listen(source)
                command =r.recognize_google(audio)
                aiProcess(command)
        except Exception as e:
            print("Error: {0}".format(e))



