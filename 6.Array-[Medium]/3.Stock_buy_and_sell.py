prices = [7, 2, 1, 5, 6, 4, 8]

#  Method - 1
def stock_and_buy(prices):
    n = len(prices)
    maxi = 0 # max profit
    for i in range(0, n):
        for j in range(i+1, n):
            if prices[j] > prices[i]:
                p = prices[j] - prices[i]
                maxi = max(maxi, p)
    return maxi
print(stock_and_buy(prices))
#  TC = O(N**2), SC = O(1)


# Method - 2
def StockAndBuy(prices):
    maxi = 0  # maxim profit
    mini = float('inf')  # minimum price
    n =len(prices)
    for i in range(0, n):
        mini = min(mini, prices[i])
        maxi = max(maxi, prices[i] - mini)
    return maxi
print(StockAndBuy(prices))
#  TC = O(N), SC = O(1)