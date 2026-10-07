class MinHeap:

    def __init__(self):
        self.heap = [0]

    def push(self, val: int) -> None:
        if len(self.heap) <= 1: 
            self.heap.append(val)
            return 
        
        self.heap.append(val)
        index = len(self.heap) - 1
        self._percolate_up(index)

        
     
    def pop(self) -> int:
        if len(self.heap) == 1: 
            return -1
        
        if len(self.heap) == 2: 
            return self.heap.pop()
        
        res = self.heap[1]
        self.heap[1] = self.heap.pop()
        self._percolate_down(1)
        return res



    def top(self) -> int:
        if len(self.heap) <= 1: 
            return -1
        
        return self.heap[1]
        

    def heapify(self, nums: List[int]) -> None:
        self.heap = [0] + nums

        # first parent node
        index = (len(self.heap) - 1) // 2

        while index > 0: 
            self._percolate_down(index)
            index -= 1
        
    def _percolate_up(self, i: int): 
        # while child is less than parent
        while i > 1 and self.heap[i] < self.heap[i // 2]: 
            self.heap[i], self.heap[i // 2] = \
                self.heap[i // 2], self.heap[i]
            i = i // 2
    

    def _percolate_down(self, i: int): 
        len_heap = len(self.heap)

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

            self.heap[i], self.heap[smallest] = \
                self.heap[smallest], self.heap[i]
            
            i = smallest




        

    
    


    

    
            
    
  

        


