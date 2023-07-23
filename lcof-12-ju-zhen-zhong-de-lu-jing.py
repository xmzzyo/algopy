from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        v = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

        def dfs(i, j, ss):
            if len(ss) == 0:
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False
            if v[i][j]:
                return False
            if board[i][j] != ss[0]:
                return False
            v[i][j] = True
            up = dfs(i - 1, j, ss[1:])
            down = dfs(i + 1, j, ss[1:])
            left = dfs(i, j - 1, ss[1:])
            right = dfs(i, j + 1, ss[1:])
            v[i][j] = False
            return up or down or left or right

        for ii in range(len(board)):
            for jj in range(len(board[0])):
                if not v[ii][jj] and dfs(ii, jj, word):
                    return True
        return False


print(Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))
