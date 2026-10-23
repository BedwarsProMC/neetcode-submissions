class ListNode:
    def __init__(self, val = None):
        self.val = val # integer
        self.next = None # ListNode

class LinkedList:
    
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    
    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            # raise IndexError('index out of bounds')
            return -1
        
        curr = self.head

        step = 0
        while step < index:
            curr = curr.next
            step += 1

        return curr.val
        

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)

        if self.length == 0:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)

        if self.length == 0:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
    

    def _get_node(self, index: int) -> ListNode:
        if index < 0 or index >= self.length:
            raise IndexError('index out of bounds')
        
        curr = self.head

        step = 0
        while step < index:
            curr = curr.next
            step += 1

        return curr

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.length:
            return False

        if index == 0:
            # remove head
            if self.length == 1:
                self.head = self.tail = None
            else:
                self.head = self.head.next

        elif index == self.length - 1:
            # return tail
            if self.length == 1:
                self.head = self.tail = None
            else:
                previous = self._get_node(self.length - 2) # NODE BEFORE CURRENT TAIL
                previous.next = None
                self.tail = previous
        else:
            # remove node in midst of list
            if self.length == 1:
                self.head = self.tail = None
            else:
                previous = self._get_node(index - 1)
                current = self._get_node(index)

                previous.next = current.next
                current.next = None

        self.length -= 1
        return True


    def getValues(self) -> List[int]:
        output = []

        curr = self.head
        while curr:
            output.append(curr.val)
            curr = curr.next

        return output




        
