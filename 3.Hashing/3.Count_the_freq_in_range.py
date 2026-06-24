def frequencyCount( arr):
        #  code here
        n = len(arr)
        freq = [0] * n
        for num in arr:
            freq[num - 1] += 1
        return freq
nums = [2,3,5,1,1,2,3,4,5,7,2,3,1]
print(frequencyCount(nums))