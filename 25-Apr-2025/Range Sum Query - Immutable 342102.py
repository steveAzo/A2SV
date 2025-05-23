# Problem: Range Sum Query - Immutable - https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: List[int]):
        prefix_sum = [0] * len(nums)
        
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            prefix_sum[i] = total
        
        self.prefix_sum = prefix_sum
        self.nums = nums


    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right] - self.prefix_sum[left] + self.nums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)