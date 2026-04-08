class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        freq =[[] for i in range(len(nums) + 1)]
        res = []

        for i in nums:
            dict[i] = 1 + dict.get(i, 0)
        
        for num, count in dict.items():
            freq[count].append(num)

        for i in range(len(freq) -1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

