class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # key as char
        # value as index of char when it was most recently seen
        h = {}
        l = 0
        res = 0
        # loop through s by index
        for r in range(len(s)):
            # check if the current character is a key in the hash map
            if s[r] in h:
                # if it is, move the left pointer to one index above where it was last seen
                # or previous l if the stored value in hashmap is smaller (ensuring we only move forward)
                l = max(h[s[r]] + 1, l)
            # set key as char
            # set value to the chars most recent index
            h[s[r]] = r
            # update res
            res = max(res, (r-l) + 1)
        return res
        