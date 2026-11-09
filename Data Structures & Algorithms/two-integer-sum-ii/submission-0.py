class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:    
        left = 0
        right = len(numbers)-1

        while left < right:
            check = numbers[left] + numbers[right]

            if check == target:
                return [left+1, right+1]

            if check < target:
                left += 1
            
            if check > target:
                right -= 1
        







        