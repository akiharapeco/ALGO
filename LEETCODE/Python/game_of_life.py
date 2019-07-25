class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def nextState(cindex, rindex):
            
            lnum = sum([cindex > 0 and rindex > 0 and board[cindex-1][rindex-1], 
                        cindex > 0 and board[cindex-1][rindex],  
                        cindex > 0 and rindex < r_len - 1 and board[cindex-1][rindex+1], 
                        rindex > 0 and board[cindex][rindex-1], 
                        rindex < r_len - 1 and board[cindex][rindex+1], 
                        cindex < c_len - 1 and rindex > 0 and board[cindex+1][rindex-1], 
                        cindex < c_len - 1 and board[cindex+1][rindex],  
                        cindex < c_len - 1 and rindex < r_len - 1 and board[cindex+1][rindex+1]])
            
            if board[cindex][rindex] == 1 and (lnum < 2 or lnum >3):
                return 0
            elif board[cindex][rindex] == 1 and (lnum == 2 or lnum == 3):
                return 1
            elif board[cindex][rindex] == 0 and lnum == 3:
                return 1
            else:
                return 0
        
        c_len = len(board)
        r_len = len(board[0])
        board[:] = [[nextState(row, col) for col in range(r_len)] for row in range(c_len)]
        return board