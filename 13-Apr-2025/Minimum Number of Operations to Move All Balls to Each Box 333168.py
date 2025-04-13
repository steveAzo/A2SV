# Problem: Minimum Number of Operations to Move All Balls to Each Box - https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/

class Solution(object):
    def minOperations(self, boxes):
        res = []

        for i in range(len(boxes)):
            count = 0
            for j in range(len(boxes)):
                if i != j and boxes[j] == '1':
                    count += abs(j-i)
            res.append(count)
        
        return res