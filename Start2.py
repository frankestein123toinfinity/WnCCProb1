#!python3.6
spam = ['apples', 'bananas', 'tofu', 'cats']
print(spam[0],end='')
for i in range(1, len(spam)-1,1):
    print(", "+spam[i],end='')
if(len(spam)!=1):
    print(" & " +spam[len(spam)-1])

while True:
    print("Enter to exit :P")
    response = input()
    if response!="headerfilemagma":
        sys.exit()
