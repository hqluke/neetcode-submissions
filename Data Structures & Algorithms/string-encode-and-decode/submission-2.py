class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        # make string so it's like "2#hi5#world"
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            # go through till j is on the #
            while s[j] != '#':
                j += 1
            # ex string: "2#hi5#world"
            # get length of string    
            length = int(s[i:j])
            # set i = j + 1 (first letter)
            i = j + 1
            # j = end of word
            j = i + length
            # append whole word - handles end of word aswell by going 1 past
            res.append(s[i:j])
            # get ready for next word
            i = j

        return res
        

