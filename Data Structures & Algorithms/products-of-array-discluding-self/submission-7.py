class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = {0:1}
        post = {}
        sol = [1]
        mult = 1

        for i in range(len(nums)-1):
            mult *= nums[i]
            sol.append(mult)

        print(sol)

        mult = 1

        for i in range(len(nums)-1, -1, -1):
            sol[i] *= mult
            mult *= nums[i]


        return sol
