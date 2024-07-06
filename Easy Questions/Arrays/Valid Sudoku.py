class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check the rows
        for row in range(9):
            rS = set()
            for col in range(9):
                value = board[row][col]
                if value in rS: 
                    return False 
                if value != ".":
                    rS.add(value)
                    
        # check the col
        for row in range(9):
            cS = set()
            for col in range(9):
                value = board[col][row]
                if value in cS:
                    return False 
                if value != ".":
                    cS.add(value)
        #check for the squares 
        squares = [(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]
        for i, j in squares: 
            squareS = set()
            for row in range(i,i+3):
                for col in range(j, j+3):
                    value = board[row][col]
                    if value in squareS:
                        return False 
                    if value != ".":
                        squareS.add(value)
                        
        return True
