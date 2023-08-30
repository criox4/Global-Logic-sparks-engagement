class Solution:
    def solve(self, s, st, cost):
        n = len(cost)
        minval = float('inf')

        for i in range(n):
            if i in st:
                st.remove(i)

                if not st:
                    minval = min(minval, cost[s][i] + cost[i][0])
                else:
                    minval = min(minval, cost[s][i] + self.solve(i, st, cost))

                st.add(i)

        return minval

    def total_cost(self, cost):
        st = set(range(1, len(cost)))
        result = self.solve(0, st, cost)

        if result == float('inf'):
            return 0
        
        return result