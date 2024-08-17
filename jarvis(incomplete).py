import speech_recognition as sr
import webbrowser
import pyttsx3

recogonizer=sr.Recognizer()
engine=pyttsx3.init() 

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__=="__main__":
    speak("Initializing Jarvis...")
    while True:
    #listen for the wake word jarvis
     r = sr.Recognizer()
     print("recogonizing")
    
     with sr.Microphone() as source:
         print("listening...")
         audio = r.listen(source,timeout=1)

     print("recogonizing...")
# recognize speech using Sphinx
     try:
         command = r.recognize_google_cloud(audio)
         print(command)
         if(command.lower())=="jarvis":
            speak("yes")
            #listen for command
            with sr.Microphone() as source:
             print("listening...")
            audio = r.listen(source)
     except sr.UnknownValueError:
        print("Sphinx could not understand audio")
     except Exception as e:
        print("Sphinx error; {0}".format(e))
 
