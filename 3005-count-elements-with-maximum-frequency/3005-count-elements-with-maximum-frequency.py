class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        f={}
        for i in nums:
            f[i]=f.get(i,0)+1
        print(f)
        s=0
        a = max(f.values())
        for x in f.values():
            if x == a:
                s+=x
        return s