class CircularQueue:
    def __init__(self, n):
        self.maxCount = n
        self.data = [None] * n
        self.count = 0
        self.front = -1
        self.rear = -1
        
    def isEmpty(self):
        return self.count == 0
    
    def isFull(self):
        return self.count == self.maxCount
    
    def add(self, x):
        if self.isFull():
            print('Queue full')
        
        self.rear = (self.rear + 1) % self.maxCount
        self.data[self.rear] = x
        self.count += 1

    def delete(self):
        if self.isEmpty():
            print('Queue empty')

        self.front = (self.front + 1) % self.maxCount
        x = self.data[self.front]
        self.count -= 1
        return x
 
circularqueue1 = CircularQueue(3)

print(circularqueue1.isEmpty())
circularqueue1.delete()
circularqueue1.add(1)
circularqueue1.add(2)
circularqueue1.add(3)
circularqueue1.add(4)
print(circularqueue1.isFull())
circularqueue1.delete()
print(circularqueue1.isEmpty())
print(circularqueue1.isFull())
print(circularqueue1.data)