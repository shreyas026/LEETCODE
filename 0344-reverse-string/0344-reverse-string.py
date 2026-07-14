# =====================
# 344. Reverse String
# =====================
# Difficulty: Easy
#
# Write a function that reverses a string. The input string is given as an array of characters `s`.
#
# You must do this by modifying the input array in-place with `O(1)` extra memory.
#
#  
#
# **Example 1:**
#
# **Input:** s = ["h","e","l","l","o"]
# **Output:** ["o","l","l","e","h"]
#
# ```
#
# **Example 2:**
#
# **Input:** s = ["H","a","n","n","a","h"]
# **Output:** ["h","a","n","n","a","H"]
#
# ```
#
#  
#
# **Constraints:**
#
# 	
# - `1 &lt;= s.length &lt;= 10^5`
# 	
# - `s[i]` is a printable ascii character.
#
# ====== SOLUTION ======

class Solution(object):
    def reverseString(self, s):
        i=0
        j=len(s)-1
        while i<j:
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
