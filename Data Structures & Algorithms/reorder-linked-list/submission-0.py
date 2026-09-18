# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle points to split into 2 lists
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        list1 = head
        list2 = slow.next
        slow.next = None # break lists

        # reverse second list
        prev = None
        curr = list2
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        list2 = prev

        # merge the two lists
        while list2:
            temp = list1.next
            list1.next = list2
            list1 = temp

            temp = list2.next
            list2.next = list1
            list2 = temp


