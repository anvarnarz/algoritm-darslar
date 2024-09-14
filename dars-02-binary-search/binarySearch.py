def linear_search(list, item):
    for n in range(len(list)):
        if list[n]==item:
            return n
    return None

def binary_search(list, item):
    low = 0
    high = len(list)-1
    while low <= high:
        mid = (low + high)//2
        guess = list[mid]
        if guess == item:
            return mid+1
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

# myList1 = [1,3,4,6,7,8,10,12,23,45,56,78,99]
# print(linear_search(myList1,11))
# print(binary_search(myList1,11))

# myList2 = [18,12,25,1,3,4,10,5,23,4,13,89]
# myList2.sort()
# print(linear_search(myList2,13))
# print(binary_search(myList2,13))

mevalar = ['olma','anor','olcha','behi','shaftoli','anjir']
# mevalar.sort()
print(mevalar)
print(binary_search(mevalar,'behi'))
