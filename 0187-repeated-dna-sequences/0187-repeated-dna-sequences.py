class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        i = 0
        j = 10
        seen=set()
        printed=[]
        while i<j and j<=len(s):
            sub = s[i:j]
            if sub in seen and sub not in printed:
                printed.append(sub)
            else:
                seen.add(sub)
            i+=1
            j+=1
        return printed

