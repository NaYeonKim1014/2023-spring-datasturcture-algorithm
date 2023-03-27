class Queue:
    def __init__(self, max_queue_size):
        self.queue = []
        self.max_queue_size = max_queue_size

    def IsEmpty(self):
        if len(self.queue) == 0 :
            return True
        else:
            return False

    def IsFull(self):
        if len(self.queue)== self.max_queue_size :
            return True
        else :
            return  False

    def add(self, item):
        if self.IsFull() == True :
           print("Queue full")
           return
        else:
            self.queue.append(item)
            return
           

    def delete(self):
        if self.IsEmpty() == True:
            print("Queue empty")
            return
        else:
            item = self.queue.pop(0)
            print(item)
            return
        
queue1 = Queue(3) # set maximum size of queue 3

print(queue1.IsEmpty())
queue1.delete()
queue1.add(1)
queue1.add(2)
queue1.add(3)
queue1.add(4)
print(queue1.IsFull())
queue1.delete()
print(queue1.IsEmpty())
print(queue1.IsFull())
print(queue1.queue)
