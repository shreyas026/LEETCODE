# ===============================
# 168. Excel Sheet Column Title
# ===============================
# Difficulty: Easy
#
# Given an integer `columnNumber`, return *its corresponding column title as it appears in an Excel sheet*.
#
# For example:
#
# A -&gt; 1
# B -&gt; 2
# C -&gt; 3
# ...
# Z -&gt; 26
# AA -&gt; 27
# AB -&gt; 28 
# ...
#
# ```
#
#  
#
# **Example 1:**
#
# **Input:** columnNumber = 1
# **Output:** &quot;A&quot;
#
# ```
#
# **Example 2:**
#
# **Input:** columnNumber = 28
# **Output:** &quot;AB&quot;
#
# ```
#
# **Example 3:**
#
# **Input:** columnNumber = 701
# **Output:** &quot;ZY&quot;
#
# ```
#
#  
#
# **Constraints:**
#
# 	
# - `1 &lt;= columnNumber &lt;= 2^31 - 1`
#
# ====== SOLUTION ======

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber > 0:
            columnNumber -= 1
            result.append(chr(columnNumber % 26 + ord('A')))
            columnNumber //= 26
        return ''.join(result[::-1])
