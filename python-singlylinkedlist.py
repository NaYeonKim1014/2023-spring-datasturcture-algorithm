class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def delete(self, value):
        if self.head is None:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.value, end=' ')
            current = current.next
        print()
    
    def search_node(self, value):
        count = 0
        current = self.head
        while current is not None:
            if current.value == value:
                return print("Found node with value",current.value,"at location number",(count+1))
            current = current.next
            count += 1
        return print("Node not found")

linked_list = LinkedList()
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
linked_list.print_list() # prints "1 2 3"
linked_list.delete(2)
linked_list.print_list() # prints "1 3"
linked_list.search_node(2)
linked_list.search_node(3)

