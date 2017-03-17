import time, random, sys, math, requests
from selenium import webdriver

driver = webdriver.Chrome()  #Accessing Root File
driver.get('https://automatetheboringstuff.com/files/rj.txt')
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' %(exc))
while True:
    print("Enter to exit :P")
    response = input()
    if response!="headerfilemagma":
        driver.quit()
        sys.exit()
