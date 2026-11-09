class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        check = []
        left = 0
        right = len(nums)-1

        nums = sorted(nums)

        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[left] + nums[right] + nums[i]
                if total < 0:
                    left += 1
                
                elif total > 0:
                    right -= 1
                
                else:
                   result.add(tuple(sorted([nums[right], nums[left], nums[i]])))
                   left += 1 
                   right -= 1
                
        
        return list(result)

        