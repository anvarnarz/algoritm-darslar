def summa(array):
    if array == []:
        return 0
    return array[0]+summa(array[1:])

if __name__ == '__main__':
    array = [10,20,30,40,50]
    print(summa(array))