text="apple"
vowel="aeiouAEIOU"
count=0
for char in text:
    if char in vowel:
        count=count+1
print(count)