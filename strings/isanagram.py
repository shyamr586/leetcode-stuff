import collections

# This is the easy solution, using the Counter subclass, the algo will create a hastable of 
# the characters in the string are put in a dictionary in the backend, hence O(n) time.
def is_anagram_using_counter(word1,word2):
    return collections.Counter(word1)==collections.Counter(word2)

def is_anagram_using_dictionary(word1,word2):
    dict1,dict2 = {},{}

    for char in word1:
        dict1[char] = dict1.get(char,0)+1   #basically tells either get the value if key exists or make default value
                                            #0 and add 1 to it.(if it exists, itll add one)

    for char in word2:
        dict2[char] = dict2.get(char,0)+1

    return dict1==dict2

if __name__ == "__main__":

    case1A = "anagram"
    case1B = "nagaram"
    case2A = "mile"
    case2B = "lime"
    case3A = "rat"
    case3B = "cat"

    print ("USING COUNTER:")
    print (f"{case1A} and {case1B}: ",is_anagram_using_counter(case1A,case1B))
    print (f"{case2A} and {case2B}: ",is_anagram_using_counter(case2A,case2B))
    print (f"{case3A} and {case3B}: ",is_anagram_using_counter(case3A,case3B),"\n")
    print ("USING DICTIONARIES:")
    print (f"{case1A} and {case1B}: ",is_anagram_using_dictionary(case1A,case1B))
    print (f"{case2A} and {case2B}: ",is_anagram_using_dictionary(case2A,case2B))
    print (f"{case3A} and {case3B}: ",is_anagram_using_dictionary(case3A,case3B))
