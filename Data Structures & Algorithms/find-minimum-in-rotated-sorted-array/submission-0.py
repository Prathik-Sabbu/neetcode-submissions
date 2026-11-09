class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = float('inf')
        left, right = 0, len(nums) - 1

        while left <= right:
            res = min(nums[left], nums[right], res)

            left += 1
            right -= 1
        
        return res

        