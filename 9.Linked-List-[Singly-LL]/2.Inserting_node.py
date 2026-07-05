class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

node1 = Node(5)
n2 = Node(10)
n3 = Node(7)
n4 = Node(8)

node1.next = n2
n2.next = n3
n3.next = n4

print(node1)
print(n2)
print(node1.val)
print(node1.next.val)
print(node1.next.next.next.val)