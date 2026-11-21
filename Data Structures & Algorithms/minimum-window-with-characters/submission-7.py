class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        hashmap = {}
        for c in t:
            hashmap[c] = hashmap.get(c, 0) + 1

        missing = len(t)
        left = 0
        best_left = 0
        best_len = float("inf")

        for right, char in enumerate(s):
            if char in hashmap:
                if hashmap[char] > 0:
                    missing -= 1
                hashmap[char] -= 1

            while missing == 0:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_left = left

                leaving = s[left]
                if leaving in hashmap:
                    hashmap[leaving] += 1
                    if hashmap[leaving] > 0:
                        missing += 1
                left += 1

        return "" if best_len == float("inf") else s[best_left : best_left + best_len]