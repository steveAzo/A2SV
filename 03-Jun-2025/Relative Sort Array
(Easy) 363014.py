# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hash_map = {}
        for i in range(len(arr2)):
            hash_map[arr2[i]] = i
        
        arr1.sort(key=lambda x: hash_map[x] if x in hash_map else x + len(arr2))

        return arr1