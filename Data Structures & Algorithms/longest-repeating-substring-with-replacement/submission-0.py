class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # use a hashmap 
        # for each char store count
        count = {}
        l = 0
        res = 0
        for r in range(len(s)):
            # update count for each char
            count[s[r]] = 1 + count.get(s[r], 0)
            # shift over if chars needing replacement (window length - most freq char) > chars we're able to replace
            if(r-l + 1) - max(count.values()) > k:
                # decrement the count of left value
                count[s[l]] -= 1
                # shift over left value
                l += 1
            # store previous valid window length (if we shifted L) or just current window length (no shift)
            res = max(res, r-l + 1)

        return res

            
            

        