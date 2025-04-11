# Problem: Minimum Time Difference - https://leetcode.com/problems/minimum-time-difference/

class Solution(object):
    def findMinDifference(self, timePoints):
        res = []
        min_time = float('inf')
        for timePoint in timePoints:
            x, y = timePoint.split(':')
            res.append(int(x)*60 + int(y))

        for i in range(len(res)):
            for j in range(len(res)):
                if i != j:
                    ans = min((res[i] - res[j])%1440, (res[j] - res[i])%1440)
                    min_time = min(min_time, ans)
                    if min_time == 0:
                        return min_time
        
        return min_time

        