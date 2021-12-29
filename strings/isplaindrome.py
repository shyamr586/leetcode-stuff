# This is to check if the given string is a palindrome
# for this one we are removing characters that are not alphabets or digits.
# im showing two solutions which can be memorized fairly easily

def two_pointer_technique(original):
    left,right = 0,len(original)-1
    
    #almost all two pointer techniques has this condition, dont forget:
    while left<right:

        if not original[left].isalnum():
            left+=1
        
        elif not original[right].isalnum():
            right-=1

        else:
            if original[left].lower()!=original[right].lower():
                return False
            
            else:
                left+=1
                right-=1

    return True

# The memory in this is O(n) but its easy to understand.

def generator_comprehension(original):
    s = "".join(char.lower() for char in original if char.isalnum())
    return s==s[::-1]

if __name__ == "__main__":

    case1 = "A man, a plan, a canal: Panama"
    case2 = "race a car"
    case3 = " "

    print("TWO POINTER TECHNIQUE:\n")
    print(f"1. {case1} : ",two_pointer_technique(case1))
    print(f"2. {case2} : ",two_pointer_technique(case2))
    print(f"3. {case3} : ",two_pointer_technique(case3),"\n")

    print ("GENERATOR COMPREHENSION:")
    print(f"1. {case1} : ",generator_comprehension(case1))
    print(f"2. {case2} : ",generator_comprehension(case2))
    print(f"3. {case3} : ",generator_comprehension(case3))