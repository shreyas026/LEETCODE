# =========================================
# 387. First Unique Character in a String
# =========================================
# Difficulty: Easy
#
# Given a string `s`, find the **first** non-repeating character in it and return its index. If it **does not** exist, return `-1`.
#
#  
#
# **Example 1:**
#
# **Input:** s = &quot;leetcode&quot;
#
# **Output:** 0
#
# **Explanation:**
#
# The character `&#39;l&#39;` at index 0 is the first character that does not occur at any other index.
#
# **Example 2:**
#
# **Input:** s = &quot;loveleetcode&quot;
#
# **Output:** 2
#
# **Example 3:**
#
# **Input:** s = &quot;aabb&quot;
#
# **Output:** -1
#
#  
#
# **Constraints:**
#
# 	
# - `1 &lt;= s.length &lt;= 10^5`
# 	
# - `s` consists of only lowercase English letters.
#
# ====== SOLUTION ======

class Solution:
    def firstUniqChar(self, s: str) -> int:
        a=Counter(s)
        for x in s:
            if a[x]==1:
                return s.index(x)
                break
        return -1
