class Node:
	# A utility function to create a new node
	def __init__(self ,key):
		self.data = key
		self.left = None
		self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSameTree2(self, p, q):
        if p and q:
            return p.val == q.val and self.isSameTree2(p.left, q.left) and self.isSameTree2(p.right, q.right)
        return p is q

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    root2 = Node(1)
    root2.left = Node(2)
    root2.right = Node(3)
    root2.left.left = Node(5)
    solution = Solution()
    print(solution.isSameTree2(root, root2))