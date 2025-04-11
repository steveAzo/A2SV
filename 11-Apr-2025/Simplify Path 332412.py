# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution(object):
    def simplifyPath(self, path):
        res = path.split('/')
        print(res)
        result = []

        i = 0
        while i < len(res):
            if res[i] == '.' or not res[i]:
                i += 1
                continue
            elif res[i] == '..':
                if result:
                    result.pop()
                i += 1
            else:
                result.append(res[i])
                i += 1

        print(result)
        ress = '/'.join(i for i in result if i)

        return '/' + ress
        