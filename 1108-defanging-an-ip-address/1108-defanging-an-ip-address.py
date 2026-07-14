# ===============================
# 1108. Defanging an IP Address
# ===============================
# Difficulty: Easy
#
# Given a valid (IPv4) IP `address`, return a defanged version of that IP address.
#
#
#
# A *defanged IP address* replaces every period `&quot;.&quot;` with `&quot;[.]&quot;`.
#
#
#
#  
#
#
# **Example 1:**
#
#
# **Input:** address = "1.1.1.1"
# **Output:** "1[.]1[.]1[.]1"
#
# ```
#
# **Example 2:**
#
#
# **Input:** address = "255.100.50.0"
# **Output:** "255[.]100[.]50[.]0"
#
# ```
#
#
#  
#
#
# **Constraints:**
#
#
#
#
# 	
# - The given `address` is a valid IPv4 address.
#
# ====== SOLUTION ======

class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        ans=""
        for x in address:
            if x=='.':
                ans+="[.]"
            else:
                ans+=x
        return ans
