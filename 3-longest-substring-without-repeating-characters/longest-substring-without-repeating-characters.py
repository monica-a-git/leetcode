class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastseen={}
        left=0
        maxl=0
        for right,char in enumerate(s):
            if char in lastseen and lastseen[char]>=left:
                left = lastseen[char]+1
            lastseen[char]=right
            maxl=max(maxl,right-left+1)
        return maxl