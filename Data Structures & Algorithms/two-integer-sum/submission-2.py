class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        one = {}
        # loop through nums
        for k,v in enumerate(nums):
            diff = target - v
            if diff in one:
                return [one[diff], k]
            one[v] = k