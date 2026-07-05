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


#  LEETCODE - 237

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next