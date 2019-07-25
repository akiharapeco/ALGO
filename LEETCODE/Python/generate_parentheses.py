from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        rep = []
        def backtrack(left = 0, right = 0, path = ''):
            if len(path) == 2 * n:
                rep.append(path)
                return
            if left < n:
                backtrack(left+1, right, path+'(')
            if right < left:
                backtrack(left, right+1, path+')')
        backtrack()
        return rep