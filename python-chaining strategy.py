class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        
    def hash_function(self, key):
        return hash(key) % self.size
        
    def set(self, key, value):
        hash_index = self.hash_function(key)
        node = self.table[hash_index]
        while node:
            if node.key == key:
                print("Error: {} already exists in the table".format(key))
                return
            node = node.next
        new_node = Node(key, value)
        new_node.next = self.table[hash_index]
        self.table[hash_index] = new_node
        
    def get(self, key):
        hash_index = self.hash_function(key)
        node = self.table[hash_index]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        raise KeyError("{} not found".format(key))


hash_table = HashTable(5)
hash_table.set("apple", 1)
hash_table.set("banana", 2)
hash_table.set("cherry", 3)
print(hash_table.get("apple"))
print(hash_table.get("banana"))
print(hash_table.get("cherry"))
hash_table.set("banana", 4) # should print an error message
print(hash_table.get("banana"))

