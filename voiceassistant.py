import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import smtplib
import os
import pyautogui
import psutil
import pyjokes




engine = pyttsx3.init()    #initializes the module

voices=engine.getProperty('voices')    #it will get voice property
engine.setProperty('voice', voices[2].id)

newvoicerate=180                       #it will change voice rate default=200
engine.setProperty('rate', newvoicerate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
    

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("current time is")
    speak(Time)
    
def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    day=int(datetime.datetime.now().day)
    speak("todays date is")
    speak(day)
    speak(month)
    speak(year)    

def wishme():
   
    hour=datetime.datetime.now().hour
    speak("welcome back sir!")
    if hour>=6 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("Good afternoon")
    elif hour>=18 and hour<=24:
        speak("Good evening")
    else:
        speak("Good night")
   
        
    speak("friday at your service!, how can I help you?")
    

    
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en=US')
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")
        
        return "None"
    return query

def sendemail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('emailid','password')
    server.sendmail('senders mail',to,content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("D:\FILES\ss.png")
    
def cpu():
    
    usage = str(psutil.cpu_percent())
    speak("CPU is at" + usage)
    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)
    
def jokes():
    
    speak(pyjokes.get_joke())
    


if __name__=="__main__":
    wishme()
    while True:
        query=takecommand().lower()
        
        
        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "dismiss" in query:
            speak("OK master, Have a nice day!")
            quit()
        elif "wikipedia" in query:
            speak("searching sir")
            query=query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=1)
            speak(result)
            
        elif "search in chrome" in query:
            speak("What should I search sir?")
            chromepath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            search=takecommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")
      
        
        elif "send email" in query:
            try:
                speak("What should I send?")
                content=takecommand()
                to="recievers mail"
                sendemail(to, content)
                speak("Email send successfully!")
            except Exception as  e:
                
                speak("sorry unable to send the email")
                print(e)
                speak(e)
                
        elif "logout" in query:
            os.system("shutdown - l")
            
        elif "shutdown" in query:
            os.system("shutdown - /s /t 1")
            
        elif "restart" in query:
            os.system("shutdown - /r /t 1")
        
        elif "play songs" in query:
            music_dir = "D:/music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))
            
        elif "remember that" in query:
            speak("what should I remember?")
            data = takecommand()
            speak("you told me to remember that" + data)
            remember = open("data.txt")
            remember.write(data)
            remember.close()
            
        elif "do you know anything" in query:
            remember=open("data.txt","r")
            speak("you told me to remember that"+remember.read())
            
        elif "screenshot" in query:
            screenshot()
            speak("done!")
            
        elif "CPU" in query:
            cpu()
            
        elif "joke" in query:
            jokes()