# Basically convert a string of roman characters to number.
def roman_to_integer(romans) -> int:
        values = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
        total = 0
        for i in range(1,len(romans)):
            if values[romans[i-1]]<values[romans[i]]:
                total-=values[romans[i-1]]
            else:
                total+=values[romans[i-1]]
        return total+values[romans[-1]]

if __name__ == "__main__":
    case1 = "III"
    case2 = "LVIII"
    case3 = "MCMXCIV"

    print ("OUTPUT:\n")
    print (f"{case1} is equal to: {roman_to_integer(case1)}")
    print (f"{case2} is equal to: {roman_to_integer(case2)}")
    print (f"{case3} is equal to: {roman_to_integer(case3)}")