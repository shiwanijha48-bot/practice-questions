
# Method - 1
def search(nums, target):
        n = len(nums)  # iterative binary search
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target: # right side check
                low = mid + 1
            else:  # left side check
                high = mid - 1
        return -1
# TC = O(log2(N)), SC = O(1)


#  Method - 2
def search(nums, target):
        def binary(low, high):
            if low > high:
                return -1
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return binary(mid + 1, high)
            else:
                return binary(low, mid - 1)
        return binary(0, len(nums) - 1)

#  TC = O(log 2 (n) ), n is no of elements in list
#  SC = O(N) : recursive stack space