# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        paths = path.split('/')

        for path in paths:
            if not path or path == '.':
                continue
            
            if path == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(path)
        
        return '/' + '/'.join(stack)

            
            