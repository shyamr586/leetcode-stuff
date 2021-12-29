# this is p common in interviews so i thought why not
# there are normal naive approaches to do in O(n) time but there are cooler ways too
# there is two approaches to this:

# if we dont need the order of the string when we return it, then:

def unordered(original):
    return "".join(set(original))

def ordered(original):
    return "".join(dict.fromkeys(original))



if __name__ == "__main__":
    case1 = "Hello"
    case2 = "WWWWWWWWoooooooooorrrrrrrrllllllllddddd"
    case3 = "- Shyam R"
    print ("UNORDERED RESULTS:\n")
    print (unordered(case1))
    print (unordered(case2))
    print (unordered(case3))
    print ("\n")
    print ("ORDERED RESULTS:\n")
    print (ordered(case1))
    print (ordered(case2))
    print (ordered(case3))
