#! /home/gonzalo/RR/Programas/Rival-Regions/RR_Selm/tutorial-env/bin/python3
from __future__ import print_function

import datetime
import os
import json
import time
from selenium.webdriver.common.by import By
from multiprocessing.connection import wait
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from helper import initDriverOption
import keyboard


if __name__ == '__main__':
    # Get local data    
    options = initDriverOption()    # import options from helperfunction
    driver = webdriver.Firefox(options=options) #  initializing driver  

    # Code execution
    driver.set_window_position(0, 0)
    driver.set_window_size(770, 1100)
    driver.get("https://quizlet.com/explanations/textbook-solutions/electrical-engineering-principles-and-applications-international-edition-6th-edition-9780273793250") # The website we want to go to

    input("Choose which exercise to copy")
    
    #Clicking on sign in with email 
    print("Doing suff")
    driver.find_element(By.XPATH,"//button[@aria-label='Sign up with email']").click()

    # Filling form
    
    driver.find_element(By.XPATH,"//select[@aria-label='birth_month']").click()
    driver.find_element(By.XPATH,"//option[@value=2]").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//select[@aria-label='birth_day']").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//option[@value=2]").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//select[@aria-label='birth_year']").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//option[@value=2]").click()
    input("Choose which exercise to copy")
    # Code end routine
    driver.close()
    driver.quit()

    








