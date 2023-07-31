class Solution:
    def leaders(self, A, N):
        leaders_list = []
        max_right = A[N - 1]  
        leaders_list.append(max_right)
        for i in range(N - 2, -1, -1):
            if A[i] >= max_right:
                leaders_list.append(A[i])
                max_right = A[i]

        leaders_list.reverse() 
        return leaders_list
