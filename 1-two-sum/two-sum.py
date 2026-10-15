class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap={}
        n = len(nums)
        for i in range(n):
            com=target-nums[i]
            if com in numMap:
                return[numMap[com],i]
            numMap[nums[i]]=i
        return []