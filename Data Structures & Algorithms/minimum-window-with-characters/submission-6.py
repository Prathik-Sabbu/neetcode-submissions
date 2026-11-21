class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        res = s
        sub = ""
        left = 0
        right = 0
        hashmap = {}
        found = ""
        works = 0
        missing = len(t)

        for i in t:
            hashmap[i] = 1 + hashmap.get(i, 0)
        
        while left < len(s) and s[left] not in hashmap:
            left += 1

        right = left
        while right < len(s) and missing > 0:
            if s[right] in hashmap:
                if hashmap[s[right]] > 0:
                    missing -= 1
                hashmap[s[right]] -= 1
            sub += s[right]
            right += 1  
        
        if missing == 0:
            works = 1
            if len(sub) < len(res):
                res = sub
        
        while left < len(s):
            leaving = s[left]
            left += 1

            if len(sub) > 0:
                sub = sub[1:]

            if leaving in t:
                hashmap[leaving] += 1
                if hashmap[leaving] > 0:
                    missing += 1
            
            while right < len(s) and missing > 0:
                if s[right] in hashmap:
                    if hashmap[s[right]] > 0:
                        missing -= 1
                    hashmap[s[right]] -= 1
                sub += s[right]
                right += 1

            if missing == 0:
                if len(sub) < len(res):
                    res = sub

        if works != 1:
            return ""

        return res



        