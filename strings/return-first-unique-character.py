# Just like 'isanagram.py', we can do this using counter or a dictionary.
# I will be doing the counter obj only just to show how flexible it is.

# Some times, this is not acceptable because even though it can give good run time. So be careful.
from collections import Counter

def return_unique_character(word):
    countobj = Counter(word)            #although they didnt mention case sensitiveness, you can convert it to lower.
    for char in countobj:
        if countobj[char] == 1:
            return char
    return -1

if __name__ == "__main__":

    case1 = "LEETCOOODE"
    case2 = "bubberducky"
    case3 = "yoyo"

    print("TWO POINTER TECHNIQUE:\n")
    print(f"1. {case1} : ",return_unique_character(case1))
    print(f"2. {case2} : ",return_unique_character(case2))
    print(f"3. {case3} : ",return_unique_character(case3),"\n")
