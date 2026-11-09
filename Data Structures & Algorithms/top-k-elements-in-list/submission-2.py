class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for i in nums:
            if i not in hashmap:
                hashmap[i] = 0

            hashmap[i] += 1

        buckets = [[] for _ in range(len(nums)+1)]
        for i in hashmap:
            buckets[hashmap[i]].append(i)
        
        result = []
        for i in range(len(buckets), 0, -1):
            if buckets[i-1]:
                for num in buckets[i-1]:
                    result.append(num)

            if len(result) == k:
                return result