# ================================================
# 3739. Count Subarrays With Majority Element II
# ================================================
# Difficulty: Hard
#
# You are given an integer array `nums` and an integer `target`.
#
# Return the number of **subarrays** of `nums` in which `target` is the **majority element**.
#
# The **majority element** of a subarray is the element that appears **strictly more than half** of the times in that subarray.
#
#  
#
# **Example 1:**
#
# **Input:** nums = [1,2,2,3], target = 2
#
# **Output:** 5
#
# **Explanation:**
#
# Valid subarrays with `target = 2` as the majority element:
#
# 	
# - `nums[1..1] = [2]`
# 	
# - `nums[2..2] = [2]`
# 	
# - `nums[1..2] = [2,2]`
# 	
# - `nums[0..2] = [1,2,2]`
# 	
# - `nums[1..3] = [2,2,3]`
#
# So there are 5 such subarrays.
#
# **Example 2:**
#
# **Input:** nums = [1,1,1,1], target = 1
#
# **Output:** 10
#
# **Explanation: **
#
# **​​​​​​​**All 10 subarrays have 1 as the majority element.
#
# **Example 3:**
#
# **Input:** nums = [1,2,3], target = 4
#
# **Output:** 0
#
# **Explanation:**
#
# `target = 4` does not appear in `nums` at all. Therefore, there cannot be any subarray where 4 is the majority element. Hence the answer is 0.
#
#  
#
# **Constraints:**
#
# 	
# - `1 &lt;= nums.length &lt;= 10^​​​​​​​5`
# 	
# - `1 &lt;= nums[i] &lt;= 10^​​​​​​​9`
# 	
# - `1 &lt;= target &lt;= 10^9`
#
# ====== SOLUTION ======

class BinaryIndexedTree:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, i, v):
        while i <= self.n:
            self.bit[i] += v
            i += i & -i

    def query(self, i):
        s = 0
        while i:
            s += self.bit[i]
            i -= i & -i
        return s


class Solution:
    def countMajoritySubarrays(self, nums, target):
        if target not in nums:
            return 0

        n = len(nums)
        bit = BinaryIndexedTree(2 * n + 1)
        s = n + 1
        bit.update(s, 1)
        ans = 0

        for x in nums:
            if x == target:
                s += 1
            else:
                s -= 1
            ans += bit.query(s - 1)
            bit.update(s, 1)

        return ans
