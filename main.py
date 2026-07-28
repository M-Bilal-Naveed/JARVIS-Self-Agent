import speech_recognition as sr
import webbrowser
import pyttsx3
from news_client import get_news
from sitesLibrary import websites
from musicLibrary import music
from open_ai_client import aiProcess

recognizer = sr.Recognizer()
engine= pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if c.lower().startswith('open'):
        site = c.lower().split(" ")[1]
        link = websites[site]
        webbrowser.open(link)

    elif c.lower().startswith('play'):
        song = c.lower().split(" ")[1]
        link = music[song]
        webbrowser.open(link)

    elif "news"in c.lower():
         articles = get_news()

         if articles:
             for article in articles:
                 speak(article["title"])
         else:
             speak("Sorry, I cannot read the news now.")

    else:
        #go to open Ai account
        output = aiProcess(c)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Jarvis")

    while True:
        #Listen audio awake word jarvis
        #obtain audio from microphone 

        r = sr.Recognizer()

        print('recognizing....')

        try:
            with sr.Microphone() as source:
                print('Listening....')
                audio = r.listen(source, timeout=5, phrase_time_limit=3)
            word = r.recognize_google(audio)

            if(word.lower() == 'jarvis'):
                speak('Ya')

                #Listen the command

                with sr.Microphone() as source:
                    print('Jarvis active')
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error: {0}".format(e))