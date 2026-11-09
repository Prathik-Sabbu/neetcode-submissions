class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) - 1
        max_value = 0

        while left < right:
            total = (right - left)*min(heights[right], heights[left])
            max_value = max(total, max_value)

            if heights[left] < heights[right]:
                left += 1
            
            else:
                right -= 1

        return max_value
        