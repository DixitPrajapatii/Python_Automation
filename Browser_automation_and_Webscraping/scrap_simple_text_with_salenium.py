from selenium import webdriver
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
    driver.get("http://automated.pythonanywhere.com")
    return driver

def clean_text(text):
    """ Extract only the temparature from text """
    output = text.split(": ")
    return output[1]

def main():
    driver = get_driver()
    time.sleep(2)   # adding sleep time because element is not found initially after loading the page. it is taking sometime to fetch the value.
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
    return clean_text(element.text)
    
print(main())
