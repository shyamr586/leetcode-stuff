"""
Given an array of integers a, your task is to calculate the digits that occur the most number of times in the
array. Return the array of these digits in ascending order.

Example: 
For a = [25, 2, 3, 57, 38, 41], the output should be solution(a) = [2, 3, 5].

Here are the number of times each digit appears in the array:

0 -> 0
1 -> 1
2 -> 2
3 -> 2
4 -> 1
5 -> 2
6 -> 0
7 -> 1
8 -> 1
"""


def solution(a):
    a = [str(num) for num in a]
    nums = "".join(a)
    counter = {}
    
    for digit in nums:
        if digit not in counter:
            counter[digit] = 1
        else:
            counter[digit]+=1
            
    max_occured = max(counter.values())
    
    list_of_index = [int(x) for x in counter.keys() if counter[x]==max_occured]
    return sorted(list_of_index)

if __name__ == "__main__":
    array1 = [25, 2, 3, 57, 38, 41]
    array2 = [2233,321313,2234,12,31231,2445,88]
    array3 = [9999999999999999999999999999999,8,212,56,34,5]

    print (f"The array of most occuring digits in array {array1} is: {solution(array1)}")
    print (f"The array of most occuring digits in array {array2} is: {solution(array2)}")
    print (f"The array of most occuring digits in array {array3} is: {solution(array3)}")