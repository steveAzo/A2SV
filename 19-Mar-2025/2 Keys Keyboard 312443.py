# Problem: 2 Keys Keyboard - https://leetcode.com/problems/2-keys-keyboard/description/

class Solution(object):
    def minSteps(self, n):
        if n <= 1:
            return 0
        operations = 0
        factor = 2
        while n > 1:
            while n % factor == 0:
                operations += factor
                n //= factor
            factor += 1

        return operations
        