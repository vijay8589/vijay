"""Write a Python program to print a given doubly linked list in reverse order."""

class Node(object):
    # Singly linked node
    def __init__(self, data=None, next=None, prev=None):
        assert isinstance(data, object)
        self.data = data
        self.next = next
        self.prev = prev


class doubly_linked_list(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append_item(self, data: object) -> object:
        # Append an item
        new_item = Node(data, None, None)
        if self.head is None:
            self.head = new_item
            self.tail = self.head
        else:
            new_item.prev = self.tail
            self.tail.next = new_item
            self.tail = new_item
        self.count += 1

    def iter(self):
        # Iterate the list
        current = self.head
        while current:
            item_val = current.data
            current = current.next
            yield item_val

    def print_foward(self):
        for node in self.iter():
            print(node)

    def reverse(self):
        """ Reverse linked list. """
        current = self.head
        while current:
            temp = current.next
            current.next = current.prev
            current.prev = temp
            current = current.prev
        temp = self.head
        self.head = self.tail
        self.tail = temp


items = doubly_linked_list()
items.append_item('vijay')
items.append_item('software')
items.append_item('developer')
items.append_item('in')
items.append_item('msys')
items.append_item('company')

print("Reverse list ")
items.reverse()
items.print_foward()
