class MinHeap:

    def __init__(self):
        self.heap = [0]

    def push(self, val: int) -> None:
        ## percolate up
        if len(self.heap) == 1:
            return self.heap.append(val)

        self.heap.append(val)
        i = len(self.heap) - 1

        # while child is smaller than parent
        while i > 1 and self.heap[i] < self.heap[i // 2]:
            self.heap[i], self.heap[i // 2] = \
                self.heap[i // 2], self.heap[i]

            i = i // 2

    def pop(self) -> int:
        if len(self.heap) == 1:
            return -1

        # one element
        if len(self.heap) == 2:
            return self.heap.pop()

        res = self.heap[1]

        self.heap[1] = self.heap.pop()

        len_heap = len(self.heap) 

        i = 1

        while i * 2 < len_heap:
            left = i * 2  # left child
            right = left + 1  # right child
            smallest = i  # parent

            if self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < len_heap and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == i:
                break

            # swap
            self.heap[i], self.heap[smallest] = \
                self.heap[smallest], self.heap[i]
            i = smallest

        return res

    def top(self) -> int:
        if len(self.heap) == 1:
            return -1
        else:
            return self.heap[1]

    def heapify(self, nums: List[int]) -> None:

        if len(nums) == 0:
            return

        self.heap = [0] + nums

        i = (len(self.heap) - 1) // 2  # first node with parent

        len_heap = len(self.heap) 

        while i > 0:
            cur = i
            while cur * 2 < len_heap:

                left = cur * 2
                right = left + 1
                smallest = cur

                if self.heap[left] < self.heap[smallest]:
                    smallest = left

                if right < len_heap and self.heap[right] < self.heap[smallest]:
                    smallest = right

                if smallest == cur:
                    break

                self.heap[cur], self.heap[smallest] = \
                    self.heap[smallest], self.heap[cur]

                cur = smallest

            i -= 1  # move to the next parent

        return










