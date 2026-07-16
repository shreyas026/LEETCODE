# ==================
# 383. Ransom Note
# ==================
# Difficulty: Easy
#
# Given two strings `ransomNote` and `magazine`, return `true`* if *`ransomNote`* can be constructed by using the letters from *`magazine`* and *`false`* otherwise*.
#
# Each letter in `magazine` can only be used once in `ransomNote`.
#
#  
#
# **Example 1:**
#
# **Input:** ransomNote = "a", magazine = "b"
# **Output:** false
#
# ```
#
# **Example 2:**
#
# **Input:** ransomNote = "aa", magazine = "ab"
# **Output:** false
#
# ```
#
# **Example 3:**
#
# **Input:** ransomNote = "aa", magazine = "aab"
# **Output:** true
#
# ```
#
#  
#
# **Constraints:**
#
# 	
# - `1 &lt;= ransomNote.length, magazine.length &lt;= 10^5`
# 	
# - `ransomNote` and `magazine` consist of lowercase English letters.
#
# ====== SOLUTION ======

class Solution:
    def canConstruct(self, r: str, m: str) -> bool:
        s,d=Counter(r),Counter(m)
        if s&d==s:
            return True
        else:
            return False
