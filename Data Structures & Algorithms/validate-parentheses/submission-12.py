class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {'{':'}', '[':']', '(':')'}
        if (len(s) % 2) != 0:
            return False

        for i in s:
            if i in hashmap:
                stack.append(i)
            else:
                if not stack or i != hashmap[stack.pop()]:
                    return False
        return (len(stack) == 0)

        