class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        res = 1
        dic = set(nums)
        minimum = min(nums)
        max_val = 0
        
        for i, num in enumerate(nums):
            print(dic, minimum, max_val, res)
            if minimum + 1 in dic:
                res += 1
                dic.discard(minimum)
                minimum += 1

            else:
                max_val = max(max_val, res)
                res = 1
                dic.discard(minimum)
                minimum = min(dic) if dic else 0

        return max_val