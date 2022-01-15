# Backtrack - Didn't pass time limit
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] != word[0]:
                    continue

                path = [(row, col)]
                if self.backtrack(board, row, col, path, word[1:]):
                    return path
                path.pop()
        return False
        
    def backtrack(self, board, row, col, path, subword):
        # arrived to a solution
        if not subword:
            return True
        
        # visit adjacent nodes
        rows = [0, 0, 1,-1]
        cols = [1,-1, 0, 0]
        for i in range(len(rows)):
            x = row + rows[i]
            y = col + cols[i]
            
            if not self.is_valid_cell(x,y, board):
                continue
            
            if self.in_path(x, y, path):
                continue
            
            if board[x][y] != subword[0]:
                continue
            
                            
            path.append((x,y))
            found_path = self.backtrack(board, x, y, path, subword[1:])
            if found_path:
                return True
            path.pop()
        
        return False

    def is_valid_cell(self, row, col, board):
        if row >= 0 and row < len(board) and col >= 0 and col < len(board[0]):
            return True
        return False
    
    def in_path(self, row, col, path):
        if (row, col) in path:
            return True
        return False
