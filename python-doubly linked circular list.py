class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.head.prev = self.tail
            self.tail.next = self.head
        else:
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail.next = new_node
            self.head.prev = new_node
            self.tail = new_node
            
    def delete_node(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                if current_node == self.head:
                    self.head = current_node.next
                    self.tail.next = self.head
                    self.head.prev = self.tail
                elif current_node == self.tail:
                    self.tail = current_node.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
                else:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                return True
            current_node = current_node.next
        return False

# create a new empty doubly linked circular list
my_list = DoublyLinkedList()

# insert some nodes to the list
my_list.insert_node(1)
my_list.insert_node(2)
my_list.insert_node(3)

# print the current state of the list
# print list 10 times circular
current_node = my_list.head
count = 0
while current_node:
    print(current_node.data,end='')
    current_node = current_node.next
    count += 1
    if count == 10:
        print()
        break
# output: 1 2 3

# remove the node with data=2 from the list
my_list.delete_node(2)

# print the current state of the list
# print list 10 times circular
current_node = my_list.head
count = 0
while current_node:
    print(current_node.data,end='')
    current_node = current_node.next
    count += 1
    if count == 10:
        print()
        break
# output: 1 3
