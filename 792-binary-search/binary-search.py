class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s,e=0,len(nums)
        while s<e:
            i=(s+e)//2
            if nums[i] <= target:
                s=i+1
            else:
                e = i

        if s>0 and nums[s-1]==target:
            return s-1
        else:
            return -1  
