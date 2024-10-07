"""
Problem - Word search

Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally
or vertically neighboring. The same letter cell may not be used more than once.
Ex.
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
output = True

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
output = False

Solution - This problem is similar to the rat in a maze problem, Where you find a path and reaches till the end.

Time Complexity: O(3^(m*n)), because on every cell we have to try 3 different directions,
                as we will not check for the cell from which we have visited in the last move.
Auxiliary Space: O(m*n), Maximum Depth of the recursion tree(auxiliary space).
"""

class Solution:
    def exist(self, board, word):
        word_index = 1
        res = []
        visited = [[False for i in range(len(board[0]))] for j in range(len(board))]
        m = len(board)
        n = len(board[0])
        # Finding the first letter and trying to find the word from there itself
        for row in range(m):
            for col in range(n):
                if board[row][col] == word[0]:
                    ans = self.helper(row, col, word_index, word, board, res, visited)
                    if ans == True:
                        return True
        return False

    def is_safe(self, r, c, word_index, word, board, visited):
        if word_index < len(word) and r >= 0 and r < len(board) \
            and c >= 0 and c < len(board[0]) and board[r][c] == word[word_index] and visited[r][c] == False:
            return True
        return False

    def helper(self, r, c, word_index, word, board, res, visited):
        if word_index >= len(word):
            res.append(True)
            return True

        visited[r][c] = True
        # Down
        if self.is_safe(r + 1, c, word_index, word, board, visited):
            if self.helper(r + 1, c, word_index + 1, word, board, res, visited) == True:
                return True
        # Left
        if self.is_safe(r , c - 1, word_index, word, board, visited):
            if self.helper(r, c - 1, word_index + 1, word, board, res, visited) == True:
                return True
        # Right
        if self.is_safe(r, c + 1, word_index, word, board, visited):
            if self.helper(r, c + 1, word_index + 1, word, board, res, visited) == True:
                return True
        # UP
        if self.is_safe(r - 1, c, word_index, word, board, visited):
            if self.helper(r - 1, c, word_index + 1, word, board, res, visited) == True:
                return True
        visited[r][c] = False
        return False

s = Solution()
# Case 1
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print("Case 1 - Ans should be TRUE : ", s.exist(board, word))
# Case 2
board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word1 = "ABCB"
print("Case 2 - Ans should be FALSE : ", s.exist(board1, word1))
# Case 3
board2 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word2 = "SEE"
print("Case 3 - Ans should be TRUE : ", s.exist(board2, word2))