import time, sys, math, requests, bs4
from selenium import webdriver
from selenium.webdriver.common.touch_actions import TouchActions


driver = webdriver.Chrome()  #Accessing Root File, ChromeDriver

#Opening Artist Page
driver.get('http://www.lyricsondemand.com/e/eminemlyrics/')
res = requests.get('http://www.lyricsondemand.com/e/eminemlyrics/')

#Status of response
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' %(exc))

bSobject = bs4.BeautifulSoup(res.text, "html.parser")

elems = bSobject.find_all('.Highlight')
print(elems[0].getText())

while True:
    print("Enter to exit :P")
    response = input()
    if response!="headerfilemagma":
        driver.quit()
        sys.exit()
