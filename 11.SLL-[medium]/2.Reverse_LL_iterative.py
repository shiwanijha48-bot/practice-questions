# reverse the linked list

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
    