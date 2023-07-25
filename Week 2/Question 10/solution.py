class Solution:
    def maxLen(self, n, arr):
        cumulative_sum_dict = {}
        max_length = 0
        current_sum = 0

        for i in range(n):
            current_sum += arr[i]

            if current_sum == 0:
                max_length = i + 1

            if current_sum in cumulative_sum_dict:
                max_length = max(max_length, i - cumulative_sum_dict[current_sum])
            else:
                cumulative_sum_dict[current_sum] = i

        return max_length