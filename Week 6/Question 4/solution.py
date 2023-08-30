class Solution:
    def follPatt(self, s):
        equal = False
        xcount = 0
        ycount = 0
        
        for i in range(len(s)):
            if s[i] == 'x':
                xcount += 1
            if s[i] == 'y':
                ycount += 1
                
                if i + 1 < len(s) and (s[i + 1] == 'x' or i == len(s) - 1) and xcount != ycount:
                    break
        
        if xcount == ycount:
            equal = True
        
        if equal:
            print(1)
        else:
            print(0)