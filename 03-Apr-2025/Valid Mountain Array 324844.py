# Problem: Valid Mountain Array - https://leetcode.com/problems/valid-mountain-array/description/

class Solution(object):
    def validMountainArray(self, arr):
        if len(arr) < 3:
            return False

        peak = 0
        i = 1
        while i < len(arr):
            if arr[i] > arr[i - 1]:
                i += 1
                continue
            else:
                peak = i - 1
                break
            i += 1
        
        if peak == 0:
            return False

        if peak >= len(arr) - 1:
            if arr[peak] < arr[peak - 1]:
                return True
            else:
                return False

        j = peak
        while j < len(arr) - 1:
            if arr[j] <= arr[j + 1]:
                return False
            else:
                j += 1
                continue

        return True        