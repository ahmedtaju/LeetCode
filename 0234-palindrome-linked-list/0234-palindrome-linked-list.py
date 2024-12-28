# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        cur=head
        elm=[]
        while head:
            
            elm.append(head.val)
            head=head.next
        a=0
        b=len(elm)-1
        while a<b:
            if elm[a]!=elm[b]:
                return False
            a+=1
            b-=1
        else:
            return True
           