class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    def topView(self, root):
        if not root:
            return []

        node_map = {}
        min_hd = float('inf')
        max_hd = float('-inf')

        queue = [(root, 0)]

        while queue:
            node, hd = queue.pop(0)

            if hd not in node_map:
                node_map[hd] = node.data
                min_hd = min(min_hd, hd)
                max_hd = max(max_hd, hd)

            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))

        top_view = []
        for hd in range(min_hd, max_hd + 1):
            top_view.append(node_map[hd])

        return top_view