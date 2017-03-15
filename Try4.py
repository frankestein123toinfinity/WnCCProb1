import requests, bs4, time
from selenium import webdriver
#Comment to test Git
driver = webdriver.Chrome()
driver.get('http://www.lyricsondemand.com/p/pinkfloydlyrics/comfortablynumblyrics.html')
res = requests.get('http://www.lyricsondemand.com/p/pinkfloydlyrics/comfortablynumblyrics.html')

noStarchSoup = bs4.BeautifulSoup(res.text, "html.parser")
pElems = noStarchSoup.select('.lcontent')
print(pElems[0].getText())

time.sleep(5)
