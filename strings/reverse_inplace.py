# This is a easy solution, however there is an easier solution, which is by using reversed(str) but its kind of
# like cheating. The slice is less preferred over reversed because slice creates a copy and reversed() does not.
# but, since we dont want to use shortcuts most of the time we can just use this and ignore space difference.

def slice_solution(original):
    original = original[::-1]
    print(original)

if __name__ == "__main__":

    case1 = "This is case one."
    case2 = "Case 2 here, hello"
    case3 = "weewoo weewoo"

    print("TWO POINTER TECHNIQUE:\n")
    print(f"1. {case1} : ")
    slice_solution(case1)
    print(f"\n2. {case2} : ")
    slice_solution(case2)
    print(f"\n3. {case3} : ")
    slice_solution(case3)