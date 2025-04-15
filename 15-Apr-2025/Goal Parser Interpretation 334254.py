# Problem: Goal Parser Interpretation - https://leetcode.com/problems/goal-parser-interpretation/description/

class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        hash_map = {
            "G": "G",
            "()": "o",
            "(all)": "al"
        }

        res = []
        for i in range(len(command)):
            if command[i] == 'G':
                res.append(command[i])
            elif command[i] == '(':
                if command[i+1] == 'a':
                    res.append('al')
                elif command[i+1] == ')':
                    res.append('o')
        
        return ''.join(res)
            


        