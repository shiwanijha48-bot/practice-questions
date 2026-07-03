nums = [1, 2, 3, 3, 3, 3, 3, 5, 6, 8, 9, 9, 10]
target = 12 

#  Method - 1

def solve(nums, target):
    n = len(nums)
    first = -1
    last = -1
    for i in range(0, n):
        if nums[i] == target:
            if first == -1:
                first = i
            last = i
    if first == -1:
        return 0
    return last - first + 1
print(solve(nums, target))
#  TC = O(N), SC = O(1)

#  Method - 2
def lowerbound(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    lb = n
    while low <= high:
        mid = (low + high)//2
        if nums[mid] >= target:
            lb = mid 
            high = mid - 1
        else:
            low = mid + 1
    return lb
# lowerbound(arr, 7)

def upperbound(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    ub = n
    while low <= high:
        mid = (low + high)//2
        if nums[mid] > target:
            ub = mid 
            high = mid - 1
        else:
            low = mid + 1
    return ub
# upperbound(arr,3)
lb = lowerbound(nums, target)
if lb == -1:
    print(0)
ub =  upperbound(nums, target)
print(ub -lb)

#  Tc = o(logn)


#  Method - 2
# ---------- helper: first index with value >= target ----------
def lower_bound( nums, target):
        n = len(nums)
        lb  = -1              # default when target isn't found
        low, high = 0, n - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                lb  = mid          # potential first position
                high = mid - 1     # keep searching left half
            else:                  # nums[mid] < target
                low = mid + 1
        return lb

    # ---------- helper: first index with value > target ----------
def upper_bound( nums, target):
        n = len(nums)
        ub  = n               # default when all elements <= target
        low, high = 0, n - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                ub  = mid          # potential upper bound
                high = mid - 1     # look further left
            else:                  # nums[mid] <= target
                low = mid + 1
        return ub

    # ---------- driver: count occurrences of target ----------
def countFreq(arr, target):
        lb = lower_bound(arr, target)
        # if target never appears, quick exit
        if lb == -1 or arr[lb] != target:
            return 0

        ub = upper_bound(arr, target)
        return ub - lb            # total number of occurrences
print(countFreq(nums, target))