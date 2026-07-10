#  Method - 1
def func(head):
        temp = head
        my_set = set()
        while temp != None:
            if temp in my_set:
                return temp
            my_set.add(temp)
            temp = temp.next
        return None

#  Method - 2
def func(head):
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast= fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
#  TC = O(N), SC = O(1)