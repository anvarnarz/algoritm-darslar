import time
import pickle
from binarySearch import binary_search
from random import randint

with open('users.dat','rb') as file:
    users = pickle.load(file)
with open('usernames.dat','rb') as file:
    usernames = pickle.load(file)
with open('usersHash.dat','rb') as file:
    usersHash = pickle.load(file)
    
def findUser(user,users,usernames=usernames):
    if isinstance(users,list):
        indeks = binary_search(usernames,user)
        return users[indeks]
    else:
        return users[user]

#  List binary search
n=1000000 # 
tic = time.time()
for i in range(n):
    user = usernames[randint(0,len(usernames)-1)]
    findUser(user,users)
toc = time.time()
print('Binary search vaqti: ', (toc-tic)/n)

# Hash tables
tic = time.time()
for i in range(n):
    user = usernames[randint(0,len(usernames)-1)]
    findUser(user,usersHash)
toc = time.time()
print('Hash jadval vaqti: ', (toc-tic)/n)