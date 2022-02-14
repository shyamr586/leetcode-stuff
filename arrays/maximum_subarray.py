# Given an array, return the max value of a subarray present in original array.

def classic_kadanes_algorithm(arr):
    max_all_time = 0
    max_current = 0
    for element in arr:
        max_current = max(max_current + element, element)
        max_all_time = max(max_current,max_all_time)
    return max_all_time

# problem with this is that it manipulates the original array
def easy_to_understand_kadanes(arr):
    for i in range(1,len(arr)):
        if arr[i-1]>0:
            arr[i]+=arr[i-1]
    return max(arr)


if __name__ == "__main__":

    case1 = [-2,1,-3,4,-1,2,1,-5,4]
    case2 = [1]
    case3 = [5,4,-1,7,8]

    print("OUTPUT USING CLASSIC:\n")
    print(f"{case1}'s maximum subarray is: {classic_kadanes_algorithm(case1)}")
    print(f"{case2}'s maximum subarray is: {classic_kadanes_algorithm(case2)}")
    print(f"{case3}'s maximum subarray is: {classic_kadanes_algorithm(case3)}\n")
    
    print("OUTPUT USING OTHER ONE:\n")
    print(f"{case1}'s maximum subarray is: {easy_to_understand_kadanes(case1)}")
    print(f"{case2}'s maximum subarray is: {easy_to_understand_kadanes(case2)}")
    print(f"{case3}'s maximum subarray is: {easy_to_understand_kadanes(case3)}")