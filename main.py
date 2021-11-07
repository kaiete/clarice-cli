# clarice cli v0.1
# (c) 2021 kaiete
# MIT license
import requests
import json

name = None
while True:
    print("> ", end="")
    msg = input().lower()
    if "hello" in msg or "hi" in msg:
        if name == None:
            print("hello there!")
        else:
            print("hello there, " + name + "!")
    elif "goodbye" in msg or "bye" in msg or "cya" in msg:
        print("bye! see you later!")
        exit("clarice left the conversation")
    elif "my name is" in msg or "i'm called" in msg:
        print("hi there, " +
              msg.replace("my name is ", "").replace("i'm called ", "") +
              "! nice to meet you.")
        name = msg.replace("my name is ", "").replace("i'm called ", "")
    elif "what" in msg and "weather" in msg:
        try:
            city
        except NameError:
            print(
                "hmmm, i'm not sure where you live. to use the weather function, you'll need to tell me."
            )
            city = input("enter your city here > ")
        finally:
            weather = requests.post(
                "https://palgrave-weather.kaiete.workers.dev", city).text
            # current.condition.text
            weather = json.loads(weather)
            weather = weather["current"]["condition"]["text"]
            print("it looks like it's currently " + weather.lower() + " in " +
                  city)
    else:
        print("hmm, i'm not sure i understand")
        pass
