from youtube_transcript_api import YouTubeTranscriptApi
from keyboard import press,press_and_release
import pyperclip
from time import sleep
# Get the clipboard data


def GetTranscript():
    clipboard_data=""
    for i in range(5):
        press("f6")
        sleep(2)
        press_and_release("ctrl + c")
        
        sleep(1)
        
        clipboard_data = pyperclip.paste()
        if  "https://www.youtube.com/watch?" in  clipboard_data:
            break
        else:
            sleep(1)
    
    url = clipboard_data.split("https://www.youtube.com/watch?v=")[1].split("&")[0]
    try:
        new=""
        for i in YouTubeTranscriptApi.get_transcript(url,languages=("en","ur")):
            new+=i["text"]
        print(new)
        return new
    except:
        return None
#sleep(5)
#print(GetTranscript())