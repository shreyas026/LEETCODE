# ==================================
# 3700. Number of ZigZag Arrays II
# ==================================
# Difficulty: Hard
#
# You are given three integers `n`, `l`, and `r`.
#
# A **ZigZag** array of length `n` is defined as follows:
#
# 	
# - Each element lies in the range `[l, r]`.
# 	
# - No **two** adjacent elements are equal.
# 	
# - No **three** consecutive elements form a **strictly increasing** or **strictly decreasing** sequence.
#
# Return the total number of valid **ZigZag** arrays.
#
# Since the answer may be large, return it **modulo** `10^9 + 7`.
#
# A **sequence** is said to be **strictly increasing** if each element is strictly greater than its previous one (if exists).
#
# A **sequence** is said to be **strictly decreasing** if each element is strictly smaller than its previous one (if exists).
#
#  
#
# **Example 1:**
#
# **Input:** n = 3, l = 4, r = 5
#
# **Output:** 2
#
# **Explanation:**
#
# There are only 2 valid ZigZag arrays of length `n = 3` using values in the range `[4, 5]`:
#
# 	
# - `[4, 5, 4]`
# 	
# - `[5, 4, 5]`
#
# **Example 2:**
#
# **Input:** n = 3, l = 1, r = 3
#
# **Output:** 10
#
# **Explanation:**
#
# ​​​​​​​There are 10 valid ZigZag arrays of length `n = 3` using values in the range `[1, 3]`:
#
# 	
# - `[1, 2, 1]`, `[1, 3, 1]`, `[1, 3, 2]`
# 	
# - `[2, 1, 2]`, `[2, 1, 3]`, `[2, 3, 1]`, `[2, 3, 2]`
# 	
# - `[3, 1, 2]`, `[3, 1, 3]`, `[3, 2, 3]`
#
# All arrays meet the ZigZag conditions.
#
#  
#
# **Constraints:**
#
# 	
# - `3 &lt;= n &lt;= 10^9`
# 	
# - `1 &lt;= l &lt; r &lt;= 75`​​​​​​​
#
# ====== SOLUTION ======

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        def mat_mul(a, b):
            res = [[0] * m for _ in range(m)]
            for i in range(m):
                for k in range(m):
                    if a[i][k]:
                        for j in range(m):
                            res[i][j] = (res[i][j] + a[i][k] * b[k][j]) % MOD
            return res

        def mat_pow(mat, p):
            res = [[int(i == j) for j in range(m)] for i in range(m)]
            while p:
                if p & 1:
                    res = mat_mul(res, mat)
                mat = mat_mul(mat, mat)
                p >>= 1
            return res

        U = [[0] * m for _ in range(m)]
        D = [[0] * m for _ in range(m)]

        for i in range(m):
            for j in range(i):
                U[i][j] = 1
            for j in range(i + 1, m):
                D[i][j] = 1

        UD = mat_mul(U, D)

        p = n - 1
        V = mat_pow(UD, p // 2)

        if p & 1:
            V = mat_mul(V, U)

        ans = 0
        for row in V:
            ans = (ans + sum(row)) % MOD

        return ans * 2 % MOD
