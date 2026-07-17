# ================
# 67. Add Binary
# ================
# Difficulty: Easy
#
# Given two binary strings `a` and `b`, return *their sum as a binary string*.
#
#  
#
# **Example 1:**
#
# **Input:** a = "11", b = "1"
# **Output:** "100"
#
# ```
#
# **Example 2:**
#
# **Input:** a = "1010", b = "1011"
# **Output:** "10101"
#
# ```
#
#  
#
# **Constraints:**
#
# 	
# - `1 &lt;= a.length, b.length &lt;= 10^4`
# 	
# - `a` and `b` consist only of `&#39;0&#39;` or `&#39;1&#39;` characters.
# 	
# - Each string does not contain leading zeros except for the zero itself.
#
# ====== SOLUTION ======

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2)+int(b,2))[2:]
