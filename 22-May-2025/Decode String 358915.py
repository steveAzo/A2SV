# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        number_stack = []
        current_str = ''
        string_stack = []
        k = 0

        for char in s:
            if char.isdigit():
                k = k * 10 + int(char)
            elif char == '[':
                number_stack.append(k)
                string_stack.append(current_str)
                k = 0
                current_str = ''
            elif char == ']':
                prev_str = string_stack.pop()
                times = number_stack.pop()
                current_str = prev_str + current_str * times
            else:
                current_str += char
            
        return current_str
