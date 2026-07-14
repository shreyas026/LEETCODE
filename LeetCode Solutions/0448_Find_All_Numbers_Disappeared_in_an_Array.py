# ===============================================
# 448. Find All Numbers Disappeared in an Array
# ===============================================
# Difficulty: Easy
#
# Given an array `nums` of `n` integers where `nums[i]` is in the range `[1, n]`, return *an array of all the integers in the range* `[1, n]` *that do not appear in* `nums`.
#
#  
#
# **Example 1:**
#
# **Input:** nums = [4,3,2,7,8,2,3,1]
# **Output:** [5,6]
#
# ```
#
# **Example 2:**
#
# **Input:** nums = [1,1]
# **Output:** [2]
#
# ```
#
#  
#
# **Constraints:**
#
# 	
# - `n == nums.length`
# 	
# - `1 &lt;= n &lt;= 10^5`
# 	
# - `1 &lt;= nums[i] &lt;= n`
#
#  
#
# **Follow up:** Could you do it without extra space and in `O(n)` runtime? You may assume the returned list does not count as extra space.
#
# ====== SOLUTION ======

class Solution(object):
    def findDisappearedNumbers(self, nums):
        s = set(nums)
        b=[]
        for i in range(1,len(nums)+1):
            if i not in s:
                b.append(i)
        return b
