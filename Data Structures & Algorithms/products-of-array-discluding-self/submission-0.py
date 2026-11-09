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

        if count > 0:
            for i in nums:
                if i == 0:
                    arr.append(sol)
                else:
                    arr.append(0)
            return arr

        for i in nums:
            arr.append(int(sol/i))
        
        return arr