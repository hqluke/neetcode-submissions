class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = ''.join(filter(str.isalnum, s))   
        #racecar
        length = len(alpha)
        midLength = math.floor(length/2)
        one = ''
        two = ''
        middle = ''
        i = 0
        while i < length:
            if i < midLength:
                one = one + alpha[i]
                i += 1
                continue

            if i == midLength and length % 2 != 0:
                middle = alpha[i]
                i+=1
                continue
            two = two + alpha[i]
            i += 1
        two = two[::-1]

        if one.lower() == two.lower():
            return True
        else:
            return False
            

