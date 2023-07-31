class Solution:
    def majorityElement(self, A, N):
        candidate = None
        count = 0

        for num in A:
            if count == 0:
                candidate = num
                count = 1
            elif candidate == num:
                count += 1
            else:
                count -= 1

        count = 0
        for num in A:
            if num == candidate:
                count += 1

        return candidate if count > N // 2 else -1