#! /home/gonzalo/RR/Programas/Rival-Regions/RR_Selm/tutorial-env/bin/python3
from __future__ import print_function
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from helper import initDriverOption, rs

pageUrl = "https://quizlet.com/explanations/textbook-solutions/electrical-engineering-principles-and-applications-6th-edition-9780133116649"

if __name__ == '__main__':
    # Get local data    
    options = initDriverOption()    # import options from helperfunction
    driver = webdriver.Firefox(options=options) #  initializing driver  

    # Code execution
    driver.set_window_position(0, 0)
    driver.set_window_size(770, 1100)
    print("Make sure your browser is zoomed out to 80%")

    while True:
        print("Extractin a exercise!")
        # Going to the page and clicking away coockies. 
        driver.get(pageUrl)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//button[@id="onetrust-accept-btn-handler"]'))).click()
        # input("Choose which exercise to copy, press enter when you are ready! ")
        while True:
            if "problems" in driver.current_url:
                print("we have a problem")
                break
        exerURL = driver.current_url
        # Clicking on sign in with email 
        driver.find_element(By.XPATH,"//button[@aria-label='Sign up with email']").click()

        # ------------ Filling form ------------
        # Fills the birth month
        driver.find_element(By.XPATH,"//select[@aria-label='birth_month']").click()
        driver.find_element(By.XPATH,"//option[@value=2]").click()

        # Fills the birth day
        driver.find_element(By.XPATH,"//div/select[@aria-label='birth_day']").click()
        driver.find_element(By.XPATH,"//div/select[@aria-label='birth_day']/option[2]").click()
        
        # Fills the birth year
        driver.find_element(By.XPATH,"//div/select[@aria-label='birth_year']").click()
        driver.find_element(By.XPATH,"//div/select[@aria-label='birth_year']/option[2]").click()

        # Fills mail, password and username
        mail = driver.find_element(By.XPATH,"//input[@id='email']")
        mail.send_keys(rs(10) + "@gmail.com")

        username = driver.find_element(By.XPATH,"//input[@id='username']")
        username.send_keys(rs(10))

        password = driver.find_element(By.XPATH,"//input[@id='password1']")
        password.send_keys(rs(12))

        # Pressing accept terms of service
        driver.find_element(By.XPATH,"//input[@name='TOS']").click()

        time.sleep(2)


        driver.find_element(By.XPATH,"//button[@type='submit']").click()

        while True:
            if driver.current_url == pageUrl:
                driver.get(exerURL)
                break
        print("Gonig back")
        option = input("Next action:\nq     | quit \nenter | continue\n> ")
        if option == 'q':
            break
        
        # Deleting cookies, reseting and loggin out of the page
        driver.delete_all_cookies()
        
    driver.close()
    driver.quit()

    








