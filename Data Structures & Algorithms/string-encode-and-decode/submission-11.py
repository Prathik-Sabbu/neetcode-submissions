class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        while i < len(s):
            j = 0
            while s[j] != '#':
                j += 1

            num = int(s[i:j])
            decoded_strs.append(s[j + 1 : num + j + 1])
            s = s[num + j + 1:]
        return decoded_strs
