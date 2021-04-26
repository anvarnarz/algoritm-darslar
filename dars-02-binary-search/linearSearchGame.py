def findNum(N=100):
    for n in range(1,100):
        ans = input(f"Siz {n}-o'yladingiz? (y/n)")
        if ans=='y':
            print("Yutdim!")
            return n

findNum(10)