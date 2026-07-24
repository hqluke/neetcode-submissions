class Solution:
    def rob(self, nums: List[int]) -> int:
        # only taking starting val (always atleast 1 val),
        # 1 through end of arr
        # 0 through arr-1
        return max(nums[0], self.finder(nums[1:]),
                            self.finder(nums[:-1]))
    # calc all possibilities
    def finder(self,numsArr):
        rob1, rob2 = 0,0
        for n in numsArr:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
