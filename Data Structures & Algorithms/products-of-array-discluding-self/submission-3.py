class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = []
        sol = 1
        count = 0

        for j in nums:
            if j != 0:
                sol *= j
            else:
                count += 1

        if count > 1:
            return [0]*len(nums)

        for i, num in enumerate(nums):
            if num == 0:
                res = [0]*len(nums)
                res[i] = sol
                return res
            arr.append(int(sol/num))
        
        return arr