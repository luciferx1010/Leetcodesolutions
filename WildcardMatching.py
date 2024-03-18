class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i,j,si,m=0,0,-1,0
        while i<len(s):
            if j<len(p) and (s[i]==p[j] or p[j]=='?'):
                j+=1
                i+=1
            elif j<len(p) and p[j]=='*':
                si=j
                m=i
                j+=1
            elif si!=-1:
                j=si+1
                m+=1
                i=m
            else:
                return False
        while j<len(p) and p[j]=='*':
            j+=1
        return j==len(p)
      