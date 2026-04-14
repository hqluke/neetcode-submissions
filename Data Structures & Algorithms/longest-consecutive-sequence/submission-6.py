class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for i in s:
            if i - 1 not in s:
                temp = i
                count = 1
                while temp + 1 in s:
                    temp += 1
                    count += 1
                res = max(res, count)
        return res