class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
            
        for i in strs:
            word = tuple(sorted(i))
            if word in hashmap:
                hashmap[word].append(i)

            else:
                hashmap[word] = [i]
        
        return list(hashmap.values())