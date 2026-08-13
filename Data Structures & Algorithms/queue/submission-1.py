class Node: 
    def __init__(self, val, prev=None, next=None): 
        self.val = val
        self.prev = prev
        self.next = next

class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None


    def isEmpty(self) -> bool:
        return True if not self.head else False
    

    def append(self, value: int) -> None:
        if not self.head: 
            self.head = self.tail = Node(value)
            return 
        self.tail.next = Node(value, self.tail)
        self.tail = self.tail.next
        return 

    def appendleft(self, value: int) -> None:
        if not self.head: 
            self.head = self.tail = Node(value)
            return 
        
        self.head.prev = Node(value, None, self.head)
        self.head = self.head.prev
        return 


    def pop(self) -> int:
        if not self.tail: 
            return -1
        
        if self.head == self.tail:
            val = self.tail.val
            self.head = self.tail = None
            return val



        val = self.tail.val
        self.tail.prev.next = None
        self.tail = self.tail.prev

        if not self.tail: #we removed all nodes
            self.tail = self.head = None
        
        return val
   

    def popleft(self) -> int:
        if not self.head: 
            return -1

        if self.head == self.tail:
            val = self.tail.val
            self.head = self.tail = None
            return val
        
        val = self.head.val
        self.head.next.prev = None
        self.head = self.head.next

        if not self.head: 
            self.head = self.tail = None
        return val
        
