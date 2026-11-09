class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        left = 0
        right = len(matrix)-1
        
        while left <= right:
            mid = left + (right - left)// 2
            print(left, right, mid, matrix[mid][0], matrix[mid][-1])

            if matrix[mid][0] > target:
                right -= 1
            
            elif matrix[mid][-1] < target:
                left += 1

            else:
                for i in matrix[mid]:
                    if i == target:
                        return True
                return False
                
        return False

        