class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # default dict of lists
        result = defaultdict(list)
        #loop through the strs list
        for s in strs:
            #create list with nums 0 - 25
            count = [0] * 26
            # loop through each char in string
            for c in s:
                # for every char write to the char position in count + 1
                count[ord(c) - ord("a")] += 1
            # have string as value, and count as key
            # have to cast count to tuple because dicts can't have lists as keys *must be immutable*
            result[tuple(count)].append(s)
        #return a list of the list of values
        return list(result.values())