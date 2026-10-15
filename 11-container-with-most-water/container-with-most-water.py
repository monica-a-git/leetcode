class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        left = 0
        right = len(height) -1
        max_height = max(height)

        while left < right:
            res = max(res, min(height[left], height[right]) * (right - left))
            if height[right] >= height[left]:
                left += 1
            else:
                right -= 1

            if res>max_height*(right-left):
                return res

        return res