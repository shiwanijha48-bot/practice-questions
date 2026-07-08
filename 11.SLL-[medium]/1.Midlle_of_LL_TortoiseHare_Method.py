# Middle of the linked list

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# Create linked list: 10 -> 20 -> 30 -> 40 -> 50
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)


#  Method - 1
def solve(head):
    n = 0
    temp = head
    while temp:
        n += 1
        temp = temp.next
    temp = head
    for i in range(n//2):
        temp = temp.next
    return temp
#  TC = O(N + N/2),  SC = O(1)
middle = solve(head)
print(middle.val)

#  Method - 2
# [TORTOISE HARE - METHOD] - 2 pointers : slow and fast. fast is 2x of slow.
# when fast will reach at last, then sllow will be at middle(half).

def func(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next # one step at a time
        fast = fast.next.next  # 2 steps at a time
    return slow
mid = func(head)
print(mid.val)


