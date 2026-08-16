def func(s):
    res = ""
    count= 0
    for i in s:
        if i == "(":
            count += 1
            if count > 1:
                res += i
        else:
            count -= 1
            if count > 0:
                res += i
    return res


s = "(()())(())"
print(func(s))

s1 = "(()())(())(()(()))"
print(func(s1))