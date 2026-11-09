class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        hashmap = {}
        left = 0
        right = 0
        result = 0
        
        for i, value in enumerate(s):
            if value not in hashmap:
                hashmap[value] = i
                right += 1
            
            else:
                result = max((right - left), result)
                right += 1
                left = max(left, hashmap[value] + 1)
                hashmap[value] = i
            
        result = max((right - left), result)      
        return result
            