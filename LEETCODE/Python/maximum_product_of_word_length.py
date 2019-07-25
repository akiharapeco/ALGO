from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words = sorted(words, key=lambda x: len(x), reverse=True)
        print(words)
        res = 0
        
        for i in range(len(words)-1):
            if len(words[i])**2 < res:
                break
            for j in range(i+1, len(words)):
                if res >= len(words[i]) * len(words[j]):
                    break
                for char in words[i]:
                    if char in words[j]:
                        break
                else:
                    res = len(words[i]) * len(words[j])
                    break
        return res