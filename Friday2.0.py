import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import smtplib
from sec import senderemail, epwd, to
from email.message import EmailMessage
import pyautogui
import webbrowser as wb
from time import sleep
import wikipedia
import pywhatkit
import requests
import json
#from newsapi import NewsApiClient
import clipboard
import os
import pyjokes
import time as tt
import string
import random
import psutil
# from googletrans import  Translator
# from FRIDayCore import Bard
from bardapi import BardCookies
import datetime


#print("\033[1m" + s + "\033[0m")

print('\n\t\t\t\t\t\t\t --------')
print('\t\t\t\t\t\t\t| FRIDAY |')
print('\t\t\t\t\t\t\t --------')
engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def getvoices(voice):
    voices = engine.getProperty('voices')
    #print(voices[1].id)
    if voice == 1:
        engine.setProperty('voice',voices[0].id)
        speak('Hello No sib, This is Friday')
    if voice == 2:
        engine.setProperty('voice',voices[1].id)
        speak('Hello Sir,')

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak('The current time is: ')
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak('The current date is :')
    speak(date)
    speak(month)
    speak(year)

def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <12:
        speak('Good morning Sir')
    elif hour >= 12 and hour < 18:
        speak('Good Afternoon! Sir')
    elif hour >= 18 and hour <24:
        speak('Good Evening sir')
    else:
        speak('Good night sir')

def wishme():
    #speak('Wlcome back sir!')
    # time()
    # date()
    #greeting()
    speak("tell me how can I help you,sir!")
# while True:
#     voice = int(input('1 for Male Friday\n 2 for Female Friday\n -> '))
#     #speak(audio)
#     getvoices(voice)
# time()
# date()
# wishme()

def TakeBengali():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('\nListeneing,sir!.......')
        # speak('Listeneing,sir!..........')
        r.pause_threshold = 1
        audio = r.listen(source, 0, 7)
    try:
        print('\nRecognizing,sir!..........')
        query = r.recognize_google(audio, language='en-IN')
        print(query)
    except Exception as e:
        print(e)
        speak('Say that again,please sir!')
        return 'None'
    return query.lower()


# def trans():
#     speak('Tell me what to translate,sir')
#     line = TakeBengali()
#     translate = Translator()
#     result = translate.translate(line)
#     text = result.text
#     speak(f'The translation for this is' + text)

def takeCommandCMD():
    query = input('Tell me how can i help you?\n')
    return query

def takeCommandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('\nListeneing,sir!.......')
         #speak('Listeneing,sir!..........')
        r.pause_threshold = 1
        audio = r.listen(source,0,7)
    try:
        print('\nRecognizing,sir!..........')
        query = r.recognize_google(audio, language='en-IN')
        print(query)
    except Exception as e:
        print(e)
        speak('Say that again,please sir!')
        return 'None'
    return query.lower()
# def BardAi():
#     Bard

    

def sendEmail(reciever, subject, content):
    server = smtplib.SMTP('smtp-mail.outlook.com', 587)
    server.starttls()
    server.login(senderemail, epwd)
    email = EmailMessage()
    email['From'] = senderemail
    email['To'] = reciever
    email['Subject'] = subject
    email.set_content(content)
    server.send_message(email)
    server.close()

def sendwhatsmsg(phone_no, message):
    Message = message
    wb.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+Message)
    sleep(12)
    pyautogui.press('enter')

def searchgoogle():
    speak('What should i search,Sir!')
    search = takeCommandMic()
    wb.open('https://www.google.com/search?q='+search)

#https://api.openweathermap.org/data/2.5/weather?q={Barisal}&ubits=imperial&appid={d5c9f99f18ad6af9022d8370f09bf919}

 # elif 'news' in query:
 #            speak('News headlines')
 #            query = query.replace('news', '')
 #            url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=6707ff0500274e85bea4c6ff6040ce4b'
 #            news = requests.get(url).text
 #            news = json.loads(news)
 #            art = news['articles']
 #            for article in art:
 #                print(article['title'])
 #                speak((article['title']))
 #
 #                print(article['description'])
 #                speak(article['description'])
 #                speak('Moving on to the next news')

def text2speech():
    text = clipboard.paste()
    print(text)
    speak(text)

# def covid():
#     r = requests.get('https://coronavirus-19-api.herokuapp.com/all')
#     data = r.json()
#     covid_data = f'Confirmed cases : {data['cases']} \n Deaths : {data['details']}\n Recovered {data['recovered']}
#     print(covid_data)
#     speak(covid_data)

def screenshot():
    name_img = tt.time()
    name_img = f'G:\\Friday 2.0\\Friday 2.0\\screenshot\\{name_img}.png'
    img = pyautogui.screenshot(name_img)
    img.show()

def passwordgen():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation

    passlen = 8
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)
    newpass = (''.join(s[0:passlen]))
    print(newpass)
    speak(newpass)

def flip_coin():
    speak('ok sir,flipping a coin for you')
    coin = ['Heads','\bTails']
    toss = []
    toss.extend(coin)
    random.shuffle(toss)
    toss = (''.join(toss[0]))
    print(toss)
    speak(' I flipped the coin sir, and you got'+toss)

def roll_dice():
    speak('Rolling a dice for you,sir!')
    dice = ['1','2','3','4','5','6']
    roll = []
    roll.extend(dice)
    random.shuffle(roll)
    roll = (''.join(roll[0]))
    print(roll)
    speak('I rolled a dice sir, you got '+roll)
def cpu_usage():
     usage = str(psutil.cpu_percent())
     speak('CPU is at '+usage)
     battery = str(psutil.sensors_battery())
     speak('Battery is at' + battery)
def bard_AI():
   
   cookie_dict = {
       '__Secure-1PSID'  : 'ZwhACmqbhSYLe_H-1XDjanDfm6C_X5MWeWjMt3OqOxanfygBFnsz2riFG7LDUOnPbhp_Ow.',
       '__Secure-1PSIDTS' : 'sidts-CjEBSAxbGf1DlzMt8ELD5cYrPGEn1zpkvDZpiNd-5QpAYwKyBEqddbf1Z72xXlELFj-HEAA',
       '__Secure-1PSIDCC' : 'APoG2W92kfbtPqHtKdiK2O1IVYYpYTHrM9zGx19aoBeL_opMNljinWpKSIgedXLz603xMhZ8Gh5p'
    }
   bard = BardCookies(cookie_dict=cookie_dict)
   while True:
        Query = takeCommandMic()
        Reply = bard.get_answer(Query)['content']
        print(Reply)
        speak(Reply)
        # return query

if __name__ == "__main__":
    getvoices(2)
    wishme()
    while True:
        query = takeCommandMic().lower()
        if 'time' in query:
            time()

        elif 'what you can do for me currently' in query:
            can_perform = 'I can Wish Greetings\n,Telling time\n, date\n, send emails\n, send whats app message\n,search in wikipedia\n,search on google\n,play mysic on youtube\n,telling news\n,weather forecast\n,telling jokes\n,take and show screenshot\n,can remember you words\n,password genarator\n ,flipping coin\n.rolling dice\ncan tell cpu and battery usage\n etc for now'
            print(can_perform)
            speak(can_perform)

        elif 'date' in query:
            date()
        elif 'email' in query:
            email_list = {
                'myself':'sibmello2021@gmail.com'
            }
            try:
                speak('Whom do you wanna send,sir!?')
                name = takeCommandMic()
                receiver = email_list[name]
                speak('What is the subject,sir!')
                subject = takeCommandMic()
                speak('What should i say,sir!')
                content = takeCommandMic()
                sendEmail(receiver, subject, content)
                speak('Mail has been sent,sir!')
            except Exception as e:
                print(e)
                speak('Unable to send,sir!')
        elif 'message' in query:
            user_name = {
                'myself': '+88 01302784441'
            }
            try:
                speak('Whom do you wanna send in WhatsApp,sir!?')
                name = takeCommandMic()
                phone_no = user_name[name]
                speak('What is the message,sir!')
                message = takeCommandMic()
                sendwhatsmsg(phone_no, message)
                speak('message has been sent,sir!')
            except Exception as e:
                print(e)
                speak('Unable to send message,sir!')

        elif 'wikipedia' in query or 'who' in query or 'what' in query or 'where' in query or 'when' in query:
            speak('Searching on wikipedia....')
            query = query.replace('wikipedia','')
            result = wikipedia.summary(query, sentences =2)
            print(result)
            speak(result)

        elif 'search' in query:
            searchgoogle()
        elif 'youtube' in query:
            speak('what should I search on youtube,sir!')
            topic = takeCommandMic()
            pywhatkit.playonyt(topic)
        elif 'weather' in query:
            city = 'barisal'
            url = 'http://api.openweathermap.org/data/2.5/weather?q=barisal&units=imperial&appid=d5c9f99f18ad6af9022d8370f09bf919'
            res = requests.get(url)
            data = res.json()
            weather = data['weather'] [0] ['main']
            temp = data['main'] ['temp']
            desp = data['weather'] [0] ['description']
            temp = round((temp - 32)*  5/9)
            print(weather)
            print(temp)
            print(desp)
            speak('weather in Barisal is {}'.format(desp))
            speak('Temparature : {} degree celcius'.format(temp))

        # elif 'news' in query:
        #     news()

        elif 'news' in query:
            speak('News headlines')
            query = query.replace('news', '')
            url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=6707ff0500274e85bea4c6ff6040ce4b'
            news = requests.get(url).text
            news = json.loads(news)
            art = news['articles']
            for article in art:
                print(article['title'])
                speak((article['title']))

                print(article['description'])
                speak(article['description'])
                speak('Moving on to the next news')

        elif 'read' in query:
            text2speech()

        # elif 'covid' in query:
        #     covid()
        elif 'my documents' in query:
            os.system('explorer C://{}'.format(query.replace('open','')))

        elif 'visual studio' in query:
            codepath = 'C:\\Users\\yoyog\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe'
            os.startfile(codepath)
        elif 'close'in query:
            os.system(f'TASKKILL /F /IM code.exe')

        elif 'code blocks' in query:
            codepath = 'C:\\Program Files\\CodeBlocks\\codeblocks.exe'
            os.startfile(codepath)
        elif 'close'in query:
            os.system(f'TASKKILL /F /IM codeblocks.exe')

        elif 'python' in query:
            codepath = 'C:\\Program Files\\Python310\\python.exe'
            os.startfile(codepath)

        elif 'pycharm' in query:
            codepath = 'C:\\Program Files\\JetBrains\\PyCharm Community Edition 2022.2\\bin\\pycharm.exe'
            os.startfile(codepath)
        # elif 'close'in query:
        #     os.system(f'TASKKILL /F /IM pycharm.exe')

        elif 'main code' in query:
            codepath = 'C:\\Program Files\\JetBrains\\PyCharm Community Edition 2022.2\\bin\\pycharm.exe'
            os.startfile(codepath)


        elif 'webcam' in query:
            codepath = 'C:\\Program Files (x86)\\Iriun Webcam\\IriunWebcam.exe'
            os.startfile(codepath)
        elif 'close'in query:
            os.system(f'TASKKILL /F /IM IriunWebcam.exe')

        elif 'jokes' in query:
            speak(pyjokes.get_joke())

        elif 'screenshot' in query:
            screenshot()

        elif 'remember' in query:
            speak('What should I remember,sir!')
            data = takeCommandMic()
            speak('You said me to remember that'+data)
            remember = open('remember.txt','w')
            remember.write(data)
            remember.close()

        elif 'do you know anything' in query:
            remember = open('remember.txt', 'r')
            speak('You told me to remember that'+remember.read())

        elif 'thank you' in query:
            speak('(anything for you, No Sib, sir!')

        elif 'can you generate a password' in query:
            passwordgen()

        elif 'flip a coin' in query:
            flip_coin()

        elif 'roll a dice' in query:
            roll_dice()
        elif 'cpu usage' in query:
            cpu_usage()
        # elif 'translate' in query:
        #     trans()
        # elif 'solve a problem' in query:
        #     BardAi()
        elif 'solve a problem' in query:
            speak('Ofcourse,Sir!')
            bard_AI()
            takeCommandMic()
        elif 'to do list' in query:
            while True:
                user = input('Enter 1.Add, 2.Show, 3.Edit, 4.Complete, 5.Exit :')
                user = user.strip()

                if '1' in user or 'add' in user:
                    todo = input('Enter a todo : ') + '\n'

                    with open('d9.txt', 'r') as file:
                        todos = file.readlines()

                    todos.append(todo)

                    with open('d9.txt', 'w') as file:
                        file.writelines(todos)
                elif '2' in user or 'show' in user:
                    with open('d9.txt', 'r') as file:
                        todos = file.readlines()

                    new_todos = [item.strip('\n') for item in todos]

                    for index, item in enumerate(new_todos):
                        item = item.strip('\n')
                        row = f'{index + 1}.{item}'
                        print(row)
                        speak(row)
                elif '3' in user or 'edit' in user:

                    number = int(input('Enter a number to edit : '))
                    number = number - 1

                    with open('d9.txt', 'r') as file:
                        todos = file.readlines()

                    new_todo = input('Enter a New todo : ')
                    todos[number] = new_todo

                    with open('d9.txt', 'w') as file:
                        file.writelines(todos)
                elif '4' in user or 'complete' in user:
                    number = int(input('Enter a number to complete : '))
                    with open('d9.txt', 'r') as file:
                        todos = file.readlines()
                        index = number - 1
                        todo_to_remove = todos[index].strip('\n')
                    todos.pop(index)

                    with open('d9.txt', 'w') as file:
                        file.writelines(todos)

                        messege = f'Request to remove{todo_to_remove} is successful'
                        print(messege)
                elif '5' in user:
                    break
                else:
                    print('Command is not valid.')


        elif 'sleep' in query or 'quit' in query or 'break' in query:
            speak('As you wish, sir!Just say wake up when you need, sir!')
            quit()
