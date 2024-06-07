def countStr(s):
    lis = ['a','e','i','o','u']
    count = 0
    for i in s:
        if i in lis:
            count +=1

    return count

s = "hello"
a = countStr(s)
print(a)