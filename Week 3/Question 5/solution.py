class Solution:
    def subArraySum(self, arr, n, s): 
        l = 0
        r = 0
        sum_ = 0
        if s == 0:
            return [-1]
        
        while r < n:
            sum_ += arr[r]
            while sum_ > s:
                sum_ -= arr[l]
                l += 1
            if sum_ == s:
                return [l + 1, r + 1]
            r += 1
        
        return [-1] 