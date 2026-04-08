class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Set pointer for left and right
        l,r = 0, len(s)-1

        while l < r:
            
            while l < r and not self.isAlpha(s[l]):
                l += 1

            while r > l and not self.isAlpha(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l = l + 1
            r = r - 1
        return True



    #helper function to only get alpha numeric chars
    def isAlpha(self,c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

        