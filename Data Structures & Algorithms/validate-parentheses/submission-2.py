class Solution:
    def isValid(self, s: str) -> bool:
        # define stack
        stack = []
        # hashmap closing to opening brackets
        co = {")" : "(", "}" : "{", "]" : "["}
        # loop through each character
        for c in s:
            # if c is a closed char see if the matching opening bracket is in the stack
            if c in co:
                # and if it is, remove it, otherwise, return false
                if stack and co[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            # if c is an open bracket, append it to the stack
            else:
                stack.append(c)
        
        return True if not stack else False
        