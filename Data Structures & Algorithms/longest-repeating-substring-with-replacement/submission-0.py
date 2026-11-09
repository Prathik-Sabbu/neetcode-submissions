class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        hashmap = {}

        for i, value, in enumerate(s):
            hashmap[value] = 1 + hashmap.get(value, 0)
            right += 1

            if (right - left) - max(hashmap.values()) > k:
                hashmap[s[left]] -= 1
                left += 1

        return (right - left)

        