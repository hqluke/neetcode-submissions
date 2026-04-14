class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # use two pointers but have them start on the left side
        # calc smallest buy and largest profit eacn time
        maxProfit = 0
        smallestBuy = prices[0]
        for num in prices:
            smallestBuy = min(smallestBuy, num)
            maxProfit = max(maxProfit, num - smallestBuy)
        return maxProfit
        