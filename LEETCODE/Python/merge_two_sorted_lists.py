# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        rep = ListNode(None)
        head = rep
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                rep.next = l1
                rep = rep.next
                l1 = rep.next
            else:
                rep.next = l2
                rep = rep.next
                l2 = rep.next
        if l1 == None:
            rep.next = l2
        else:
            rep.next = l1
        return head.next