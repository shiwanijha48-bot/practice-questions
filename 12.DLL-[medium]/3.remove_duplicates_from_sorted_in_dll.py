#  Method - 1
def removeDuplicates(self, head):
        # code here
        # return head after editing list
        curr = head
        while curr:
            if curr.prev and curr.prev.data == curr.data:
                if curr.prev == head:
                    curr.prev = None
                    head = curr
                else:
                    curr.prev.prev.next = curr
                    curr.prev = curr.prev.prev
            curr = curr.next
        return head
        #  TC = O(N),  SC = O(1)

#  MEthod - 2
def removeDuplicates(self, head):
        # code here
        # return head after editing list
        cur = head
        while cur and cur.next:
            if cur.data == cur.next.data:
            # Remove cur.next node
               duplicate = cur.next
               cur.next = duplicate.next
               if duplicate.next:
                   duplicate.next.prev = cur
            else:
                cur = cur.next
        return head