class Solution:
    MOD = 10**9 + 7
    def power(self, N, R):
        def mod_pow(b, e, m):
            result = 1
            while e > 0:
                if e % 2 == 1:
                    result = (result * b) % m
                b = (b * b) % m
                e //= 2
            return result

        return mod_pow(N, R, self.MOD)
