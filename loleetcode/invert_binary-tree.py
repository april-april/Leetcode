class Node:

	def __init__(self,key):
		self.left = None
		self.right = None
		self.val = key

# recursive solution
def invertTree(root):
    if root:
        root.left, root.right = invertTree(root.right), invertTree(root.left)
        return root

# iterative solutuon
def invertTree2(root):
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            node.left, node.right = node.right, node.left
            stack += node.left, node.right
    return root

def main():
    root = Node(1)
    root.left	 = Node(2)
    root.right	 = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    inverted = invertTree(root)
    print(inverted.left.val, inverted.right.val)

if __name__ == "__main__":
    main()