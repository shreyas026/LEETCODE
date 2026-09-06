class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        a = len(s)
        b = len(t)

        dp = [[0] * (b+1) for _ in range(a+1)]

        for i in range(a+1):
            dp[i][b]= 1
        for i in range(a-1,-1,-1):
            for j in range(b-1,-1,-1):
                dp[i][j]= dp[i+1][j]

                if s[i]==t[j]:
                    dp[i][j]+=dp[i+1][j+1]

        return dp[0][0]
        