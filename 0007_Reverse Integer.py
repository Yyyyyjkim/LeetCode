class Solution:
    def reverse(self, x):
        if x>=0:
            a = list(str(x))
            a.reverse()
            result = int("".join(a))
        else:
            a = list(str(x))[1:]
            a.reverse()
            result = int("".join(a))*(-1)

        if result < (-2**31) or result >= (2**31):
            return 0
        else:
            return result
        
x = -123
x = 123
x = 120
x = 0
