class Node: 
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        
    def get(self, index: int) -> int:
        cur = self.head
        i = 0
        while cur: 
            if i == index: 
                return cur.data

            cur = cur.next
            i += 1
            
        
        return -1

        
    def insertHead(self, val: int) -> None:
        if not self.head: 
            self.head = Node(val)
            return 
        
        node = Node(val, next=self.head)
        self.head = node
        return 


    def insertTail(self, val: int) -> None:
        if not self.head: 
            self.head = Node(val)
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
    
        cur = self.head
        i = 0
        while cur: 
            if i == index - 1: 
                # last_element
                if not cur.next: 
                    return False
                else: 
                    cur.next = cur.next.next
                    return True
            
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
        

    
        