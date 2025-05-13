# Problem: Sum of Subarray Minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        def nse(arr):
            res = [len(arr)] * len(arr)
            stack = []
            for i in range(len(arr)):
                while stack and arr[i] < arr[stack[-1]]:
                    res[stack[-1]] = i - stack[-1]
                    stack.pop()
                stack.append(i)
            while stack:
                res[stack[-1]] = len(arr) - stack[-1]
                stack.pop()

            return res
        
        def psee(arr):
            res = [-1] * len(arr)
            stack = []
            for i in range(len(arr) - 1, - 1, - 1):
                while stack and arr[i] <= arr[stack[-1]]:
                    res[stack[-1]] = stack[-1] - i
                    stack.pop()
                stack.append(i)
            while stack:
                res[stack[-1]] = stack[-1] + 1
                stack.pop()

            return res
        
        nse_ = nse(arr)
        print(nse_)
        psee_ = psee(arr)
        print(psee_)

        total = 0
        mod = 10 ** 9 + 7
        for i in range(len(arr)):
            total = (total + (nse_[i] * psee_[i] * arr[i]) % mod) % mod
        
        return total
            