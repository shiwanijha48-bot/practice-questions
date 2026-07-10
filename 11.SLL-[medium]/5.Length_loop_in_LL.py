#  Method - 1
def fuunc(head):
    travel = 0
    temp = head
    my_dict = dict()
    while temp is not None:
        if temp in my_dict:
            return travel - my_dict[temp]
        my_dict[temp] = travel
        travel += 1
        temp = temp.next
    return 0
#  TC = O(N)  , SC = O(N)
         

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
#  TC = O(N),   SC = O(1)
