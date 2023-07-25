import heapq

class Solution:
    def kthLargest(self, k, arr, n):
        min_heap = []
        result = []
        
        for num in arr:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            else:
                if num > min_heap[0]:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, num)
            
            if len(min_heap) < k:
                result.append(-1)
            else:
                result.append(min_heap[0])
        
        return result