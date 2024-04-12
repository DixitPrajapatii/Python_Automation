from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

def get_driver():
    # set option to make browser easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("http://automated.pythonanywhere.com//login")
    return driver

def clean_text(text):
    """ Extract only the temparature from text """
    output = text.split(": ")
    return output[1]

def main():
    driver = get_driver()
    time.sleep(2)   # adding sleep time because element is not found initially after loading the page. it is taking sometime to fetch the value.
    driver.find_element(by="id", value="id_username").send_keys("automated")
    time.sleep(2)
    driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
    time.sleep(2)
    driver.find_element(by="xpath",value="/html/body/nav/div/a").click()
    print(driver.current_url)
    time.sleep(2)
    
print(main())
