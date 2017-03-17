import time, sys

string = input('Enter Singer:' )
string = string.lower()
string = string.replace(' ', '')

print(string)

url_singer = 'http://www.lyricsondemand.com/' + string[0] + '/' + string + 'lyrics'

print(url_singer)

while True:
    print("Enter to exit :P")
    response = input()
    if response!="headerfilemagma":
        sys.exit()
