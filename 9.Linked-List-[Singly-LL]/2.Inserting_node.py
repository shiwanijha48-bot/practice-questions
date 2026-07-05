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

# print(node1)
# print(n2)
# print(node1.val)
# print(node1.next.val)
# print(node1.next.next.next.val)

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr =  curr.next
            curr.next = new_node

#  TC = O(N), SC = O(1)
   
    def traversal(self):
        if self.head is None:
            print("SLL is empty")
        else:
            curr = self.head
            while curr is not None:
                print(curr.val, end = "")
                curr = curr.next
                print()

#  TC = O(N), SC = O(1)
    def insert(self, val, index):
        new_node = Node(val)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            curr = self.head
            prev_node = None
            count = 0
            while curr is not None and count < index:
                prev_node = curr
                curr = curr.next
                count += 1
            prev_node.next = new_node
            new_node.next = curr

#  TC = O(N), O(1)
   
    def delete(self, val):
        temp = self.head
        if temp is None:
            print("SLL is empty")
            return
        if temp.val == val:
            self.head = temp.next
            return
        found = False
        prev = None
        while temp is not None:
            if temp.val == val:
                found = True
                break
            prev = temp
            temp = temp.next
        if found:
                prev.next = temp.next
                return
        else:
                print("Node not found")
#  TC = O(N),   SC = O(1)


s11 = SinglyLinkedList()
s11.append(10)
s11.append(22)
# s11.traversal()
s11.insert(55,1)
# s11.traversal()
s11.delete(55)
s11.traversal()
    
