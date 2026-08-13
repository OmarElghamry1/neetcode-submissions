class MinStack:

    def __init__(self):
        self.length = 0
        self.arr = []


    def push(self, val: int) -> None:
        self.arr.insert(self.length, val)
        self.length += 1

    def pop(self) -> None:
        poped = self.arr[-1]
        self.arr[:] = self.arr[:-1]
        self.length -=1
        return poped

    def top(self) -> int:
        return self.arr[-1]
        

    def getMin(self) -> int:
        min = self.arr[0]
        for i in self.arr:
            if i < min: 
                min = i
        return min
            
        
