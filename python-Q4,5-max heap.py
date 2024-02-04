class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def __str__(self):
        return str(self.heap)
    
    def _parent(self, idx):
        return (idx - 1) // 2
    
    def _left_child(self, idx):
        return 2 * idx + 1
    
    def _right_child(self, idx):
        return 2 * idx + 2
    
    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def _sift_up(self, idx):
        parent_idx = self._parent(idx)
        if idx > 0 and self.heap[idx] > self.heap[parent_idx]:
            self._swap(idx, parent_idx)
            self._sift_up(parent_idx)
    
    def _sift_down(self, idx):
        max_idx = idx
        left_child_idx = self._left_child(idx)
        right_child_idx = self._right_child(idx)
        if (left_child_idx < len(self.heap) and 
            self.heap[left_child_idx] > self.heap[max_idx]):
            max_idx = left_child_idx
        if (right_child_idx < len(self.heap) and 
            self.heap[right_child_idx] > self.heap[max_idx]):
            max_idx = right_child_idx
        if idx != max_idx:
            self._swap(idx, max_idx)
            self._sift_down(max_idx)
    
    def insert(self, value):
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)
    
    def delete_max(self):
        if not self.heap:
            return None
        self._swap(0, len(self.heap) - 1)
        max_value = self.heap.pop()
        self._sift_down(0)
        return max_value


# Create a new heap
heap = MaxHeap()

# Insert some values into the heap
heap.insert(14)
heap.insert(15)
heap.insert(10)
heap.insert(2)
heap.insert(20)

# print heap 
print(heap)

# Insert some values more into the heap
heap.insert(5)

print(heap)

# Delete the maximum value from the heap
max_val = heap.delete_max()
print(max_val)  

print(heap)
