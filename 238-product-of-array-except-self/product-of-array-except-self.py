class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i,n=1,len(nums)
        ans = [1]*n

        while i<n:
            ans[i] = ans[i-1] * nums[i-1]
            i+=1

        right = 1   
        i = n-1
        while i>=0:
            ans[i] *= right
            right *= nums[i]
            i-=1

        return ans
         