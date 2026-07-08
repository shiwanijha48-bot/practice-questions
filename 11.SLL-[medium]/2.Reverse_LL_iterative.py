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

#  Method - 1  [brute force]

def solve(head):
        temp = head
        stack = []
        
        # First pass: Store all values in stack
        while temp is not None:
            stack.append(temp.val)  # Push current node's value to stack
            temp = temp.next
        
        temp = head  # Reset temp to head for second pass
        
        # Second pass: Pop values from stack and update nodes
        while temp is not None:
            temp.val = stack.pop()  # Replace current value with stack's top
            temp = temp.next
        
        return head
#  TC = O(N), SC = O(N)


#  Method - 2

def func(head):
        temp = head    # Current node we're processing
        prev = None    # Previous node (starts as None)
        
        while temp is not None:
            front = temp.next     # Store next node before we lose it
            temp.next = prev      # Reverse the link: point to previous
            prev = temp           # Move prev pointer forward
            temp = front          # Move current pointer forward
        
        return prev  # prev is now the new head of reversed list
#  TC = O(N), TC = O(1)

#  Method - 3
def solve(head):
     # Base case: empty list or single node
        if head is None or head.next is None:
            return head
        
        # Recursively reverse the rest of the list
        new_head = solve(head.next)
        
        # Fix the current connection
        front = head.next          # The node that comes after current
        front.next = head          # Make it point back to current
        head.next = None           # Remove current's forward connection
        
        return new_head  # Return the head of the reversed list
#  TC = O(N), SC = O(N)