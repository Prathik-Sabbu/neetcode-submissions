class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for i in strs:
            decode = len(i)
            encoded_string += str(f"{decode}#")
            encoded_string += str(i)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        while s:
            if s[0].isdigit():
                pound = s.find('#')
                num = int(s[0:pound])
                decoded_strs.append(s[pound + 1 : num + pound + 1])
                s = s[num + pound + 1:]
        return decoded_strs

