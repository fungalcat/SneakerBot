from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import time
from random import randint
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from re import sub

driver = webdriver.Chrome()
driver.get("https://www.footlocker.com/product/jordan-retro-12--mens/30690301.html")


try:
    size_select = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/div[5]/div/div[2]/div[2]/div/form/div[2]/div[2]/div/fieldset/div/div[6]/div/div/label/span"))
    )
except:
	pass
size_select.click()
    
