#pip install pyttsx3
import pyttsx3
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


id=r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\IVONA 2 Voice Brian22"


engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 175)
engine.setProperty('voice', id)


def Speak(*args, **kwargs):
    audio = ""
    for i in args:
        audio += str(i)
    print(Fore.CYAN+audio)
    engine.say(audio)
    engine.save_to_file(audio,"temp//ms.wav")
    engine.runAndWait()
