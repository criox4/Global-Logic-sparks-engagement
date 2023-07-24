class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    def height(self, root, depth):
        if not root:
            return depth
        left = self.height(root.left, depth + 1)
        right = self.height(root.right, depth + 1)
        if left == -1 or right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return max(left, right)

    def isBalanced(self, root):
        return self.height(root, 0) != -1
