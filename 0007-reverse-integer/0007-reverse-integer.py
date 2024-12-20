class Solution:
    def reverse(self, x: int) -> int:
        reversed=0
        y=x
        if x>0:
            s=1
        else:
            s=-1
        x=s*x
        while x!=0:
            d=x%10
            reversed=reversed*10+d
            x //=10
        if -2**31<=reversed<=2**31:
            if y>0:
                return reversed
            else:
                return -1*reversed
        return 0
        