class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        start = []
        count = 0
        maxnum = 0
        for k,v in enumerate(nums):
            if v == 0 and v+1 in nums:
                start.append(v)
            if v > count:
                if v-1 not in nums:
                    count = v
                    start.append(v)

        final = 0
        for i in nums:
            lcs = 1
            curr = i
            while curr + 1 in nums:
                lcs += 1
                curr += 1
            if lcs > final:
                final = lcs
        return final

            
        