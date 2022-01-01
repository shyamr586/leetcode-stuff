# Return an array where the index of the array must be the multiplication of every other element of the original.

def product_of_array_except_self(arr):
    prefix,postfix = 1,1
    output = [1]*len(arr)

    for i in range(len(arr)):
        output[i] *= prefix
        prefix *= arr[i]

    for i in range(len(arr)-1,-1,-1):
        output[i] *= postfix
        postfix *= arr[i]

    return output

if __name__ == "__main__":
    case1= [2,9,24,3]
    case2= [1,2,3,4]
    case3= [-1,1,0,-3,3]

    print("OUTPUT\n")
    print(f"{case1}: {product_of_array_except_self(case1)}")
    print(f"{case2}: {product_of_array_except_self(case2)}")
    print(f"{case3}: {product_of_array_except_self(case3)}")

    