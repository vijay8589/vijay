class Node:
    def __int__(self, data):
        self.data = data
        self.ref  = None

class LinkedList:
    def __int__(self):
        self.head = None



def add_end(self, data):
    new_node = Node(data)
    if self.head is None:
        self.head = new_node
    else:
        n = self.head
        while n.ref is not None:
            n = n.ref
        n.ref = new_node

LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_end(100)
LL1.add_begin(20)
LL1.Print_LL()