# ====================
# 7. Reverse Integer
# ====================
# Difficulty: Medium
#
# Given a signed 32-bit integer `x`, return `x`* with its digits reversed*. If reversing `x` causes the value to go outside the signed 32-bit integer range `[-2^31, 2^31 - 1]`, then return `0`.
#
# **Assume the environment does not allow you to store 64-bit integers (signed or unsigned).**
#
#  
#
# **Example 1:**
#
# **Input:** x = 123
# **Output:** 321
#
# ```
#
# **Example 2:**
#
# **Input:** x = -123
# **Output:** -321
#
# ```
#
# **Example 3:**
#
# **Input:** x = 120
# **Output:** 21
#
# ```
#
#  
#
# **Constraints:**
#
# 	
# - `-2^31 &lt;= x &lt;= 2^31 - 1`
#
# ====== SOLUTION ======

class Solution:
    def reverse(self, x: int) -> int:

        ans=""
        if x<0:
            ans+="-"
        x=str(abs(x))
        s=""
        for ch in x:
            s = ch+s            
           
        return  int(ans+s) if 2**31 -1 >= int(s) else 0
