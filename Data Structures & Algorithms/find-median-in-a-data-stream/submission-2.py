class MedianFinder:

    def __init__(self):
        self.arr = []
        

    def addNum(self, num: int) -> None:
        self.arr.append(float(num))

    def findMedian(self) -> float:
        self.arr.sort()
        length = len(self.arr)
        if length < 1:
            return
        if length == 1:
            return self.arr[0]
        isEven = length % 2 == 0
        if isEven:
            return ((self.arr[length // 2] + self.arr[length // 2 - 1]) / 2)
        else:
            #[4,3,8,5,7] 5
            #[0,1,2,3,4]
            return self.arr[length//2]
            