#%%
def step(n):
    if (n<0):
        return 0
    elif (n==0):
        return 1
    elif (n==1):
        return 1
    elif(n==2):
        return 2
    else:
        return (step(n-3)+step(n-2)+step(n-1))

n=4
print(step(n))
# %%
