# =================================
# 345. Reverse Vowels of a String
# =================================
# Difficulty: Easy
#
# Given a string `s`, reverse only all the vowels in the string and return it.
#
# The vowels are `&#39;a&#39;`, `&#39;e&#39;`, `&#39;i&#39;`, `&#39;o&#39;`, and `&#39;u&#39;`, and they can appear in both lower and upper cases, more than once.
#
#  
#
# **Example 1:**
#
# **Input:** s = &quot;IceCreAm&quot;
#
# **Output:** &quot;AceCreIm&quot;
#
# **Explanation:**
#
# The vowels in `s` are `[&#39;I&#39;, &#39;e&#39;, &#39;e&#39;, &#39;A&#39;]`. On reversing the vowels, s becomes `&quot;AceCreIm&quot;`.
#
# **Example 2:**
#
# **Input:** s = &quot;leetcode&quot;
#
# **Output:** &quot;leotcede&quot;
#
#  
#
# **Constraints:**
#
# 	
# - `1 &lt;= s.length &lt;= 3 * 10^5`
# 	
# - `s` consist of **printable ASCII** characters.
#
# ====== SOLUTION ======

class Solution:
    def reverseVowels(self, s: str) -> str:
        a=list(s)
        j=len(s)-1
        i=0
        while i<j:
            if a[i] not in "aeiouAEIOU":
                i+=1
            if a[j] not in "aeiouAEIOU":
                j-=1
            if a[i] in "aeiouAEIOU" and a[j] in "aeiouAEIOU":
                a[i],a[j]=a[j],a[i]
                i+=1
                j-=1
        ans=""
        for x in a:
            ans+=x
        return ans
