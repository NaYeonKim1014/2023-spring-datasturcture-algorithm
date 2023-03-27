class Stack:
    def __init__(self,max_stack_size):
        self.stack = []
        self.max_stack_size = max_stack_size
        self.top = -1

    def IsFull(self):
        if self.top == self.max_stack_size -1:
            return True
        else:
            return False

    def IsEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def add(self, item):
        if self.IsFull() == True :
            print("stack full")
            return
        else:
            self.top += 1
            self.stack.append(item)
            return
        
    def delete(self):
        if self.IsEmpty() == True:
            print("stack empty")
            return
        else:
            item = self.stack.pop()
            self.top -= 1
            return item
        
stack1 = Stack(3) # set maximum size of stack 3

print(stack1.IsEmpty())
stack1.delete()
stack1.add(1)
stack1.add(2)
stack1.add(3)
stack1.add(4)
print(stack1.IsFull())
stack1.delete()
print(stack1.IsEmpty())
print(stack1.IsFull())
print(stack1.stack)





