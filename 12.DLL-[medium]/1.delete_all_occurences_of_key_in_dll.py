class Solution:
    #Function to delete all the occurances of a key from the linked list.
    def deleteAllOccurOfX(self, head, x):
        # code here
        curr = head
        while curr:
            if curr.data == x:
                if curr.prev is None:
                    head = curr.next
                    if head:
                        head.prev = None
                    curr = head
                else:
                    curr.prev.next = curr.next
                    if curr.next:
                        curr.next.prev = curr.prev
                    curr = curr.next
            else:
                curr = curr.next
        return head