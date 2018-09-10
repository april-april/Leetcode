class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

class Solution(object):
    def isMatch(self, s, t):
        if not(s and t):
            return s is t
        return (s.val == t.val and 
                self.isMatch(s.left, t.left) and 
                self.isMatch(s.right, t.right))

    def isSubtree(self, s, t):
        if self.isMatch(s, t): return True
        if not s: return False
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    root2 = Node(2)
    root2.left = Node(4)
    root2.right = Node(5)
    solution = Solution()
    print(solution.isSubtree(root, root2))

if __name__ == "__main__":
    main()