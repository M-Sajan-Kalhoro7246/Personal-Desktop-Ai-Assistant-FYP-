#pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.keys import Keys
import requests
from urllib.parse import unquote
chrome_options = webdriver.ChromeOptions()

#chrome_options.add_argument('--headless=new')
# chrome_options.headless = True
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
driver.minimize_window()

class MusicPlayer:
    global driver
    def __init__(self,VidName:str) -> None:
        self.Volume=100

        self.VidName=VidName

        self.url=unquote(self.GetVidUrl().replace('\\u0026', '&'))
        
        driver.get(self.url)
        sleep(5)
        self.PauseOrPlay()
    
    def GetVidUrl(self):
        cont = requests.get("https://www.youtube.com/results?search_query="+self.VidName.replace(" ","+"))
        count = 0
        data = cont.content
        data = str(data)
        lst = data.split('"')
        for i in lst:
            count += 1
            if i == "WEB_PAGE_TYPE_WATCH":
                break
        return f"https://www.youtube.com{lst[count - 5]}"
    
    def Vol(self,VolInt:int):
        if VolInt > 100 or VolInt < 0:
            return "MOYE MOYE"
        #50 , 100 -5
        #50 = 100 - (x * 5)
        if VolInt>self.Volume:
            #VolInt = volume + (x*5)
            #(VolInt-Volume)/5=x
            steps=(VolInt-self.Volume)//5
            self.Volume=VolInt
            video = driver.find_element(By.CLASS_NAME,"html5-video-player")
            for _ in range(steps):
                sleep(0.1)
                video.send_keys(Keys.UP)
        else:
            #VolInt = volume + (x*5)
            #(VolInt-Volume)/5=x
            steps=(VolInt-self.Volume)//-5
            self.Volume=VolInt
            video = driver.find_element(By.CLASS_NAME,"html5-video-player")
            for _ in range(steps):
                sleep(0.1)
                video.send_keys(Keys.DOWN)

    def PauseOrPlay(self):
        driver.find_element(By.CLASS_NAME,"html5-video-player").click()

    def Next(self):
        x=driver.find_element(By.CLASS_NAME,"html5-video-player")
        x.send_keys(Keys.SHIFT, 'n') 

    def Quit(self):
        driver.close()
    def Play(self):
        driver.find_element(By.CLASS_NAME,"html5-video-player").click()
    def Pause(self):
        driver.find_element(By.CLASS_NAME,"html5-video-player").click()
if __name__=="__main__":
    print("Searching..........")
    ncs=MusicPlayer("New Hindi Mashup Songs")
    ncs.Play()
    print("Starting ............")
    while 1:
        pass