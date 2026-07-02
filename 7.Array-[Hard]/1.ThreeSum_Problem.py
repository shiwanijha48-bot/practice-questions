arr = [-1, 0, 1, 2, -1, -4]

#  Method -1 
def func(arr, target):
    n = len(arr)
    my_set = set()
    for i in range(0, n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if arr[i] + arr[j] + arr[k] == 0:
                    temp = [arr[i],arr[j], arr[k]]
                    temp.sort()
                    my_set.add(tuple(temp))
    return [list(ans) for ans in my_set]
print(func(arr, 0))
#  tc = 0(n**3), sc = o(no of triplets)

#  Method - 2
def Func(arr, target):
    res = set()
    n = len(arr)
    for i in range(n):
        my_set = set()
        for j in range(i+1, n):
            third = -(arr[i] + arr[j])
            if third in my_set:
                temp = [arr[i],arr[j], third]
                temp.sort()
                res.add(tuple(temp))
            my_set.add(arr[j])
    return [list(ans)for ans in res]
print(Func(arr, 0))
#  Tc = o(n**2), sc = o(n) + no of triplets

#  Method - 3
def Solve(arr, target):
    n = len(arr)
    ans = []
    arr.sort()
    for i in range(n):
        if i != 0 and arr[i] == arr[i-1]:
            continue
        j = i+1
        k = n-1
        while j < k:
            total_sum = arr[i] + arr[j]+ arr[k]
            if total_sum < 0:
                j+= 1
            elif total_sum > 0:
                k -= 1
            else:
                temp = [arr[i], arr[j], arr[k]]
                ans.append(temp)
                j += 1
                k -= 1
                # skip the duplicates if occured
                while j < k and arr[j] == arr[j-1]:
                    j += 1
                while j < k and arr[k] == arr[k+1]:
                    k -= 1
    return ans
print(Solve(arr, 0))
#  Tc = o(nlogn + n**2), sc = o(no of triplets)