import time, random, sys, math, requests
from selenium import webdriver

driver = webdriver.Chrome()  #Accessing Root File
driver.get('http://www.google.com/');
search_box = driver.find_element_by_name('q')
search_box.send_keys('COD Liver Oil')
search_box.submit()
while True:
    print("Enter to exit :P")
    response = input()
    if response!="headerfilemagma":
        driver.quit()
        sys.exit()
