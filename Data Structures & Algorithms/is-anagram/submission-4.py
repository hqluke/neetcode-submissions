class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #check if strs are diff lengths
        if len(s) != len(t):
            return False

        # Create two dictionaries and populate with s and t
        one, two = {}, {}
        # Populate dicts
        for i in range(len(s)):
            # say word is test
            # one[s[i]] = one[t]
            # it would then get populated to 1 because we add 1 to the default 0 which we defined through the get
            one[s[i]] = 1 + one.get(s[i], 0)
            two[t[i]] = 1 + two.get(t[i], 0)
        # Check if they're equal
        return one == two
        
           
            


