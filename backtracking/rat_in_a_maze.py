
"""
Consider a rat placed at (0, 0) in a square matrix mat of order n* n.
It has to reach the destination at (n - 1, n - 1).
Find all possible paths that the rat can take to reach from source to destination.
The directions in which the rat can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right).
Value 0 at a cell in the matrix represents that it is blocked and rat cannot move to it while value 1
at a cell in the matrix represents that rat can be travel through it.

Input:
N = 4
m[][] = {{1, 0, 0, 0},
         {1, 1, 0, 1},
         {1, 1, 0, 0},
         {0, 1, 1, 1}}
Output:
DDRDRR DRDDRR

Time Complexity: O(3^(m*n)), because on every cell we have to try 3 different directions,
                as we will not check for the cell from which we have visited in the last move.
Auxiliary Space: O(m*n), Maximum Depth of the recursion tree(auxiliary space).

"""
def rat_in_a_maze(board):
    m = len(board[0])
    n = len(board)

    visited = [[False for i in range(m)] for j in range(n)]
    res = []
    helper(n, m, 0, 0, board, visited, res, "")

    return res

def is_safe(r, c, board, visited):
    if r >= 0 and c >= 0 and r < len(board) and c < len(board[0]) and visited[r][c] == False and board[r][c] == 1:
        return True
    return False

def helper(n, m, i, j, board, visited, res, path):
    if i == len(board) - 1 and j == len(board[0]) - 1:
        res.append(path)
        return

    # check the safe moves and make move
    # Down - r + 1, c
    if is_safe(i + 1, j, board, visited):
        visited[i][j] = True
        # path += "D"
        helper(n, m, i + 1, j, board, visited, res, path + "D")
        visited[i][j] = False

    # Left - r, c - 1
    if is_safe(i, j - 1, board, visited):
        visited[i][j] = True
        helper(n, m, i, j - 1, board, visited, res, path + "L")
        visited[i][j] = False

    # Right - r, c + 1
    if is_safe(i, j + 1, board, visited):
        visited[i][j] = True
        helper(n, m, i, j + 1, board, visited, res,  path + "R")
        visited[i][j] = False

    # UP - r - 1, c
    if is_safe(i - 1, j, board, visited):
        visited[i][j] = True
        helper(n, m, i - 1, j, board, visited, res, path + "U")
        visited[i][j] = False

a = rat_in_a_maze([[1, 0, 0, 0],
         [1, 1, 0, 1],
         [1, 1, 0, 0],
         [0, 1, 1, 1]])
print(a)