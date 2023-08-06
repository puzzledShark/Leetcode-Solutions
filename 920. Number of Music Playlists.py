# n     Represents how many songs there are
# goal  Hom many songs you want to listen to
# k     Point at which other songs can be played  
class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        mod = 10**9 + 7
        dp = [[0] * (goal + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            for j in range(1, goal + 1):
                dp[i][j] = dp[i - 1][j - 1] * (n - i + 1) + dp[i][j - 1] * max(i - k, 0)
                dp[i][j] %= mod

        return dp[n][goal]
    

# Test Code
solution = Solution()
result = solution.numMusicPlaylists(3,3,1)

# Print the result
print("Result:",result)
