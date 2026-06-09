class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        max_profit = 0
        i = 0
        j = i+1
        min_bp = prices[i]

        while j < n:
            if min_bp > prices[j]:
                min_bp = prices[j]
                i=j
                j=i+1
            else:
                max_profit = max(max_profit,prices[j] - min_bp)
                j+=1

            

        return max_profit
                