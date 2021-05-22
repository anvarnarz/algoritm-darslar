a,b,c=20,8,10

def addNums(a,b):
    summa = a + b
    return summa

def getLargest(a,b,c):
    if a>b:
        if a>c:
            return a
        else: 
            return c
    else:
        if b>c:
            return b
        else:
            return c

print(getLargest(-5,6,22/5))

def faktorial(N):
    i=1
    fakt=1
    while i!=N+1:
        fakt = fakt*i        
        i += 1
    return fakt

print(faktorial(5))