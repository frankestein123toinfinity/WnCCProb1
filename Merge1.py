import time, sys, math, requests, bs4
from selenium import webdriver
from selenium.webdriver.common.touch_actions import TouchActions

#Test for One Singer
string = input('Enter Singer:' )
string = string.lower()
string = string.replace(' ', '')
print(string)
#Obtain URL of Singer and store
url_singer = 'http://www.lyricsondemand.com/' + string[0] + '/' + string + 'lyrics'

driver = webdriver.Chrome()  #Accessing Root File, ChromeDriver

#Opening Artist Page
driver.get(url_singer)
res = requests.get(url_singer)

#Status of response
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' %(exc))

bSobject = bs4.BeautifulSoup(res.text, "html.parser")
#Try to find all elements that point to Songs by Artist
#Next open in New Tab, Scrape for lyrics, find no of matches, close tab and switch to next Tab
#Plan Uptil now....
elems = bSobject.select('.fullalbm')
print(elems[0].getText())

while True:
    print("Enter to exit :P")
    response = input()
    if response!="headerfilemagma":
        driver.quit()
        sys.exit()
