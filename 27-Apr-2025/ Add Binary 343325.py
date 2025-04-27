# Problem:  Add Binary - https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_pointer = len(a) - 1
        b_pointer = len(b) - 1
        carry = 0
        result = []

        while a_pointer >= 0 or b_pointer >= 0 or carry:
            total = carry

            if a_pointer >= 0:
                total += int(a[a_pointer])
                a_pointer -= 1
            
            if b_pointer >= 0:
                total += int(b[b_pointer])
                b_pointer -= 1
            
            result.append(str(total%2))
            carry = total //2
        
        return ''.join(reversed(result))
        