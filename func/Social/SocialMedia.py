#pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless=new')
# chrome_options.headless = True
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)


media={
    "Youtube bio":["",
               '//*[@id="meta"]'],
    "Instagram live details":["",
                 "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul"]
}


def SocialTexter(website,XPATH):
    driver.get(website)
    sleep(2)
    while 1:
        try:
            A=driver.find_element(By.XPATH,XPATH).text
            return A
        except:
            print("failed . . .")

def SocialMedia():
    data=""
    for i,y in media.items():
        data+="\n"+"-"*20+"\n"
        data+=f"{i} \n"
        data+=SocialTexter(y[0],y[1])
    driver.quit()
    return data
