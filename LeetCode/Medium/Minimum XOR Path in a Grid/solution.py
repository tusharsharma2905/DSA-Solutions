class Solution(object):
    def minCost(self, grid):
        m, n = len(grid), len(grid[0])
        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(grid[0][0])
        
        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    continue
                
                current_set = set()

                if r > 0:
                    for val in dp[r - 1][c]:
                        current_set.add(val ^ grid[r][c])
     
                if c > 0:
                    for val in dp[r][c - 1]:
                        current_set.add(val ^ grid[r][c])
                        
                dp[r][c] = current_set

        return min(dp[m - 1][n - 1])