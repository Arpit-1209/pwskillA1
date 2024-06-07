def palin(s):
    a = s[::-1]
    if a==s:
        return True

s ="dad"
if palin(s):
    print("palindrome")
else:
    print("not palindrome")
    