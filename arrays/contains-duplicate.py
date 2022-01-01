# Check if there is a duplicate number in the list.
# return True if  duplicate.
def duplicate_checker(arr):
    return len(arr)!=len(set(arr))

if __name__ == "__main__":
    case1= [1,2,3,1]
    case2= [1,2,3,4]
    case3= [1]

    print("OUTPUT\n")
    print(f"For {case1}: {duplicate_checker(case1)}")
    print(f"For {case2}: {duplicate_checker(case2)}")
    print(f"For {case3}: {duplicate_checker(case3)}")