'''
We have to check if the given number is a happy number. A happy number will equate the square of its digits
to 1. If it does not, the number is not a happy number and at a point the sum of squares of the digits will loop.

Example:

19
Pass 1: 1^2 + 9^2 = 82
Pass 2: 8^2 + 2^2 = 68
Pass 3: 6^2 + 8^2 = 100
Pass 4: 1^2 + 0^2 + 0^2 = 1 => Happy number.

2
Pass 1: 4
Pass 2: 16
Pass 3: 37
Pass 4: 58
Pass 5: 89
Pass 6: 145
Pass 7: 42
Pass 8: 20
Pass 9: 4 => Not happy number because pass 1 had same result
'''

def is_happy_my_solution(n):
    arr = []
    total = 0
    while total not in arr:
        total = helper(n)
        
        if total == 1:
            return True
        
        arr.append(n)
        n=total
    return False


def helper(num):
    s = 0
    for elem in str(num):
        s += int(elem)**2
    return s

def is_happy_cooler_looking_solution(n):
    mem = set()
    while n != 1:
        n = sum([int(i) ** 2 for i in str(n)])
        if n in mem:
            return False
        else:
            mem.add(n)
    else:
        return True

if __name__ == "__main__":
    n1 = 19
    n2 = 2
    n3 = 70
    n4 = 98
    n5 = 1

    print(f"\nIs {n1} a happy number? {is_happy_cooler_looking_solution(n1)}")
    print(f"Is {n2} a happy number? {is_happy_cooler_looking_solution(n2)}")
    print(f"Is {n3} a happy number? {is_happy_cooler_looking_solution(n3)}")
    print(f"Is {n4} a happy number? {is_happy_my_solution(n4)}")
    print(f"Is {n5} a happy number? {is_happy_my_solution(n5)}\n")