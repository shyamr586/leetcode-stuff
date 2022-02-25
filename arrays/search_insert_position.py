# Return the index of the target in a sorted array or index of where it would be if not found.

def binary_search(arr,val):

    l=0
    r=len(arr)-1
    mid = (l+r)//2

    while l<=r:
        if arr[mid]==val:
            return mid
        elif val>arr[mid]:
            l = mid+1
        else:
            r = mid-1
        mid = (l+r)//2
    return l                #usually we return -1 to say not found but since it asks for position of where it should
                            #be, we return the left position.

if __name__=='__main__':
    arr1 = [1,3,5,6]
    val1 = 5
    arr2 = [1,3,5,6]
    val2 = 7
    arr3 = [1,3,5,6]
    val3 = 0

    print (f"{val1} does/would occur in index {binary_search(arr1,val1)} of array {arr1}")
    print (f"{val2} does/would occur in index {binary_search(arr2,val2)} of array {arr2}")
    print (f"{val3} does/would occur in index {binary_search(arr3,val3)} of array {arr3}")