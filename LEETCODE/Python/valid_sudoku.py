from typing import List
from functools import reduce

def hasRepetition(nums):
    num_dict = {}
    for num in nums:
        if not num == ".":
            if num_dict.get(num):
                return True
            else:
                num_dict[num] = 1
    return False
    
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if hasRepetition(board[i]):
                return False
        for j in range(9):
            if hasRepetition(list(map(lambda x: x[j], board))):
                return False
        for i in range(3):
            for j in range(3):
                if hasRepetition(list(reduce(lambda x, y: x+y, list(map(lambda x: x[3*j:3*j+3] , board[3*i:3*i+3]))))):
                    return False
        return True