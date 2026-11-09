class Solution:
    def trap(self, height: List[int]) -> int:
        volume = 0
        stack = []

        for i,value in enumerate(height):
            while stack and value > height[stack[-1]]:
                valley = stack.pop()

                if not stack:
                    break

                left_wall = stack[-1]

                width = i - left_wall - 1
                max_height = min(height[left_wall], value) - height[valley]

                volume += width * max_height

            stack.append(i)

        return volume
            

        