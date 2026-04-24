class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # we need two hashmaps 1 for number of t's char in curr window.
        # other for total number of t chars
        if len(s) < len(t):
            return ""

        curr = {}
        count = {}
        # populate count
        for v in t:
            count[v] = 1 + count.get(v, 0)
        # count is populated
        # need to loop through S from left to right with two pointers
        # move right if window doesn't have all of t's chars
        # check current r and see if it's in count, if so + 1 to curr[r]
        # check if we have all the chars
        # once we have them all, store current window s[l:r+1] (+1 to store current r char)
        # move window left, decrement curr[l] count if it's in count, 
        # try and update min window if it can be removed without decrementing curr[l]
        # if window is smaller(check with r-l + 1 < len(res)) update res to s[l:r+1]
        # once we don't have enough chars in current window, start moving right again
        # return once we hit end of window
        res = ""
        l = 0
        have = 0
        # need distinct keys, could have repeating chars in T
        need = len(count)
        for r in range(len(s)):
            # update curr window count if s[r] in count
            if s[r] in count.keys():
                curr[s[r]] = 1 + curr.get(s[r], 0)
                # check if curr window and count have same chars of r
                # +1 to have if so (curr[s[r]] value gets updated before we check, allowing for this)
                if curr[s[r]] == count[s[r]]:
                    have += 1
                # decrement left to try and get smaller window if we have what we need
                while have == need:
                    # if res="" or curr window is smaller, update res
                    if not res or len(res) > (r-l) + 1:
                        # update res
                        res = s[l:r+1]
                    # check if left char is in count and decrement curr[l] if so
                    if s[l] in count:
                        # check if the values equal each other, decrement have if so
                        if curr[s[l]] == count[s[l]]:
                            have -= 1
                        curr[s[l]] -= 1
                    # move right regardless
                    l += 1
        return res                
                


                