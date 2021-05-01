def sana(n):
    print(n)    
    if n<=1:
        return
    else:
        sana(n-1)

sana(10)