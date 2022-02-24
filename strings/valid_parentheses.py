'''
The problem asks to return true if all the open brackets, i.e, (,[,{ are closed and the closing brackets are in
order.

Example:

    (] -> not valid
    {[()]} -> valid because the last open braces is closed first
    () -> also valid
'''

def validityChecker(s):
    if len(s)%2!=0:
        return False
    dict1 = {"(":")","{":"}","[":"]"}
    
    stack = []
    
    for char in s:
        if char in dict1:
            stack.append(dict1[char])
        else:
            if stack == [] or char != stack.pop():
                return False
    return not stack

if __name__ == "__main__":
    s1 = "(]"
    s2 = "{[()]}"
    s3 = "()"

    print (f"Is {s1} a valid parantheses?: {validityChecker(s1)}")
    print (f"Is {s2} a valid parantheses?: {validityChecker(s2)}")
    print (f"Is {s3} a valid parantheses?: {validityChecker(s3)}")
