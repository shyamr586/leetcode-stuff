''' 
Given a string of characters like "A", "B", return the number of the column.

    A -> 1
    B -> 2
    ...
    Z -> 26
    AA -> 27
    ...
    ZY -> 701
'''

# NOTE: the answer for this needed some thinking, there is no calculations.
def calculate_column(columnTitle):
    title = columnTitle[::-1]
    answer = 0
    
    for i in range(0,len(title)):
        
        asci = ord(title[i])-64
        answer+= asci*(26**i) 
        
    return answer

if __name__ == "__main__":
    title1 = "A"
    title2 = "ZY"
    title3 = "FXSHRXW"

    print (f"The column number for title {title1} is: {calculate_column(title1)}")
    print (f"The column number for title {title2} is: {calculate_column(title2)}")
    print (f"The column number for title {title3} is: {calculate_column(title3)}")