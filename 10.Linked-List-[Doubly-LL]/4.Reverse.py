#  Reverse a Doubly Linkedlist
# / Method - 1

class Solution:
    def reverse(self, head):
        # code here
        stack = []
        temp = head
        while temp is not None:
            stack.append(temp.data)
            temp = temp.next
        temp = head
        while temp is not None:
            e = stack.pop()
            temp.data = e
            temp = temp.next
        return head

    # TC = O(2N) = O(N)
    # SC = O(N)


#  Method - 2
class Solution:
    def reverse(self, head):
        # code here
        curr = head
        prev = None
        if head.next == None:
            return head
        while curr is not None:
            front = curr.next
            curr.next = prev
            curr.prev = front
            prev = curr
            curr = front
        return prev
        
        #  TC = O(N)  , SC = O(1)
        