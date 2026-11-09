class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashmap = {}

        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]] = 0
            if t[i] not in hashmap:
                hashmap[t[i]] = 0
            hashmap[s[i]] += 1
            hashmap[t[i]] -= 1
        
        return not any(val != 0 for val in hashmap.values())