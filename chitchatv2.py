from datetime import datetime
import openai
import pyttsx3
import speech_recognition as sr
from api_key import API_KEY


openai.api_key = API_KEY

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

r = sr.Recognizer()
mic = sr.Microphone(device_index=1)


say = ""
you = "You"
bot = "Assistant"

while True:
    with mic as source:
        print("\nlistening...")
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)
    print("no longer listening.\n")

    try:
        user_input = r.recognize_google(audio)
    except:
        continue

    prompt = you + ": " + user_input + "\n" + bot+ ": "

    if "exit" in user_input:
        break
    elif "who are you" in user_input:
        engine.say("I am Chip chat, a Chat bot Created in Python by D Zeus. I am based off of GPT-3 and is currently limited.")
        engine.runAndWait("I am Chip chat, a Chat bot Created in Python by D Zeus. I am based off of GPT-3 and is currently limited.")
        print()
    elif "what time" in user_input:
        current_time_now = datetime.now()
        current_time = current_time_now.strftime("%H:%M")
        engine.say("The time in the Philippines today is: "+ current_time)
        engine.runAndWait()
        print("The time in the Philippines today is: "+ current_time)
    elif "what date" in user_input:
        current_date_now = datetime.now()
        current_date = current_date_now.strftime("%m-%d-%Y")
        engine.say("The date in the Philippines today is: "+ current_date)
        engine.runAndWait()
        print("The date in the Philippines today is: "+ current_date)
    else:
        say += prompt  # allows for context

        # OPENAI API
        response = openai.Completion.create(engine='text-davinci-003', prompt=say, max_tokens=100)
        response_str = response["choices"][0]["text"].replace("\n", "")
        response_str = response_str.split(you + ": ", 1)[0].split(bot + ": ", 1)[0]

        say += response_str + "\n"
        print(response_str)

        engine.say(response_str)
        engine.runAndWait()