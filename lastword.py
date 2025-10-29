class Solution:
    def lengthOfLastWord(self,S):
        word=S.strip().split()
        if word:
            return len(word[-1])
        else:
            return 0
param_1="i am tejaswini puvvada"
reset=Solution().lengthOfLastWord(param_1)
print(reset)