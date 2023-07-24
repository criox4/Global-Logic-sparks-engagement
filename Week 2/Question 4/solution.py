
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    def height(self, root, ans):
        if not root:
            return 0
        lh = self.height(root.left, ans)
        rh = self.height(root.right, ans)
        ans[0] = max(ans[0], lh + rh)
        return max(lh, rh) + 1

    def diameter(self, root):
        ans = [0]
        self.height(root, ans)
        return ans[0] + 1
