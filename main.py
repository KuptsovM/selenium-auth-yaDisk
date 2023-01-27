import sys

from selenium.webdriver.common.by import By

from settings import *
from selenium import webdriver

def authDrChrome():
    driver = webdriver.Chrome()
    return driver

def run():
    driver = authDrChrome()
    try:

        driver.get(DISK_URL)
        try:
            driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/button').click()
            driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[1]/div[1]/button').click()
            driver.find_element(By.XPATH, '//*[@id="passp-field-login"]').send_keys(YANDEX_LOGIN)
            driver.find_element(By.XPATH, '//*[@id="passp:sign-in"]').click()

        except Exception as e:
            print(e)




    except Exception as e:
        print(e)



if __name__ == "__main__":
    run()
