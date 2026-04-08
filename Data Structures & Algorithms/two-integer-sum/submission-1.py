class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        one = {}
        # populate dict with target - value
        for k,v in enumerate(nums):
            one[k] = target - v
        #search the dict and try to match with needed number in nums
        for k,v in one.items():
            for i, o in enumerate(nums):
                if k != i and one[k] == nums[i]:
                    return [k,i]