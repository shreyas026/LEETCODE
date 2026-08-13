# =====================================================
# 3090. Maximum Length Substring With Two Occurrences
# =====================================================
# Difficulty: Easy
#
# Given a string `s`, return the **maximum** length of a substring such that it contains *at most two occurrences* of each character.
#
#  
#
# **Example 1:**
#
# **Input:** s = &quot;bcbbbcba&quot;
#
# **Output:** 4
#
# **Explanation:**
#
# The following substring has a length of 4 and contains at most two occurrences of each character: `&quot;bcbbbcba&quot;`.
#
# **Example 2:**
#
# **Input:** s = &quot;aaaa&quot;
#
# **Output:** 2
#
# **Explanation:**
#
# The following substring has a length of 2 and contains at most two occurrences of each character: `&quot;aaaa&quot;`.
#
#  
#
# **Constraints:**
#
# 	
# - `2 &lt;= s.length &lt;= 100`
# 	
# - `s` consists only of lowercase English letters.
#
# ====== SOLUTION ======

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        res = l = 0
        fq = defaultdict(int)

        for r, ch in enumerate(s):
            fq[ch] += 1
            while fq[ch] > 2:
                fq[s[l]] -= 1
                l += 1
                
            res = max(res, r - l + 1)

        return res
