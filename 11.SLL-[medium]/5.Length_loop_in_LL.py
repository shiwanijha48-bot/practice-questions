#  Method - 1
def fuunc(head):
    travel = 0
    
     





#  Method - 2

def lengthOfLoop( head):
        #code here
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                count=1
                temp = slow.next
                while temp != slow:
                    temp = temp.next
                    count += 1
                return count
        return 0
