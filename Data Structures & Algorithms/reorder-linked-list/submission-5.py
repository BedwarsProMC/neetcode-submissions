# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        list1 = head
        list2 = slow.next
        slow.next = None

        prev = None
        while list2:
            nxt = list2.next
            list2.next = prev
            prev = list2
            list2 = nxt
        
        list2 = prev
        while list2:
            temp = list1.next
            list1.next = list2
            list1 = temp

            temp = list2.next
            list2.next = list1
            list2 = temp
        