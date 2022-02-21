# Not a leetcode problem, but can be asked in interviews.
# Given a list with duplicate and non-duplicate values, return a dictionary with key as the element of array and
# value as the number of occurances.

import collections


def usingCollections(arr):
    count_obj = collections.Counter(arr)
    return count_obj
    # this returns a coutner object which is a dict subclass.
    # if dictionary is strictly needed and not a subset, use dict(count_obj)

def usingKeys(arr):
    dict1 = {}
    for elem in arr:
        if elem in dict1.keys():
            dict1[elem]+=1
        else:
            dict1[elem]=1
    return dict1

def usingIn(arr):
    dict1 = {}
    for elem in arr:
        if elem in dict1:
            dict1[elem]+=1
        else:
            dict1[elem]=1
    return dict1

def usingGet(arr):
    dict1 = {}
    for elem in arr:
        dict1[elem] = dict1.get(elem,0) + 1
    return dict1

if __name__ == "__main__":
    arr = [1,1,1,1,1,1,2,3,2,2,3,3,4,5,5]
    print (f"The result using 'collections' is: {usingCollections(arr)}\n")
    print (f"The result using 'keys' is: {usingKeys(arr)}\n")
    print (f"The result using 'in' is: {usingIn(arr)}\n")
    print (f"The result using 'get' is: {usingGet(arr)}\n")