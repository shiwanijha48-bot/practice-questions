#  Method - 1
def fourSum(nums, target):
        n = len(nums)
        my_set = set()
        for i in range(0, n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    for l in range(k+1, n):
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            temp = [nums[i], nums[j], nums[k], nums[l]]
                            temp.sort()
                            my_set.add(tuple(temp))
        # return [list(ans) for ans in my_set] or"
        res = []
        for ans in my_set:
            res.append(list(ans))
        return res
#  TC = O(N**4), SC = O(N)

#  Method - 2
def fourSum(nums, target):
        res = set()
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                my_set = set()
                for k in range(j+1, n):
                    fourth = target - (nums[i] + nums[j] + nums[k])
                    if fourth in my_set:
                        temp = [nums[i], nums[j], nums[k], fourth]
                        temp.sort()
                        res.add(tuple(temp))
                    my_set.add(nums[k])
        # return [list(ans)for ans in res]
        result = []
        for ans in res:
            result.append(list(ans))
        return result
#  TC = O(N**3) + O(NLOGN),    SC = O(NO OF ANS)

#  Method - 3
def fourSum(nums, target):
        n = len(nums)
        ans = []
        nums.sort()
        for i in range(0,n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                k = j + 1
                l = n - 1
                while k < l:
                    total = nums[i] + nums[j] + nums[k] + nums[l]
                    if total == target:
                        ans.append([nums[i], nums[j], nums[k], nums[l]] )
                        k+=1
                        l-=1
                        while k < l and nums[k] == nums[k-1]:
                            k+=1
                        while l > k and nums[l] == nums[l+1]:
                            l-=1
                    elif total < target:
                        k+=1
                    else:
                        l-=1
        return ans
#  TC = O(N**3), SC = O(NO OF ANS)