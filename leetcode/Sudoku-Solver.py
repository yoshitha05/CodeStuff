class Solution(object):
    def solveSudoku(self, board):
        \\\
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        \\\
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []

        # Pre-fill the sets and track empty cells
        for r in range(9): 
            for c in range(9):
                if board[r][c] == '.':
                    empty_cells.append((r, c))
                else:
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[(r // 3) * 3 + (c // 3)].add(num)

        def solve(index=0):
            \\\Backtracking function with precomputed empty cells.\\\
            if index == len(empty_cells):  # All cells filled
                return True
            
            r, c = empty_cells[index]
            box_id = (r // 3) * 3 + (c // 3)

            for num in \123456789\:
                if num not in rows[r] and num not in cols[c] and num not in boxes[box_id]:
                    # Place number
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_id].add(num)

                    # Recur
                    if solve(index + 1):
                        return True

                    # Backtrack
                    board[r][c] = '.'
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box_id].remove(num)

            return False  # No valid number found

        solve()
