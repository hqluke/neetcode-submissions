class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list = []
        for x in nums:
            if x in list:
                return True;
            list.append(x)
        return False;
        