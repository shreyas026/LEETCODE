# ================================================================
# 1941. Check if All Characters Have Equal Number of Occurrences
# ================================================================
# Difficulty: Easy
#
# Given a string `s`, return `true`* if *`s`* is a **good** string, or *`false`* otherwise*.
#
# A string `s` is **good** if **all** the characters that appear in `s` have the **same** number of occurrences (i.e., the same frequency).
#
#  
#
# **Example 1:**
#
# **Input:** s = &quot;abacbc&quot;
# **Output:** true
# **Explanation:** The characters that appear in s are &#39;a&#39;, &#39;b&#39;, and &#39;c&#39;. All characters occur 2 times in s.
#
# ```
#
# **Example 2:**
#
# **Input:** s = &quot;aaabb&quot;
# **Output:** false
# **Explanation:** The characters that appear in s are &#39;a&#39; and &#39;b&#39;.
# &#39;a&#39; occurs 3 times while &#39;b&#39; occurs 2 times, which is not the same number of times.
#
# ```
#
#  
#
# **Constraints:**
#
# 	
# - `1 &lt;= s.length &lt;= 1000`
# 	
# - `s` consists of lowercase English letters.
#
# ====== SOLUTION ======

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        f={}
        for i in s:
            f[i]=f.get(i,0)+1
        a=[]
        for i in f.values():
            a.append(i)
        b=set(a)
        if len(b)==1:
            return True
        else:
            return False
