# ==================
# 263. Ugly Number
# ==================
# Difficulty: Easy
#
# An **ugly number** is a *positive* integer which does not have a prime factor other than 2, 3, and 5.
#
# Given an integer `n`, return `true` *if* `n` *is an **ugly number***.
#
#  
#
# **Example 1:**
#
# **Input:** n = 6
# **Output:** true
# **Explanation:** 6 = 2 &times; 3
#
# ```
#
# **Example 2:**
#
# **Input:** n = 1
# **Output:** true
# **Explanation:** 1 has no prime factors.
#
# ```
#
# **Example 3:**
#
# **Input:** n = 14
# **Output:** false
# **Explanation:** 14 is not ugly since it includes the prime factor 7.
#
# ```
#
#  
#
# **Constraints:**
#
# 	
# - `-2^31 &lt;= n &lt;= 2^31 - 1`
#
# ====== SOLUTION ======

class Solution:
    def isUgly(self, n: int) -> bool:
        if n<=0:
            return False
        for i in [2,3,5]:
            while n%i==0:
                n//=i
        return n==1
