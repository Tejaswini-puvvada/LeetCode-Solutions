class Solution:
    def reverse(self,x:int)->int:
        int_min=-2**31
        int_max=2**31-1
        if x<0:
            sign=-1
        else:
            sign=1
        x=abs(x)
        rev=0
        while x>0:
            digit=x%10
            rev=rev*10+digit
            x=x//10
        rev=rev*sign
        if rev<int_min or rev>int_max:
            return 0
        else:
            return rev
sol=Solution()
print(sol.reverse(123))