#Importing req libs .......
import speech_recognition as sr
import wikipedia
import pyttsx3
import pywhatkit
import pyjokes
import requests, json , sys
import datetime

def engine_talk(text):
    engine.say(text)
    engine.runAndWait()

listener = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)
   
def weather(city):
    # API key
    api_key = "a0f651da4e2011e572e8389f7f18c76f"
   
    # url
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    city_name = city
   
    # complete web url
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
   
    # return response object
    response = requests.get(complete_url)
   
    # json format
    x = response.json()
   
    # Now x contains list of nested dictionaries
    # Check the value of "cod" key is equal to
    # "404", means city is found otherwise,
    # city is not found
    if x["cod"] != "404":
   
        # store the value of "main"
        # key in variable y
        y = x["main"]
   
        # store the value corresponding
        # to the "temp" key of y
        current_temperature = y["temp"]
        ##similarly it can give various info    
        ##current_humidiy = y["humidity"]
   
        return str(current_temperature)



def user_commands():
    try:
        with sr.Microphone() as source:
            print("Waiting for your command, please say!!")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'google' in command:
                command = command.replace('google', '')
                print(command)
    except:
        pass
    return command
   
   
def run_google():
    command = user_commands()
    if 'play' in command:
        song = command.replace('play', '')
        engine_talk('Playing' +song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        engine_talk('The current time is' +time)
    elif 'who is' in command:
        name = command.replace('who is' , '')
        info =  wikipedia.summary(name, 1)
        print(info)
        engine_talk(info)

    elif 'what is' in command:
        name = command.replace('what is' , '')
        info =  wikipedia.summary(name, 1)
        print(info)
        engine_talk(info)
    elif 'about' in command:
        name = command.replace('about' , '')
        info =  wikipedia.summary(name, 1)
        print(info)
        engine_talk(info)
    elif 'joke' in command:
        engine_talk(pyjokes.get_joke())
    elif 'fun' in command:
        engine_talk(pyjokes.get_joke())
    elif 'weather' in command:
        engine_talk('which city you look for')
        city = user_commands()
        weather_api = weather(city)
        engine_talk(weather_api + 'degree fahreneit' )

    elif 'stop' in command:
        sys.exit()
    else:
        engine_talk('I could not hear you properly, please try again')
       
       
while True:
    run_google()
