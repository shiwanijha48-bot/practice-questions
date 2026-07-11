# # Doubly linked list
# forward and backward both the directions

# like in google, different tabs-  tab1, tab2, tab3.
# we can go to any tab.

# Create a node
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n1.next = n2
n2.next = n3
n2.prev = n1
n3.prev = n2

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_head(self, val):
        new_node = Node(val)
        if not self.head :
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
#  TC = O(1),  SC = O(1)
    
    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr
#  TC = O(N), SC = O(1)
    
    def insert_at(self, val, position):
        new_node = Node(val)
        if position == 0:
            self.insert_at_head(val)
            return
        curr  = self.head
        count = 0
        while curr and count < position - 1:
            curr = curr.next
            count += 1
        if curr is None:
            print("Position out of bound")
            return
        new_node.next = curr.next
        new_node.prev = curr
        if curr.next:
            curr.next.prev = new_node
        curr.next = new_node

    def traverse_forward(self):
        current = self.head
        while current:
            print(current.val, end=" ")
            current = current.next    # Move forward
        print()

    def traverse_backward(self):
        if not self.head:
            print("DLL is empty")
            return
        current = self.head
        while current.next:        # Go to the last node
            current = current.next
        while current:
            print(current.val, end=" ")
            current = current.prev  # Move backward
        print()


d11 = DoublyLinkedList()
d11.insert_at_head(12)
d11.insert_at_head(22)
d11.append(100)
d11.insert_at(50, 2)
print("Forward Traversal:")
d11.traverse_forward()

print("Backward Traversal:")
d11.traverse_backward()