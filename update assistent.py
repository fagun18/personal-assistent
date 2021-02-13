import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import wolframalpha
import json
import requests
import smtplib


print('i    am    your     personal    AI     assistant    -   fagoonti')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,  Good    Morning")
        print("Hello,  Good    Morning")
    elif hour>=12 and hour<18:
        speak("Hello,  Good   Afternoon")
        print("Hello,  Good   Afternoon")
    else:
        speak("Hello,  Good   Evening")
        print("Hello,  Good   Evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("sorry , please say that again")
            return "None"
        return statement

speak("i   am    your     personal    AI     assistant   -  fagoonti")
wishMe()

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('adibahar855@gmail.com', 'fagun5784')
    server.sendmail('adibahar855@gmail.com', to, content)
    server.close()


if __name__=='__main__':


    while True:
        speak("Tell    me    how    can    I    help    you    now?")
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "fagoonti" in statement or "ok bye" in statement or "stop" in statement:
            speak('your   personal   assistant    fagoonti    is   shutting   down  ,Good   bye')
            print('your   personal   assistant    fagoonti    is   shutting   down  ,Good   bye')
            break

        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)


      

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube   is   open   now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google   chrome   is   open   now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google   Mail   open   now")
            time.sleep(5)

        elif "today weather" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats   the   city   name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")



        elif 'what is the time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"fagoon  the time is {strTime}")

        elif 'what is the date' in statement:
            year = int(datetime.datetime.now().year)
            month = int(datetime.datetime.now().month)
            date = int(datetime.datetime.now().day)
            speak("the current Date is")
            speak(date)
            speak(month)
            speak(year)

        elif 'email to fagoon' and 'send email' in statement:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "mbfagun115946@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email")  


        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am  fagoonti   your persoanl  assistant. I   am   programmed   to   minor   tasks   like'
                  'opening   youtube ,  google   chrome  ,  gmail   and   stackoverflow ,  predict   time,  search   wikipedia, predict   weather' 
                  ' in   different   cities ,   get   top   headline   news   from   bbc   and   you   can   ask   me   computational   or   geographical   questions   too!')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by  fagoon")
            print("I was built by  fagoon")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'news for me' in statement:
            news = webbrowser.open_new_tab("https://www.bbc.com/news/world")
            speak('Here are some headlines from the bbc,  Happy  reading')
            time.sleep(10)


        elif 'open fagunti' in statement:
            news = webbrowser.open_new_tab("index.html")
            speak('Here your university webpage ')
            time.sleep(6)

        elif 'search for me'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)


        elif "log off" in statement or "shutdown" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

time.sleep(3)
