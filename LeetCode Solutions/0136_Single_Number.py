# ====================
# 136. Single Number
# ====================
# Difficulty: Easy
#
# Given a **non-empty** array of integers `nums`, every element appears *twice* except for one. Find that single one.
#
# You must implement a solution with a linear runtime complexity and use only constant extra space.
#
#  
#
# **Example 1:**
#
# **Input:** nums = [2,2,1]
#
# **Output:** 1
#
# **Example 2:**
#
# **Input:** nums = [4,1,2,1,2]
#
# **Output:** 4
#
# **Example 3:**
#
# **Input:** nums = [1]
#
# **Output:** 1
#
#  
#
# **Constraints:**
#
# 	
# - `1 &lt;= nums.length &lt;= 3 * 10^4`
# 	
# - `-3 * 10^4 &lt;= nums[i] &lt;= 3 * 10^4`
# 	
# - Each element in the array appears twice except for one element which appears only once.
#
# ====== SOLUTION ======

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a=0
        for x in nums:
            a^=x
        return a
