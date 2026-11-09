class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        check = []
        left = 0
        right = len(nums)-1

        nums = sorted(nums)

        for i in range(len(nums)):
            value = nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if value + nums[left] + nums[right] < 0:
                    left += 1
                
                elif value + nums[left] + nums[right] > 0:
                    right -= 1
                
                else:
                   result.add(tuple(sorted([nums[right], nums[left], value])))
                   left += 1 
                   right -= 1
                
        
        return list(result)

        