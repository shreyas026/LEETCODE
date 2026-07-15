# ====================
# 709. To Lower Case
# ====================
# Difficulty: Easy
#
# Given a string `s`, return *the string after replacing every uppercase letter with the same lowercase letter*.
#
#  
#
# **Example 1:**
#
# **Input:** s = &quot;Hello&quot;
# **Output:** &quot;hello&quot;
#
# ```
#
# **Example 2:**
#
# **Input:** s = &quot;here&quot;
# **Output:** &quot;here&quot;
#
# ```
#
# **Example 3:**
#
# **Input:** s = &quot;LOVELY&quot;
# **Output:** &quot;lovely&quot;
#
# ```
#
#  
#
# **Constraints:**
#
# 	
# - `1 &lt;= s.length &lt;= 100`
# 	
# - `s` consists of printable ASCII characters.
#
# ====== SOLUTION ======

class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()
