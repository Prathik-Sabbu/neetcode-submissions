class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)
        res = right

        while left <= right:
            mid = (left + right) // 2
            
            tot_hours = sum(math.ceil(p / mid) for p in piles)

            if tot_hours <=  h:
                res = mid
                right = mid - 1

            else:
                left = mid + 1

        return res