import speech_recognition as sr

import os
import sys
import webbrowser

from datetime import datetime

def talk(words):
    print(words)
    os.system("say " + words)

talk("Hi, ask me something")

def command():
    r = sr.Recognizer()
    
    with sr.Microphone() as source: 
        print("Speak")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        task = r.recognize_google(audio).lower()
        print("You said: " + task)
    except sr.UnknownValueError:
        talk("I did not understand you")
        task = command()
    
    return task

def makeSomething(task):
    if 'open website'.lower() in task:
        talk("Already opening")
        url = 'https://vk.com/public_lar'
        webbrowser.open(url)

    elif 'date'.lower() in task:
        talk("Day after day")
        current_date = datetime.now().date()
        print(current_date)

    elif 'time'.lower() in task:

        if 5 <= datetime.now().hour <= 17:
            talk("Good day")
        if 17 <= datetime.now().hour <= 22:
            talk("Good evening")
        if (4 <= datetime.now().hour <= 22) or (0 <= datetime.now().hour <= 4):
            talk("Goodnight")

        current_time = datetime.now().time()
        print(current_time)

    elif 'stop'.lower() in task:
        talk("Yes of course without problems")
        sys.exit()

while True:
    makeSomething(command())
