class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        stack = []
        profit = 0
        test = 0

        for i in prices:
            if not stack:
                stack.append(i) 
                test = i

            if test > i:
                while stack:
                    stack.pop()
                test = i

            stack.append(i)
            profit = max(profit, stack[-1] - test)

        return profit