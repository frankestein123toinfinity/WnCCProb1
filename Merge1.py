import time, sys, math, requests, bs4
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.touch_actions import TouchActions

#Test for One Singer
string = "eminem"               #input('Enter Singer:' )
string = string.lower()
string = string.replace(' ', '')
#Obtain URL of Singer and store
url_singer = 'http://www.lyricsondemand.com/' + string[0] + '/' + string + 'lyrics'

driver = webdriver.Chrome()  #Accessing Root File, ChromeDriver

#Opening Artist Page
res = requests.get(url_singer)

#Status of response
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' %(exc))

bSobject = bs4.BeautifulSoup(res.text, "html.parser")
#Try to find all elements that point to the artist's albums
#Use this to access complete lyrics list
#Only problem being find_all not returning all elements... Ye bas ho jaaye BC 

elems = bSobject.findAll(class_="fullalbm", limit =50, recursive=True)
print(elems[0].getText())
elems1 = elems.find_all_next(class_="fullalbm")
print(elems1[0].getText())

while True:
    print("Enter to exit :P")
    response = input()
    if response!="headerfilemagma":
        driver.quit()
        sys.exit()
