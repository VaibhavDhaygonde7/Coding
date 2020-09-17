import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import webbrowser
import os
import smtplib   #for sending email
import random

# off the firewall settings before running this code

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)             
#voices[0] for male voice and voices[1] for female voice
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)    # due to this we will get the hours from 0 to 24
    if hour >= 0 and hour < 12:
        speak("Good Morning")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am Jarvis sir. Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1    # this will take wait for the user to speak if user takes a pause
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")   # this is the same voice recognizer used in google
        print(f"User said: {query}\n") 

    except Exception as e:
        # print(e)  
        print("Say that again please...")
        return "None"     # this is not 0, this is just a string
    return query

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('your-email-address@gmail.com', 'your-password-here')
    server.sendmail('s.dhaygonde@gmail.com', to, content)
    server.close()
    
if __name__ == "__main__":
    wishMe()
    music_dir = 'C:\\Users\\sdhaygo\\Desktop\\Songs'
    songs = os.listdir(music_dir)
    while True:
        query = takeCommand().lower()

        if 'information' in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
            print(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open my website' in query:
            webbrowser.open("vaibhav7.in")
        
        elif 'play music' in query:
            print(songs)
            speak("Which song sir?")
            querymusic = takeCommand().lower()
            if 'faded' in querymusic:
                os.startfile(os.path.join(music_dir, songs[0]))
            elif 'rings' in querymusic:
                os.startfile(os.path.join(music_dir, songs[1]))
            elif 'attention' in querymusic:
                os.startfile(os.path.join(music_dir, songs[2]))
            elif 'safar' in querymusic:
                os.startfile(os.path.join(music_dir, songs[3]))
            elif 'student anthem' in querymusic:
                os.startfile(os.path.join(music_dir, songs[4]))
            elif 'yalgaar' in querymusic:
                os.startfile(os.path.join(music_dir, songs[5]))
            elif 'zindagi' in querymusic:
                os.startfile(os.path.join(music_dir, songs[6]))
        elif 'play random song' in query:
                music_dir = 'C:\\Users\\sdhaygo\\Desktop\\Songs'
                songs = os.listdir(music_dir)
                n = random.randint(0,5)
                os.startfile(os.path.join(music_dir, songs[n]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        
        elif 'open code' in query:
            codePath = "C:\\Users\\sdhaygo\Desktop\\Vaibhav's  folder\\vscode-win32-x64-1.39.0 (1)\\Code.exe"
            os.startfile(codePath)

        elif 'email to suresh' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "receiver's-address@gmail.com"
                sendEmail(to, content)
                speak("Your email has been sent")
            except Exception as e:
                # print(e)
                speak("Sorry sir. I am not able to send the email")

        elif 'your master' in query:
            speak("My master is Vaibhav, who is an Indian")

        elif 'who are you' in query:
            speak("My name is Jarvis and I am a mini A.I. or Artificial Intelligence. I was made by Vaibhav and I was made in India")
        
        # elif 'do you like siri' or 'do you like alexa' or 'do you like google' in query:
        #     speak("Yes I like her")

        elif 'best country' in query:
            speak("According to me, the best country in the world is India")
        
        elif 'can you do' in query:
            speak("I can perform simple tasks like opening file, google, youtube, websites, etc. I can play music for you or even send e-mail, if you gave me the command to do so!")
        
        elif 'play faded' in query:
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'play rings' in query:
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'play attention' in query:
            os.startfile(os.path.join(music_dir, songs[2]))

        elif 'play safar' in query:
            os.startfile(os.path.join(music_dir, songs[3]))

        elif 'student anthem' in query:
            os.startfile(os.path.join(music_dir, songs[4]))

        elif 'play yalgaar' in query:
            os.startfile(os.path.join(music_dir, songs[5]))

        elif 'play zindagi' in query:
            os.startfile(os.path.join(music_dir, songs[6]))

        elif 'quit' in query:
            speak("Thank you sir. Quitting")
            break