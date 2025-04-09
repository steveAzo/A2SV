# Problem: Selection Sort - https://practice.geeksforgeeks.org/problems/selection-sort/1

class Solution:
    def selectionSort(self, arr):
        for i in range(len(arr) - 1):
            min_value = arr[i]
            min_index = i
            for j in range(i + 1, len(arr)):
                if arr[j] < min_value:
                    min_value = arr[j]
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]