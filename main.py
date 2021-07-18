import speech_recognition as sr
import pyttsx3 as ts
import pywhatkit as wk
import datetime as dt
import wikipedia as wiki
import pyjokes as pj

listener = sr.Recognizer()
engine = ts.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'buddy' in command:
                command = command.replace('buddy','')
                print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    if 'play' in command:
        song = command.replace('play','')
        talk('okay buddy')
        wk.playonyt(song)
    elif 'time' in command:
        time = dt.datetime.now().strftime('%I:%M %p')
        talk('Current time is'+ time)
        print(time)
    elif 'tell me about' or 'who is' in command:
        info = wiki.summary(command, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pj.get_joke())
    else:
        talk('I am not trained for that buddy, please try another command')


talk('Hello master how can i help you')
while True:
    try:
        run_alexa()
        talk('anything else')
    except:
        pass