class Solution:
    def missingNumber(self, array, n):
        t_sum = (n * (n + 1)) // 2
        a_sum = sum(array)
        missing = t_sum - a_sum
        return missing
