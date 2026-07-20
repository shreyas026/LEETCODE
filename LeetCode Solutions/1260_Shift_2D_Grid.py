# =====================
# 1260. Shift 2D Grid
# =====================
# Difficulty: Easy
#
# Given a 2D `grid` of size `m x n` and an integer `k`. You need to shift the `grid` `k` times.
#
# In one shift operation:
#
# 	
# - Element at `grid[i][j]` moves to `grid[i][j + 1]`.
# 	
# - Element at `grid[i][n - 1]` moves to `grid[i + 1][0]`.
# 	
# - Element at `grid[m - 1][n - 1]` moves to `grid[0][0]`.
#
# Return the *2D grid* after applying shift operation `k` times.
#
#  
#
# **Example 1:**
#
# []
#
# **Input:** `grid` = [[1,2,3],[4,5,6],[7,8,9]], k = 1
# **Output:** [[9,1,2],[3,4,5],[6,7,8]]
#
# ```
#
# **Example 2:**
#
# []
#
# **Input:** `grid` = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
# **Output:** [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
#
# ```
#
# **Example 3:**
#
# **Input:** `grid` = [[1,2,3],[4,5,6],[7,8,9]], k = 9
# **Output:** [[1,2,3],[4,5,6],[7,8,9]]
#
# ```
#
#  
#
# **Constraints:**
#
# 	
# - `m == grid.length`
# 	
# - `n == grid[i].length`
# 	
# - `1 &lt;= m &lt;= 50`
# 	
# - `1 &lt;= n &lt;= 50`
# 	
# - `-1000 &lt;= grid[i][j] &lt;= 1000`
# 	
# - `0 &lt;= k &lt;= 100`
#
# ====== SOLUTION ======

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        arr = []

        for row in grid:
            for num in row:
                arr.append(num)

        k %= len(arr)

        arr = arr[-k:] + arr[:-k]

        idx = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = arr[idx]
                idx += 1

        return grid
