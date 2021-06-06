import time
import os.path
import argparse

from pathlib import Path

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from retry import retry
from gooey import Gooey

@Gooey(
    program_name='MyDesk'
)
def main():
    parser = argparse.ArgumentParser(description='MyDesk')
    parser.add_argument('secure_id', metavar='RSA SECURE ID')
    args = parser.parse_args()
    
    option = Options()
    #options.add("--headless")
    
    driver = webdriver.Chrome(options=option, executable_path=Path("chromedriver").absolute())
    
    try:
        driver.get("http://mydesk.morganstanley.com")
        
        loginform_is_visible = EC.visibility_of_element_located((By.XPATH, "//form[@name='loginForm']"))
        loginform = WebDriverWait(driver, 20).until(loginform_is_visible)

        username_is_visible = EC.visibility_of_element_located((By.XPATH, "//form[@name='loginForm']//input[@name='login']"))
        username = WebDriverWait(driver, 20).until(username_is_visible)
        username.send_keys("")

        password_is_visible = EC.visibility_of_element_located((By.XPATH, "//form[@name='loginForm']//input[@name='passwd']"))
        password = WebDriverWait(driver, 20).until(password_is_visible)
        password.send_keys("")

        secureid_is_visible = EC.visibility_of_element_located((By.XPATH, "//form[@name='loginForm']//input[@name='passwd1']"))
        secureid = WebDriverWait(driver, 20).until(secureid_is_visible)
        secureid.send_keys("" + args.secure_id)
        
        loginform.submit()
        
        download_link_is_visible = EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Hosted Workstation')]"))
        download_link = WebDriverWait(driver, 20).until(download_link_is_visible)
        download_link.click()

        waitForFile()
    except:
        raise
    finally:
        driver.close()

@retry(tries=5, delay=3)
def waitForFile():
    if not Path(os.path.expanduser("~/Downloads/launchExtMSAD.ica")).exists():
        raise FileNotFoundError


if __name__ == '__main__':
    main()
