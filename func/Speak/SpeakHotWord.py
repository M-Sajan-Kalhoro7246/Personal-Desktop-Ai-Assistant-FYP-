#pip install pyttsx3
import pyttsx3
import colorama
from threading import Thread
from func.Listen.ListenJs import Listen
import pygame
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


id=r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\IVONA 2 Voice Brian22"


engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 175)
engine.setProperty('voice', id)


IS_HOT_WRD=False
HOT_WORD_DECT_IS_ON=False

def HOT_WORD_DECT():
    global IS_HOT_WRD,HOT_WORD_DECT_IS_ON
    while 1:
        if HOT_WORD_DECT_IS_ON:
            A=Listen(PRINT=False).lower()
            if "jarvis" in A:
               if HOT_WORD_DECT_IS_ON:
                IS_HOT_WRD=True
                return
               else:
                   pass
        else:
            return


def Speak(*args, **kwargs)->None:
    global IS_HOT_WRD,HOT_WORD_DECT_IS_ON

    HOT_WORD_DECT_IS_ON=True
    Thread(target=HOT_WORD_DECT).start()

    audio = "".join(args)

    print(Fore.CYAN+audio)
    engine.save_to_file(audio,r"temp//data.wav")
    engine.runAndWait()

    try:
        pygame.mixer.init()
        pygame.mixer.music.load(r"temp//data.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
            if IS_HOT_WRD:
                IS_HOT_WRD=False
                break
    except Exception as e:
        print(e)
    finally:
        HOT_WORD_DECT_IS_ON=False
        pygame.mixer.music.stop()
        pygame.mixer.quit()


