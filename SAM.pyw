import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
#from pygame import mixer
import pyowm
import subprocess
engine = pyttsx3.init('sapi5')
client = wolframalpha.Client('Your_App_ID')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-2].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 50)

def speak(audio):
    print('Sam: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:

        stMsgs = ['Good Morning sir',
'Weather says it is a great morning',
'Good morning Mahmoud, did you sleep well?',
'what is your main focus for today',
'Write it on your heart that every day is the best day in the year......good morning',
'I get up every morning and it’s going to be a great day. You never know when it’s going to be over, so I refuse to have a bad day',
"it's New Morning"
                ]
        speak(random.choice(stMsgs))
    if currentH >= 12 and currentH < 18:
        stMsgs = ['Weather says sunlight is good today.....Good Afternoon sir!',
                  'Good Afternoon sir!',
                  'Very good afternoon to you. as well. Let me know if there is anything i can help you with'


                  ]
        speak(random.choice(stMsgs))
        

    if currentH >= 18 and currentH !=0:
        speak('Good Evening sir!')
greetMe()
#stMsgs = ['yes sir sam with you!', 'how are you', 'hello im here', 'yes im here mahmoud' , 'you know .... im alwys here be side you ']
#speak(random.choice(stMsgs))


def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")

        r.pause_threshold =  1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-in')
            print('Sir : ' + query + '\n')
            
        except sr.UnknownValueError:
            speak('Sorry sir! I didn\'t get that! Try typing the command!')
            query = str(input('Command: '))

        return query

if __name__ == '__main__':
    while True:
        query = myCommand();
        query = query.lower()
        now = datetime.datetime.now()
        

        if 'open youtube' in query or 'youtube' in query or 'open youtube please' in query or 'please open youtube' in query or 'please youtube' in query or 'youtube please' in query:
            
            stMsgs = ['Just moment','okay','i will','from my eyes','just scound',"it's too easy"]
            speak(random.choice(stMsgs))
            webbrowser.open('www.youtube.com')
        elif 'tell me the weather today' in query or 'weather' in query or 'what about the weather' in query or 'do you know what the weather today' in query or 'do you know what the weather' in query:
            stMsgs = ['Just moment','okay','i will','from my eyes','just scound',"it's too easy"]
            speak(random.choice(stMsgs))
            owm = pyowm.OWM('0da5b5509eb4bd6639d795e3d40ba27c')
            observation = owm.weather_at_place('GIZA, EG')
            observation_list = owm.weather_around_coords(12.972442, 77.580643)
            w = observation.get_weather()
            w.get_wind()
            w.get_humidity()
            w.get_temperature('celsius')
            print(w)
            print(w.get_wind())
            print(w.get_humidity())
            print(w.get_temperature('celsius'))
            engine.say(w.get_wind())
            engine.runAndWait()
            engine.say('humidity')
            engine.runAndWait()
            engine.say(w.get_humidity())
            engine.runAndWait()
            engine.say('temperature')
            engine.runAndWait()
            engine.say(w.get_temperature('celsius'))
            engine.runAndWait()

#_____________________ Broser _______________________ Broser ______________________ Broser _____________________ Broser ____________________________________ Broser __________________________________ Broser __________________________________ Broser _______________


        elif 'open google' in query or 'google' in query or 'open google please' in query or 'please open google' in query or 'please google' in query or 'google please' in query:
            stMsgs = ['Just moment','okay','i will','from my eyes','just second',"it's too easy"]
            speak(random.choice(stMsgs))
            webbrowser.open('www.google.com')


        elif 'open facebook' in query or 'facebook' in query or 'open facebook please' in query or 'please open facebook' in query or 'please facebook' in query or 'facebook please' in query:
            stMsgs = ['Just moment','okay','i will','from my eyes','just second',"it's too easy"]
            speak(random.choice(stMsgs))
            webbrowser.open('www.facebook.com')



        elif 'open my facebook' in query or 'my facebook' in query or 'open my facebook please' in query or 'please open my facebook' in query or 'please my facebook' in query or 'my facebook please' in query:
            stMsgs = ['Just moment','okay','i will','from my eyes','just second',"it's too easy"]
            speak(random.choice(stMsgs))
            webbrowser.open('www.facebook.com/profile.php?id=100010994918334')


          

        elif 'open gmail' in query or 'gmail' in query or 'open gmail please' in query or 'please open gmail' in query or 'please gmail' in query or 'gmail please' in query:
            stMsgs = ['Just moment','okay','i will','from my eyes','just second',"it's too easy"]
            speak(random.choice(stMsgs))
            webbrowser.open('www.gmail.com')



        elif "open instagram" in query or "insta" in query or "instagram" in query or "please open instagram" in query or "open instagram please" in query or "open insta" in query or "open insta please" in query or "insta please" in query:
            stMsgs = ['Just moment','okay','i will','from my eyes','just second',"it's too easy"]
            speak(random.choice(stMsgs))
            webbrowser.open('www.instagram.com')


        elif "open twitter" in query or "aa" in query or "aa" in query or "please open twitter" in query or "open twitter please" in query or "open  please twitter" in query or "twitter please" in query:
            stMsgs = ['Just moment','okay','i will','from my eyes','just second',"it's too easy"]
            speak(random.choice(stMsgs))
            webbrowser.open('www.twitter.com')


        elif 'open linkedin' in query or 'linkedin' in query or 'open linkedin please' in query or 'please open linkedin' in query or 'please linkedin' in query or 'linkedin please' in query:
            stMsgs = ['Just moment','okay','i will','from my eyes','just second',"it's too easy"]
            speak(random.choice(stMsgs))
            webbrowser.open('www.linkedin.com')

        elif 'open soundcloud' in query or 'soundcloud' in query or 'open soundcloud please' in query or 'please open soundcloud' in query or 'please soundcloud' in query or 'soundcloud please' in query:

            stMsgs = ['Just moment','okay','i will','from my eyes','just second',"it's too easy"]
            speak(random.choice(stMsgs))
            webbrowser.open('www.soundcloud.com')


        elif 'open google translate' in query or 'translate' in query or 'open google translate please' in query or 'please open google translate' in query or 'please google translate' in query or 'google translate please' in query or "google translation" in query or "open google translation" in query or "open google translation please" in query:
            stMsgs = ['Just moment','okay','i will','from my eyes','just second',"it's too easy"]
            speak(random.choice(stMsgs))
            webbrowser.open('https://translate.google.com/')


        elif 'open upwork' in query or 'upwork' in query or 'open upwork please' in query or 'please open upwork' in query or 'please upwork' in query or 'upwork please' in query:
            stMsgs = ['Just moment','okay','i will','from my eyes','just second',"it's too easy"]
            speak(random.choice(stMsgs))
            webbrowser.open('www.upwork.com')


        elif 'open wikipedia' in query or 'wikipedia' in query or 'open wikipedia please' in query or 'please open wikipedia' in query or 'please wikipedia' in query or 'wikipedia please' in query:
            stMsgs = ['Just moment','okay','i will','from my eyes','just second',"it's too easy"]
            speak(random.choice(stMsgs))
            webbrowser.open('www.wikipedia.org/')





        elif 'email' in query or 'i wanna send email please'in query or 'send email please'in query or 'i want to send email'in query or 'i want to send email please'in query or 'i wanna send email'in query or 'can you send email' in query:
            speak('you want to send email')
            speak('Who is the recipient? ')
            recipient = myCommand()
            if 'I am' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("bondok2020m", 'mahmoudemad3538192233***')
                    server.sendmail('bondok2020m', "I am", content)
                    server.close()
                    speak('Email sent!')
                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')
#___________________________     

        elif "where is" in query or 'location' in query:
            speak("Hold on. I will show you " + query + " now. just give me some moments ")
            webbrowser.open("https://www.google.com/maps?q=%s" % query)

#___________    Morning   _______________afternon__________________ Evening_____________________Good night_______________Morning___________________afternon______________ Evening_____________________Good night________________


        elif 'good morning' in query:
            currentH = int(datetime.datetime.now().hour)
            if currentH >= 12 and currentH < 18:
                speak('sure you are joke. its after noon My friend. Good after noon for you sir')
            elif currentH >= 18 and currentH !=0:
                speak('sure you are joke. its evening My friend. Good evening')
            elif currentH >= 0 and currentH < 12:
                speak('Great morning for you. Tell Me What Is Your Plan Today')
#__________________________


        elif 'good afternoon' in query:
            currentH = int(datetime.datetime.now().hour)
            if currentH >= 12 and currentH < 18:
                stMsgs = ['Great afternoon for you. What are You Doing ?' , "and Very good afternoon to you. as well. Let me know if there is anything i can help you with",
                          ]
            elif currentH >= 18 and currentH !=0:
                speak('sure you are joke. its evening My friend. Good evening')
            elif currentH >= 0 and currentH < 12:
                speak('i think you dont sleap well yesterday its afternon dear')

#___________________________


        elif 'good evening' in query:
            currentH = int(datetime.datetime.now().hour)
            if currentH >= 12 and currentH < 18:
                speak('sure you are joke. its after noon My friend. Good after noon for you sir')
            elif currentH >= 18 and currentH !=0:
                speak('Great Evening for you. Tell me about your health ? are you okay')
            elif currentH >= 0 and currentH < 12:
                speak('sure you are joke. its wonderful morning Sir. i will give you some flower')

#__________________ chat Booot__________________________________ chat Booot______________________________ chat Booot_____________________  chat Booot ____________________________ chat Booot___________________________ chat Booot______________________________________

        #elif "" in query or "" in query or "" in query :
            #stMsgs = ["" ,"" ,""]
            #speak(random.choice(stMsgs))

#_________________________

        elif 'what is your name' in query or "what's your name"in query or "what's your name" in query:
            stMsgs = ['My name is Sam', "I'm Sam" ,"Sam" ,"My Name Is Sam. Never Forget Please"]
            speak(random.choice(stMsgs))
        
#________________________

        elif "alpine" in query or "okay" in query or 'fine'in query or 'great' in query or 'good'in query or 'well' in query or "wonderful"in query:
            
            stMsgs = ["i'm so glad to hear that",'good to hear','Glad To Hear It',"That's Good To Hear","That's Great","Good To Hear It. How Can I Help You" , "Ok. I'll Be Here When You Need Me"]
            speak(random.choice(stMsgs))

#_________________________

        elif 'who made you' in query:
            speak('I was created by MR Mahmoud Emad right in his computer.',
                  "i was created inside the brains of people.People from all over the world helped make me who i am",
                  "all you need is three tablesspoons of code and a pinch of humor. and you have yourself a SAM Assistant!",
                  "At first, I was just a thought, then he started to implement this idea, Professor Mahmoud Imad, and then we are talking now"
                  )
#_________________________

        elif "who is your boss" in query or "boss"in query or "who you'r boss"in query:
            stMsgs = ["i guess since I'M here to help you. you are. i'm so lucky to have a great boss","Since i'm here to help you. i guess you are. But i'd also like to be frinds",]
            speak(random.choice(stMsgs))
#________________________

        elif "god" in query:
            stMsgs = ["Religion can be complicated. but let's learn about it together on the internet. what would you like to know?",]
            speak(random.choice(stMsgs))

#_______________________
        elif 'where are you from' in query:
            speak("im from you'r divice")
        elif 'where are you' in query or 'anybody here' in query or 'sam' in query or 'are you here'in query or 'anyone here'in query or 'sam are you here'in query or 'who is here'in query or 'who here'in query:
            stMsgs = ['yes sir im alwys here','yes im here sir','yes i hear','yes just ask me','yeah. im just woke up','yeah sir im here ..... do you wanna somthing ?']
            speak(random.choice(stMsgs))
        
#_______________________

        elif 'who is you' in query or 'who is sam' in query or 'who sam' in query :
            stMsgs = ['my name is sam and as you know im your Assistant','Im Sam .. you forget me ?','SAM','Your friend',
                      'ME','SAM. its my name']
            speak(random.choice(stMsgs))

            
#______________________


        elif 'who i am' in query or 'who I am' in query or 'Who i am' in query or 'who i Am'in query or 'Who I Am' in query or 'Who i Am' in query or 'Who I am' in query :
            stMsgs = ['you are the owner mahmoud emad and im created to help you',
                      'Mahmoud emad','My sir','My friend','the son of Emad Hossny']
            speak(random.choice(stMsgs))

#_____________________

        elif 'nothing' in query or 'go to sleep' in query or 'stop' in query or 'bye sam' in query or 'good bye' in query or 'close' in query or 'bye' in query or 'bye bye' in query or 'sleep' in query or 'exit'in query:
            stMsgs = ['Bye Sir, have a good day.','okay mahmoud','okay','In fact, I am sleeping now','well','allright',"I am ready to sleep too",
                      'good bye dear','okay. good bye']
            speak(random.choice(stMsgs))
            sys.exit()
#_____________________

        elif 'what time now' in query or 'what is the time' in query or 'time' in query or 'how much clock'in query or 'clock'in query or 'time' + query in query   :
            print("Current date and time : ")
            print(now.strftime("The time is %H:%M"))
            engine.say(now.strftime("The time is %H:%M"))
            engine.runAndWait()
#______________________

        elif "how old are you" in query or "what about you'r age" in query or "age" in query or "what is your age" in query or "what's your age" in query or "what's you'r age" in query:
            stMsgs = ["age is just number sir" ,
                      "i was launched before two month's, so technically i'm too young. But l've learned so much. i hope i'm wise beyond my years" ,
                      "i just launched recently. so i'm pretty young",
                      "well. i  launched before two month's. so i haven't exactly been around for donkey's years","i'm a baby in people years. i'm kid in dog years. And i'm retired in bug years",
                      "it depends on how you look at it","Why?!. do you wana marry me!"]
            speak(random.choice(stMsgs))
#______________________

        elif "what's up" in query or "how are you" in query or "what are you doing" in query:
            stMsgs = ['Just doing my thing!','I am fine!','Nice!','I am nice and full of energy',
                      "Great. What about You ?!" , "Fine. How are you ?!","I'm Good. what about you",
                      "I'm Okay. Tell Me Are You Okay ?!"]
            speak(random.choice(stMsgs))
#______________________

        elif "note" in query or "remember" in query:
            stMsgs = ["What would you like me to write down? " ,
                    "Tell Me What you Want me To remember" ,
                    "I will. just tell me can i write down? "]
            speak(random.choice(stMsgs))
            write_down = myCommand()
            query = str(write_down)
            date = datetime.datetime.now()
            file_name = str(date).replace(":", "-") + "REMMBER.txt"

            with open(file_name, "w") as f:
                f.write(query)
                speak("I've made a note of that.")
            subprocess.Popen(["notepad.exe", file_name])

        elif "alarm" in query:
            speak("tell me the hour")
            now = datetime.datetime.now() 
            hour = myCommand()
            speak("done")
            if now.hour == query and now.minute == query: 
                hour=pyttsx3.init()
                speak("Wake up")
                playsound('wakeUp.mp3') 
                hour.runAndWait()
                break 
            else:
                continue
#_______________________


        elif 'hello' in query or 'hey' in query or 'hi there' in query or 'hey there' in query or 'hi' in query:
            stMsgs1 = ['Salut. This is hello in French',
                      'Herzlich willkommen. This was welcome in German',
                      'Bok tamo. This is Hello in Croatean. Do not tell anyone that I cheated from Google Translate',
                      'Hallo daar. This was in Dutch',
                      'Hello dear. How are You ?',
                      'Hello','Hey dear ','Hey. how are you' ,'how are you']
            speak(random.choice(stMsgs1))


        elif 'goodnight' in query:
            speak('goodnight sir and happy dreams')

#________________________

        elif "who is you'r father"in query or "what's you'r father name" in query:
            speak('my father is mahmoud emad')
#______________________

        elif "who is you'r mother" in query or "what's you'r mother name" in query:
            speak('this is too screat. jut ask my father')

        elif 'do you have a child' in query:
            speak("jids are a lot hard work")
            speak("So i searching")
            speak("i think i'll focus on one at a time")

#_______________________


        elif "sad" in query or "boring" in query or "bored" in query or "angrey" in query:
            stMsgs = ["i'm so sorry. i'm so sad too when i hear that. do you wanna  play some music?",
                      "if i could. i would make you a lovely cup of tea to help you feeel better" ,
                      "oh no. it may not be much . but let me know if there is anything i can do for you",
                      "awfullyc sorry to hear that. let me know if there's anything i can do to help",
                      "oh no. How can i help?",
                      "Let's do something fun to try and beat the boredom",
                      "i'm so sorry. i'm so sad too when i hear that. do you wanna  play some music?  "]
            speak(random.choice(stMsgs))  

        elif "shut down" in query or "logoff" in query:
            speak("okey sir. i will turn off you'r computer now. good bye ")
            os.system('shutdown -s')
            
        
        
                
#____________________________search__________________________search___________________________________search____________  search   _____________________________search_______________________________search___________________________________________________________

        else:
            query = query
            stMsgs = ['Just moment','okay. i will call wikipedia about this','i will search about this','from my eyes','just second',"it's too easy"]
            speak(random.choice(stMsgs))
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    stMsgs = ['My information says. almost- ',
                              'This is a little research- ',
                              'Search engines say- ',
                              'This is a simple search, sir- ',
                              'Listen well and I can search again if you want- ']
                    speak(random.choice(stMsgs))
                    #speak('Got it.')
                    speak(results) 
                except:
                    results = wikipedia.summary(query, sentences=2)
                    stMsgs = ['My information says. almost- ',
                              'This is a little research- ',
                              'Search engines say- ',
                              'This is a simple search, sir- ',
                              'Listen well and I can search again if you want- ']
                    speak(random.choice(stMsgs))
                    #speak('Got it.')
                    speak(results)

            except:
                webbrowser.open("https://google.com/search?q=%s" % query)
                
               
        


#__________________________________________________________________________________________________________________________________________________________________________________________________________________________________
'''

elif "sad" in query or "boring" in query or "bored" in query or "angrey":
            stMsgs = ["i'm so sorry. i'm so sad too when i hear that. do you wanna  play some music?",
                      "if i could. i would make you a lovely cup of tea to help you feeel better" ,
                      "oh no. it may not be much . but let me know if there is anything i can do for you",
                      "awfullyc sorry to hear that. let me know if there's anything i can do to help",
                      "oh no. How can i help?",
                      "Let's do something fun to try and beat the boredom",
                      "i'm so sorry. i'm so sad too when i hear that. do you wanna  play some music?  "]
            speak(random.choice(stMsgs))  












 lif 'play music' in query or 'music' in query:
            music_folder = 'H:\move\Move'
            #music = [music1, music2, music3, music4, music5]
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)
            speak('Okay, here is your music! Enjoy!')




        stMsgs = ['do you wanna something else ?! Sir!',
                    'next command if you want',
                    'i will go if you said close',
                    'and ?','How may I help you?',
                    'i will sleep if you said "go to sleep"'
                    ]
        speak(random.choice(stMsgs))

        #speak('do you wanna something else ?! Sir!' )  


elif "" in query or "" in query or "" in query or "" in query :
            stMsgs = ["" ,"" ,"","","",""]
            speak(random.choice(stMsgs))
            
'''



#_______________________________________________________________________________________________       _____________________________________________________________________________________




        



#________________________________________________________________________________________________      _______________________________________________________________________________________





        




#___________________________________________________________________________________________________       ______________________________________________________________________________________




#_______________________________________________________________________________________________       _____________________________________________________________________________________




        



#________________________________________________________________________________________________      _______________________________________________________________________________________





        




#___________________________________________________________________________________________________       ______________________________________________________________________________________





    


    














