import time, random, sys, math, requests, bs4
from selenium import webdriver

driver = webdriver.Chrome()  #Accessing Root File
res = requests.get('http://www.lyricsfreak.com/print.php?id=153716')
noStarchSoup = bs4.BeautifulSoup(res.text, "html.parser")
print(type(noStarchSoup))
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' %(exc))

elems = noStarchSoup.select('pre')
print(elems[0].getText())
while True:
    print("Enter to exit :P")
    response = input()
    if response!="headerfilemagma":
        driver.quit()
        sys.exit()
