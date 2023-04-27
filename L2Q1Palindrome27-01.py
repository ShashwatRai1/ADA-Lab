mytext=input("Enter the String")
l=len(mytext)
stat=1
x=0
y=l-1
while(x<y):
    if(mytext[x]==mytext[y]):
        x=x+1
        y=y-1
    else:
        stat=0
        break
if(stat==1):
    print("string is palindrome")
else:
    print("string is not palindrome")