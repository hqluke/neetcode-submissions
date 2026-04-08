class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # create list size of nums
        res = [1] * len(nums)
        # store prefix numbers
        # ex nums = [1,2,4,6]
        # res = [1,1,2,8]
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        # multiply by postfix going backwards, rightside gets solved first
        # ex continued 
        #nums = [1,2,4,6]
        # res = [1,1,2,8]
        # res = [48,24,12,8]
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix 
            postfix *= nums[i]

        return res



        