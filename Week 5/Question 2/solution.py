class Solution:
    def find_permutation(self, S):
        def backtrack(start):
            if start == len(S) - 1:
                permutations.append(''.join(S))
                return

            seen_chars = set()  

            for i in range(start, len(S)):
                if S[i] in seen_chars:
                    continue

                S[start], S[i] = S[i], S[start]  
                backtrack(start + 1)
                S[start], S[i] = S[i], S[start]  
                seen_chars.add(S[i])

        S = list(S)
        permutations = []
        backtrack(0)
        permutations.sort()  
        return permutations