class Solution:
    def is_armstrong(self,num):
        temp=num
        digits=len(str(num))
        reverse=0
        while num>0:
            digit=num%10
            reverse=reverse+digit**digits
            num=num//10
        return temp==reverse
param=1234
ret=Solution().is_armstrong(param)
if ret:
    print("armstrong")
else: 
    print("not an armstrong")
