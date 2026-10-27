class Solution(object):
    def createGrid(self, m, n):
        g = [['#' ] * n for _ in range(m)]

        for j in range(n):
            g[0][j] = '.'
            
        for i in range(m):
            g[i][n - 1] = '.'
            
        return ["".join(row) for row in g]