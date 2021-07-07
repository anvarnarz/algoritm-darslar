from random import sample
hududlar = set(range(1,31))
binolar = {
    'B01':set(sample(hududlar,3)), 
    'B02':set(sample(hududlar,4)),
    'B03':set(sample(hududlar,4)),
    'B04':set(sample(hududlar,5)),
    'B05':set(sample(hududlar,5)),
    'B06':set(sample(hududlar,3)),
    'B07':set(sample(hududlar,2)),
    'B08':set(sample(hududlar,5)),
    'B09':set(sample(hududlar,4)),
    'B10':set(sample(hududlar,3)),
    'B11':set(sample(hududlar,5)),
    'B12':set(sample(hududlar,2)),
    'B13':set(sample(hududlar,3)),
    'B14':set(sample(hududlar,5)),    
}

x=[]
for bino in binolar.values():
    for value in bino:
        x.append(value)
x=set(x)

binolar['B15']=hududlar-x
if __name__ == '__main__':
    import pickle
    with open('binolar.dat','wb') as file:
        pickle.dump(binolar,file)
        pickle.dump(hududlar,file)
