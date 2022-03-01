'''
Return the most frequent item of the array. 
'''
from collections import Counter
def majority_element(nums):
    counter_obj = Counter(nums)
    return counter_obj.most_common()[0][0]

if __name__ == "__main__":
    nums1 = [1,2,3,1,3,4,2,1]
    nums2 = [2,2,2,2,2]
    nums3 = [9,9,3,10,7,10,9]

    print (f"{majority_element(nums1)} is the majority element in {nums1}")
    print (f"{majority_element(nums2)} is the majority element in {nums2}")
    print (f"{majority_element(nums3)} is the majority element in {nums3}")