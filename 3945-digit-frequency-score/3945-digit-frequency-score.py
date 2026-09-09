class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        f={}
        for i in str(n):
            f[i]=f.get(i,0)+1
        a=0
        for i,j in f.items():
            a+=int(i)*j
        return a