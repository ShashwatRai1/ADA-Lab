def power(a,b):
    if (b==0):
        return 1
    elif(b>0):
        return (a*power(a,b-1))
    else:
        return (1/(a*power(1/a,b+1)))


a=int(input("Enter base number "))
b=int(input("Enter power number"))
print(power(a,b))