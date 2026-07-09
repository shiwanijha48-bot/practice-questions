#  Method - 1
 
def func(head):
        temp = head
        my_set = set()
        while temp != None:
            if temp in my_set:
                return True
            my_set.add(temp)
            temp = temp.next
        return False
#  TC = O(N,   SC = O(1))

#  METHOD - 2
def func(head):
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast= fast.next.next
            if slow == fast:
                return True
        return False
#  TC = O(N), SC = O(1)