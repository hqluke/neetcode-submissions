class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        res = 0

        # allows us to return when the middle == target
        # can go all the way down to l=r and that value would be the middle value
        while l <= r:
            # middle check
            mid = (r+l) // 2
            if nums[mid] == target:
                return mid

            # find pivot point
            if nums[l] <= nums[mid]:
                # find which side target is on
                # target on right side
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                # target on left side
                else:
                    r = mid - 1

            else:
                # target on left side
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                # target on right side
                else:
                    l = mid + 1
        return -1
