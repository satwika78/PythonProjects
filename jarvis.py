import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("good morning")
    elif(hour>=12 and hour<18):
        speak("good afternoon")
    else:
        speak("good evening")
    speak("I am jarvis your assistant. How can I help you")
def takeCommand():
    #it takes voice input from the user and gives string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        r.energy_threshold = 200
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query =r.recognize_google(audio,language='en-in')
        print(f"User Said: {query}\n")
    except Exception as e:
        #print(e)
        print("say that again please")
        return "None"
    return query
def sendemail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('mygmail@gmail.com','password')
    server.send('yourgmail@gmail.com')

if __name__ == "__main__":
    wishme()
    while True:
        query=takeCommand().lower()
    #logic for executing task based on query 
        if 'wikipedia' in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'open vardhaman website' in query:
            webbrowser.open("vardhaman.org")
        elif 'play music' in query:
            music_dir = 'E:\\music_dir'
            songs = os.listdir(music_dir)
            print(songs)
            print('playing songs')
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'time' in query:
            strtime = datetime.datetime.now().strftime('%H:%M:%S')
            print(strtime)
            speak(f"the time is {strtime}")
        elif 'open vscode' in query:
            codepath = "C:\\Users\\satwika\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'send email' in query:
            try:
                speak("what should i send")
                content = takeCommand()
                to='yourgmail@gmail.com'
                sendemail(to,content)
                speak("email is sent successfully")
            except Exception as e:
                print(e)
                speak("sorry! email not sent")
        if 'quit' in query:
            speak("bye! take care")
            exit()   

        