num=464
temp=num
reverse=0
while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num=num//10
if reverse==temp:
    print("palindrome")
else:
    print("not palindrome")
