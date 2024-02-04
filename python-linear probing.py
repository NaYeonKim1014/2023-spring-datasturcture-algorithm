class HashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def __hash_function(self, key):
        return hash(key) % self.size

    def __probe(self, key):
        index = self.__hash_function(key)
        while self.keys[index] is not None and self.keys[index] != key:
            index = (index + 1) % self.size
        return index

    def set(self, key, value):
        index = self.__probe(key)
        self.keys[index] = key
        self.values[index] = value

    def get(self, key):
        index = self.__probe(key)
        if self.keys[index] is None:
            raise KeyError(f"{key} not found")
        return self.values[index]

# create a hash table of size 5
hash_table = HashTable(5)

# add some key-value pairs
hash_table.set("apple", 1)
hash_table.set("banana", 2)
hash_table.set("cherry", 3)

# retrieve the values for some keys
print(hash_table.get("apple"))   # output: 1
print(hash_table.get("banana"))  # output: 2
print(hash_table.get("cherry"))  # output: 3

# try to retrieve a non-existent key
try:
    hash_table.get("durian")
except KeyError as e:
    print(str(e))  # output: 'durian not found'
