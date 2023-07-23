from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
        path = []

        def search(i, j):
            if len(path) == len(word):
                return True
            if i - 1 >= 0 and not visited[i - 1][j] and board[i - 1][j] == word[len(path)]:
                path.append(word[len(path)])
                visited[i - 1][j] = 1
                if search(i - 1, j):
                    return True
                path.pop()
                visited[i - 1][j] = 0
            if i + 1 < len(board) and not visited[i + 1][j] and board[i + 1][j] == word[len(path)]:
                path.append(word[len(path)])
                visited[i + 1][j] = 1
                if search(i + 1, j):
                    return True
                path.pop()
                visited[i + 1][j] = 0
            if j - 1 >= 0 and not visited[i][j - 1] and board[i][j - 1] == word[len(path)]:
                path.append(word[len(path)])
                visited[i][j - 1] = 1
                if search(i, j - 1):
                    return True
                path.pop()
                visited[i][j - 1] = 0
            if j + 1 < len(board[0]) and not visited[i][j + 1] and board[i][j + 1] == word[len(path)]:
                path.append(word[len(path)])
                visited[i][j + 1] = 1
                if search(i, j + 1):
                    return True
                path.pop()
                visited[i][j + 1] = 0

        for m in range(len(board)):
            for n in range(len(board[0])):
                if board[m][n] == word[0]:
                    path = [word[0]]
                    visited = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
                    if search(m, n):
                        return True
        return False


print(Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))
print(Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"))
print(Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"))
