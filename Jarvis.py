import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import pyautogui
import pyjokes
import pyaudiot

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The Current time is")
    speak(Time)

    

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The Current date is")
    speak(date)
    speak(month)
    speak(year)
    
    
    


def wishme():
    speak("Welcome Back Sir!")
    speak("This is your Jarvis AI Assistant speaking")
    time()
    date()
    hour = datetime.datetime.now().hour
    if hour >=6 and hour <12:
        speak("Good Morning Avichal Sir!")
    elif hour >=12 and hour <18:
        speak("Good Afternoon Avichal Sir!")
    elif hour >=18 and hour <24:
        speak("Good Evening Avichal Sir!")   
    else: 
        speak("Good Night Avichal Sir")         
    speak("Jarvis at your service  , How can I help you?")


def takeCommand():
    r = sr.Recognizer()
     
    with sr.Microphone(device_index=0) as source:
         
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
  
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        return "None"
     
    return query

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\abc\\Desktop\\4th sem\\Jarvis\\ss.png")   

def jokes():
    speak(pyjokes.get_joke())          

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        if 'time' in query:
            time()
        elif 'date' in query:
            date()   
        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)    

        elif 'search in chrome' in query:
            speak("What should I search?")
            mozillapath = 'C:\\ Program Files (x86)\\ Mozilla Firefox\\ firefox.exe %s'  
            search = takeCommand().lower()
            wb.get(mozillapath).open_new_tab(search+'.com')

        elif 'play songs' in query:
            songs_dir = 'E:\\ SONGSS'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[2]))  

        elif 'screenshot' in query:
            screenshot()
            speak("Done!")      

        elif 'joke' in query:
            jokes()
            print(pyjokes.get_joke())

        elif 'how are you' in query: 
            speak("I am fine, Thank you") 
            speak("How are you, Sir") 
  
        elif 'fine' in query or "good" in query: 
            speak("It's good to know that your fine") 

        elif 'offline' in query:
            exit(0)