# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_freq = defaultdict(int)
        prefix_freq[0] = 1
        current_mod = 0
        count = 0
        for i in range(len(nums)):
            current_mod = (current_mod + nums[i]) % k
            if current_mod < 0:
                current_mod += k

            count += prefix_freq[current_mod]
            prefix_freq[current_mod] += 1
        
        return count
        