from random import randrange
def qsort(array):
    if len(array)<2:        
        return array
    else:
        # pivot = array.pop(0)
        pivot = array.pop(randrange(len(array)))        
        kichik = [i for i in array if i<=pivot]
        katta = [i for i in array if i>pivot]
        # print(f"{kichik}+[{pivot}]+{katta}")
        return qsort(kichik) + [pivot] + qsort(katta)

if __name__ == '__main__':
    # array1 = [1, 5, 12, 0, -5, 66]
    # print(array1)
    # print(qsort(array1))
    array2 = list(range(20))
    print(array2)
    print(qsort(array2))
    array3 = ['olma', 'anjir', 'shaftoli', 'qovun', 'tarvuz']
    print(qsort(array3))