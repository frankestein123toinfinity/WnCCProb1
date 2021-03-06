import time, sys, math, requests, bs4
from bs4 import BeautifulSoup


def removeSpace(string):            #Used to remove SPace and convert to lowercase
    string = string.lower()
    string = string.replace(' ', '')
    return string

def statusofResponse(res):          #Name is obvious :P
    try:
        res.raise_for_status()
    except Exception as exc:
        print('There was a problem: %s' %(exc))


def wordCount(singer, wordSearch):
    #Obtain URL of Singer and store
    singer = removeSpace(singer)
    url_singer = 'http://www.lyricsondemand.com/' + singer[0] + '/' + singer + 'lyrics'

    res = requests.get(url_singer)      #Opening Artist Page

    statusofResponse(res)           #Status of response

    bsObject = bs4.BeautifulSoup(res.text, "html.parser")   #Beautiful Soup object

    #Try to find all elements that point to the artist's albums
    #Use this to access complete lyrics list
    #find_all returns all elements in different index, was
    #having problems with it, now A.OKAY!

    elems = bsObject.find_all(class_='fullalbm')
    album = []
    for i in range (0,len(elems)):
        album.append(elems[i].getText())

    #Make album text usable in URL
    for i in range (0,len(album)):
        album[i] = removeSpace(album[i])        #Removes Spaces
        album[i] = album[i].replace("lyrics","")        #Removes lyrics keyword in Album part
        album[i] = album[i].replace("album","")        #Removes album keyword in Album part

    album = [item.strip() for item in album if str(item)]       #Removes all instances of /n in album

    url_singer_Album = []       #list containing URLS of ALbums

    for i in range (0,len(album)):
        url_singer_Album.append(url_singer + "/" + album[i] + "album" + "lyrics.html")

    counter = 0         #No. of Occurences

    for i in range (0, len(album)):
        res_album = requests.get(url_singer_Album[i])
        statusofResponse(res_album)
        bsAlbumObject = bs4.BeautifulSoup(res_album.text, "html.parser")
        elems_Album = bsAlbumObject.find_all(class_="lcontent")
        lyrics = elems_Album[0].getText()           #String in which Lyrics are stored
        lyrics = lyrics.lower()
        counter += lyrics.count(wordSearch)

    return counter
