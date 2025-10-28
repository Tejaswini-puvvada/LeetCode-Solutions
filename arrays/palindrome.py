class Solution:
    def isPalindrome(self, num):
        temp = num
        reverse = 0
        while num > 0:
            digit = num % 10
            reverse = reverse * 10 + digit
            num = num // 10
        return temp == reverse

param_1 = 121
ret = Solution().isPalindrome(param_1)
print(ret)
