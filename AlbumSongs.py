import time, sys, math, requests, bs4
from bs4 import BeautifulSoup

def statusofResponse(res):
    try:
        res.raise_for_status()
    except Exception as exc:
        print('There was a problem: %s' %(exc))

res_album = requests.get("http://www.lyricsondemand.com/a/adelelyrics/19albumlyrics.html")
statusofResponse(res_album)
bsAlbumObject = bs4.BeautifulSoup(res_album.text, "html.parser")
elems_Album = bsAlbumObject.find_all(class_="lcontent")
print(elems_Album[0].getText())

while True:
    print("Enter to exit :P")
    response = input()
    if response!="headerfilemagma":
        driver.quit()
        sys.exit()
