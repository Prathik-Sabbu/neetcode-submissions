class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for i in nums:
            if i not in hashmap:
                hashmap[i] = 0

            hashmap[i] += 1


        result = []
        for i in range(k):
            result.append(max(hashmap, key=hashmap.get))
            delete = hashmap.pop(max(hashmap, key=hashmap.get))
        
        return result