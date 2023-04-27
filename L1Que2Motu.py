n=10
motu=0
a=0
b=0
count=0
i=1
while(i<=n):
    a=i
    b=2*i
    i=i+1
    if (count+a+b>=n):
        if(count+a>=n):
            print("patlu")
        else:
            print("Motu")
        break
    count=count+a+b