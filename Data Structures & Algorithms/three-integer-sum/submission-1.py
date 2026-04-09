class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # sort it so we can always iterate from left to right:
        # a + (l + r) == 0 ?
        nums.sort()

        for i,a in enumerate(nums):
            # if we're past the first loop and nums are same advance.
            if i > 0 and a == nums[i-1]:
                continue
            # set pointers to 1 ahead of a, and back length
            l = i + 1
            r = len(nums) - 1
            while l < r:
                # set sum = all three values
                threeSum = a + nums[l] + nums[r]
                # if value too large move right pointer to the left
                if threeSum > 0:
                    r -= 1
                # if value too small, move left pointer to the right
                elif threeSum < 0:
                    l += 1
                else:
                    # == 0? append it to res and keep checking
                    res.append([a,nums[l], nums[r]])
                    # continue checking if a matches any other positions
                    l += 1
                    r -= 1
                    # make sure left isn't a duplicate
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res

        