# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

class Solution(object):
    def lengthOfLIS(self, nums):
        sorted_arr = []

        for num in nums:
            #use binary search to get the index to which num can be placed in the sorted_arr
            indx = bisect_left(sorted_arr, num)

            if indx == len(sorted_arr):
                sorted_arr.append(num)
            else:
                sorted_arr[indx] = num
        
        return len(sorted_arr)
        