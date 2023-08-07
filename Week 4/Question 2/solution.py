class Solution:
    def maxProduct(self, arr, n):
        max_product = arr[0]
        min_product = arr[0]
        answer = arr[0]
        
        for i in range(1, n):
            if arr[i] < 0:
                max_product, min_product = min_product, max_product
            
            max_product = max(arr[i], max_product * arr[i])
            min_product = min(arr[i], min_product * arr[i])
            
            answer = max(answer, max_product)
        
        return answer