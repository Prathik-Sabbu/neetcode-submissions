class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sets = set(nums)
        max_val = 0
        res = 0
        
        for i in nums:
            if (i - 1) not in sets:
                count = 0
                while (i + count in sets):
                    res += 1
                    count += 1

                max_val = max(max_val, res)
                res = 0
                
        return max_val