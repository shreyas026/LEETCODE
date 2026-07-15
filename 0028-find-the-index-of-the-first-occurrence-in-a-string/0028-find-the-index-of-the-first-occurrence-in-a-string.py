# ========================================================
# 28. Find the Index of the First Occurrence in a String
# ========================================================
# Difficulty: Easy
#
# Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.
#
#  
#
# **Example 1:**
#
# **Input:** haystack = &quot;sadbutsad&quot;, needle = &quot;sad&quot;
# **Output:** 0
# **Explanation:** &quot;sad&quot; occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
#
# ```
#
# **Example 2:**
#
# **Input:** haystack = &quot;leetcode&quot;, needle = &quot;leeto&quot;
# **Output:** -1
# **Explanation:** &quot;leeto&quot; did not occur in &quot;leetcode&quot;, so we return -1.
#
# ```
#
#  
#
# **Constraints:**
#
# 	
# - `1 &lt;= haystack.length, needle.length &lt;= 10^4`
# 	
# - `haystack` and `needle` consist of only lowercase English characters.
#
# ====== SOLUTION ======

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i=0
        k=len(haystack)-len(needle)+1
        a=-1
        for j in range(len(needle)-1,len(haystack)):
            k-=1
            if haystack[i:j+1]==needle:
                print(haystack[i:j+1])
                a=i
                break
                  
            else:
                i+=1
        return a
