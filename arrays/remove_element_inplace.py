# Given an array, remove the occurancce of a specified element throughout the array, in-place.

def remove_inplace(arr,val):
    arr[:] = [x for x in arr if x!=val]
    return arr

if __name__ == '__main__':
    arr1 = [2,3,4,3,5]
    val1 = 3
    arr2 = [10,10,10,2,3]
    val2 = 10
    arr3 = [7,0,9,1,5]
    val3 = 0

    print(f"Removing {val1} from {arr1} gives {remove_inplace(arr1,val1)}")
    print(f"Removing {val2} from {arr2} gives {remove_inplace(arr2,val2)}")
    print(f"Removing {val3} from {arr3} gives {remove_inplace(arr3,val3)}")