class Solution:
    def FirstNonRepeating(self, A):
        m = {}
        n = len(A)
        dp = ['0'] * n
        dp[0] = A[0]
        m[A[0]] = 1
        
        for i in range(1, n):
            m[A[i]] = m.get(A[i], 0) + 1
            if dp[i-1] == '#':
                if m[A[i]] == 1:
                    dp[i] = A[i]
                else:
                    dp[i] = '#'
            elif dp[i-1] != A[i]:
                dp[i] = dp[i-1]
            else:
                dp[i] = '#'
                for j in range(i+1):
                    if m[A[j]] == 1:
                        dp[i] = A[j]
                        break
        
        ans = "".join(dp)
        return ans
