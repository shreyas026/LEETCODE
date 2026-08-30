class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n ==0:
            return False
        else:
            return n and not (n & n - 1)