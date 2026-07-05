class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []
        
        # 1. Initialize the sets and find all empty cells
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty.append((r, c))
                else:
                    val = board[r][c]
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + c // 3].add(val)
                    
        def backtrack(index=0):
            # Base case: If we've filled all empty cells, the board is solved
            if index == len(empty):
                return True
            
            r, c = empty[index]
            box_idx = (r // 3) * 3 + c // 3
            
            for val in map(str, range(1, 10)):
                # O(1) validation
                if val not in rows[r] and val not in cols[c] and val not in boxes[box_idx]:
                    # Place the number
                    board[r][c] = val
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[box_idx].add(val)
                    
                    if backtrack(index + 1):
                        return True
                        
                    # Backtrack (Undo the placement)
                    board[r][c] = '.'
                    rows[r].remove(val)
                    cols[c].remove(val)
                    boxes[box_idx].remove(val)
                    
            return False
            
        backtrack()

