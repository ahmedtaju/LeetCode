# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length=0
        dummy=temp=head
        while dummy:
            length+=1
            dummy=dummy.next
        middle=(length//2)
        for _ in range(middle):
            temp=temp.next
        return temp