# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution(object):
    def maxArea(self, heights):
        max_vol = 0

        left, right = 0, len(heights) - 1

        while left < right:
            current_vol = (right - left) * min(heights[left], heights[right])
            max_vol = max(max_vol, current_vol)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_vol