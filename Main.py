from Module import *
import sys, math

singer_dict = {}
singer_list = []

print("The site I have used has sensored cuss words")
print("For Eg. fuck is written as f*ck and so on. Shit has not been censored.")
print("Keeping this in mind, Enter Cuss word to Be Searched(in Lower Case):")
wordSearch = input()
wordSearch = wordSearch.lower()
print("Provide No. of Artists followed by their Names:")
n = int(input())

for i in range(0,n):
     singer = input()
     singer_list.append(singer)

for i in range(0,n):
     singer_dict[wordCount(singer_list[i], wordSearch)] = singer_list[i]
print("")
print("Final Result:")
print("")

for key in sorted(singer_dict, reverse=True):
    print("%s with %s %ss" % (singer_dict[key], key, wordSearch ))

print("")

while True:
    print("Enter to exit :P")
    response = input()
    if response!="headerfilemagma":
        sys.exit()
