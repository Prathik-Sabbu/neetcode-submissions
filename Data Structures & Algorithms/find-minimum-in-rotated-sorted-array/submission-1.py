class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        res = float('inf')

        while left <= right:
            mid = (left + right)//2
            res = min(res, nums[mid])

            if  nums[left] < nums[mid]:
                res = min(res, nums[left])
                left = mid + 1
            elif nums[right] < nums[mid]:
                res = min(res, nums[right])
                right = mid - 1
            else:
                left += 1
            
            

        return res
                

        