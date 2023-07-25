class Solution:
    def doUnion(self, a, n, b, m):
        union_set = set()
        for i in range(n):
            union_set.add(a[i])
        for i in range(m):
            union_set.add(b[i])
        return len(union_set)