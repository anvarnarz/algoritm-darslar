def findNum(N=10):
    for n in range(1,N):
        ans = input(f"Siz {n}-o'yladingiz? (y/n)")
        if ans=='y':
            print("Yutdim!")
            return n

findNum(10)