from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #check if strs are diff lengths
        if len(s) != len(t):
            return False

        # Create two dictionaries and populate with s and t
        one = defaultdict(int)
        two = defaultdict(int)
        # Populate dicts
        for x in s:
             one[x] += 1
        for x in t:
            two[x] += 1
        # Compare length of dicts
        for x in s:
            if one[x] != two[x]:
                return False;
        return True;
        
           
            


