# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution(object):
    def sortPeople(self, names, heights):
        
        
        res = list(zip(names, heights))
        for i in range(len(res) - 1):
            swapped = True
            for j in range(len(res) - (i+1)):
                if res[j][1] < res[j + 1][1]:
                    res[j], res[j + 1] = res[j + 1], res[j]
                    swapped = False
            if swapped:
                break
        result = []
        for k in res:
            result.append(k[0])
        
        return result
        
        

        

        return names
        