class Solution:
    def findMin(self, nums: List[int]) -> int:
        # setup result with random number from list so we can compare it later
        res = nums[0]
        # left and right pointers
        l,r = 0, len(nums)-1
        while l <= r:
            # if nums[l] < nums[r], the min number is guarenteed to either be the previous middle value
            # that's stored in res, or nums[l]
            # break out of loop and return value if so
            if nums[l] < nums[r]:
                res = min(res,nums[l])
                break
            # calculate the middle (integer division)
            m = (l+r) // 2
            # compare res to nums[m] because this is the value we're pivoting off of
            res = min(res,nums[m])
            # see which side has the smaller values and then interate over the smaller side
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res
