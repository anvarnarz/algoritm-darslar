from tqdm import tqdm
from faker import Faker
# from pprint import pprint as print
import pickle

fake = Faker()

users_hash = {}
usernames = []
n = 10_000_000
for i in tqdm(range(n)):
    user = fake.profile()
    username = user['username']
    
    usernames.append(username)
    users_hash[username] = user

usernames = list(set(usernames))
usernames.sort()
users = []
for username in usernames:
    users.append(users_hash[username])


with open('usernames.dat','wb') as file:
    pickle.dump(usernames,file)
with open('users.dat','wb') as file:
    pickle.dump(users,file)
with open('usersHash.dat','wb') as file:
    pickle.dump(users_hash,file)