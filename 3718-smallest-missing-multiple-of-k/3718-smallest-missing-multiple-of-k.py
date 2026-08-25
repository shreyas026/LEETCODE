from typing import List

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        p = set(nums)

        mul = k

        while mul in p:
            mul += k

        return mul