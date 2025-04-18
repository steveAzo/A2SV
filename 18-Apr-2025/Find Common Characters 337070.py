# Problem: Find Common Characters - https://leetcode.com/problems/find-common-characters/

class Solution(object):
    def commonChars(self, words):
        store = []
        for word in words:
            hash_map = [0 for _ in range(26)]
            for char in word:
                pos = ord(char) - ord('a')
                hash_map[pos] += 1
            store.append(hash_map)
        
        result = []
        processed = set()
        for char in words[0]:
            if char in processed:
                continue

            pos = ord(char) - ord('a')
            freq = store[0][pos]
            for i in range(1, len(words)):
                freq = min(freq, store[i][pos])
                
           
            if freq > 0:
                for _ in range(freq):
                    result.append(char)

                processed.add(char)
            
        return result
        