# Problem: https://leetcode.com/problems/zigzag-conversion/
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        row = 0
        rows = [[] for x in range(min(numRows, len(s)))]
        direction = 'down'
        for ch in s:
            if direction == 'down' and row < numRows:
                rows[row].append(ch)
                row += 1
                
            if direction == 'up' and row >= 0:
                rows[row].append(ch)
                row -= 1
                
            if direction == 'up' and row < 0:
                direction = 'down'
                row = 1
            elif direction == 'down' and row >= numRows:
                direction = 'up'
                row = numRows - 2

        result = ""
        for row in rows:
            result += "".join(row)
        
        return result
            
                
                
        
        
        
