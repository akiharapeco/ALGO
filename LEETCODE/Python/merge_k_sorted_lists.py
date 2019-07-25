from typing import List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    head = rep = ListNode(None)
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

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        else:
            amount = len(lists)
            interval = 1
            while interval < amount:
                for i in range(0, amount - interval, interval * 2):
                    lists[i] = mergeTwoLists(lists[i], lists[i+interval])
                interval *= 2
            return lists[0] 