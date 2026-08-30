class Solution:
    def shuffle(self, a: List[int], n: int) -> List[int]:
        l = a[:n]
        r = a[n:]
        ans = []
        for i in range(n):
            ans.append(l[i])
            ans.append(r[i])
        return ans