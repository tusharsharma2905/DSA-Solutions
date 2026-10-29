class Solution(object):
    def isValidSudoku(self, board):
        seen = set()
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue

                row_entry = (r, val)
                col_entry = (val, c)
                box_entry = (r // 3, c // 3, val)

                if row_entry in seen or col_entry in seen or box_entry in seen:
                    return False
                    
                seen.add(row_entry)
                seen.add(col_entry)
                seen.add(box_entry)
                
        return True