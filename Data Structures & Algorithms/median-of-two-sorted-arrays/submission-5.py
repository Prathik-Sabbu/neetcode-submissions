class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)

        if not (l1 + l2):
            return
        
        index = (l1 + l2+1) // 2

        if l1 > l2:
            nums1, nums2 = nums2, nums1
            l1, l2 = l2, l1
        
        left = 0
        right = l1

        while left <= right:
            i = (left + right)//2
            j = index - i

            maxLeftX = nums1[i - 1] if i > 0 else float('-inf')
            minRightX = nums1[i] if i < l1 else float('inf')

            maxLeftY = nums2[j - 1] if j > 0 else float('-inf')
            minRightY = nums2[j] if j < l2 else float('inf')

            print(maxLeftX, minRightX, maxLeftY, minRightY, i, j)

            if maxLeftX > minRightY:
                right = i - 1
            
            elif minRightX < maxLeftY:
                left = i + 1
            
            else:
                if (l1+l2)%2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                
                else:
                    return max(maxLeftY, maxLeftX)