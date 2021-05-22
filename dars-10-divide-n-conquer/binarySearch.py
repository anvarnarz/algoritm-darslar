def binarySearch(array,value,start=0,end=None):
    if end is None:
        end = len(array)-1
    if start>end:
        return None
    
    mid = (start+end)//2
    if array[mid]==value:
        return mid
    elif array[mid]>value:
        return binarySearch(array,value,start,mid-1)
    else:
        return binarySearch(array,value,mid+1,end)
    return None
    
if __name__ == '__main__':
    array = [1,5,10,22,45,78,92,99]
    print(binarySearch(array,22))