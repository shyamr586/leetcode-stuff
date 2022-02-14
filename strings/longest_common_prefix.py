def longest_common_prefix(strs):
    shortest = min(strs,key=len)

    for i in range(len(shortest)):
        for word in strs:
            if word[i]!=shortest[i]:
                return shortest[:i]
        
    return shortest

if __name__ == "__main__":
    case1 = ["flower","flow","flight"]
    case2 = ["dog","racecar","car"]
    case3 = ["a"]

    print ("OUTPUT:\n")
    print(f"Longest common substring for {case1} is {longest_common_prefix(case1)}")
    print(f"Longest common substring for {case2} is {longest_common_prefix(case2)}")
    print(f"Longest common substring for {case3} is {longest_common_prefix(case3)}")