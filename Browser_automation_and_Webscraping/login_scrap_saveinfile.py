from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time as t
from datetime import datetime

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
    temp_value = float(text.split(": ")[1])
    return temp_value

def write_file(content):
    """write text into the text file """
    # full_time = datetime.today()        # to get the full datetime
    # date ,time = full_time.date(),full_time.time()   
    # date = ''.join(str(date).split("-"))   # splitting and joining again to get value like 130424 (without -)
    # the above one is manually doing date separation and the below is using date module

    file_name  = f'{datetime.now().strftime("%Y-%m-%d-%H%M%S")}.txt'   #using date module 
    with open(f'E://Python_Automation//Resouces//data//{file_name}', 'w') as file:   #opening file with filename
        file.write(str(content))    #writing the content 
        file.close()

def main():
    driver = get_driver()
    t.sleep(1)   # adding sleep time because element is not found initially after loading the page. it is taking sometime to fetch the value.
    driver.find_element(by="id", value="id_username").send_keys("automated")
    t.sleep(1)
    driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
    t.sleep(2)
    driver.find_element(by="xpath",value="/html/body/nav/div/a").click()
    t.sleep(2)
    # text = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]").text
    # temp = clean_text(text)
    
    for i in range(5):          # to specify how many files you want to create
        text = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]").text
        t.sleep(2)
        temp = clean_text(text)
        write_file(temp)
        
print(main())
