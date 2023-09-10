import sys
import time                           #To stop execution for limited time
import pyttsx3                        #text to speech.
import speech_recognition as sr       #speech to text.
import pyaudio                        #To play and record audio on a variety of platforms.  
import datetime                       #To access Date and time.
import webbrowser                     #TO access Windows default browser.
import pywhatkit                      #To search on google.
import os                             #To access os files.
import subprocess as sp               #Subprocesses with accessible I/O streams.
import pyautogui                      #To take screenshots.
import random                         #Random variable generators.
import keyboard                       #To access keyboards shortcut keys.
import winshell                       #winshell - convenience functions to access Windows shell functionality.
import pyautogui                      #To control volume
from googletrans import Translator
from pywikihow import search_wikihow  #To know how to do anything according to google.
from playsound import playsound       #to play music
import Brain.Aibrain 


voice=int()
engine = pyttsx3.init('sapi5')                 #sapi5:- Application programming interface (API) for voice recog. and synthesis.  
voices = engine.getProperty('voices')          #Gets the current value of a property.
engine.setProperty('voice',voices[int(voice)].id)       #Adds a property value to set to the event queue.

def Ai_voice():
    global engine
    global voice
    if os.path.exists("Body\\voice\\"):
        file=open("Body\\voice\\voice.txt", "r")
        voice=file.read(1)
        file.close()
        engine = pyttsx3.init('sapi5')                 #sapi5:- Application programming interface (API) for voice recog. and synthesis.  
        voices = engine.getProperty('voices')          #Gets the current value of a property.
        engine.setProperty('voice',voices[int(voice)].id) 
    else:
        voice=0

def Set_aivoice(command):
    global engine
    global voice
    if "female" in command:
        file=open("Body\\voice\\voice.txt", "w")
        file.write("1")
        engine = pyttsx3.init('sapi5')                 #sapi5:- Application programming interface (API) for voice recog. and synthesis.  
        voices = engine.getProperty('voices')          #Gets the current value of a property.
        engine.setProperty('voice',voices[1].id) 
        file.close()
    elif "male" in command:
        file=open("Body\\voice\\voice.txt", "w")
        file.write("0")
        engine = pyttsx3.init('sapi5')                 #sapi5:- Application programming interface (API) for voice recog. and synthesis.  
        voices = engine.getProperty('voices')          #Gets the current value of a property.
        engine.setProperty('voice',voices[0].id) 
        file.close()


def takeCommand(alm=0): 
    '''It takes microphine input from user and return string output'''
    
    r= sr.Recognizer()                              #Creates a new ``Recognizer`` instance, which represents a collection of speech recognition functionality.
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        if alm==1:
            r.pause_threshold= 1 
        else:
            r.pause_threshold= 0.7               # seconds of non-speaking audio before a phrase is considered complete
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio, language="en-in")  
    except:
        return "none" 
    
    command= str(command).lower()
    command= transtoen(command)
    
    return command   

def speak(audio):
    '''To speak output by Marshall'''
    global engine
    engine.say(audio)
    engine.setProperty("rate", 175)
    engine.runAndWait()

def transtoen(command):
    line=str(command)
    translate= Translator()
    result= translate.translate(line)
    data =result.text
    return data



def greets(): 
    """Greets the user according to the time"""
    hour=int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak(f"Good Morning  ")
    elif hour>=12 and hour<18:
        
        speak(f"Good Afternoon  ") 
    else: 
        speak(f"Good Evening  ") 
    speak("how can i help you ?") 

def C_replace(command):
    '''Replace unwanted words with blank'''
    command = command.replace("marshall","")
    command = command.replace("google","")
    command = command.replace("youtube","")
    command = command.replace("search","")
    command = command.replace("tell me","")
    command = command.replace("what","")
    command = command.replace("who","")
    command = command.replace("is the","")
    command = command.replace("is","")
    command = command.replace("mean by","")  
    command = command.replace("play video","") 
    command = command.replace("on youtube","") 
    command = command.replace("can you ","")
    command = command.replace("for me","")
    command = command.replace(" about","")
    return command

opening_text = [
    " Hold on a second ! I'm on it .",
    "Okay , I'm working on it.",
    "Just a second.",
]
last_text= [
    "i didnt understand.",
    "please give me correct command.",

]

def closeApp(command):
    '''To close any software'''
    speak(random.choice(opening_text))
    
    if "youtube" in command:
        os.system("TASKKILL /F /im chrome.exe")

    elif "google" in command or "chrome" in command:
        os.system("TASKKILL /F /im chrome.exe")

    elif "command prompt" in command or "cmd" in command:
        os.system("TASKKILL /F /im cmd.exe")

    elif "notepad" in command:
        os.system("TASKKILL /F /im notepad.exe")
    
    else:
        speak(f"sorry, i can't do that.")
def wait_M(): 
    '''stop marshall for some time duration'''
    while True:
        c=takeCommand().lower()
        if c=="none":
            continue
        elif "wake up" in c or "hello" in c:
            break
def sleep_M():
    speak(f"okay, i am going into sleep mode. you can call me anytime just by saying my name.") 
    wait_M() 
    speak(f"hello  , how can i help you ?")
def close_Marashall():
    '''stop the execution'''
    sleep_M()

def open_G():
    '''To just open google'''
    webbrowser.open("https://www.google.com/") 
def search_g(command):
    '''Search on google'''
    command = C_replace(command)
    if command=="":
        speak(f" , complete your sentence.")
    else:
        speak(random.choice(opening_text))
        speak("this is what i found")
        pywhatkit.search(command) 
def Ask_and_search(): 
    '''Search on google by asking command from user'''
    speak("what do you want to search")
    command = takeCommand().lower() 
    while True:
        if command=="none":
            speak(f" , say something")
            break
        elif "open google" in command or "open chrome" in command:
            speak("opening google")
            open_G()
            break
        else:
            command=C_replace(command)
            command=f"https://www.google.com/search?q={command}"
            webbrowser.open(command)
            break
def gautoTools(command):

    if "open new window" in command or "new window" in command:
        keyboard.press_and_release("Ctrl + n")
    
    elif "open new tab" in command or "new tab" in command:
        keyboard.press_and_release("Ctrl + t")

    elif "next open tab" in command or "next tab" in command:
        keyboard.press_and_release("Ctrl + Tab")
     
    elif "previous open tab" in command or "previous tab" in command:
        keyboard.press_and_release("Ctrl + PgUp") 
    
    elif "specific tab" in command or "first tab" in command:
        keyboard.press_and_release("Ctrl + 1") 

    elif "rightmost tab" in command or "last tab" in command:
        keyboard.press_and_release("Ctrl + 9")
    
    elif "open home page" in command:
        keyboard.press_and_release("Alt + Home")

    elif "close current tab" in command or "close tab" in command:
        keyboard.press_and_release("Ctrl + w")
     
    elif "close current window" in command or "close window" in command:
        keyboard.press_and_release("Alt + F4")

    elif "open chrome menu" in command or "chrome menu" in command:
        keyboard.press_and_release("Alt + f") 
    
    elif "bookmarks manager" in command or "bookmark manager" in command:
        keyboard.press_and_release("Ctrl + Shift + o") 
    
    elif "history page" in command or "history" in command:
        keyboard.press_and_release("Ctrl + h")

    elif "downloads" in command or "download" in command:
        keyboard.press_and_release("Ctrl + j")
    
    elif "chrome task manager" in command or "task manager" in command:
        keyboard.press_and_release("Shift + Esc")

    elif "reload" in command:
        keyboard.press_and_release("F5")
    
    elif "bookmark this page" in command:
        keyboard.press_and_release("Ctrl + d")
    
    elif "full screen" in command or "exit full screen" in command:
        keyboard.press_and_release("F11")
    
    elif "minimise" in command:
        keyboard.press("Alt + SPACE")
        time.sleep(1)
        keyboard.press_and_release("n")
        keyboard.release("Alt + SPACE")

    elif "maximize" in command:
        keyboard.press("Alt + SPACE")
        time.sleep(1)
        keyboard.press_and_release("x")
        keyboard.release("Alt + SPACE")

    elif "zoom in" in command:
        keyboard.press("Ctrl")
        time.sleep(1)
        keyboard.press_and_release("=")
        keyboard.release("Ctrl")

    elif "zoom out" in command:
        keyboard.press("Ctrl")
        time.sleep(1)
        keyboard.press_and_release("-")
        keyboard.release("Ctrl")

    elif "default size" in command or "normal size" in command:
        keyboard.press_and_release("Ctrl + 0")
    
    elif "wait" in command:
        speak(f"okay  ")
        wait_M() 
        speak(f"yes  ")

    elif "turn off" in command or "stop automatic" in command:
        speak(f"ok  , chrome automate is off now")
        return 0
    
    elif "automate" in command or "automatic" in command: 
        speak("Chrome automate is already on") 

    elif "close google" in command or "close chrome" in command:
        closeApp(command)
        speak("chrome automate is off now")
        return 0

    elif "turn off yourself" in command: 
            close_Marashall()

    else:
        speak("invalid command, chrome automate is still on.") 
def gautomate():
    speak(f"ok   done, ")
    speak("after using chrome automate , please give me a command to turn off automate") 
    while True:
        c=takeCommand().lower() 
        if c=="none":
            continue 
        elif c!="none":
            a=gautoTools(c)
            if a==0:
                break
            else:
                continue

''' Youtube related functions'''
def Ask_and_play():
    '''Play video on youtube by asking command from user'''
    speak("what do you want to play")
    command = takeCommand().lower() 
    while True:
        if command=="none":
            speak(f" , say something") 
            break
        elif "open youtube" in command:
            speak("opening youtube")
            open_yt()
            break
        else:
            command=C_replace(command)
            pywhatkit.playonyt(command)
            break
def play_V_on_yt(command):
    '''Play video on youtube'''
    command=C_replace(command)
    if command=="":
        speak(f" , complete your sentence.")
    else:
        speak(random.choice(opening_text))
        pywhatkit.playonyt(command) 
def open_yt():
    '''Just open youtube'''
    webbrowser.open("https://www.youtube.com/")
def ytautoTools(command):
    if "pause" in command or "start" in command or "play" in command:
        keyboard.press_and_release("k")

    elif "restart" in command:
        keyboard.press_and_release("0")

    elif "volume up" in command or "increase volume" in command:
        volume(command)

    elif "volume down" in command or "decrease volume" in command:
        volume(command)

    elif "mute" in command:
        keyboard.press_and_release("m")
     
    elif "skip" in command or "forward" in command:
        keyboard.press_and_release("l") 
    
    elif "back" in command or "reverse" in command:
        keyboard.press_and_release("j") 

    elif "full screen" in command or "exit full screen" in command:
        keyboard.press_and_release("f")
    
    elif "theatre mode" in command:
        keyboard.press_and_release("t")

    elif "mini player" in command:
        keyboard.press_and_release("i")
     
    elif "close mini player" in command or "current dialogue" in command:
        keyboard.press_and_release("ESCAPE")
    
    elif "previous video" in command:
        keyboard.press_and_release("SHIFT + p")

    elif "next video" in command:
        keyboard.press_and_release("SHIFT + n") 
    
    elif "increase playback rate" in command:
        keyboard.press_and_release("SHIFT +.") 
    
    elif "caption" in command:
        keyboard.press_and_release("c")

    elif "zoom in" in command:
        keyboard.press_and_release("]")
    
    elif "zoom out" in command: 
        keyboard.press_and_release("[") 
    
    elif "wait" in command:
        speak(f"okay  ")
        wait_M() 
        speak(f"yes  ")

    elif "turn off" in command or "stop " in command and "automate" in command:
        speak(f"ok, youtube automate is off now.")
        return 0
    
    elif "automate" in command: 
        speak("Youtube automate is already on") 

    elif "close youtube" in command or "close current window" in command:
        closeApp(command)
        speak("Youtube automate is off now") 
        return 0
    
    elif "turn off yourself" in command: 
            close_Marashall()

    else:
        speak("invalid command, youtube automate is still on.")
def ytautomate():
    speak(f"ok   done, ")
    speak("after using youtube automate , please give me a command to turn off automate") 
    while True:
        c=takeCommand().lower() 
        if c=="none":
            continue 
        elif c!="none":
            a=ytautoTools(c)
            if a==0:
                break
            else:
                continue

'''Windows apps'''
def open_camera():
    speak(random.choice(opening_text))
    sp.run('start microsoft.windows.camera:', shell=True)   
def Take_photo():
    open_camera()
    time.sleep(2)
    keyboard.press_and_release("ENTER")
def open_cmd(): 
    speak(random.choice(opening_text))
    os.system('start cmd')
def empty_bin():
    try:
        winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
        speak("Recycle Bin Recycled")
    except:
        speak(f" , recycle bin is already empty")
def open_notepad():
    speak(random.choice(opening_text))
    os.startfile("C:\Windows\System32\\notepad.exe")
def volume(command):
    if "volume up" in command or "increase volume" in command:
        pyautogui.press("volumeup")
    elif "volume down" in command or "decrease volume" in command:
        pyautogui.press("volumedown")
    elif "mute" in command:
        pyautogui.press("mute")

'''Screenshot'''       
def take_ss():
    '''To take screenshot'''
    speak(f"ok, what should i name that file?")
    name=takeCommand()
    if name=="none":
        name=str(random.randint(1,100))
    ssname=name+ ".png"
    if os.path.exists("C:\\Marshall\\screenshots\\"):
        pass
    else:
        os.makedirs("C:\\Marshall\\screenshots\\")
    path= "C:\\Marshall\\screenshots\\" + ssname
    ss=pyautogui.screenshot()
    ss.save(path)
    os.startfile("C:\\Marshall\\screenshots\\")
    speak("here is your screenshot")

'''Write and show marshall note'''
def W_Note():
    '''write daily notes'''
    speak(f"What should i write?")
    note = takeCommand()
    if note=="none":
        speak(f" , say something.")
    else:
        if os.path.exists("C:\\Marshall\\Marshall notes\\"):
            pass
        else:
            os.makedirs("C:\\Marshall\\Marshall notes\\")
        file = open("C:\\Marshall\\Marshall notes\\Marshall_note.txt", 'a')
        speak(f"Should i include date and time")
        reply = takeCommand()
        if 'yes' in reply or 'sure' in reply:
            userdate = datetime.date.today().strftime("%B %d %Y")
            userTime = datetime.datetime.now().strftime("%I : %M %p")
            file.write("\n")
            file.write(userdate)
            file.write("\n")
            file.write(userTime)
            file.write(" :- ")
            file.write(note)
            file.write("\n")
            file.close()
        else:
            file.write(note)
            file.close()
        speak(f"done  ")
def open_note():
    speak(f"ok wait, here is your Notes")
    os.startfile("C:\\Marshall\\Marshall notes\\Marshall_note.txt")

'''system shutdown and restart'''
def restart():
    speak(f"Hold On a Second ! Your system is on its way to restart")
    os.system("shutdown /r")
def shutdown():
    speak(f"Hold On a Second ! Your system is on its way to shut down")
    os.system("shutdown /s")
def sleep_mode():
    speak(f"ok ! your system is on its way to go to sleep mode")
    sp.call("shutdown /h")
def abort_shutdown():
    speak(f"ok ! aborting system shut down")
    os.system("shutdown /a")

'''Date and time'''
def date():
    current_date = datetime.date.today().strftime("%B %d %Y")
    speak(f"its {current_date}")
def current_time():
    current_time = datetime.datetime.now().strftime("%I : %M %p")
    speak(f"its {current_time}")
def todays_day():
    todays_day = datetime.datetime.now().strftime("%A")
    speak(f"its {todays_day}")
def eng_translator():
    speak("tell me ! what you want to translate in hindi?")
    t=takeCommand(1)
    speak(random.choice(opening_text))
    webbrowser.open(f"https://translate.google.com/?sl=auto&tl=hi&text={t}%0A&op=translate")

'''Open College website'''
def open_clg_web(command):
    speak(random.choice(opening_text))
    webbrowser.open(command)
def clg_web_link(command):
    if "open" in command:
        if "college website" in command or "college site" in command or "gcoec website" in command:
            open_clg_web("http://www.gcoec.ac.in/gcoec/")
 
        elif "university website" in command or "university site" in command:
            open_clg_web("https://unigug.ac.in/")

        elif "university exam department" in command or "uviersity exam section" in command:
            open_clg_web("https://unigug.ac.in/EXAM/")

        elif "university exam time table" in command or "university exam time tables" in command:
            open_clg_web("https://unigug.ac.in/tita/")

        elif "sports portal" in command or "sport section" in command:
            open_clg_web("https://unigug.ac.in/dept/index.php?sid=10")

        elif "department of engineering" in command:
            open_clg_web("https://unigug.ac.in/ENGINERRING/")

        elif "syllabus portal" in command:
            open_clg_web("https://unigug.ac.in/syllabus/")

        elif "examination schedule" in command or "exam schedule" in command:
            open_clg_web("https://gug.digitaluniversity.ac/PreExamv2_Schedule_Report.aspx?ID=28113")

        elif "exam time table" in command or "exam time tables" in command:
            open_clg_web("https://gug.digitaluniversity.ac/PreExamV2_TimeTable_Report.aspx?ID=28114")

        elif "exam result" in command or "exam results" in command:
            open_clg_web("https://gug.digitaluniversity.ac/Content.aspx?ID=1115")
        
        elif "question papers" in command:
            open_clg_web("https://gug.digitaluniversity.ac/QPCourseSelection.aspx?ID=944") 
 
        elif "maha dbt" in command or "scholarship" in command:
            open_clg_web("https://mahadbt.maharashtra.gov.in/Login/Login")
        
        elif "easy pay payment" in command or "payment portal" in command:
            open_clg_web("https://eazypay.icicibank.com/eazypayLink?P1=mBO7cjSAmo9OXu/JIqWW9w=")
        
        elif "sbi payment portal" in command:
            open_clg_web("https://www.onlinesbi.com/sbicollect/icollecthome.htm?corpID=2976360")
def Location(command):
    '''Find the location of any place'''
    command = command.replace("marshall ", "")
    command = command.replace("where is ", "")
    command = command.replace("tell ", "")
    command = command.replace("me ", "")
    command = command.replace("the ", "")
    command = command.replace("location of ", "")
    if command=="":
        speak(f" , complete your sentence.")
    else:
        if "governnt" in command:
            command=command.replace("governnt", "government")
        speak(f"This is the location of {command}")
        webbrowser.open("https://www.google.com/maps/place/" + command + "")

'''Windows handling'''
def Win_handle(command):
        def replac(command):
            command = command.replace("drive", "")
            command = command.replace("open", "")
            command = command.replace(" ", "")
            command = command.replace("folder", "")
            command = command.replace("file", "")
            return command
        if "open recycle bin" in command:
            keyboard.press("windows")
            keyboard.press_and_release("r")
            time.sleep(2)
            keyboard.release("windows")
            for elements in "shell": keyboard.press_and_release(elements)
            keyboard.press_and_release("shift + ;")
            for elements in "recyclebinfolder": keyboard.press_and_release(elements)
            time.sleep(1)
            keyboard.press_and_release("spacebar")
            keyboard.press_and_release("Enter")

        elif "open this pc" in command or "open my computer" in command:
            sp.run(["explorer", ","])
            
        elif "open file explorer" in command:
            keyboard.press_and_release("windows + e")
        
        elif "open downloads" in command:
            keyboard.press_and_release("windows + r")
            time.sleep(2)
            for elements in "downloads":
                keyboard.press_and_release(elements)
            time.sleep(1)
            keyboard.press_and_release("spacebar")
            keyboard.press_and_release("Enter")

        elif "start menu" in command:
            keyboard.press_and_release("Windows")

        elif "close folder" in command or "close current window" in command or "close window" in command:
            keyboard.press_and_release("Ctrl + w")

        elif "drive" in command and "open" in command:
            command= replac(command)
            sp.run(["explorer", ","])
            time.sleep(2)
            keyboard.press_and_release("Ctrl + l")
            keyboard.press_and_release("spacebar")
            for ele in command:
                keyboard.press_and_release(ele)
            keyboard.press_and_release("shift + ;")
            keyboard.press_and_release("Enter")

        elif "folder" in command and "open" in command or "open" in command and "file" in command:
            command= replac(command)
            keyboard.press_and_release("ctrl + l")
            keyboard.press_and_release("spacebar")
            for ele in command:
                keyboard.press_and_release(ele)
            keyboard.press_and_release("Enter")
        
        elif "create new folder" in command:
            keyboard.press_and_release("ctrl + shift + n")

        elif "go back" in command or "parent folder" in command:
            keyboard.press_and_release("alt + up")

        elif "previous folder" in command:
            keyboard.press_and_release("alt + left")

        elif "next folder" in command:
            keyboard.press_and_release("alt + right")

        elif "large icon" in command:
            keyboard.press_and_release("ctrl + shift + 2")

        elif "small icon" in command:
            keyboard.press_and_release("ctrl + shift + 6")

        elif "go to desktop" in command:
            keyboard.press_and_release("windows + d")

        else: speak(f"Sorry, I cannot do that.")

def TaskExe(command):
    if "female voice" in command and "switch" in command or "male voice" in command and "switch" in command:
        speak("ok  , wait a second.")
        Set_aivoice(command)
        speak("Hello  , How can i help you?")

    elif "search" in command:
        search_g(command)

    elif "open google" in command or "open chrome" in command:
        Ask_and_search()

    elif "automate google" in command or "automate chrome" in command or "automatic google" in command or "automatic chrome" in command: 
        gautomate()

    elif "open youtube" in command:
        Ask_and_play()

    elif "play video" in command:
        play_V_on_yt(command)

    elif "automate youtube" in command or "youtube automate" in command or "automatic youtube" in command or "youtube automatic" in command: 
        ytautomate()
 
    elif "screenshot" in command:
        take_ss()
    
    elif "open camera" in command or "webcam" in command:
        open_camera()
         
    elif "take a photo" in command or "take a selfie" in command:
        Take_photo()

    elif "open command prompt" in command or "open cmd" in command:
        open_cmd()

    elif "open notepad" in command:
        open_notepad()

    elif "write a note" in command:
        W_Note()

    elif "show my notes" in command or "show my note" in command:
        open_note()

    elif "empty recycle bin" in command:
        empty_bin()

    elif "volume up" in command or "increase volume" in command:
        volume(command)

    elif "volume down" in command or "decrease volume" in command:
        volume(command)

    elif "mute" in command:
        volume(command)

    elif "restart system" in command:
        restart()

    elif "hibernate system" in command or "sleep system" in command:
        sleep_mode()

    elif "shutdown system" in command:
        shutdown()

    elif "abort shutdown" in command:
        abort_shutdown()

    elif "today's date" in command or "tell me date" in command or "what is date" in command:
        date()

    elif "current time" in command or "tell me time" in command or "what is time" in command:
        current_time() 
        
    elif "today's day" in command or "tell me day" in command or "what is day" in command:
        todays_day()

    elif "translate to hindi" in command or "translate in hindi" in command:
       eng_translator()

    elif "open university website" in command or "open university site" in command or "open university exam department" in command or "open uviersity exam section" in command or "open university exam time table" in command or "open university exam time tables" in command or "open sports portal" in command or "open sport section" in command or "open department of engineering" in command or "open syllabus portal" in command or "open examination schedule" in command or "open exam schedule" in command or "open exam time table" in command or "open exam time tables" in command or "open exam result" in command or "open exam results" in command or "open question papers" in command or "open maha dbt" in command or "open scholarship portal" in command or "open easy pay payment" in command or "open payment portal" in command or "open sbi payment portal" in command or "open college website" in command or "open college site" in command or "open gcoec website" in command:
        clg_web_link(command)
    
    elif "go to desktop" in command or "large icon" in command or "small icon" in command or "previous folder" in command or "next folder" in command or "go back" in command or "parent folder" in command or "create new folder" in command or "open" in command or "close current window" in command or "close window" in command or "close folder" in command or "open recycle bin" in command or "start menu" in command or "open this pc" in command or "open my computer" in command or "open file explorer" in command or "open downloads" in command:
        Win_handle(command)

    elif "close" in command:
        closeApp(command)
        
    elif "turn off yourself" in command:
        close_Marashall()

    elif "location" in command: 
        Location(command)

    else: 
        command = Brain.Aibrain.Reply(command)
        speak(command)