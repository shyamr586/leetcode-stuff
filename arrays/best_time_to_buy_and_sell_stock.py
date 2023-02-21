# Basically, there is an array of prices where the value of that index is the price of that index.
# We have to find the maximum profit we could get by buying on the day with least price and selling with most price
# after buying it.

def using_kadanes_algorithm(prices):
    maxCur = 0
    maxAll = 0
    for i in range (1,len(prices)):
        maxCur = max(0,prices[i]-prices[i-1]+maxCur)
        maxAll = max(maxCur,maxAll)
    return maxAll

def using_sliding_window(prices):
    left,right = 0,1
    maxAll = 0

    while right<len(prices)-1:
        if prices[left]<prices[right]:
            maxCurr = prices[right]-prices[left]
            maxAll = max(maxAll,maxCurr)
        else:
            left=right
        right+=1
    return maxAll

if __name__ == "__main__":

    case1 = [7,1,5,3,6,4]
    case2 = [7,6,4,3,1]

    print("OUTPUT USING KADANES ALGO:\n")
    print(f"Prices: {case1}, max profit: {using_kadanes_algorithm(case1)}")
    print(f"Prices: {case2}, max profit: {using_kadanes_algorithm(case2)}\n")
    print("OUTPUT USING SLIDING WINDOW:\n")
    print(f"Prices: {case1}, max profit: {using_sliding_window(case1)}")
    print(f"Prices: {case2}, max profit: {using_sliding_window(case2)}\n")