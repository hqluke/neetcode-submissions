class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert to set to get O(1) look ups and have no repeated values
        numSet = set(nums)
        longest = 0
        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest