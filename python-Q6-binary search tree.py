class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def deleteNode(root, key):
    if root is None:  # If tree is empty
        return root

    if key < root.val:  # If key is smaller than root value
        root.left = deleteNode(root.left, key)
    elif key > root.val:  # If key is greater than root value
        root.right = deleteNode(root.right, key)
    else:  # If key matches root value
        if root.left is None:  # If node has no left child
            temp = root.right
            root = None
            return temp
        elif root.right is None:  # If node has no right child
            temp = root.left
            root = None
            return temp
        else:  # If node has both left and right children
            temp = findMinNode(root.right)  # Find minimum node in right subtree
            root.val = temp.val  # Copy minimum node value to root
            root.right = deleteNode(root.right, temp.val)  # Delete minimum node from right subtree
    return root

def findMinNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def printTree(root, level=0):
    if root is not None:
        printTree(root.right, level + 1)
        print(' ' * 4 * level + '->', root.val)
        printTree(root.left, level + 1)

root = TreeNode(30)
root.left = TreeNode(5)
root.left.left = TreeNode(2)
root.right = TreeNode(40)
root.right.left = TreeNode(35)
root.right.right = TreeNode(80)

print('Before deletion:')
printTree(root)
print('-' * 20)

root = deleteNode(root, 2)

print('After deletion:')
printTree(root)
