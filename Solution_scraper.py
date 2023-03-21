#! /home/gonzalo/RR/Programas/Rival-Regions/RR_Selm/tutorial-env/bin/python3
from __future__ import print_function
import random
import string
import time
from selenium.webdriver.common.by import By
from multiprocessing.connection import wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from helper import initDriverOption
import keyboard

def rs(length):
    """
    Generate a random string of a given length.
    
    Args:
        length (int): The desired length of the string.
    
    Returns:
        A random string of the specified length.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))


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
    # Fills the birth month
    driver.find_element(By.XPATH,"//select[@aria-label='birth_month']").click()
    driver.find_element(By.XPATH,"//option[@value=2]").click()

    # Fills the birth year
    driver.find_element(By.XPATH,"//div/select[@aria-label='birth_year']").click()
    driver.find_element(By.XPATH,"//div/select[@aria-label='birth_year']/option[25]").click()


    # Fills the birth day
    driver.find_element(By.XPATH,"//div/select[@aria-label='birth_day']").click()
    driver.find_element(By.XPATH,"//div/select[@aria-label='birth_day']/option[2]").click()

    # Fills mail, password and username
    mail = driver.find_element(By.XPATH,"//input[@id='email']")
    mail.send_keys(rs(10) + "@gmail.com")

    username = driver.find_element(By.XPATH,"//input[@id='username']")
    username.send_keys(rs(10))

    password = driver.find_element(By.XPATH,"//input[@id='password1']")
    password.send_keys(rs(10))

    # Pressing accept terms of service
    driver.find_element(By.XPATH,"//input[@name='TOS']").click()

    time.sleep(2)


    driver.find_element(By.XPATH,"//button[@type='submit']").click()


    time.sleep(2)
    driver.execute_script("window.history.go(-1)")
    
    input("Contine...")
    # Code end routine
    driver.close()
    driver.quit()

    








