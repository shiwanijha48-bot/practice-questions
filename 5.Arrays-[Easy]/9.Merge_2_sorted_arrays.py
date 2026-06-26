# Method - 1
num1 = [1, 1, 1, 2, 4, 6, 7]
num2 = [ 1, 2, 3, 6, 7, 8, 9, 10]
n = len(num1)
m = len(num2)
i, j = 0, 0
res = []
while i < n and j < m:
    if num1[i] <= num2[j]:
        if len(res) == 0 or res[-1] != num1[i]:
            res.append(num1[i])
        i += 1
    else:
        if len(res) == 0 or res[-1] != num2[j]:
            res.append(num2[j])
        j += 1
while i < n:
    if res[-1] != num1[i]:
        res.append(num1[i])
    i += 1
while j < m:
    if res[-1] != num2[j]:
        res.append(num2[j])
    j += 1
print(res)
#  TC = O(N+M) , SC = O(N+M) ; o(1)= as this the answer space only

#  Method -2
x = [1, 1, 1, 2, 4, 6, 7]
y = [ 1, 2, 3, 6, 7, 8, 9, 10]
ans = []
for i in x:
    if i not in ans:
        ans.append(i)
for i in y:
    if i not in ans:
        ans.append(i)
ans.sort()
print(ans)

#  Tc = o(n logn)