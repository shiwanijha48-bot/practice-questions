#  Method - 1
class Solution:
    def oddEvenList(head):
        if head is None or head.next is None:
            return head
        values = []
        temp = head
 # First pass
        while temp :
            values.append(temp.val)
            if temp.next:
                temp = temp.next.next
            else:
                break
        temp = head.next
 # Second pass
        while temp:
            values.append(temp.val)
            if temp.next:
                temp = temp.next.next
            else:
                break
# Third Pass
        temp = head
        index = 0
        while temp is not None:
            temp.val = values[index]
            index += 1
            temp = temp.next
        return head


#  Method - 2
def func(head):
        if head is None or head.next is None:
            return head
        odd = head
        even = head.next
        even_head = even
        while even is not None and even.next is not None:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next 
        odd.next = even_head
        return head

#  tc = o(n//2) = o(n)