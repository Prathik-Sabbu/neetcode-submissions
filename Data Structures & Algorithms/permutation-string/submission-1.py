class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        if s1 == s2:
            return True

        hashmaps1 = {}
        hashmaps2 = {}

        left = 0
        right = left + len(s1)

        for i in range(len(s1)):
            hashmaps1[s1[i]] = 1 + hashmaps1.get(s1[i],0)
            hashmaps2[s2[i]] = 1 + hashmaps2.get(s2[i],0)            

        if hashmaps2 == hashmaps1:
            return True
        
        while right < len(s2):
            hashmaps2[s2[left]] = hashmaps2.get(s2[left],0) - 1
            if hashmaps2.get(s2[left],0) == 0:
                del hashmaps2[s2[left]]
            hashmaps2[s2[right]] = 1 + hashmaps2.get(s2[right],0) 
            left += 1
            right += 1
            
            if hashmaps1 == hashmaps2:
                return True
            
        return False

        
        