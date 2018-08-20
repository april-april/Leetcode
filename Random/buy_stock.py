def maxProfit(prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) == 0:
            return None

        minimum_price = prices[0]
        max_profit = 0

        for stock in range(1, len(prices)):
            profit = prices[stock] - minimum_price
            max_profit = max(profit, max_profit)
            minimum_price = min(stock, minimum_price)

        return max_profit

def main():
    testArray = [10, 9, 4, 5, 1, 20, 14]
    answer = maxProfit(testArray)
    print(answer)

main()
