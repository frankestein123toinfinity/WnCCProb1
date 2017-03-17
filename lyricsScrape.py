import time, sys, math, requests, bs4
from selenium import webdriver
from selenium.webdriver.common.touch_actions import TouchActions

driver = webdriver.Chrome()  #Accessing Root File

driver.get('http://www.lyricsondemand.com/p/passengerlyrics/lethergolyrics.html')
res = requests.get('http://www.lyricsondemand.com/p/passengerlyrics/lethergolyrics.html')
noStarchSoup = bs4.BeautifulSoup(res.text, "html.parser")
print(type(noStarchSoup))
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' %(exc))

elems = noStarchSoup.select('.lcontent')
print(elems[0].getText())

while True:
    print("Enter to exit :P")
    response = input()
    if response!="headerfilemagma":
        driver.quit()
        sys.exit()
