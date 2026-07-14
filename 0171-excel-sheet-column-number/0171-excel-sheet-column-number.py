# ================================
# 171. Excel Sheet Column Number
# ================================
# Difficulty: Easy
#
# Given a string `columnTitle` that represents the column title as appears in an Excel sheet, return *its corresponding column number*.
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
# **Input:** columnTitle = &quot;A&quot;
# **Output:** 1
#
# ```
#
# **Example 2:**
#
# **Input:** columnTitle = &quot;AB&quot;
# **Output:** 28
#
# ```
#
# **Example 3:**
#
# **Input:** columnTitle = &quot;ZY&quot;
# **Output:** 701
#
# ```
#
#  
#
# **Constraints:**
#
# 	
# - `1 &lt;= columnTitle.length &lt;= 7`
# 	
# - `columnTitle` consists only of uppercase English letters.
# 	
# - `columnTitle` is in the range `[&quot;A&quot;, &quot;FXSHRXW&quot;]`.
#
# ====== SOLUTION ======

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        a = 0
        for x in columnTitle:
            a = a*26+(ord(x)-ord('A')+1)
        return a
