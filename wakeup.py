import os
import pyttsx3
import speech_recognition as sr


engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')


engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listeneing,sir!..........')
        r.pause_threshold = 1
        audio = r.listen(source,0,7)
    try:
        print('Recognizing,sir!.......')
        query = r.recognize_google(audio, language='en')
        print(query)
    except Exception as e:
        print(f'Sorry, say that again,sir!')
        return takeCommandMic()
    return query.lower()

while True:
    wake_Up = takeCommandMic()

    if 'wake up' in wake_Up:
        speak('Friday at your service, Sir!')
        os.startfile('G:\\Friday 2.0\\Friday 2.0\\Friday2.0.exe')
    elif 'shutdown' in wake_Up:
        speak('I am shutting down......., Sir')
        print('\n\t\t\t\t\t\t\t\tI am shutting down......., Sir ')
        quit()

    else:
        print('nothing....')
