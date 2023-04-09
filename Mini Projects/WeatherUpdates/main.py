import requests
import json
import pyttsx3
e = pyttsx3.init()
e.say("enter city to find the current temperature: ")
e.runAndWait()
c=input("enter city to find the current temperature: ")
e.say(c)
e.runAndWait()
url=f'https://api.weatherapi.com/v1/current.json?key=229410641fee48c784a22154230304&q={c}'
r=requests.get(url)
# print(r.text)
wdic=json.loads(r.text)
print(wdic["current"]["temp_c"])
e.say(f'The current weather of {c} is {wdic["current"]["temp_c"]}')
e.runAndWait()