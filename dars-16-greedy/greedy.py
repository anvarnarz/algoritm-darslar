# Greedy algorithms
# Ochko'z algorimtlar
import pickle
from pprint import pprint as print

# Ma`lumotlarni o'qiymiz
with open('binolar.dat','rb') as file:
    binolar = pickle.load(file)
    hududlar = pickle.load(file)
    
# print(binolar)

# Greedy algorithm
yakuniy_binolar = set()
while hududlar:    
    best_bino = None
    qamralgan_hududlar = set()
    for bino, bino_qamrovi in binolar.items():
        qamrov = hududlar & bino_qamrovi
        print(f"{bino}:{qamrov}")
        if len(qamrov)>len(qamralgan_hududlar):
            best_bino = bino
            qamralgan_hududlar = qamrov        
    hududlar -= qamralgan_hududlar
    yakuniy_binolar.add(best_bino)
    print(f"Tanlangan bino: {best_bino}")
    print(f"Qolgan hududlar: {hududlar}")
    print(f"Tanlangan binolar:{yakuniy_binolar}")
    input()

# for key in yakuniy_binolar:
    # print(binolar[key])
    