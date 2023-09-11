from logging import shutdown
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
from googlesearch import search

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[1].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")
        
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("I am sorry, please say that again")
            return "None"
        return statement

print("Loading your AI personal assistant Legend")
speak("Loading your AI personal assistant Legend")
wishMe()

if __name__=='__main__':


    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement==0:
            continue
        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant Legend is shutting down,Good bye')
            print('your personal assistant Legend is shutting down,Good bye')
            break
        
        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail is open now")
            time.sleep(5)
        
        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'camera' in statement or 'take photo' in statement:
            speak("Can I have a Legendary Smile?")
            ec.capture(0,"Legend's camera","img.jpg")

        elif 'news' in statement:
            news=webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak("Here are some headlines from the Times of India, Enjoy Reading")
            time.sleep(6)
        
        elif 'search' in statement:
            #statement=statement.replace("search","")
            #result=webbrowser.open(statement)
            for j in search(statement,tld="co.in",num=1,stop=1,pause=2):
                print(j)
                webbrowser.open_new_tab(statement)
            speak("Here is the result of what you wanted to search")
            print("Here is the result of what you wanted to search")
            time.sleep(6)
        
        elif 'who made you' in statement:
            speak("I was built by the legend Syed Nameer")
            print("I was built by the legend Syed Nameer")
        
        elif 'log off' in statement:
            speak("Your Legendary Laptop will shut down in 10 seconds, please close all the applications")
            #subprocess.call(["shutdown","/1"])
            os.system("shutdown /s /t 1")
            time.sleep(3)