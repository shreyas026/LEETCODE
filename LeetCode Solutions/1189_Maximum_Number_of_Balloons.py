# ==================================
# 1189. Maximum Number of Balloons
# ==================================
# Difficulty: Easy
#
# Given a string `text`, you want to use the characters of `text` to form as many instances of the word **&quot;balloon&quot;** as possible.
#
# You can use each character in `text` **at most once**. Return the maximum number of instances that can be formed.
#
#  
#
# **Example 1:**
#
# **[]**
#
# **Input:** text = &quot;nlaebolko&quot;
# **Output:** 1
#
# ```
#
# **Example 2:**
#
# **[]**
#
# **Input:** text = &quot;loonbalxballpoon&quot;
# **Output:** 2
#
# ```
#
# **Example 3:**
#
# **Input:** text = &quot;leetcode&quot;
# **Output:** 0
#
# ```
#
#  
#
# **Constraints:**
#
# 	
# - `1 &lt;= text.length &lt;= 10^4`
# 	
# - `text` consists of lower case English letters only.
#
#  
#
# **Note:** This question is the same as 2287: Rearrange Characters to Make Target String.
#
# ====== SOLUTION ======

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        return min(
            text.count('b'),
            text.count('a'),
            text.count('l') // 2,
            text.count('o') // 2,
            text.count('n')
        )
