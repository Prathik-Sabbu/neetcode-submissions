class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        maximum = 0
        len_heights = len(heights)

        for i, value in enumerate(heights):            
            while stack and (heights[stack[-1]] >= value):
                index = stack.pop()
                width = (i - 1 - stack[-1]) if stack else i
                maximum = max(width*heights[index], maximum)

            stack.append(i)

        while stack:
            index = stack.pop()
            width = (len_heights - 1 - stack[-1]) if stack else len_heights
            maximum = max(width*heights[index], maximum)
        
        return maximum
            
        