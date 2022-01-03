def two_pointer_technique(x):
    s = str(x)
    l = 0
    r = len(s)-1
    while l<r:
        if s[l]!=s[r]:
            return False
        l+=1
        r-=1
    return True

#if slicing can be done and extra memory is fine,
def slicing_technique(x):
    return str(x)==str(x)[::-1]

#if int cannot be converted to str, we can reverse the int by using reminders and adding them like the loop given:
def reverse_integer_technique(original):
    copy = original
    reversed_num = 0
    while copy>0:
        reversed_num = reversed_num*10 + copy%10
        copy//=10
    return original==reversed_num

if __name__ == '__main__':
    case1 = 121
    case2 = -121
    case3 = 10
    case4 = 420024

    print ("OUTPUT USING TWO POINTER\n")
    print (f"{case1} is a palindrome. True or false? {two_pointer_technique(case1)}")
    print (f"{case2} is a palindrome. True or false? {two_pointer_technique(case2)}")
    print (f"{case3} is a palindrome. True or false? {two_pointer_technique(case3)}")
    print (f"{case4} is a palindrome. True or false? {two_pointer_technique(case4)}\n")

    print ("OUTPUT USING SLICING\n")
    print (f"{case1} is a palindrome. True or false? {slicing_technique(case1)}")
    print (f"{case2} is a palindrome. True or false? {slicing_technique(case2)}")
    print (f"{case3} is a palindrome. True or false? {slicing_technique(case3)}")
    print (f"{case4} is a palindrome. True or false? {slicing_technique(case4)}\n")
    
    print ("OUTPUT BY REVERSING INT\n")
    print (f"{case1} is a palindrome. True or false? {reverse_integer_technique(case1)}")
    print (f"{case2} is a palindrome. True or false? {reverse_integer_technique(case2)}")
    print (f"{case3} is a palindrome. True or false? {reverse_integer_technique(case3)}")
    print (f"{case4} is a palindrome. True or false? {reverse_integer_technique(case4)}\n")