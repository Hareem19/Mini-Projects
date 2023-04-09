# import os
# if __name__ == '__main__':
#     x = input("SAY PLEASE         ")
#     command = f"say {x}"
#     os.system(command)
import pyttsx3
engine = pyttsx3.init()
engine.say("Write plz which you want to say, I will speak for you....         \n"
           "press q for quit this conversation")
engine.runAndWait()
if __name__ == '__main__':
    while(True):
        x = input("Write plz, I will speak for you....         \n"
                  "q for quit the convo ")
        if x=="q":
            engine.say("see you soon...")
            engine.runAndWait()
            break
        elif x =="How are you?":
            engine.say("great.. how are you")
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()

