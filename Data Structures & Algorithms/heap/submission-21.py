class MinHeap:

    def __init__(self):
        self.heap = [0]

    def push(self, val: int) -> None:

        if len(self.heap) == 1: 
            self.heap.append(val)
            return 
        
        
        self.heap.append(val)
        len_heap = len(self.heap)

        i = len_heap - 1

        while i > 1 and self.heap[i] < self.heap[i // 2]: 

            self.heap[i], self.heap[i // 2] = \
                self.heap[i // 2], self.heap[i]

            i = i // 2

        return 
        

    def pop(self) -> int:

        if len(self.heap) == 1: 
            return -1
        
        if len(self.heap) == 2: 
            return self.heap.pop()
        
        res = self.heap[1]

        self.heap[1] = self.heap.pop()

        len_heap = len(self.heap)

        i = 1

        while i * 2 < len_heap: 
            left = i * 2
            right = left + 1
            smallest = i 

            if self.heap[left] < self.heap[smallest]: 
                smallest = left
            
            if right < len_heap and self.heap[right] < self.heap[smallest]: 
                smallest = right
            
            if i == smallest: 
                break 
            
            self.heap[smallest], self.heap[i] = \
                self.heap[i], self.heap[smallest]
            
            i = smallest

        return res



    def top(self) -> int:
        if len(self.heap) == 1: 
            return -1

        return self.heap[1]


    def heapify(self, nums: List[int]) -> None:

        self.heap = [0] + nums

        len_heap = len(self.heap) 

        cur = (len_heap - 1) // 2 # first node with parent

        while cur > 0: 
            i = cur
            while i * 2 < len_heap: 
                left = i * 2
                right = left + 1
                smallest = i 

                if self.heap[left] < self.heap[smallest]: 
                    smallest = left
                
                if right < len_heap and self.heap[right] < self.heap[smallest]: 
                    smallest = right
                
                if i == smallest: 
                    break 
                
                self.heap[smallest], self.heap[i] = \
                    self.heap[i], self.heap[smallest]
                
                i = smallest

            cur -= 1 # next parent



