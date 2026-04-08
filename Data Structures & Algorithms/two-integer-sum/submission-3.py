class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        one = {}
        # loop through nums
        for k,v in enumerate(nums):
            # find difference in numbers
            diff = target - v
            # if that diffs in the dict return the position it was found, current index
            if diff in one:
                return [one[diff], k]
            # otherwise store the value as the key, key as value
            one[v] = k