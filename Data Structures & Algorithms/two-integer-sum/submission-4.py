class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            second = target - nums[i]
            if second in hashmap:
                return [hashmap[second], i]
            hashmap[nums[i]] = i
