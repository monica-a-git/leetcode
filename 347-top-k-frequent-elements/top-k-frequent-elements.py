class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maps={}
        for val in nums:
            maps[val]=maps.get(val,0)+1

        items=sorted(maps.keys(), key= lambda x: maps[x], reverse=True)
        return items[0:k]