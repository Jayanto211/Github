# text to speech program

import pyttsx3 # install pyttsx3 library for text to speech

if __name__ == '__main__':
    command=pyttsx3.init()
    print("Welcome to Text to Speech Program or Press (q) To Quit")
    while True:
        x=input("Enter The Word To Pronounce : ")
        if x=="q":
            command.say("bye bye see you later")
            command.runAndWait()
            break
        command.say(x)
        command.runAndWait()