import time, sys, math, requests, bs4
from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome()     #Unnecessary bt Meh...


#Test for Singer
def removeSpace(string):
    string = string.lower()
    string = string.replace(' ', '')
    return string

singer = "Adele"                    #input('Enter Singer:' )
#Obtain URL of Singer and store
singer = removeSpace(singer)
url_singer = 'http://www.lyricsondemand.com/' + singer[0] + '/' + singer + 'lyrics'

#Opening Artist Page
res = requests.get(url_singer)

def statusofResponse(res):
    try:
        res.raise_for_status()
    except Exception as exc:
        print('There was a problem: %s' %(exc))

#Status of response
statusofResponse(res)

#Beautiful Soup object
bsObject = bs4.BeautifulSoup(res.text, "html.parser")

#Try to find all elements that point to the artist's albums
#Use this to access complete lyrics list
#Only problem being find_all not returning all elements... Ye bas ho jaaye BC

elems = bsObject.find_all(class_='fullalbm')
album = []
for i in range (0,len(elems)):
    album.append(elems[i].getText())

#erase all instances of /n
for i in range (0,len(album)):
    album[i] = removeSpace(album[i])
    album[i] = album[i].replace("lyrics","")

album = [item.strip() for item in album if str(item)]

url_singer_Album = []

for i in range (0,len(album)):
    url_singer_Album.append(url_singer + "/" + album[i] + "album" + "lyrics.html")

wordSearch="He"
counter = 0


for i in range (0, len(album)):
    print(url_singer_Album[i])
    res_album = requests.get(url_singer_Album[i])
    statusofResponse(res_album)
    bsAlbumObject = bs4.BeautifulSoup(res_album.text, "html.parser")
    elems_Album = bsAlbumObject.find_all(class_="lcontent")
    lyrics = elems_Album[0].getText()
    print(lyrics)


while True:
    print("Enter to exit :P")
    response = input()
    if response!="headerfilemagma":
        driver.quit()
        sys.exit()
