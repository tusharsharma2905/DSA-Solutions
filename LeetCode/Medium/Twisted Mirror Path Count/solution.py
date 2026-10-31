class Solution(object):
    def uniquePaths(self, grid):
        MOD = 10**9 + 7
        rows, cols = len(grid), len(grid[0])
        dp = [[0] * 2 for _ in range(cols + 1)]
        dp[1] = [1, 1]
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dp[c + 1] = [dp[c + 1][1], dp[c][0]]
                else:
                    val = (dp[c + 1][1] + dp[c][0]) % MOD
                    dp[c + 1] = [val, val]
                    
        return dp[-1][0]