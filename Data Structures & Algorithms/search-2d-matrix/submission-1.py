class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row, col = len(matrix), len(matrix[0])
        left = 0
        right = (row * col) - 1
        
        while left <= right:
            mid = left + (right - left)// 2
            mid_val = matrix[mid // col][mid % col]

            if mid_val == target:
                return True
            
            elif mid_val > target:
                right -= 1
            
            else:
                left += 1
                
        return False

        