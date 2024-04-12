# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time 

# def get_driver():
#     # set option to make browser easier
#     options = webdriver.ChromeOptions()
#     options.add_argument("disable-infobars")
#     options.add_argument("start-maximized")
#     options.add_argument("disable-dev-shm-usage")
#     options.add_argument("no-sandbox")
#     options.add_experimental_option("excludeSwitches", ["enable-automation"])
#     options.add_argument("disable-blink-features=AutomationControlled")

#     driver = webdriver.Chrome(options=options)
#     driver.get("https://www.google.com/")
#     return driver


# def main():
#     driver = get_driver()
#     driver.find_element(by="xpath", value="/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea").send_keys("gmail login" + Keys.RETURN)
#     time.sleep(2)
    
# print(main())

from datetime import datetime

# full_time = datetime.today()
# date ,time = full_time.date(),full_time.time()
# # print(time.hour)
# # print(time.minute)
# # print(time.second)
# date = ''.join(str(date).split('-'))
# print(date)

print(datetime.now().strftime("%Y-%m-%d-%H%M%S"))