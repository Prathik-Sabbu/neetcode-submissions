class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box = {0:set(),
               1:set(),
               2:set(),
               3:set(),
               4:set(),
               5:set(),
               6:set(),
               7:set(),
               8:set()}

        for i in range(9):
            row = set()
            col = set()
            for j in range(9):
                num = ((int(i/3)*3) + int(j/3))
                if board[i][j] != ".":
                    if board[i][j] in row:
                        return False
                    else:
                        row.add(board[i][j])

                if board[j][i] != ".":
                    if board[j][i] in col:
                        return False
                    else:
                        col.add(board[j][i])

                if board[i][j] != ".":
                    if board[i][j] in box[num]:
                        return False
                    else:
                        box[num].add(board[i][j])
                        
        return True

