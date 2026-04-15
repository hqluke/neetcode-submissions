class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # loop through, store the items in a set
        # left pointer acts as the start of the substring
        # right slides
        check = set()
        res = 0
        l = 0
        for r in range(len(s)):
            while s[r] in check:
                check.remove(s[l])
                l += 1
            check.add(s[r])
            res = max(res,len(check))
        return res
        