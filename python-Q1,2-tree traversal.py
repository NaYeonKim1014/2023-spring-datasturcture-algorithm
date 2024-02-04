class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#중위 순회 구현
def iterative_inorder(root):
    stack = []
    current = root
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            print(current.val)
            current = current.right
        else:
            break

#레벨 순서 순회 구현
def level_order(root):
    if not root:
        return
    
    queue = [root] # 큐에 루트 노드를 추가
    while queue:
        node = queue.pop(0) # 큐에서 첫 번째 노드를 빼냄
        print(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


# 이진 트리 구현
root = Node('+')
root.left = Node('*')
root.right = Node('E')
root.left.left = Node('*')
root.left.right = Node('D')
root.left.left.left = Node('/')
root.left.left.right = Node('C')
root.left.left.left.left = Node('A')
root.left.left.left.right = Node('B')

# 중위 순회 실행
iterative_inorder(root)

#구분선 실행
print('-----------')

# 레벨 순서 순회 실행
level_order(root)