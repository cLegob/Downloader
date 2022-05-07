from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui as pg
import time

filename = input("filename: ")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.file.io/")

driver.find_element(By.XPATH, value ='//*[@id="top"]/header/div/div[2]/div[1]/div[2]/label').click()

time.sleep(1)
for x in range(6):
    pg.press("tab")

time.sleep(1)
pg.typewrite("desktop")

pg.press("enter")

time.sleep(1)
for x in range(2):
    pg.press("tab")
    
pg.press("down")
pg.press("up")
pg.press("enter")
    
time.sleep(1)
pg.typewrite(filename)

pg.press("enter")

time.sleep(1)

driver.find_element(By.XPATH, value='//*[@id="top"]/header/div/div[2]/div[1]/div[2]/div/button').click()
print(driver.find_element(By.XPATH, value='//*[@id="download-url"]').text)
driver.close()
