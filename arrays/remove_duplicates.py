# Given an ascending array with duplicates, like [0,0,0,0,0,1,1,2,2,3,3,3,3,4], change the array in place
# and return the length of the non repeating numbers.

from os import remove


def remove_duplicates(nums):
    x = 0
    for i in range(1,len(nums)):
        if nums[x]!=nums[i]:
            x+=1
            nums[x] = nums[i]
        i+=1
    return nums,len(nums[:x+1])

if __name__=='__main__':
    arr1 = [0,0,0,0,0,1,1,2,2,3,3,3,3,4]
    arr2 = [0,0,1,1,1,2,2,3,3,4]
    arr3 = [0,4,4,4,4,8,8]

    list1,len1 = remove_duplicates(arr1)
    list2,len2 = remove_duplicates(arr2)
    list3,len3 = remove_duplicates(arr3)

    print(f"The array {arr1} serted gives:\n\n\tList:{list1} \n\tLength:{len1}\n")
    print(f"The array {arr2} serted gives:\n\n\tList:{list2} \n\tLength:{len2}\n")
    print(f"The array {arr3} serted gives:\n\n\tList:{list3} \n\tLength:{len3}\n")