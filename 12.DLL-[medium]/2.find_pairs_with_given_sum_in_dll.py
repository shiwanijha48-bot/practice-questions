# Method - 1
def findPairsWithGivenSum(self, target : int, head : Optional['Node']) -> List[List[int]]:
        # code here
        temp1 = head
        res = []
        while temp1 is not None:
            temp2 = temp1.next
            while temp2 is not None:
                if temp1.data + temp2.data == target:
                    res.append([temp1.data, temp2.data])
                temp2 = temp2.next
            temp1= temp1.next
        return res
        
        #  TC = O(N**2)
        #  SC = O(1)

#  Method - 2
def findPairsWithGivenSum(self, target : int, head : Optional['Node']) -> List[List[int]]:
        # code here
        my_set = set()
        temp = head
        res = []
        while temp is not None:
            rem = target - temp.data
            if rem in my_set:
                res.append([rem, temp.data])
            my_set.add(temp.data)
            temp = temp.next
        res.sort()
        return res
        #  TC = O(nlogon + n)
        # SC = O(N)

#  MEthod - 3
def findPairsWithGivenSum(self, target : int, head : Optional['Node']) -> List[List[int]]:
        # code here
        res = []
        left = head
        right = head
        while right.next is not None:
            right = right.next
        while left is not None and right is not None and left.data < right.data:
                total = left.data + right.data
                if total == target:
                    res.append([left.data, right.data])
                    left = left.next
                    right = right.prev
                elif total > target:
                    right = right.prev
                else:
                    left = left.next
        return res
        #  TC = O(N) + O(N) = O(N)
        #  SC =O(1)