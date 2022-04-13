# Copyright © 2021 Aryan Anshuman. All rights reserved.

from types import CodeType
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voices' , voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    # It will take microphone input from the user and will return a string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... ")
        # r.adjust_for_ambient_noise(source, duration=1)
        # r.energy_threshold = 50 
        r.pause_threshold = 1   # If non speaking audio is appeared for 1 second then it will consider speaking complete
        audio = r.listen(source)

    try:
        print("Recognizing... ")
        query = r.recognize_google(audio , Language = 'en-in')
        print(f"User said : {query}\n")

    except Exception as e:
        # print(e) 
        print("Please say that again... ")
        return "None"

    return query

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour >= 0 and hour < 12):
        speak("Good Morning! ")

    elif(hour >= 12 and hour < 18):
        speak("Good Afternoon! ")
    
    else:
        speak("Good Evening")

    speak("I am your Assistant, made by you")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    # speak("Aryan Anshuman is a good boy")
    while True:
        query = takeCommand().lower()   # Convert to lowercase letters
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia" , "")
            results = wikipedia.summary(query , sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        # elif 'play music' in query:
        #     music_dir = ""  # Your directory
        #     songs = os.listdir(music_dir)
        #     print(songs)
        #     os.startfile(os.path.join(music_dir , songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().startime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Aryan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)


        elif 'email to aryan' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "a.aryan@iitg.ac.in"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry bosh :( , I am not able to send this email")   
