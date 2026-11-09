class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = {0:1}
        post = {}
        sol = []
        mult = 1

        for i in range(len(nums)-1):
            mult *= nums[i]
            pre[i+1] = mult

        mult = 1

        for i in range(len(nums)-1, -1, -1):
            post[i] = mult
            mult *= nums[i]

        for i in range(len(nums)):
            sol.append(pre[i] * post[i])

        return sol
