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
