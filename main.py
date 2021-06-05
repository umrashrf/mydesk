import time

from pathlib import Path

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains


def main():
    secure_id = input("RSA Secure ID: ")

    option = Options()
    #options.add("--headless")
    
    driver = webdriver.Chrome(options=option, executable_path=Path("chromedriver").absolute())
    
    try:
        driver.get("http://mydesk.morganstanley.com")
        
        time.sleep(0.5)

        loginform = driver.find_element_by_xpath("//form[@name='loginForm']")

        username = driver.find_element_by_xpath("//form[@name='loginForm']//input[@name='login']")
        username.send_keys("")

        password = driver.find_element_by_xpath("//form[@name='loginForm']//input[@name='passwd']")
        password.send_keys("")

        secureid = driver.find_element_by_xpath("//form[@name='loginForm']//input[@name='passwd1']")
        secureid.send_keys("" + secure_id)
        
        loginform.submit()

        download_button = driver.find_element_by_xpath("//a[contains(text(), 'Hosted Workstation')]")
        download_button.click()

        time.sleep(15)
    except:
        driver.close()
        raise

if __name__ == '__main__':
    main()
