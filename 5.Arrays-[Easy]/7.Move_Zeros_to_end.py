#  method - 1
nums = [1, 0, 2, 4, 3, 0, 0, 3, 5, 1]
n = len(nums)
temp = []
for i in range(0, n):
    if nums[i] != 0:
        temp.append(nums[i])
m = len(temp)
for j in range(0, m):
    nums[j] = temp[j]
for j in range(m, n):
    nums[j] = 0
print(temp)
print(nums)
#  tc =  o(2n), sc = o(n): temp


#  method - 2
nums1 = [1, 2, 4, 3, 3, 5, 1, 0, 0, 0]
j = 0
if len(nums1) == 1:
    print(nums1)
for i in range(0, len(nums1)):
    if nums1[i] != 0:
        nums1[j], nums1[i] = nums1[i], nums1[j]
        j += 1
print(nums1)
#  tc = o(n), sc = o(1)

#  method - 3
nums2 = [1, 2, 4, 3, 3, 5, 1, 0, 0, 0]
if len(nums2) == 1: # edge case
    print(nums2)

i = 0
while i < len(nums2): # find first zero
    if nums2[i] == 0: # element mil gya, jo zero tha
        break # then stop and save that "i"
    i += 1 # otherwise i badhao, and chceck where you get your first zero
if i == len(nums2): # if no zero exits
    print(nums2) # then print arr as it is
j = i+ 1 # if there is zero, then takeanotrher pointr j
while j < len(nums2): # traverse until you find num != 0
    if nums2[j] != 0: # if you get, then swap
        nums2[i], nums2[j] = nums2[j], nums2[i]
        i += 1 # inc i , and check other zero.
    j += 1 # inc it to find another number
print(nums2)

#  tc = o(n), sc = o(1)
