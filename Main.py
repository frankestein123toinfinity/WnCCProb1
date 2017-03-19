from Module import *
import sys, math

singer_dict = {}
singer_list = []

print("The site I have used has sensored cuss words")
print("For Eg. fuck is written as f*ck and so on. Shit has not been censored.")
wordSearch = input("Keeping this in mind, Enter Cuss word to Be Searched(in Lower Case):")
print("Provide No. of Artists followed by their Names:")
n = int(input())

for i in range(0,n):
     singer = input()
     singer_list.append(singer)

for i in range(0,n):
     singer_dict[wordCount(singer_list[i], wordSearch)] = singer_list[i]

for key in sorted(singer_dict, reverse=True):
    print("%s: %s" % (key, singer_dict[key]))

while True:
    print("Enter to exit :P")
    response = input()
    if response!="headerfilemagma":
        sys.exit()
