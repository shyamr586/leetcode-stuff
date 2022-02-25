# Basically, check if one string is present in other and return which index value it starts. -1 if not there.

def checker(haystack,needle):

    for i in range(len(haystack)-len(needle)+1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1

if __name__ == '__main__':
    haystack1 = "haystack"
    needle1 = "stack"
    haystack2 = "leetcode"
    needle2 = "fun"
    haystack3 = "sitting idle (fun)"
    needle3 = "fun"

    print (f"\n{needle1} is present in {haystack1} from index {checker(haystack1,needle1)}")
    print (f"{needle2} is present in {haystack2} from index {checker(haystack2,needle2)}")
    print (f"{needle3} is present in {haystack3} from index {checker(haystack3,needle3)}\n")