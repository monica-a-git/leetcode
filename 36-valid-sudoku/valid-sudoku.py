class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(len(board)):
            for c in range(len(board[r])):
                cell = board[r][c]

                if cell == ".":
                    continue

                if cell in rows[r]:
                    return False

                if cell in cols[c]:
                    return False

                box_index = (r // 3) * 3 + (c // 3)
                if cell in boxes[box_index]:
                    return False

                rows[r].add(cell)
                cols[c].add(cell)
                boxes[box_index].add(cell)

        return True