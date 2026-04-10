class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights) - 1
        res = 0
        while l < r:
            # calc area
            area = (r-l) * min(heights[l], heights[r])
            # move pointer based on which is higher
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            res = max(res,area)
        return res
            
                




