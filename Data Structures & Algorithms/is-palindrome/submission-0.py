class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0 
        j = len(s)-1
        s1=s.lower()
        while(i<j):
            if not s1[i].isalnum():
                i+=1
                continue
            elif not s1[j].isalnum():
                j-=1
                continue
            if s1[i]!=s1[j]:
                return False
            else :
                i+=1
                j-=1
        return True