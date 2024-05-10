from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pathlib
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import warnings
from time import time as t
warnings.simplefilter('ignore')
ScriptDir = pathlib.Path().absolute()
url = "https://chat.openai.com/"


# Use undetected_chromedriver
options = uc.ChromeOptions()
options.add_argument('--profile-directory=Default')
options.add_argument(f'--user-data-dir={ScriptDir}\\chromedata')
#options.add_argument("--headless=new")
#driver = webdriver.Chrome(options=options)
driver = uc.Chrome(options=options)
driver.maximize_window()
driver.get(url=url)

def ChatGpt(query,link:str=""):
    C=t()
    prompt_element=driver.find_element(By.ID,"prompt-textarea")

    prompt_element.clear()
    prompt_element.send_keys(query)
    prompt_element.send_keys(Keys.ENTER)
    sleep(1)
    while 1:
        try:
            sleep(0.1)
            driver.find_element(By.XPATH,'//*[@id="__next"]/div[1]/div[2]/main/div[2]/div[2]/form/div/div/div/button').click()
            break
        except :
            pass
    driver.find_elements(By.CLASS_NAME,"markdown")[-1].click()
    A=driver.find_elements(By.CLASS_NAME,"markdown")[-1].text
    while 1:
        sleep(0.1)
        if driver.find_elements(By.CLASS_NAME,"markdown")[-1].text==A:
            break
        else:
            A=driver.find_elements(By.CLASS_NAME,"markdown")[-1].text
    print(t()-C)
    return A

if __name__=="__main__":
    while 1:
        A=input(">>> ")+"***use python programing language. just write complete code nothing else***"
        C=t()
        print(ChatGpt(A))
        print(t()-C)