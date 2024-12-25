# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n=ListNode()
        if not head:
            return head
        n.next=head
        cur=n.next
        cur1=head.next
        while cur1:
            if cur1.next:
                cur2=cur1.next
            else:
                cur2=None
            if cur.val==cur1.val:
                cur.next=cur2
            else:
                cur=cur.next
            cur1=cur2
        return n.next
        