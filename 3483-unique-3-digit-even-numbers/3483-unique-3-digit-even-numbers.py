class Solution:
    def totalNumbers(self, d: List[int]) -> int:
        ans = []
        for p in permutations(d,3):
            s=""
            for x in p:
                s+=str(x)
            if int(s) not in ans and int(s)%2==0 :
                a = int(s)
                if len(str(a))==3:
                    ans.append(int(s))
            s=""
        
        return len(ans)