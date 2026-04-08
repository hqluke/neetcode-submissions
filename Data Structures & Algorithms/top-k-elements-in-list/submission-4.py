class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        bucket = defaultdict(list)
        res = []

        for x in nums:
            dict[x] = 1 + dict.get(x, 0)
        for key,v in dict.items():
            bucket[v].append(key)
        for freq in range(len(nums), -1, -1):
            if freq in bucket:
                for num in bucket[freq]:
                    res.append(num)
                    if len(res) == k:
                        return res
        return res
