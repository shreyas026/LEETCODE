# ============================================================
# 1358. Number of Substrings Containing All Three Characters
# ============================================================
# Difficulty: Medium
#
# Given a string `s` consisting only of characters *a*, *b* and *c*.
#
# Return the number of substrings containing at least one occurrence of all these characters *a*, *b* and *c*.
#
#  
#
# **Example 1:**
#
# **Input:** s = &quot;abcabc&quot;
# **Output:** 10
# **Explanation:** The substrings containing at least one occurrence of the characters *a*, *b* and *c are &quot;*abc*&quot;, &quot;*abca*&quot;, &quot;*abcab*&quot;, &quot;*abcabc*&quot;, &quot;*bca*&quot;, &quot;*bcab*&quot;, &quot;*bcabc*&quot;, &quot;*cab*&quot;, &quot;*cabc*&quot; *and* &quot;*abc*&quot; *(**again**)*. *
#
# ```
#
# **Example 2:**
#
# **Input:** s = &quot;aaacb&quot;
# **Output:** 3
# **Explanation:** The substrings containing at least one occurrence of the characters *a*, *b* and *c are &quot;*aaacb*&quot;, &quot;*aacb*&quot; *and* &quot;*acb*&quot;.** *
#
# ```
#
# **Example 3:**
#
# **Input:** s = &quot;abc&quot;
# **Output:** 1
#
# ```
#
#  
#
# **Constraints:**
#
# 	
# - `3 &lt;= s.length &lt;= 5 x 10^4`
# 	
# - `s` only consists of `&#39;a&#39;`, `&#39;b&#39;` or `&#39;c&#39;` characters.
#
# ====== SOLUTION ======

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last_pos = {'a': -1, 'b': -1, 'c': -1}
        count = 0
        
        for right, char in enumerate(s):
            last_pos[char] = right
            
            if last_pos['a'] != -1 and last_pos['b'] != -1 and last_pos['c'] != -1:
                count += min(last_pos['a'], last_pos['b'], last_pos['c']) + 1
                
        return count
