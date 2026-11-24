class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left = 0
        maxp=0
        for right in range(1,len(prices)):
            if prices[right]>prices[left]:
                profit=prices[right]-prices[left]
                maxp=max(maxp,profit)
            else:
                left=right
        return maxp