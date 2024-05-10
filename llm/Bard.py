from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pathlib
import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import warnings
from bardapi import BardCookies
from PIL import ImageGrab
from pyautogui import sleep
from time import time as t
warnings.simplefilter('ignore')
ScriptDir = pathlib.Path().absolute()
url = "https://bard.google.com"
options = uc.ChromeOptions()
options.add_argument('--profile-directory=Default')
options.add_argument(f'--user-data-dir={ScriptDir}\\chromedata')
options.add_argument("--headless=new")
driver = uc.Chrome(options=options)
driver.maximize_window()
driver.get(url=url)
cookies = driver.get_cookies()
cookie_dict={}
# Print the extracted cookies
for cookie in cookies:
    cookie_dict[cookie["name"]]=cookie["value"]
bard = BardCookies(cookie_dict=cookie_dict)

def Bard(prompt:str):
    return bard.get_answer(prompt)['content']

def BardImage(prompt,img=None):
    if img==None:
        ImageGrab.grab().save(r"temp/temp.png")
        img=r"temp/temp.png"
    image = open(img, 'rb').read()
    bard_answer=bard.ask_about_image(prompt,image)
    return bard_answer['content']

if __name__=="__main__":
    while 1:
        i=input(">>> ")
        C=t()
        print(Bard(i))
        print(t()-C)