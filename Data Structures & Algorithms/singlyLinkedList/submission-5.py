class Node: 
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next
        

class LinkedList:
    def __init__(self):
        self.head = None
        
        
    def get(self, index: int) -> int:
        if not self.head: 
            return -1
        
        i = 0
        cur = self.head
        while True: 
            if i == index: 
                return cur.data
            cur = cur.next
            i += 1
            if cur is None: 
                break
        return -1

        
    def insertHead(self, val: int) -> None:
        if not self.head: 
            self.head = Node(val)
            return 
        
        node = Node(val, self.head)
        self.head = node
        return 
        

    def insertTail(self, val: int) -> None:
        if not self.head: 
            self.insertHead(val)
            return 
        
        cur = self.head
        while cur.next: 
            cur = cur.next
        
        cur.next = Node(val)
        return 
        
    
    def remove(self, index: int) -> bool:
        if not self.head: 
            return False

        if index == 0: 
            self.head = self.head.next
            return True

        i = 0
        cur = self.head
        while cur: 
            if i + 1 == index: 
                if cur.next: 
                    cur.next = cur.next.next
                    return True
                else: 
                    cur.next = None
                    return False
            cur = cur.next
            i += 1
        return False

    def getValues(self) -> List[int]:
        res = []
        cur = self.head

        while cur: 
            res.append(cur.data)
            cur = cur.next

        return res
        

    
        
        
        

    
        