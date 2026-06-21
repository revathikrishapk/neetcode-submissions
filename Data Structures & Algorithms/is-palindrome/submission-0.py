class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        l=0
        r=len(s)-1
        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
                return True
        return False
