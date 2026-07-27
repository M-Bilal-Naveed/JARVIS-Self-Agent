import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine= pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    print(c)

if __name__ == "__main__":
    speak("Initializing Jarvis")

    while True:
        #Listen audio awake word jarvis
        #obtain audio from microphone 

        r = sr.Recognizer()

        print('recognizing')

        try:
            with sr.Microphone() as source:
                print('Listening....')
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)

            if(word.lower() == 'jarvis'):
                speak('Ya')

                #Listen the command

                with sr.Microphone as source:
                    print('Jarvis active')
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error: {0}".format(e))