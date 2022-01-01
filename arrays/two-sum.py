# Given an array and target, we gotta return the index of the two elements in array that sums to target

def solution_using_dictionary(arr,target):
    dictionary = {}
    for index,element in enumerate(arr):
        if target-element in dictionary:
            return [dictionary[target-element],index]
        else:
            dictionary[element] = index
    return -1

if __name__ == "__main__":

    arr1 = [2,7,11,15]
    target1 = 9
    arr2 = [3,2,4]
    target2 = 6
    arr3 = [3,3]
    target3 = 6

    print ("OUTPUT:\n")
    print (f"{target1} can be found in {arr1} in index positions: {solution_using_dictionary(arr1,target1)}")
    print (f"{target2} can be found in {arr2} in index positions: {solution_using_dictionary(arr2,target2)}")
    print (f"{target3} can be found in {arr3} in index positions: {solution_using_dictionary(arr3,target3)}")
    