import smtplib
import pyttsx3

engine = pyttsx3.init()

def speak(arg):
    rate = engine.getProperty('rate')
    volume = engine.getProperty('volume')
    voices = engine.getProperty('voices')

    engine.setProperty('rate', 160)
    engine.setProperty('volume', 2)
    engine.setProperty('voice', voices[0].id)

    engine.say(arg)
    engine.runAndWait()

def Sender(user, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your_email@gmail.com', 'your_password')
    server.sendmail('your_email@gmail.com', user, content)
    server.close()

user_inp = input("Send Email (Y/N)?")

while True:
    if user_inp == "yes".lower() or user_inp == "y".lower():
        speak("What should I say?")
        content = input("> ")
        user = "receiver@gmail.com"    
        Sender(user, content)
        speak("Email has been sent!")
    else:
        break
