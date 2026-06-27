class MedianFinder:

    def __init__(self):
        self.arr = []
        

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        self.arr.sort()
        length = len(self.arr)
        # if last bit of length is a 1 (IE odd number), just take middle num of array
            # (length & 1) does a bitwise and check on lowest bit position (IE the far right bit), 
            # if it is a 1, it's odd. It'll return a 1 which == True in python
        # if its even, we take the middle pos and middle pos -1 and add those then divide by 2
        return (self.arr[length // 2] if (length & 1) else
                (self.arr[length // 2] + self.arr[length // 2 - 1]) / 2)
            