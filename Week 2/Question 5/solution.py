class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    def isBST(self, root):
        def inorder(node, values):
            if not node:
                return
            inorder(node.left, values)
            values.append(node.data)
            inorder(node.right, values)

        values = []
        inorder(root, values)

        for i in range(1, len(values)):
            if values[i] <= values[i - 1]:
                return False
        return True
